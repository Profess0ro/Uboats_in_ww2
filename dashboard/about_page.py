import streamlit as st

def show_about():
    st.markdown("""
                <div style="background-color: rgba(255,255,255,0.8); padding: 1rem; border-radius: 10px; text-align: left;">
                    <h4>🛠️ Project Methodology & Workflow</h4>
                    This project was built with a strong focus on data preparation, transformation, and back-end logic, rather than front-end design.<br><br>
                    <b>Workflow overview:</b><br>
                    • <b>Data Source:</b> Selected a World War II U-boat dataset from <a href="https://www.kaggle.com/datasets/cormac42/ww2-u-boats" target="_blank">Kaggle</a>.<br>
                    • <b>Data Cleaning:</b> Cleaned and restructured the data to ensure consistency and accuracy.<br>
                    • <b>Manual Location Mapping:</b> Retrieved and verified fate coordinates from <a href="https://uboat.net/boats/listing.html" target="_blank">uboat.net</a>.<br>
                    • <b>Custom Dataset:</b> Compiled and saved the fate locations in a separate Excel file, converted to CSV.<br>
                    • <b>Database Construction:</b> Built a SQLite database called <i>SummaryUboats</i> as the main data source.<br>
                    • <b>SQL Calculations:</b> Created queries to calculate service days, average efficiency per sunk ship, type-based stats, and more.<br>
                    • <b>Visualization:</b> Used Streamlit to build a minimalistic dashboard that focuses on clarity and interactivity rather than UI complexity.<br><br>
                    <i>This project emphasizes data analysis and transformation over visual styling, highlighting how historical data can be shaped into valuable insights using SQL and Python.</i>
                </div>
                """, unsafe_allow_html=True)

    
    st.markdown("""
        <div style="background-color: rgba(255,255,255,0.9); padding: 1.5rem; border-radius: 12px; text-align: left; font-family: sans-serif;">
            <h3 style="margin-top: 0;">📬 Contact</h3>
            <p>If you would like to get in touch, feel free to reach out via the following platforms:</p>
            <ul style="list-style: none; padding-left: 0;">
                <li><a href="https://github.com/Profess0ro" target="_blank" style="text-decoration: none; color: #0366d6;">🐙 GitHub</a></li>
                <li><a href="https://www.linkedin.com/in/freddy-larsson-4082752ab/" target="_blank" style="text-decoration: none; color: #0a66c2;">💼 LinkedIn</a></li>
                <li>📧 Email: <a href="mailto:professoro88@gmail.com" style="text-decoration: none; color: #333;">professoro88@gmail.com</a></li>
            </ul>
            <img src="dashboard/images/freddy.jpg" alt="Freddy Larsson" style="max-width: 200px; margin-top: 1rem; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
