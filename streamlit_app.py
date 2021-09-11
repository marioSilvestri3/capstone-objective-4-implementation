import streamlit as st
import plotly.express as px
from functions import prepped_data, mlr_fig
from sidebar import sidebar

st.title('Customer Churn Dashboard')

# Prediction Sidebar
sidebar()

# Load Data
df = prepped_data()

# Contract Length Histogram
slice_df = df[['Churn', 'Contract']]
fig = px.histogram(slice_df, x='Contract', barmode='stack', color='Churn', height=400)
st.plotly_chart(fig, use_container_width=True)

# Internet Service Type Histogram
slice_df = df[['Churn', 'Internet Service']]
fig = px.histogram(slice_df, x='Internet Service', barmode='stack', color='Churn', height=400)
st.plotly_chart(fig, use_container_width=True)

# Contract Length Histogram
slice_df = df[['Churn', 'Payment Method']]
fig = px.histogram(slice_df, x='Payment Method', barmode='stack', color='Churn', height=400)
st.plotly_chart(fig, use_container_width=True)

# Multiple Linear Regression Chart
st.plotly_chart(mlr_fig(), use_container_width=True)
