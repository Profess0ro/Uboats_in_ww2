datasets: https://www.kaggle.com/datasets/cormac42/ww2-u-boats

[Business Requirements](#business-requirements)

# Hypotheses

**1. The model that was built the most of, was it most effective during it´s time on duty?** <br>
By calculating the days served and damage done by every model of uboat, I can analyse if they built most of the most effective model and use days served as a measuring of operating efficiency.<br><br>
**2. Did the uboats that last until the end of the war be more effective than the ones that sunk during the war?** <br>
Since Germany surrender at the beginning of May 1945, I can divide the uboats in 2 different categories (one for those who met their fate before April 1945 and another for those who met their fate after April 1945) and then see if the most effective submarines survived the war.<br><br>
**3. Did the german loose more or less of their uboats after D-Day?** <br>
By calculating the uboats build and the ones they lost by each month, I can see the percentage of their uboat fleet by each month. Did they loose more of their fleet before or after D-Day? <br><br>
**4. Which area was the most dangerous for the german uboats? was there any time of the war that was effecting this area?** <br>
By placing all the fates locations on a map, which area was the most dangerous for the uboats to be in? Was their any happening during the war that change this?

# Business Requirements

### **Operational efficiency** 

The purpose of this analysis is to evaluate the operational efficiency of each U-boat during it´s active service time in the water. Efficiency will be measured by analyzing the total tonnage sunk and the number of vessels sunk (both merchant and warships). This analysis aims to provide researchers and other interested parties with a clearer understanding of how successful different U-boat classes were in their operations, with a focus on merchant and warship sinkings.<br>

**Requirements:**
- Collect data on all U-boats operational service, including the number of vessels sunk and total tonnage.
- Analyze and compare the efficiency of each U-boat class.
- Present the results through statistics and visualizations showing efficiency over time and across different operations.
- Provide the ability to compare performance across different U-boat classes and operation types.<br>
<hr>

### **Timebased analysis of losses**

The goal of this analysis is to develop a timeline that displays the number of U-boats lost or missing over time. 

**Requirements:**

- Collect data on U-boat losses (sunk or missing) over time, categorized by date, location, and type of engagement.
- Develop a timeline visualization that shows the trend of U-boat losses over the course of the war.
<hr>

### **Analysis of Submarine Performance Trends**

The goal of this analysis is to identify trends among submarines from different classes in order to understand which class experienced higher or lower loss rates. Analyse which u-boat class was most effective with its submarine operations.

**Requirements:**<br>
Gather data on submarines from all nations, including:
- Number of submarines deployed.
- Number of vessel sunk by type of u-boat.
- Number of submarines lost or damaged.

**Perform a comparative analysis to calculate:**<br>
**Loss rate:** The ratio of submarines lost or damaged to the total number of submarines commissioned for each nation.<br>
**Success rate:** The ratio of vessels sunk to the total number of submarines deployed for each class.
<hr>

### **Identify Where Most Submarines Were Sunk**

**Requirement:**<br>
Analyze data to determine the geographical areas where the majority of submarines were sunk during World War II. This analysis should include identifying and visualizing the exact locations where submarines were sunk and clustering these locations to highlight the highest-risk zones.

- **Identify Locations:** <br>
Gather information on the exact coordinates (latitude and longitude) of where submarines were sunk.<br>
- **Cluster Analysis:** 
<br>Perform a clustering analysis to group nearby sinking sites and identify high-intensity zones.<br>
- **Risk Zones:**<br> 
Visualize these high-intensity zones on a map to clearly display where the greatest risks for submarines were located.<br>
- **Trend Analysis:**<br> 
Analyze if any trends can be identified over time, showing shifts in submarine sinking patterns or risks based on different phases of the war.
<hr>

### **Reporting and Visualization for the General Public**
Provide a simple and engaging visualization for a broader audience interested in World War II maritime history. The visualizations should enhance public knowledge and interest in the historical significance of submarine operations and their impacts during the war.<br>
**Requirement:**<br>
Develop interactive dashboards and reports to visualize key insights from submarine analyses, including operational performance, losses, and geographical trends. The dashboards should be user-friendly and designed for a non-technical audience.

**Objectives:**<br>
- **Interactive Dashboards:** <br>Create intuitive dashboards that allow users to explore data related to submarine operations, including filters for different time periods, submarine classes, and geographical areas.<br>
- **Data Visualization:**<br> Utilize charts, maps, and graphs to effectively present data on submarine performance, losses, and risk zones in a visually appealing manner.<br>
- **Accessibility:**<br> Ensure that the dashboards are designed to be accessible to individuals with varying levels of technical expertise, making the information approachable and informative for all users.<br>
<hr>

### Target Audience:
All these analyses will be used by researchers, historians, and others interested in naval history and warfare to understand the effectiveness of U-boats during their operations in WW2.
<hr>
