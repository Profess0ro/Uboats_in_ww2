import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from pandas.tseries.offsets import MonthEnd


# Function to establish a connection to the SQLite database
def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

# Function to display the timeline page
def show_timeline():
    # Displaying the title and description of the timeline
    st.subheader("🕰️ Timeline for Germany's U-boat fleet during WWII")
    st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <p>
                Use the slider to select a specific month within the recorded period.<br>
                You will see:<br>
                - How many U-boats were commissioned by that date<br>
                - How many U-boats were active during that month<br>
                - The distribution of U-boat fates up to that point
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Establishing database connection and retrieving data
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM SummaryUboats", conn)

    # Convert the 'Commissioned' and 'FateDate' columns to datetime format
    df["Commissioned"] = pd.to_datetime(df["Commissioned"], errors="coerce")
    df["FateDate"] = pd.to_datetime(df["FateDate"], errors="coerce")

    # Creating a timeline from the first to the last recorded month
    start_date = df["Commissioned"].min()
    end_date = df["FateDate"].max()
    months = pd.date_range(start=start_date, end=end_date, freq="MS")

    # Adding an interactive slider for the user to select a month
    selected_month = st.select_slider(
        " ",
        options=months,
        value=months[-1],
        format_func=lambda x: x.strftime("%B %Y")
    )

    # Adjusting the selected month to the end of the month
    end_of_month = selected_month + MonthEnd(0)

    # Filtering the U-boat data up until the selected month
    commissioned_until_now = df[df["Commissioned"] <= end_of_month]
    fate_until_now = df[df["FateDate"] <= end_of_month]
    
    # Calculate the number of active U-boats at the selected month
    active_count = max(0, len(commissioned_until_now) - len(fate_until_now))
    
    # Get the count of U-boat fates up to the selected month
    fate_counts = df[df["FateDate"] <= end_of_month]["Fate"].value_counts()

    # Plot the number of active U-boats for the selected month
    fig, ax = plt.subplots(figsize=(3, 3), dpi=200)
    ax.bar([selected_month], [active_count], width=20, color="red")

    ax.set_xticks([])  # Hides the x-axis ticks
    ax.set_ylim(0, 700)  # Sets the y-axis limit
    ax.set_xlabel("Amount of active U-boats")

    # Saving the plot to a buffer for displaying in Streamlit
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    # Creating layout with three columns for displaying different components
    col1, col2, col3 = st.columns(3)

    # First column: Displaying statistics for commissioned, fated, and active U-boats
    with col1:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: center;">
            <h4>
                <b>Total commissioned U-boats:</b> <span style="color: red;">{len(commissioned_until_now)}</span><br>
                <b>Total U-boats that met their fate:</b> <span style="color: red;">{len(fate_until_now)}</span><br>
                <b>Active U-boats {selected_month.strftime('%B %Y')}:</b> <span style="color: red;">{active_count}</span>
            </h4>
        </div>
        """, unsafe_allow_html=True)       

        st.image(buf, width=400)

    # Second column: Displaying a pie chart for the distribution of U-boat fates
    with col2:
        if len(fate_counts) > 0:
            # Generating color palette for pie chart
            cmap = plt.get_cmap("tab20")
            colors = cmap(np.linspace(0, 1, len(fate_counts)))

            # Plotting the pie chart for U-boat fates
            fig, ax = plt.subplots(figsize=(5, 3), dpi=200)
            wedges, _ = ax.pie(
                fate_counts,
                startangle=140,
                colors=colors,
                wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'}
            )
            ax.axis("equal")  # Ensures that pie chart is circular
            ax.set_title("U-boat Fates")

            st.pyplot(fig)

            # Preparing information about each fate with counts and colors
            total_fates = sum(fate_counts)
            fate_info = [(fate, count, color) for (fate, count), color in zip(fate_counts.items(), colors)]

            # Splitting the fate information into three groups for display
            fate_split = [fate_info[i:i+4] for i in range(0, len(fate_info), 4)]

            # Creating columns for the legend
            legend_col1, legend_col2, legend_col3 = st.columns(3)

            # Displaying the fate information in columns
            for col, group in zip([legend_col1, legend_col2, legend_col3], fate_split):
                with col:
                    html_block = "<div style='background-color: rgb(255,255,255); padding: 1rem; border-radius: 10px; text-align: left;'>"
                    for fate, count, color in group:
                        percent = (count / total_fates) * 100
                        hex_color = matplotlib.colors.to_hex(color)
                        html_block += f"<span style='color:{hex_color}'><b>{fate}:</b> {count} ({percent:.1f}%)</span><br>"
                    html_block += "</div>"
                    st.markdown(html_block, unsafe_allow_html=True)
        else:
            # If no fates are recorded, show this message
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: center;">
                No fates recorded for this period.
            </div>
            """, unsafe_allow_html=True)

    # Third column: Explanation of different U-boat fates
    with col3:
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <b>Broken up:</b> The U-boat was decommissioned and dismantled.<br>
            <b>Buried:</b> The wreckage was found and buried, often as part of military burial.<br>
            <b>Captured:</b> The U-boat was taken into enemy custody.<br>
            <b>Decommissioned:</b> The U-boat was retired from active service.<br>
            <b>Missing:</b> The U-boat disappeared without trace and was presumed lost at sea.<br>
            <b>Run aground:</b> The U-boat ran aground, usually due to navigational error.<br>
            <b>Scrapped:</b> The U-boat was dismantled for parts or materials.<br>
            <b>Scuttled:</b> The U-boat was deliberately sunk by its own crew to avoid capture.<br>
            <b>Stricken:</b> Officially removed from service, usually due to irreparable damage.<br>
            <b>Sunk:</b> The U-boat was destroyed and sunk in combat.<br>
            <b>Surrendered:</b> The U-boat was surrendered to the enemy, usually after the war.<br>
        </div>
        """, unsafe_allow_html=True)
