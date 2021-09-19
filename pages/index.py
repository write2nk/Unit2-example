# Imports from 3rd party libraries

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict customers who will default!


            A credit default represents the financial failure of an entity. 
            Default is the failure to repay a debt, including interest or principal, on a loan or security.
            This App  predicts who is capable of defaulting in a credict card payment based on the following criteria:
            Limit Balance, Education Level, marital status, Repayment level, Age, Total Amount paid, Total bills accrued. 

            This App will benefit the financial institution when giving loans/credits to individuals, to
            predict a customer who would default in their credit repayment. 

            To use this app, just toggle the buttons and set the feature variables to your own
            custom values. Click this link to use this web app and predict a credit card defaulter. 
            Click the predict credit defaulter button to get started!

            """
        ),
        dcc.Link(dbc.Button('Predict Credit Defaulter', color='primary'), href='/predictions')
    ],
    md=4,
)
df = pd.read_csv(r"C:\\Users\\Nkiru\\Unit2-example\\data\\my_file1.csv")
fig = px.bar(df, x="Education_Level", y="Age", color="Default_Status", barmode="group")
#app.layout = html.Div(children=[
#    html.H1(children='Hello Dash'),

#    html.Div(children='''
#        Dash: A web application framework for your data.
#    '''),
#    ])





app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

])


column2 = dbc.Col(
    [
         dcc.Graph(id='example-graph',figure=fig),
    ]
)

layout = dbc.Row([column1, column2])