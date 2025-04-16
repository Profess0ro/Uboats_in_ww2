# 🇩🇪 WWII German U-boats Analysis Dashboard

An interactive data dashboard and analysis project that explores the operational efficiency, fate, and historical trends of German U-boats during World War II.

📊 Dataset: [Kaggle – WW2 U-boats](https://www.kaggle.com/datasets/cormac42/ww2-u-boats)  
🔗 Additional Source: [Uboat.net](https://uboat.net/boats/listing.html)

---

## 🧪 Project Hypotheses

**1. Was the most-produced U-boat model also the most effective?**  
By calculating the average days served and damage done (ships/tonnage sunk) by each U-boat model, we can evaluate if Germany mass-produced the most effective class of submarine.

**2. Were submarines that survived the war more effective than those sunk earlier?**  
By categorizing U-boats based on their fate before or after May 1st, 1945, we can compare their operational efficiency.

**3. Did Germany lose more U-boats before or after D-Day?**  
By analyzing monthly losses relative to the total fleet size, we can identify if losses increased after the Allied invasion in June 1944.

**4. Which geographic areas were the most dangerous for German U-boats, and did risk levels change over time?**  
By mapping the fate locations of all U-boats, we can visualize risk zones and evaluate whether certain battles or campaigns shifted where U-boats were most vulnerable.

---

## 📌 Business Requirements

### 1. Operational Efficiency Analysis

**Goal:**  
Evaluate how effectively each U-boat class performed during its service time using metrics such as ships sunk and total tonnage.

**Requirements:**
- Collect data on operational service time, vessels sunk, and tonnage.
- Compare U-boat classes on performance.
- Visualize efficiency trends over time.

---

### 2. Time-Based Losses Analysis

**Goal:**  
Display how U-boat losses evolved throughout the war using a time-series.

**Requirements:**
- Categorize sunk/missing U-boats by date and cause.
- Develop timeline visualizations to identify loss patterns.

---

### 3. Submarine Class Performance Trends

**Goal:**  
Identify which U-boat classes had the highest and lowest loss and success rates.

**Requirements:**
- Collect data on submarines deployed, sunk, and damaged.
- Analyze loss rates and success rates per class.

---

### 4. Geographic Risk Zone Identification

**Goal:**  
Find and visualize high-risk areas where U-boats were most often sunk.

**Requirements:**
- Add geolocation data (latitude, longitude) to fate events.
- Perform clustering to highlight danger zones.
- Visualize trends over time on interactive maps.

---

### 5. Public Visualization & Engagement

**Goal:**  
Make complex data accessible and engaging to the general public.

**Requirements:**
- Develop interactive dashboards with filters and maps.
- Create intuitive and non-technical visualizations.
- Ensure accessibility for users of all backgrounds.

---

## 👥 Target Audience

This dashboard is designed for:
- Researchers & historians
- Military and naval enthusiasts
- Educators and students
- General public interested in WWII maritime history

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web dashboard
- **SQLite** – Lightweight database
- **Pandas** – Data analysis
- **Plotly & PyDeck** – Maps and visualizations
- **HTML/CSS** – Enhanced styling inside Streamlit markdowns

---