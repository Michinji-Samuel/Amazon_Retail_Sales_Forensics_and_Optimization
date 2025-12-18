# 🛒 Amazon International Apparel Sales: Data Cleaning Challenge
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Pandas%20|%20NumPy%20|%20Seaborn-green)
![Status](https://img.shields.io/badge/Status-Completed-orange)

**Author:** Samuel Wahome Michinji
**Date:** December 2025
**Project Type:** Advanced Data Cleaning, Forensic Extraction & Predictive Modeling Prep

---

## 📌 Project Overview
I originally sourced this dataset to teach Data Cleaning to beginners. However, the **initial inspection** (using `df.info()` and `df.isna()`) revealed that the data was exceptionally "dirty," closely mimicking the chaotic nature of real-world enterprise data.

The diagnostic phase uncovered a critical issue: the file wasn't a single table, but two separate sales reports stacked on top of each other with an **Inventory Report** hidden in the middle. Instead of a simple CSV import, this project required a custom "Forensic Loading" strategy to rescue the data.

### 🎯 Objectives
1.  **Diagnostic & Forensic Extraction:** Identify structural breaks and recover data from a file with multiple header structures and split data blocks.
2.  **Data Harmonization:** Merge inventory reports hidden within sales logs to impute missing values.
3.  **Feature Engineering:** Extract `Size` parameters from `SKU` strings to fill 17,000+ missing values.
4.  **Business Intelligence:** Generate actionable insights regarding revenue drivers, customer concentration, and seasonal trends.

---

## 📊 Analysis Framework
After cleaning, the data is analyzed through three strategic lenses using `Matplotlib` and `Seaborn`:

### 1. 💰 Sales & Financial Performance
* **Pareto Analysis:** Testing the **80/20 Rule**—Do 20% of our styles drive 80% of revenue?
* **Seasonal Trends:** Heatmaps showing peak performance months.
* **Profitability:** Scatter plots identifying "Cash Cow" products (High Volume / High Price).

### 2. 👥 Customer & Market Analysis
* **VIP Identification:** Ranking top 10 customers by total spend.
* **Customer Concentration:** Calculating the revenue risk posed by reliance on top clients.
* **Basket Analysis:** (Excluding shipping) Which styles are frequently bought together?

### 3. 📦 Product & Inventory Health
* **Dead Stock:** Identifying styles with <50 units sold in 12 months.
* **Size Distribution:** Informing future manufacturing ratios based on size popularity (S vs. XL).
* **Pricing Consistency:** Detecting variance in `RATE` for identical SKUs.

---

## 🏁 Conclusion & Recommendations

### 🔧 Technical Achievements
* **Data Rescue:** Recovered **23,000+ valid transactions** from a raw file containing split data blocks and hidden inventory tables.
* **Imputation Success:** Restored **99% of missing Stock values** by extracting the hidden middle block and **missing Sizes** using Regex extraction on SKU patterns.

### 💡 Key Business Insights
1.  **Pareto Efficiency:** The business follows a strict power law. The **Top 20 Styles** drive the majority of revenue.
    * *Action:* Guarantee 100% in-stock rate for these 20 items.
2.  **Customer Concentration Risk:** **39% of revenue** comes from just **8 clients** (Top 5%).
    * *Action:* Implement a "Key Account Management" protocol for these VIPs immediately to prevent churn.
3.  **Inventory Bloat:** **874 Styles** sold less than 50 units in 12 months.
    * *Action:* Launch a clearance sale to liquidate this dead stock and free up warehouse space.
4.  **Pricing Leakage:** Identified specific SKUs (e.g., `BTM005-XL`) with unexplained 18% price variance.
    * *Action:* Audit the sales team's discounting permissions.

### 🚀 Next Steps
* **Predictive Modeling:** Leverage this high-quality cleaned dataset to build Machine Learning models for **Sales Forecasting** (Time Series) and **Customer Churn Prediction**.
* **Automate Data Pipeline:** Build a script to automatically parse future monthly reports using the logic defined in "Forensic Data Loading."

---

### 📬 Connect & Collaborate
If you found this notebook helpful or have questions about the regex patterns used:
* **LinkedIn:** [Samuel Wahome](https://www.linkedin.com/in/samuel-wahome-60023b152/)
* **Portfolio:** [wahomedata.com](https://wahomedata.com/)
* **GitHub:** [Michinji-Samuel](https://github.com/Michinji-Samuel)