import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

def show_timeline():
    st.subheader("🕰️ Timeline for Germanys u-boat fleet during the WWII")

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
    fate_until_now = df[df["FateDate"] <= selected_month]
    active_count = len(commissioned_until_now) - len(fate_until_now)

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
            <h3>
                <b>Total commissioned U-boats:</b> <span style="color: red;">{len(commissioned_until_now)}</span><br>
                <b>Total U-boats that met their fate:</b> <span style="color: red;">{len(fate_until_now)}</span><br>
                <b>Active U-boats {selected_month.strftime('%B %Y')}:</b> <span style="color: red;">{active_count}</span>
            </h3>
        </div>
        """, unsafe_allow_html=True)       

        st.image(buf, width=400)


    with col2:

        if len(fate_counts) > 0:
            # Plotting the Fate statistics as a bar chart
            fig, ax = plt.subplots(figsize=(5, 3), dpi=200)
            fate_counts.plot(kind="bar", ax=ax, color="red")
            ax.set_title("U-boat Fates")
            ax.set_xticklabels(fate_counts.index, rotation=45, ha="right")

            # Show fate text counts below the bar chart
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: center;">
                {' '.join([f"<b>{fate}:</b> {count}<br>" for fate, count in fate_counts.items()])}
            </div>
            """, unsafe_allow_html=True)

            # Display the bar chart
            st.pyplot(fig)
        else:
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: center;">
                No fates recorded for this period.
            </div>
            """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <b>Fate explanations:</b><br>
            <b>Stricken:</b> A boat that was removed from active duty but not necessarily destroyed.<br>
            <b>Scuttled:</b> A boat that was deliberately sunk, typically by its own crew to prevent capture.<br>
            <b>Scrapped:</b> A boat that was dismantled and decommissioned for parts.<br>
            <b>Decommissioned:</b> A boat that was taken out of service, often because it was no longer deemed useful.<br>
            <b>Broken up:</b> A boat that was dismantled for parts or scrap, similar to scrapping.<br>
        </div>
        """, unsafe_allow_html=True)