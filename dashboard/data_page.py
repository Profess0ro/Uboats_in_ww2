import streamlit as st
import pandas as pd
import sqlite3 

# --- Establish connection to the SQLite database ---
def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

# --- Render U-boat summary data ---
def show_data():
    st.subheader("📊 Overview of U-boats")
    
    # Load data from database
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM SummaryUboats", conn)
    
    # Ensure numeric conversion (in case of missing or malformed values)
    df["AverageDayPerShip"] = pd.to_numeric(df["AverageDayPerShip"], errors="coerce")
    
    # Display the data in an interactive table
    st.dataframe(df, use_container_width=True)

    # Display data source and note
    st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            All of this data is summarized from the following sources:<br> 
            🔗 <a href="https://uboat.net/boats/listing.html" target="_blank">U-boat.net</a><br>
            📊 <a href="https://www.kaggle.com/datasets/cormac42/ww2-u-boats" target="_blank">Kaggle Dataset</a><br><br>
            <b>Note:</b> The column <i>'WarOutCome'</i> is used to categorize whether a U-boat survived the war, based on if its fate occurred after May 1st, 1945.
        </div>
    """, unsafe_allow_html=True)
