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
## Process
### Project Implementation
This is a data science project that predicts customers who default on their credit card refund. 
It is implemented using Python - Dash. To download the complete implementation code, visit this GitHub repo. 
The dataset used for this project was obtained here, and further useful details about this project implementation are found 
here.The dataset contains 30,000 rows and twenty-six columns of anonymous credit cardholders in Taiwan and their default status. Table.1 shows the head of the data. Steps taken to implement the project:
            1.	Data wrangling and feature engineering  
            2.	Exploratory Data Analysis and Visualization
            3.	Model implementation and Evaluation
            4.	Model Interpretation

#### Data Wrangling and Preprocessing:
I checked the data to identify the nature of the dataset; there was no record of missing data. The columns are all int values. I converted some columns to string datatypes using their categorical values. Some of the column names do not seem appealing; I modified their names. However, new features were created from the existing features. The columns are summarized as follows:
Default status: A binary variable showing default payment (Yes = 1, No = 0), as the response variable.
Limit Bal: Amount of the given credit (in NT dollar) includes both the individual consumer credit and their family (supplementary) credit.
Gender: (1 = male; 2 = female).
Education  lvl: (1 = graduate school; 2 = university; 3 = high school; 4 = others).
Mar_status (1 = married; 2 = single; 3 = others).
Age continuous variable
History of past payment. the past monthly payment records (from April to September 2005) as follows: 
Pay_Sept = the repayment status in September, 2005; 
Pay_Aug:  the repayment status in August 2005
Pay_April = the repayment status in April 2005. 
The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.
Bill_Sept – Bill_April: Amount of bill statement (NT dollar). 
Bill Sept = Amount of bill statement in September 2005; 
Bill Aug = Amount of bill statement in August till April 2005
Bill July = Amount of bill statement in Au, 2005. 
Pay_Amt_Sept – Pay_Amt_April 2005: Amount of last payment (NT dollar). 
Pay_amt_sept = amount paid in September and so on till Pay_amt_April, 2005; 
New features
Total paid: Sum of Amount paid (repayment) made by a customer from September to April. 
Total bill: Sum of all the bills accrued by a customer from September to April
Bal: The difference between the credit loan, the total amount paid, and the total bill, 
            """
    ),

        
    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
#### Exploratory Data Analysis and Visualization
Data Visualization presents the graphical representation of the distribution of each column, its relationships with the target variable.
I used a simple pie chart as shown in Fig.1 to show the distribution of defaulters. There are more defaulters (77%) than non-defaulters(22%). 
The pie chart shows an imbalanced class.Fig.2 shows the relationship between Marital status and credit card default. I observed that the married 
default more than singles and others.
            """
        ),
        html.Img(src='assets/fig1.png', className='img-fluid'),
        html.Img(src='assets/fig3.png', className='img-fluid'),
        
        dcc.Markdown(
            """
            I also checked the relationship between credit default and educational level and credit card default, as shown in Fig.3. 
            It is seen that those with high school degrees seem to have a higher tendency of defaulting when compared with those from 
            graduate schools, universities and others. I used the histogram in Fig.4 to show the frequency distribution of the age. 
            It is seen that the distribution is unimodal and left-skewed with some number of outliers. The mean age is 35, and the 
            median age is 34. 


            """
        
        ),

        html.Img(src='assets/fig4.png', className='img-fluid'),
        html.Img(src='assets/fig5.png', className='img-fluid'),
        
                
    ]
)
column3 = dbc.Col(
    [
        dcc.Markdown(
            """
### Predictive model.
            
The data set was randomly split into train and test set in the ratio of 80:20. 80% was used for training and cross-validation, 
while 20% was used for testing the model. To ensure proper implementation of a high precision predictive model, I implemented a linear 
model using Logistic regression. First, I created a data Pipeline for each classifier model by adding category encoders and simple 
imputers and then fitting each model to the dataset to find out the most well-fitted model for the selected dataset. The baseline score 
was 77% because of the imbalance class. Therefore, I decided to use ROC-AUC metric. The logistic regression score was 77%, so I decided 
to apply a tree model, I applied a decision tree classifier, and the validation score was 79%. I further tried the ensemble model; 
Random forest, and a validation score of 81% was obtained. I then applied an XGBoost classifier model, and the model gave a  
cross-validation score of 82%. I decided to work with the XGBoost classifier since it gave the highest AUC score. 
Hyperparameter tuning was done to select the best hyperparameters using Randomized Search CV.  
To select only the relevant features for the proper performance of the model, the feature importance of the predictor variables was 
generated and plotted. Fig 5 shows the top 10 features that are important for predicting credit card defaulters. 
Finally, the XGBClassifer model was applied to the test set to predict credit card defaulters.


            """   
        ),

        html.Img(src='assets/fig6.png', className='img-fluid')



    ]
)





layout = dbc.Row([column1, column2, column3])