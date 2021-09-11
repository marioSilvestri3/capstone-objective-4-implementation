import streamlit as st
import pandas as pd
from functions import predict


def verify():
    st.write(st.session_state['Internet'])


def sidebar():
    with st.sidebar.form('prediction'):
        st.text('Churn Prediction Query')

        select_senior = st.radio(
            'Senior Citizen',
            ('Yes', 'No'),
            key='senior')

        select_dependent = st.radio(
            'Dependents',
            ('Yes', 'No'))

        select_lines = st.radio(
            'Multiple Lines',
            ('Yes', 'No'))

        select_internet = st.radio(
            'Internet',
            ('DSL', 'Fiber Optic', 'No'),
            key='internet', )

        st.text('Internet Services')
        select_security = st.checkbox('Online Security', key='security')
        select_backup = st.checkbox('Online Backup', key='backup')
        select_protection = st.checkbox('Device Protection', key='protection')
        select_tech = st.checkbox('Tech Support', key='tech')
        select_tv = st.checkbox('Streaming TV', key='tv')
        select_movies = st.checkbox('Streaming Movies', key='movies')

        select_contract = st.radio(
            'Contract',
            ('Month-to-month', 'One year', 'Two year'))

        select_paperless = st.radio(
            'Paperless Billing',
            ('Yes', 'No'))

        select_payment = st.radio(
            'Payment Method',
            ('Mailed check', 'Electronic Check', 'Credit card (automatic)', 'Bank transfer (automatic)'))

        submitted = st.form_submit_button('Predict')
        if submitted:
            keys = ['security', 'backup', 'protection', 'tech', 'tv', 'movies']
            if st.session_state['internet'] == 'No':
                for key in keys:
                    if st.session_state[key]:
                        st.write('Select an Internet Service type '
                                 'or deselect all Internet Services')
                        break

            X = pd.DataFrame({'Senior Citizen': [st.session_state['senior']],
                              # TODO
                              })
