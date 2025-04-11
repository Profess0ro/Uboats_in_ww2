import streamlit as st
import sqlite3

def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

# Function to display the map with U-boat fate information
def show_statistics():
    st.subheader("📊 Statistics from the german fleet of U-boats")


    option = st.radio(
        "Choose what type of statistic to display:",
        ("Top 5 most effective U-boats")
    )

    col1, col2, = st.columns(2)

    conn = get_connection()

    if option == "Top 5 most effective U-boats":
        query = get_top5_effective_uboats()
        df