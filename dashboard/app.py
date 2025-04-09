import streamlit as st
import sqlite3
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="WWII U-boat Dashboard", layout="wide")
st.title("🔱 WWII German U-boat Dashboard")

# --- SIDEBAR NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["Home", "U-boat Data", "Map", "Timeline", "Submarine Types"])

# --- DATABASE CONNECTION ---
@st.cache_data
def load_summary_data():
    df = pd.read_csv("dashboard/data/csv/SummaryUboats.csv")
    return df

# --- HOME PAGE ---
if menu == "Home":
    st.subheader("🎯 Dashboard Purpose")
    st.markdown("""
    This dashboard visualizes the activity, effectiveness, and fate of German U-boats during World War II.  
    Explore U-boat statistics, view interactive maps, analyze dangerous zones, and filter by submarine types, year, and more.
""")
    
# --- U-BOAT DATA PAGE ---
elif menu == "U-boat Data":
    st.subheader("📊 Overview of U-boats")
    summary_df = load_summary_data()
    st.dataframe(summary_df, use_container_width=True)