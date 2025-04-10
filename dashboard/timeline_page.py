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
    col1, col2 = st.columns(2)

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

        st.image(buf, width=300)


    with col2:
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <p> More info to be shown</p>
        </div>
        """, unsafe_allow_html=True)