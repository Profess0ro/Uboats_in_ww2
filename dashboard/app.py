import streamlit as st
import sqlite3
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="WWII U-boat Dashboard", layout="wide")
st.title("🔱 WWII German U-boat Dashboard")

# --- CUSTOM CSS STYLE ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://nationalinterest.org/wp-content/uploads/2021/05/U-Boat-1_0.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }

    [data-testid="stSidebar"] {
        background-color: #c8c8c8;
        color: white;
    }

    h1, h2, h3, h4, h5, h6, p {
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["Home", "U-boat Data", "Map", "Timeline", "Submarine Types"])

# --- DATABASE CONNECTION ---
@st.cache_data
def load_summary_data():
    conn = sqlite3.connect("dashboard/data/uboats.db")
    df = pd.read_sql_query("SELECT * FROM SummaryUboats", conn)
    conn.close()
    return df


# --- HOME PAGE ---
if menu == "Home":
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
        <h3>📊 Overview of U-boats</h3><br>
        <p>This dashboard visualizes the activity, effectiveness, and fate of German U-boats during World War II.<br>
        Explore U-boat statistics, view interactive maps, analyze dangerous zones, and filter by submarine types, year, and more.</p>
    </div>
    """, unsafe_allow_html=True)
    
# --- U-BOAT DATA PAGE ---
elif menu == "U-boat Data":
    st.subheader("📊 Overview of U-boats")
    
    df = load_summary_data()
    st.dataframe(df, use_container_width=True)

    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
    All of this data are summarized from the following page and dataset:<br> 
    <a href="https://uboat.net/boats/listing.html">U-boat.net</a><br>
    <a href="https://www.kaggle.com/datasets/cormac42/ww2-u-boats">Dataset from kaggle.com</a><br><br>
    * The column 'WarOutCome' is used to categorize whether a U-boat survived the war, based on if its fate occurred after May 1st, 1945.
    </div>
    """, unsafe_allow_html=True)