# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
best_xgb = load('assets/best_xgb.joblib')
print('Model loaded successfully')

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('limit-bal', 'value'),
    Input('pay-level', 'value'),
    Input('total-bill', 'value'),
    Input('total-paid', 'value'),
    Input('education-lvl', 'value')]
)

def predict(limit_bal, pay_level, total_bill, total_paid,  education_lvl):
    df = pd.DataFrame(
        columns  = ['Limit_Bal', 'Pay_Level', 'Total_bill', 'Total_paid',  'Education_lvl'],
        data = [[limit_bal, pay_level, total_bill, total_paid,  education_lvl]]
    )

    y_pred = best_xgb.predict(df)[0]

    if y_pred == 1:
        return f'The model predicted {y_pred} implies that the customer will default'
    else:
        return f'The model predicted {y_pred} implies that the customer will not default'
    #return f'The model predicted thet the cutomer has {y_pred} default'



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictors', className='mb-5'), 
        dcc.Markdown('#### Limit Bal'), 
        dcc.Input(
            id = 'limit-bal',
            placeholder='Enter Limit Bal', 
            type = 'number',
            value = '10000',
            className='mb-5',  
        ), 

        dcc.Markdown('#### Total Bill'), 
        dcc.Input(
            id = 'total-bill',
            placeholder='Enter Total Bill', 
            type = 'number',
            value = '1000',
            className='mb-5',  
        ), 

         dcc.Markdown('#### Total Paid'), 
        dcc.Input(
            id = 'total-paid',
            placeholder='Enter Total paid', 
            type = 'number',
            value = '1000',
            className='mb-5',  
        ), 

        
        dcc.Markdown('#### Pay Level'), 
        dcc.Slider(
            id='pay-level', 
            min=-2, 
            max=8, 
            step=1, 
            value=-2, 
            marks={n: str(n) for n in range(-2,9,1)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Education Level'), 
        dcc.Dropdown(
            id='education-lvl', 
            options = [
                {'label': 'Graduate School', 'value': 'Graduate School'}, 
                {'label': 'university', 'value': 'university'}, 
                {'label': 'high school', 'value': 'high school'}, 
                {'label': 'others', 'value': 'others'},  
            ], 
            value = 'Graduate School', 
            className='mb-5', 
        ), 
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.H2('Credit Defaulter', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])