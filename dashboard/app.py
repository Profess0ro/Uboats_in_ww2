import streamlit as st

# Import custom page functions
from data_page import show_data
from map_page import show_map
from timeline_page import show_timeline
from statistics_page import show_statistics
from about_page import show_about, show_raw_data

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="WWII U-boat Dashboard", layout="wide")
st.title("🔱 WWII German U-boat Dashboard")

# --- CUSTOM STYLING ---
# Adds a background image and custom styling for sidebar and text
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
menu = st.sidebar.radio("Navigation", [
    "Home", 
    "U-boat Data", 
    "Map", 
    "Timeline", 
    "Statistics", 
    "About this project"
])

# --- PAGE ROUTING ---
if menu == "Home":
    st.markdown("""
        <div style="background-color: rgba(255,255,255,0.85); padding: 1.5rem; border-radius: 10px; text-align: left;">
            <h3>👋 Welcome to the German U-boat Data Dashboard</h3>
            Explore detailed insights about the German U-boat fleet from World War II.<br><br>
            Use the navigation menu on the left to dive into statistics, maps, and summaries based on real data from historical sources.<br>
            This dashboard is designed to make the data accessible and engaging – whether you're a history enthusiast or a data nerd.<br><br>
            Enjoy exploring!
        </div>
    """, unsafe_allow_html=True)

elif menu == "U-boat Data":
    show_data()

elif menu == "Map":
    show_map()

elif menu == "Timeline":
    show_timeline()

elif menu == "Statistics":
    show_statistics()

elif menu == "About this project":
    show_about()
    show_raw_data()
