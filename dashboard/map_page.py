import streamlit as st
import pandas as pd
import sqlite3
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Function to create a database connection
def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

# Function to display the map with U-boat fate information
def show_map():
    st.subheader("🗺️ Map of U-boat Fates")

    # Introduction text with background styling
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
        On this map, you can explore the fates and locations of WWII German U-boats. <br>
        The coordinates represent the exact positions of most of the fates, with approximately 95% of the data derived from precise longitude and latitude values. <br>
        However, some entries are less specific, such as general areas like 'the English Channel.' <br><br>
        This data has been carefully compiled from the reputable source, <a href="https://uboat.net/boats/listing.html" target="_blank">U-boat.net</a>
        , for an accurate historical overview. <br><br>
        Use the multiselect menu to filter U-boats by their fate. You can choose one or multiple fates to see the corresponding markers on the map.<br>
        The fates of the U-boats are explained below the map for your reference.
    </div>
    """, unsafe_allow_html=True)

    # Include Font Awesome script for icons
    st.markdown("""
    <script src="https://kit.fontawesome.com/214e058f0e.js" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)

    # Database connection
    conn = get_connection()
    
    # Query to get U-boat fate data from the database
    fates_df = pd.read_sql_query("""
        SELECT UboatName, Fate, FateDate, latitude, longitude 
        FROM fates
        """, conn)

    # Convert necessary columns to the appropriate data types
    fates_df["latitude"] = fates_df["latitude"].astype(float)
    fates_df["longitude"] = fates_df["longitude"].astype(float)
    fates_df["FateDate"] = pd.to_datetime(fates_df["FateDate"], errors='coerce')

    # Fetch unique fate options for the multiselect dropdown
    unique_fates = fates_df['Fate'].unique()

    # Multiselect widget to choose fates
    selected_fates = st.multiselect(
        "",
        options=unique_fates,
        default=[]  # Empty list to ensure no fates are selected by default
    )

    # Filter the dataframe to include only selected fates
    filtered_fates_df = fates_df[fates_df['Fate'].isin(selected_fates)] if selected_fates else pd.DataFrame()

    # Create a map centered over the Atlantic Ocean
    m = folium.Map(location=[50, -20], zoom_start=3, tiles="cartoDB positron")

    # Add a marker cluster to group nearby markers
    marker_cluster = MarkerCluster().add_to(m)

    # Define a custom icon for the markers
    icon_html = '<i class="fa fa-crosshairs" style="font-size:24px;color:red;"></i>'

    # Add markers for each selected U-boat fate
    for _, row in filtered_fates_df.iterrows():
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

    # Display the map in the Streamlit app
    folium_static(m, width=1200, height=700)

    st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <b>Broken up:</b> The U-boat was decommissioned and dismantled.<br>
            <b>Buried:</b> The wreckage was found and buried, often as part of military burial.<br>
            <b>Captured:</b> The U-boat was taken into enemy custody.<br>
            <b>Decommissioned:</b> The U-boat was retired from active service.<br>
            <b>Missing:</b> The U-boat disappeared without trace and was presumed lost at sea.<br>
            <b>Run aground:</b> The U-boat ran aground, usually due to navigational error.<br>
            <b>Scrapped:</b> The U-boat was dismantled for parts or materials.<br>
            <b>Scuttled:</b> The U-boat was deliberately sunk by its own crew to avoid capture.<br>
            <b>Stricken:</b> Officially removed from service, usually due to irreparable damage.<br>
            <b>Sunk:</b> The U-boat was destroyed and sunk in combat.<br>
            <b>Surrendered:</b> The U-boat was surrendered to the enemy, usually after the war.<br>
        </div>
        """, unsafe_allow_html=True)