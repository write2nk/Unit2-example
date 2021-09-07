# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

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
            Default is the failure to repay a debt, including interest or principal, on a loan or security
            This App  predicts who is capable of defaulting in a credict card payment based on the follwoing criteria:
            Limit Balance, Education Level, marital status, Repayment level, Total Amount paid, Total bills accrued. 

            This App will benefit the financial institution when giving loans/credits to individuals, to
            predict a customer who would default in their credit repayment. 

            Click the predict credit defaulter button to get

            You can use this app to predict a customer that is capable of defaulting

            """
        ),
        dcc.Link(dbc.Button('Predict Credit Defaulter', color='primary'), href='/predictions')
    ],
    md=4,
)



column2 = dbc.Col(
    [
        html.Img(src='assets/image1.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])