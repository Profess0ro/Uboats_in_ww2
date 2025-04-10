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
@st.cache_resource
def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)


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
    
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM SummaryUboats", conn)

    st.dataframe(df, use_container_width=True)

    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
    All of this data is summarized from the following sources:<br> 
    🔗 <a href="https://uboat.net/boats/listing.html" target="_blank">U-boat.net</a><br>
    📊 <a href="https://www.kaggle.com/datasets/cormac42/ww2-u-boats" target="_blank">Kaggle Dataset</a><br><br>
    <b>Note:</b> The column <i>'WarOutCome'</i> is used to categorize whether a U-boat survived the war, based on if its fate occurred after May 1st, 1945.
    </div>
    """, unsafe_allow_html=True)

# --- MAP PAGE ---
elif menu == "Map":
    st.subheader("🗺️ Map of U-boat Fates")

    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
        On this map, you can explore the fates and locations of WWII German U-boats. <br>
        The coordinates represent the exact positions of most of the fates, with approximately 95% of the data derived from precise longitude and latitude values. <br>
        However, some entries are less specific, such as general areas like 'the English Channel.' <br><br>
        This data has been carefully compiled from the reputable source, <a href="https://uboat.net/boats/listing.html" target="_blank">U-boat.net</a>
        , for an accurate historical overview.
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <script src="https://kit.fontawesome.com/214e058f0e.js" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)

    conn = get_connection()
    fates_df = pd.read_sql_query("SELECT * FROM fates", conn)

    # Convert datatypes
    fates_df["latitude"] = fates_df["latitude"].astype(float)
    fates_df["longitude"] = fates_df["longitude"].astype(float)
    fates_df["FateDate"] = pd.to_datetime(fates_df["FateDate"], errors='coerce')

    
    import folium
    from folium.plugins import MarkerCluster
    from streamlit_folium import folium_static

    # Create map centered over the Atlantic
    m = folium.Map(location=[50, -20], zoom_start=3, tiles="cartoDB positron")

    marker_cluster = MarkerCluster().add_to(m)

    icon_html = '<i class="fa fa-crosshairs" style="font-size:24px;color:red;"></i>'

    # Collects information from the table to the markers
    for _, row in fates_df.iterrows():
        popup_text = f"""
        <b>Name:</b> {row['UboatName']}<br>
        <b>Fate:</b> {row['Fate']}<br>
        <b>Date:</b> {row['FateDate'].date() if pd.notnull(row['FateDate']) else 'Unknown'}
        """
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.DivIcon(html=icon_html)
        ).add_to(marker_cluster)

    # Displays the map
    folium_static(m, width=1200, height=700)
