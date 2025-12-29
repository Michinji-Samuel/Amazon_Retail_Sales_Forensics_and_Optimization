# 🛒 Amazon International Apparel Sales: Data Science Pipeline

**Author:** Samuel Wahome Michinji  
**Date:** December 2025  
**Project Type:** End-to-End Data Science (Forensic Cleaning $\rightarrow$ Feature Engineering $\rightarrow$ Predictive Modeling)

---

## 📌 Project Overview
I originally sourced this dataset to teach Data Cleaning to beginners. However, the initial inspection revealed that the data was exceptionally "dirty," closely mimicking the chaotic nature of real-world enterprise data.

The project evolved into a two-phase operation:
1.  **Phase 1 (Forensic Cleaning):** Rescuing 23,000+ transactions from a broken file structure containing multiple stacked reports.
2.  **Phase 2 (Predictive Modeling):** Building a Machine Learning model to forecast daily sales demand and optimize inventory.

---

## 🎯 Objectives
* **Diagnostic & Forensic Extraction:** Identify structural breaks and recover data from a file with multiple header structures and split data blocks.
* **Data Harmonization:** Merge inventory reports hidden within sales logs to impute missing values.
* **Feature Engineering:** Extract `Size` parameters from `SKU` strings to fill 17,000+ missing values and create time-based features for modeling.
* **Demand Forecasting:** Train a regression model to predict daily units sold (`PCS`) based on Price, Stock, and Date.

---

## 🧹 Phase 1: The "Data Rescue" (Forensic Cleaning)
The raw file wasn't a single table, but two separate sales reports stacked on top of each other with an **Inventory Report** hidden in the middle.

### 🔧 Key Technical Achievements
* **Data Rescue:** Recovered **23,000+ valid transactions** from a raw file containing split data blocks.
* **Imputation Success:** Restored **99% of missing Stock values** by extracting the hidden middle block.
* **Regex Extraction:** Filled **missing Sizes** by parsing complex SKU patterns (e.g., extracting 'XL' from `BTM005-XL-BLK`).

---

## 🤖 Phase 2: Predictive Modeling & Demand Forecasting
**Goal:** Build a model to predict daily sales volume (`PCS`) to prevent stockouts and dead inventory.

### 📉 Model Evolution
1.  **Feature Engineering:** Created `Is_Weekend`, `Month`, and One-Hot Encoded 20+ product categories.
2.  **Baseline Failure (Linear Regression):** The baseline model produced a **Negative $R^2$ (-1.78)**.
    * *Diagnosis:* The model failed because retail data is "Zero-Inflated" (most days have 0 sales). Linear regression cannot handle these non-linear spikes.
3.  **The Solution (Random Forest):** We switched to a **Random Forest Regressor**, which successfully captured the non-linear patterns and "zero-sales" days.

### 📊 Model Performance
| Metric | Linear Baseline | Random Forest (Final) | Improvement |
| :--- | :--- | :--- | :--- |
| **RMSE** (Error) | 38.63 | **16.27** | **58% Reduction** |
| **MAE** (Avg Miss) | 11.60 | **7.36** | **+36% Accuracy** |
| **R² Score** | -1.78 | **0.51** | **From Broken to Baseline** |

### 💾 Deployment
The final model was serialized and saved as `amazon_sales_forecaster.pkl`. This file can now be loaded into a production environment to generate instant forecasts for future scenarios.

---

## 🖥️ Phase 3: Interactive Dashboard (The System)
*Response to Feedback: "Create a deployable system, not just a notebook."*

To bridge the gap between Data Science and Business Operations, I built an interactive **Streamlit Dashboard**. This allows Inventory Managers to simulate scenarios without touching Python code.

### 🌟 Features
* **User-Friendly Interface:** Simple dropdowns and number inputs for Product, Price, and Stock.
* **Real-Time Inference:** Loads the serialized Random Forest model (`.pkl`) to generate instant predictions.
* **Business Logic:** Automatically flags "High Demand" or "Low Demand" scenarios to guide decision-making.

### 🚀 How to Run the App
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the dashboard:
    ```bash
    streamlit run app.py
    ```

---

## 💡 Key Business Insights

### 1. 💰 Sales Drivers (Machine Learning Analysis)
Our Random Forest Feature Importance revealed a surprising truth:
* **Price Sensitivity (`RATE`)** and **Stock Availability** are the #1 and #2 drivers of sales.
* **Seasonality (`Month`)** is less important than previously thought.
* *Action:* Dynamic pricing strategies will yield better results than seasonal marketing pushes.

### 2. 👥 Customer Concentration Risk
* **Pareto Efficiency:** The business follows a strict power law. The **Top 20 Styles** drive the majority of revenue.
* **Risk:** **39% of revenue** comes from just **8 clients** (Top 5%).
* *Action:* Implement a "Key Account Management" protocol for these VIPs immediately to prevent churn.

### 3. 📦 Inventory Health
* **Dead Stock:** **874 Styles** sold less than 50 units in 12 months.
* **Pricing Leakage:** Identified specific SKUs (e.g., `BTM005-XL`) with unexplained 18% price variance.
* *Action:* Launch a clearance sale to liquidate dead stock and audit the sales team's discounting permissions.

---

## 🚀 Next Steps
* **Dashboarding:** Build a Streamlit app that loads the `.pkl` model and allows the Inventory Manager to simulate "What-If" scenarios (e.g., "If I lower price by 10%, how much will I sell?").
* **Automated Pipeline:** Script the "Forensic Loading" logic to automatically parse future monthly PDF/CSV reports.

---

## 📬 Connect & Collaborate
If you found this notebook helpful or have questions about the cleaning logic or model tuning:

* **LinkedIn:** [Samuel Wahome](https://linkedin.com/in/samuel-wahome)
* **Portfolio:** [wahomedata.com](https://wahomedata.com)
* **GitHub:** [Michinji-Samuel](https://github.com/Michinji-Samuel)
