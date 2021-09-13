import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LogisticRegression, LinearRegression


def prepped_data() -> pd.DataFrame:
    df = pd.read_csv('https://raw.githubusercontent.com'
                     '/mariosilvestri3/capstone-objectives-1-2-3'
                     '/main/customer-churn-prepped.csv')
    return df


@st.cache
def semi_raw_data() -> pd.DataFrame:
    df = pd.read_csv('https://raw.githubusercontent.com'
                     '/mariosilvestri3/capstone-objectives-1-2-3'
                     '/main/customer-churn-raw.csv')
    df = df.drop(columns=['LoyaltyID', 'Customer ID', 'Total Charges'])
    return df


@st.cache
def model():
    df = prepped_data()
    _model = LogisticRegression()
    y = df['Churn_Yes']
    X = df.drop(columns=['Churn_Yes'])
    _model.fit(X, np.ravel(y))
    return _model


def predict(X_data):
    df = pd.DataFrame.from_dict(X_data)
    print(model().predict(df)[0])
    return model().predict(df)[0]


@st.cache
def mlr_fig():
    df = semi_raw_data()
    X = df.drop(columns=['Churn'])
    # Encode categorical data as numerical data.
    X = pd.get_dummies(X, columns=['Senior Citizen', 'Partner', 'Dependents',
                                   'Phone Service', 'Multiple Lines',
                                   'Internet Service', 'Online Security',
                                   'Online Backup', 'Device Protection',
                                   'Tech Support', 'Streaming TV',
                                   'Streaming Movies', 'Contract',
                                   'Paperless Billing', 'Payment Method'],
                       prefix_sep=' = ', drop_first=False)
    y = df['Churn']
    y = pd.get_dummies(y)

    model = LinearRegression()
    model.fit(X, y)

    colors = ['Positive' if c > 0 else 'Negative' for c in model.coef_[1]]

    fig = px.bar(y=X.columns, x=model.coef_[1], color=colors,
                 color_discrete_map={'Negative': 'blue', 'Positive': 'red'},
                 title="Churn Predictors",
                 orientation='h', labels=(dict(x='Coefficient', y='Feature')),
                 height=900, width=800)
    fig.update_yaxes(categoryorder='total ascending', type='category')
    fig.update_layout(legend=dict(orientation='h',
                                  yanchor='top', y=1.05, x=1, xanchor='right'))
    return fig
