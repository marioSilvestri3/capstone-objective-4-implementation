import streamlit as st
import plotly.express as px
from functions import semi_raw_data, mlr_fig
from sidebar import sidebar

st.title('Customer Churn Dashboard')
st.text('Capstone for Mario Silvestri')

st.markdown('---')

st.subheader('Customer attributes influencing churn rate')

# Prediction Sidebar
sidebar()

# Load Data
df = semi_raw_data()

# Contract Length Histogram
slice_df = df[['Churn', 'Contract']]
fig = px.histogram(slice_df, x='Contract', barmode='stack', color='Churn', height=400,
                   title='Contract Length', labels={'Contract': ''})
st.plotly_chart(fig, use_container_width=True)

# Internet Service Type Histogram
slice_df = df[['Churn', 'Internet Service']]
fig = px.histogram(slice_df, x='Internet Service', barmode='stack', color='Churn', height=400,
                   title='Internet Service', labels={'Internet Service': ''})
st.plotly_chart(fig, use_container_width=True)

# Contract Length Histogram
slice_df = df[['Churn', 'Payment Method']]
fig = px.histogram(slice_df, x='Payment Method', barmode='stack', color='Churn', height=400,
                   title='Payment Method', labels={'Payment Method': ''})
st.plotly_chart(fig, use_container_width=True)

st.markdown('---')

st.subheader('Attributes\' relative influence on churn rate')

# Multiple Linear Regression Chart
st.plotly_chart(mlr_fig(), use_container_width=True)
