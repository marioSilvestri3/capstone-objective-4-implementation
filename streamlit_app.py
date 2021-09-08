import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.title('Customer Churn Dashboard')


@st.cache
def load_data():
    dataframe = pd.read_csv('https://raw.githubusercontent.com/mariosilvestri3/capstone'
                            '/bf1edf1b098c856b49eaf32e6832c91ff891bd74/data/customer-churn-raw.csv')
    return dataframe


# Drop Unimportant Columns
df = load_data().drop(columns=['LoyaltyID', 'Customer ID', 'Total Charges'])


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

# Monthly Charges Histogram
slice_df = df[['Churn', 'Monthly Charges']]
fig = px.histogram(slice_df, x='Monthly Charges', color='Churn', nbins=12, height=600)
st.plotly_chart(fig, use_container_width=True)

# Multiple Linear Regression Model
X = df.drop(columns=['Churn'])
X = pd.get_dummies(X, columns=['Senior Citizen', 'Partner', 'Dependents',
                               'Phone Service', 'Multiple Lines',
                               'Internet Service', 'Online Security',
                               'Online Backup', 'Device Protection',
                               'Tech Support', 'Streaming TV',
                               'Streaming Movies', 'Contract',
                               'Paperless Billing', 'Payment Method',])
y = df['Churn']
y = pd.get_dummies(y)
model = LinearRegression(n_jobs=10)
model.fit(X, y)

# Multiple Linear Regression Chart
colors = ['Positive' if c > 0 else 'Negative' for c in model.coef_[1]]

fig = px.bar(y=X.columns, x=model.coef_[1], color=colors,
             color_discrete_map={'Negative': 'blue', 'Positive': 'red'},
             title="Correlation of feature to churn",
             orientation='h', labels=(dict(x='Correlation', y='Feature')),
             height=900, width=800)
fig.update_yaxes(categoryorder='total ascending', type='category')
fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.05, x=1, xanchor='right'))
st.plotly_chart(fig, use_container_width=True)
