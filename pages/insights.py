# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
## Insights
### Permutation Importance.
I applied the permutation importance to understand how the presence of each feature affects the model performance.
 Model accuracy mostly suffers if we shuffle a column that is most important to a model for prediction. The first row shows how 
 much model performance decreased with a random shuffling (in this project, I used "ROC-AUC" as the performance metric). 
 The amount of randomness in the permutation importance calculation is measured by repeating the process with multiple shuffles—the 
 figure after the ± measures how performance varied from one reshuffling to the next. The summary of the features and their weight 
 importance is shown in table 2 in their decreasing order.  It is shown that the Total bill accrued by the customer is the most 
 important feature, followed by total paid, the remaining balance, Pay sept which shows the number of months a customer have offset 
 their debt, the limit balance, which is the credit amount and finally the age. 

            """
        ),
        html.Img(src='assets/fig7.png', className='img-fluid')

    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
### Partial Dependency Plot
Partial dependence plots show how each variable or predictor affects the model's predictions. This is useful for 
ensuring the impact of each variable on another variable. For example, one may ask, what impact do Age and Marital status have 
on credit default? To rephrase this, I want to fully understand how variations in age or marital status would affect credit default. 
Fig. 1 shows The PDP Plot for Gender, while Fig.2 shows the PDP plot for Marital staus and Limit Balance
            """
        ),
        html.Img(src='assets/Fig8.png', className='img-fluid'),
        html.Img(src='assets/Fig9.png', className='img-fluid')

    ],
)

column3 = dbc.Col(
    [
        dcc.Markdown(
            """
#### Explaining the prediction with Shap 
SHAP values break down a prediction to show the impact of each feature. The SHAP value explains why the model says 
that a customer would default or not default in this project.  Fig 3 shows the SHAP values for the feature variables. 
The feature variables that mostly influence the model's performance are in pink color with their visual sizes, 
which shows the magnitude of the feature's effect, The feature values that decrease the prediction are in blue. 
If you subtract the length of the blue bars from the length of the pink bars, it equals the distance from the base 
value to the output. The model predicted 71%, while the base value is 0.1818. Fig. 4 shows a printout of a summary 
of prediction with explainability.

            """
        ),
        html.Img(src='assets/Fig10.png', className='img-fluid'),
       

        dcc.Markdown(
            """
            In conclusion, I have identified the most important features that enhance the prediction of a credit 
            cardholder. They include Total Bills, Total paid, Balance,  Limit Balance, Pay_Sept, and Age, 
            although the educational level is a bit close but doesn't significantly affect the model prediction 
            performance. This project is beneficial to the financial institution to predict credit cardholders who 
            would default. If you have found this app useful, kindly share to increase visibility! 
 


            """
        
        ),
         html.Img(src='assets/Fig11.png', className='img-fluid')

    ],
)


layout = dbc.Row([column1, column2, column3])