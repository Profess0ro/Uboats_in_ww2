import streamlit as st
import sqlite3
import pandas as pd

# Import queries used to fetch data from the database
from queries.queries import (
    most_sunked_ships,
    effective_boats,
    longest_serving_time,
    type_longest_serving_days
)

# Create a reusable connection function to handle SQLite connection
def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)

# Function to show statistical views of the German U-boat fleet
def show_statistics():
    st.subheader("📊 Statistics from the German fleet of U-boats")

    # Introductory information box with markdown and custom styling
    st.markdown("""
        <div style="background-color: rgba(255, 255, 255, 0.9); padding: 1rem; border-radius: 10px;">
            <h5><b>Choose a statistic to explore the performance and history of German U-boats during WWII.</b></h5>
            <p>This section presents different statistical views of the U-boat fleet. You can explore:</p>
            <ul>
                <li><b>The U-boats that sank the most ships</b> – See which U-boats were most successful in sinking enemy ships.</li>
                <li><b>The best efficiency per day</b> – Rank the U-boats based on how quickly they sank ships during their service.</li>
                <li><b>The longest-serving U-boats</b> – Discover which U-boats served the longest in WWII.</li>
                <li><b>Average days in service per U-boat type</b> – See how different types of U-boats fared over the course of the war.</li>
            </ul>
            <p>Once you select a statistic, detailed information will be displayed below.</p>
        </div>
    """, unsafe_allow_html=True)

    # Dictionary to store each statistics option with its corresponding query and description
    stats_options = {
        "U-boats that sunk most ships": {
            "query_func": most_sunked_ships,
            "description": """
                <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                    <b>These are the German U-boats that sank the most ships during WWII.</b><br>
                    The table below shows all U-boats ranked by the total number of ships they sank during their service.<br>
                    This includes both merchant and warships encountered during their missions.<br><br>
                    If you want to read more about a specific U-boat, copy the Wikipedia link provided in the table.
                </div>
            """
        },
        "U-boats with the best efficiency per day": {
            "query_func": effective_boats,
            "description": """
                <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                    <b>All German U-boats ranked by efficiency – based on the average number of days taken to sink each ship.</b><br>
                    This table displays every U-boat, sorted by how quickly they sank ships during their service.<br>
                    Efficiency is calculated by dividing the total number of ships sunk by the number of days in service.<br>
                    A lower average means the U-boat sank more ships in a shorter time.<br><br>
                    If you want to read more about a specific U-boat, copy the Wikipedia link.
                </div>
            """
        },
        "U-boats with the longest time in service": {
            "query_func": longest_serving_time,
            "description": """
                <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                    <b>These are the U-boats that served the longest during WWII.</b><br>
                    The list is sorted by the total number of days each U-boat was in active service.<br>
                    Longer service duration may indicate successful missions, effective crews, or simply survivability through the war.<br><br>
                    If you want to read more about a specific U-boat, copy the Wikipedia link.
                </div>
            """
        },
        "Average days in service per U-boat type": {
            "query_func": type_longest_serving_days,
            "description": """
                <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                    <b>Average Days in Service per U-boat Type</b><br>
                    This table presents the average number of days each U-boat type remained in service.<br> 
                    It offers insight into which types were deployed the longest, possibly reflecting their reliability,<br>
                    strategic value, or timing of deployment during the war.<br><br>
                    The data may help uncover which designs had the most prolonged operational use in the German Navy's U-boat fleet.
                </div>
            """
        }
    }

    # Let the user choose a statistic from a dropdown menu (label hidden)
    option = st.selectbox(
        "",
        list(stats_options.keys()),
        label_visibility="collapsed"
    )

    # If a valid option is selected
    if option:
        selected = stats_options[option]  # Get selected query and description

        # Connect to the database and run the associated SQL query
        with get_connection() as conn:
            df = pd.read_sql_query(selected["query_func"](), conn)

        # Reset DataFrame index to make sure it's clean before displaying
        df = df.reset_index(drop=True)

        # Display the data as a scrollable, wide dataframe
        st.dataframe(df, hide_index=True, use_container_width=True)

        # Provide a download button to let the user export the data as CSV
        st.download_button(
            label="📥 Download table as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"{option.replace(' ', '_').lower()}.csv",
            mime="text/csv"
        )

        # Show the description/info box related to the selected statistic
        st.markdown(selected["description"], unsafe_allow_html=True)
