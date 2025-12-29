import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Amazon Sales Forecaster", page_icon="🔮")

# --- 1. LOAD MODEL ---
@st.cache_resource
def load_model():
    with open('amazon_sales_forecaster.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file not found! Please make sure 'amazon_sales_forecaster.pkl' is in the same folder.")
    st.stop()

# --- 2. UI LAYOUT ---
st.title("🔮 Amazon Demand Forecasting System")
st.markdown("Enter product details below to predict daily sales volume.")

col1, col2 = st.columns(2)

with col1:
    # User Inputs for "Raw" features
    date_val = st.date_input("Select Date", datetime.today())
    category = st.selectbox("Product Category", 
                            ['TAG', 'JNE', 'SET', 'KUR', 'TP ', 'BTM', 'Western', 'Ethnic', 'Other']) 
                            # (Add all your main categories here)
    size = st.selectbox("Size", ['Free', 'XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL'])

with col2:
    stock_level = st.number_input("Current Stock Level", min_value=0, value=50)
    price = st.number_input("Selling Price (RATE)", min_value=0.0, value=500.0)

# --- 3. PREPROCESSING (The Tricky Part) ---
# We must convert these inputs into the EXACT format the model was trained on.

# A. Time Features
month = date_val.month
day_of_week = date_val.weekday()
is_weekend = 1 if day_of_week >= 5 else 0

# B. Size Encoding (Must match your notebook mapping!)
size_mapping = {
    'Free': 0, 'XS': 1, 'S': 2, 'M': 3, 'L': 4, 'XL': 5, 'XXL': 6, '3XL': 7, 'Unknown': 2
}
size_encoded = size_mapping.get(size, 2)

# C. One-Hot Encoding for Category
# The model expects columns like 'Category_JNE', 'Category_SET', etc.
# We create a dictionary of ALL possible columns initialized to 0.
# Note: You need to list ALL columns your model was trained on here. 
# Use 'X_train.columns' from your notebook to double check this list!
model_columns = [
    'Month', 'Is_Weekend', 'Size_Encoded', 'Stock', 'RATE', 
    'Category_BL0', 'Category_BL1', 'Category_BTM', 'Category_CH2', 
    'Category_CMB', 'Category_J00', 'Category_J01', 'Category_J02', 
    'Category_J03', 'Category_J04', 'Category_JAN', 'Category_JNE', 
    'Category_LAB', 'Category_MEN', 'Category_NW0', 'Category_PJ0', 
    'Category_PJN', 'Category_PSE', 'Category_SAR', 'Category_SET', 
    'Category_SHI', 'Category_TAG', 'Category_btm', 'Category_jne', 
    'Category_pJN', 'Category_sEt', 'Category_set'
    ]

input_data = pd.DataFrame(0, index=[0], columns=model_columns)

# Fill in the basic values
input_data['RATE'] = price
input_data['Stock'] = stock_level
input_data['Month'] = month
input_data['Size_Encoded'] = size_encoded
input_data['Is_Weekend'] = is_weekend

# Set the specific Category column to 1
cat_col_name = f"Category_{category}"
if cat_col_name in input_data.columns:
    input_data[cat_col_name] = 1

# --- 4. PREDICTION ---
if st.button("Generate Forecast", type="primary"):
    try:
        prediction = model.predict(input_data)[0]
        
        # Display Result
        st.divider()
        st.subheader(f"📈 Predicted Sales: {prediction:.1f} Units")
        
        # Interpretation
        if prediction > 20:
            st.success("High Demand Expected! Ensure stock is available.")
        elif prediction < 5:
            st.warning("Low Demand Expected. Consider a discount?")
        else:
            st.info("Moderate Demand.")
            
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        st.write("Debug - Input Data:", input_data)