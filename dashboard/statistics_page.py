import streamlit as st
import sqlite3
import pandas as pd

from queries.queries import top5_effective_uboats

def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

# Function to display the map with U-boat fate information
def show_statistics():
    st.subheader("📊 Statistics from the german fleet of U-boats")

    st.markdown("""
        <div style="background-color: rgba(255, 255, 255, 0.9); padding: 1rem; border-radius: 10px;">
            <h5>Choose a statistic to display by selecting an option below</h5>
        </div>
    """, unsafe_allow_html=True)

    option = st.selectbox(
        "",
        ["Top 5 most effective U-boats"],
        label_visibility="collapsed"
    )

    col1, col2, = st.columns(2)

    conn = get_connection()

    if option == "Top 5 most effective U-boats":
        query = top5_effective_uboats()
        df = pd.read_sql_query(query, conn)

        df = df.reset_index(drop=True)

        with col1:
            st.dataframe(df, hide_index=True, use_container_width=True)

        with col2:
            st.markdown("""
                <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                    <b>This is the 5 most effective U-boats that served during WWII.</b><br>
                    These U-boats are ranked based on the number of ships they sunk during their service.<br>
                    This information helps highlight the efficiency of these boats in their missions.<br><br>
                    If you want to read more about the specific U-boat, click on the wikipedia link.
                </div>
            """, unsafe_allow_html=True)