import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import matplotlib

def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

def show_timeline():
    st.subheader("🕰️ Timeline for Germanys u-boat fleet during the WWII")
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
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM SummaryUboats", conn)

    df["Commissioned"] = pd.to_datetime(df["Commissioned"], errors="coerce")
    df["FateDate"] = pd.to_datetime(df["FateDate"], errors="coerce")

    # Creates a timeline by using all of the months in the range of dates
    start_date = df["Commissioned"].min()
    end_date = df["FateDate"].max()
    months = pd.date_range(start=start_date, end=end_date, freq="MS")

    # Interactive slider for the user to choose month 
    selected_month = st.select_slider(
        " ",
        options=months,
        value=months[-1],
        format_func=lambda x: x.strftime("%B %Y")
    )

    commissioned_until_now = df[df["Commissioned"] <= selected_month]
    missing_commissioned = df[df["Commissioned"] > selected_month]
    st.write("Commissioned after selected month:", missing_commissioned)
    fate_until_now = df[df["FateDate"] <= selected_month]
    active_count = max(0, len(commissioned_until_now) - len(fate_until_now))
    missing_fates = df[df["FateDate"] > selected_month]
    

    fate_counts = df[df["FateDate"] <= selected_month]["Fate"].value_counts()

    # Shows only one bar for the selected month
    fig, ax = plt.subplots(figsize=(3, 3), dpi=200)
    ax.bar([selected_month], [active_count], width=20, color="red")

    ax.set_xticks([])
    ax.set_ylim(0, 700)
    ax.set_xlabel("Amount of active U-boats")

    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    # Layout med kolumner
    col1, col2, col3 = st.columns(3)

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
        st.write("Commissioned after selected month:", missing_commissioned)
        st.write("Fates after selected month:", missing_fates)
        st.image(buf, width=400)


    with col2:
        if len(fate_counts) > 0:
            # Färgpalett
            cmap = plt.get_cmap("tab20")
            colors = cmap(np.linspace(0, 1, len(fate_counts)))

            # Pie chart utan labels och procent
            fig, ax = plt.subplots(figsize=(5, 3), dpi=200)
            wedges, _ = ax.pie(
                fate_counts,
                startangle=140,
                colors=colors,
                wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'}
            )
            ax.axis("equal")
            ax.set_title("U-boat Fates")

            st.pyplot(fig)

            # Koppla fate + count + color i en lista
            total_fates = sum(fate_counts)
            fate_info = [(fate, count, color) for (fate, count), color in zip(fate_counts.items(), colors)]

            # Dela upp i grupper om 4 för kolumner
            fate_split = [fate_info[i:i+4] for i in range(0, len(fate_info), 4)]

            legend_col1, legend_col2, legend_col3 = st.columns(3)

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
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: center;">
                No fates recorded for this period.
            </div>
            """, unsafe_allow_html=True)




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