import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"

st.title("SALES FORCAST DASHBOARD")

#load data from backend 

response = requests.get(f"{API_URL}/sales_data")

salesdata = response.json()
#print (salesdata)

#convert this into dataframe
df = pd.DataFrame(salesdata)

# Show dataframe
st.subheader("Sales Dataset")
st.dataframe(df)

# Plot chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Sales Trend"
)

#print (fig)

st.plotly_chart(fig)


# Prediction section
st.subheader("Predict Future Sales")

marketing_spend = st.number_input(
    "Marketing Spend",
    min_value=0.0,
    value=500.0
)

month = st.slider(
    "Month",
    min_value=1,
    max_value=12,
    value=10
)

if st.button("Predict Sales"):
    payload ={
        "marketing_spend":marketing_spend,
        "month":month
    }
    
    Prediction_response = requests.post(
        f"{API_URL}/predict",
        json=payload
    )
    
    prediction = Prediction_response.json()
    
    st.success(
        f"Predicted Sales: {prediction['predicted_sales']}"
    )