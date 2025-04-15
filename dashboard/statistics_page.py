import streamlit as st
import sqlite3
import pandas as pd

from queries.queries import most_sunked_ships, effective_boats, longest_serving_time, type_longest_serving_days


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
        ["U-boats that sunk most ships",
         "U-boats with the best efficiency per day",
         "U-boats with the longest time in service",
         "Average days in service per U-boat type"],
        label_visibility="collapsed"
    )

    conn = get_connection()

    if option == "U-boats that sunk most ships":
        query = most_sunked_ships()
        df = pd.read_sql_query(query, conn)

        df = df.reset_index(drop=True)


        st.dataframe(df, hide_index=True, use_container_width=True)


        st.markdown("""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                <b>These are the German U-boats that sank the most ships during WWII.</b><br>
                The table below shows all U-boats ranked by the total number of ships they sank during their service.<br>
                This includes both merchant and warships encountered during their missions.<br><br>
                If you want to read more about a specific U-boat, copy the Wikipedia link provided in the table.
            </div>
            """, unsafe_allow_html=True)
    
    if option == "U-boats with the best efficiency per day":
        query = effective_boats()
        df = pd.read_sql_query(query, conn)


        st.dataframe(df, hide_index=True, use_container_width=True)


        st.markdown("""
            <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
                <b>All German U-boats ranked by efficiency – based on the average number of days taken to sink each ship.</b><br>
                This table displays every U-boat, sorted by how quickly they sank ships during their service.<br>
                Efficiency is calculated by dividing the total number of ships sunk by the number of days in service.<br>
                A lower average means the U-boat sank more ships in a shorter time.<br><br>
                If you want to read more about a specific U-boat, copy the Wikipedia link.
            </div>
            """, unsafe_allow_html=True)
        
    if option == "U-boats with the longest time in service":
        query = longest_serving_time()
        df = pd.read_sql_query(query, conn)

        st.dataframe(df, hide_index=True, use_container_width=True)

        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <b>These are the U-boats that served the longest during WWII.</b><br>
            The list is sorted by the total number of days each U-boat was in active service.<br>
            Longer service duration may indicate successful missions, effective crews, or simply survivability through the war.<br><br>
            If you want to read more about a specific U-boat, copy the Wikipedia link.
        </div>
        """, unsafe_allow_html=True)

    if option == "Average days in service per U-boat type":
        query = type_longest_serving_days()
        df = pd.read_sql_query(query, conn)

        st.dataframe(df, hide_index=True, use_container_width=True)

        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px;">
            <b>Average Days in Service per U-boat Type</b><br>
                This table presents the average number of days each U-boat type remained in service.<br> 
                It offers insight into which types were deployed the longest, possibly reflecting their reliability,<br>
                strategic value, or timing of deployment during the war.<br><br>
                The data may help uncover which designs had the most prolonged operational use in the German Navy's U-boat fleet.
        </div>
        """, unsafe_allow_html=True)