import streamlit as st
import pandas as pd
from functions import predict

keys = ['security', 'backup', 'protection', 'support', 'tv', 'movies']


def sidebar():
    with st.sidebar.form('prediction'):
        st.subheader('Churn Prediction Query')

        select_senior = st.radio(
            'Senior Citizen', (
                'Yes', 'No'),
            key='senior')

        select_dependent = st.radio(
            'Dependents', (
                'Yes', 'No'),
            key='dependents')

        select_lines = st.radio(
            'Multiple Lines', (
                'Yes', 'No', 'No Phone Service'),
            key='lines')

        select_internet = st.radio(
            'Internet Service', (
                'DSL', 'Fiber Optic', 'No'),
            key='internet')

        st.text('Internet Subscriptions')

        select_security = st.checkbox(
            'Online Security',
            key='security')
        select_backup = st.checkbox(
            'Online Backup',
            key='backup')
        select_protection = st.checkbox(
            'Device Protection',
            key='protection')
        select_tech = st.checkbox(
            'Tech Support',
            key='support')
        select_tv = st.checkbox(
            'Streaming TV',
            key='tv')
        select_movies = st.checkbox(
            'Streaming Movies',
            key='movies')

        select_contract = st.radio(
            'Contract', (
                'Month-to-month', 'One year', 'Two year'),
            key='contract')

        select_paperless = st.radio(
            'Paperless Billing', (
                'Yes', 'No'),
            key='paperless')

        select_payment = st.radio(
            'Payment Method', ('Mailed check',
                               'Electronic Check',
                               'Credit card (automatic)',
                               'Bank transfer (automatic)'),
            key='payment')

        submitted = st.form_submit_button('Predict')
        if submitted:
            st.write("")
            if st.session_state['internet'] == 'No':
                for key in keys:
                    if st.session_state[key]:
                        st.error('Error: Select an Internet Service (DSL/Fiber Optic) '
                                 'or deselect all Internet Subscriptions')
                        return

            X_row = dict.fromkeys(['Senior Citizen_Yes',
                                   'Dependents_Yes',
                                   'Multiple Lines_No phone service',
                                   'Multiple Lines_Yes',
                                   'Internet Service_Fiber optic',
                                   'Internet Service_No',
                                   'Online Security_No internet service',
                                   'Online Security_Yes',
                                   'Online Backup_No internet service',
                                   'Online Backup_Yes',
                                   'Device Protection_No internet service',
                                   'Device Protection_Yes',
                                   'Tech Support_No internet service',
                                   'Tech Support_Yes',
                                   'Streaming TV_No internet service',
                                   'Streaming TV_Yes',
                                   'Streaming Movies_No internet service',
                                   'Streaming Movies_Yes',
                                   'Contract_One year',
                                   'Contract_Two year',
                                   'Paperless Billing_Yes',
                                   'Payment Method_Credit card (automatic)',
                                   'Payment Method_Electronic check',
                                   'Payment Method_Mailed check'], [0])

            if st.session_state['senior'] == 'Yes':
                X_row['Senior Citizen_Yes'] = [1]

            if st.session_state['dependents'] == 'Yes':
                X_row['Dependents_Yes'] = [1]

            if st.session_state['lines'] == 'No Phone Service':
                X_row['Multiple Lines_No phone service'] = [1]

            if st.session_state['lines'] == 'Yes':
                X_row['Multiple Lines_Yes'] = [1]

            if st.session_state['internet'] == 'No':
                X_row['Internet Service_No'] = [1]
                X_row['Online Security_No internet service'] = [1]
                X_row['Online Backup_No internet service'] = [1]
                X_row['Device Protection_No internet service'] = [1]
                X_row['Tech Support_No internet service'] = [1]
                X_row['Streaming TV_No internet service'] = [1]
                X_row['Streaming Movies_No internet service'] = [1]

            if st.session_state['internet'] == 'Fiber Optic':
                X_row['Internet Service_Fiber optic'] = [1]

            if st.session_state['security']:
                X_row['Online Security_Yes'] = [1]

            if st.session_state['backup']:
                X_row['Online Backup_Yes'] = [1]

            if st.session_state['protection']:
                X_row['Device Protection_Yes'] = [1]

            if st.session_state['support']:
                X_row['Tech Support_Yes'] = [1]

            if st.session_state['tv']:
                X_row['Streaming TV_Yes'] = [1]

            if st.session_state['movies']:
                X_row['Streaming Movies_Yes'] = [1]

            if st.session_state['contract'] == 'One year':
                X_row['Contract_One year'] = [1]

            if st.session_state['contract'] == 'Two year':
                X_row['Contract_Two year'] = [1]

            if st.session_state['paperless'] == 'Yes':
                X_row['Paperless Billing_Yes'] = [1]

            if st.session_state['payment'] == 'Credit card (automatic)':
                X_row['Payment Method_Credit card (automatic)'] = [1]

            if st.session_state['payment'] == 'Electronic check':
                X_row['Payment Method_Electronic check'] = [1]

            if st.session_state['payment'] == 'Mailed check':
                X_row['Payment Method_Mailed check'] = [1]

            X_row = pd.DataFrame.from_dict(X_row)

            prediction = int(predict(X_row))

            markdown = 'Prediction: ' + ('**Churn**' if prediction else '**Won\'t Churn**')

            prediction_box = st.markdown(markdown)
