import streamlit as st
import sqlite3
import pandas as pd


from data_page import show_data
from map_page import show_map
from timeline_page import show_timeline
from statistics_page import show_statistics
from about_page import show_about

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
menu = st.sidebar.radio("Navigation", ["Home", "U-boat Data", "Map", "Timeline", "Statistics", "About this project"])


# --- HOME PAGE ---
if menu == "Home":
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
        <h3>📊 Overview of U-boats (Unterseeboots)</h3><br>
        <p>This dashboard visualizes the activity, effectiveness, and fate of German U-boats during World War II.<br>
        Explore U-boat statistics, view interactive maps, analyze dangerous zones, and filter by submarine types, year, and more.</p>
    </div>
    """, unsafe_allow_html=True)
    
# --- U-BOAT DATA PAGE ---
elif menu == "U-boat Data":
    show_data()

# --- MAP PAGE ---
elif menu == "Map":
    show_map()

# --- TIMELINE PAGE ---
elif menu == "Timeline":
    show_timeline()

# --- STATISTICS PAGE ---
elif menu == "Statistics":
    show_statistics()

# --- ABOUT PAGE ---
elif menu == "About this project":
    show_about()