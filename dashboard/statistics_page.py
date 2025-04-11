import streamlit as st
import sqlite3
import pandas as pd

from queries.queries import top5_most_sunked_ships, top5_effective_boats


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
        ["Top 5 most ships sunked",
         "Top 5 most efficient U-boats"],
        label_visibility="collapsed"
    )

    conn = get_connection()

    if option == "Top 5 most ships sunked":
        query = top5_most_sunked_ships()
        df = pd.read_sql_query(query, conn)

        df = df.reset_index(drop=True)


        st.dataframe(df, hide_index=True, use_container_width=True)


        st.markdown("""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                <b>This is the 5 U-boats that sunked the most ships during WWII.</b><br>
                These U-boats are ranked based on the number of ships they sunk during their service.<br>
                Both merchant ships and warships they met on the oceans<br><br>
                If you want to read more about the specific U-boat, copy the wikipedia link.
            </div>
            """, unsafe_allow_html=True)
    
    if option == "Top 5 most efficient U-boats":
        query = top5_effective_boats()
        df = pd.read_sql_query(query, conn)


        st.dataframe(df, hide_index=True, use_container_width=True)


        st.markdown("""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                <b>This is the 5 most efficient U-boats based on the average number of days they took to sink each ship.</b><br>
                These U-boats are ranked by their efficiency, calculated by dividing the total number of ships they sunk by the number of days they served.<br>
                A lower value indicates a more efficient U-boat, meaning they sank more ships in less time.<br><br>
                If you want to read more about the specific U-boat, copy the Wikipedia link.
            </div>
            """, unsafe_allow_html=True)