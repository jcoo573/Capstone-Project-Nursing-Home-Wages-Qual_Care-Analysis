**Ensuring Quality Care: Investigating How Adjusted Wages Influence Nursing Home Performance**
**Capstone Project | Western Governors University**  
📅 *January 2025*  
👩‍💻 **Author:** Jennifer A. Cook  

---

**Project Overview**
This project investigates the relationship between nursing home staff wages, adjusted for cost of living, and the quality of care in nursing homes**, with a specific focus on Non-Profit facilities.  

Using publicly available datasets, statistical analysis, and Tableau visualizations, this study identifies key factors influencing nursing home performance** and provides actionable insights for policymakers and administrators.

---

**Tools & Technologies**
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, SciPy, Scikit-learn)
- **Tableau** (Interactive dashboard visualization)
- **GitHub/GitLab** (Version control)
- **Jupyter Notebooks** (Exploratory Data Analysis)
- **VS Code** (Development Environment)

---

**Data Sources**
This project uses publicly available datasets from:
1. CMS Nursing Home Compare Data → [data.cms.gov](https://data.cms.gov/provider-data/archived-data/nursing-homes)  
2. U.S. Bureau of Labor Statistics (BLS) Nursing Home Staff Wages → [bls.gov](https://www.bls.gov/oes/2023/may/naics4_623100.htm)  
3. State Cost of Living Index (MERIC) → [meric.mo.gov](https://meric.mo.gov/data/cost-living-data-series)  
4. State Minimum Wages (NCSL) → [ncsl.org](https://www.ncsl.org/labor-and-employment/state-minimum-wages)  

---

**Analysis Workflow**
**Data Ingestion & Cleaning (`clean_data.py`)**
- Load datasets using **Pandas**
- Standardize state names & merge cost-of-living adjustments
- Normalize wages to **cost-of-living adjusted wages**
- Save cleaned datasets to `data/` directory

**Exploratory Data Analysis (`data_exploration.ipynb`)**
- Generate summary statistics and check for missing values
- Conduct correlation analysis between wages, staffing, and quality ratings
- Create scatterplots and boxplots for visual trends

**Statistical Analysis (`statistical_analysis.ipynb`)**
- ANOVA Test: Differences in ratings across ownership types
- Multiple Linear Regression: Predicting overall quality ratings based on staffing, wages, and complaints
- Kruskal-Wallis Test: Verifying statistical significance of findings

**Visualization (`export_to_tableau.py`)**
Export processed dataset (`tableau_ready_provider.csv`)
- Create Tableau dashboard for interactive analysis

---

**Key Findings**
- Staffing levels had the strongest positive correlation with higher ratings.  
-  More substantiated complaints directly lowered quality ratings.  
-  Adjusted wages had a weaker relationship than staffing or complaints, suggesting that staffing investment matters more.  
-  Non-Profit facilities performed better** at similar wage levels compared to For-Profit and Government homes.  

*These insights emphasize that improving staffing ratios and complaint resolution processes should be prioritized over wage increases alone.*

---

**Tableau Dashboard**
Interactive Tableau Dashboard Link: *https://haproxy-traffic-splitter/views/EnsuringQualityCare*  
---


