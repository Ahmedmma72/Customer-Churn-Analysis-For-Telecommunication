import pandas as pd

def readAll_ImortantFeat():
    # Load the first dataset from ../Dataset/Telco_customer_churn_services.xlsx
    services = pd.read_excel('../Dataset/Telco_customer_churn_services.xlsx')
    # Load the second dataset from ../Dataset/Telco_customer_churn.xlsx
    compound = pd.read_excel('../Dataset/Telco_customer_churn.xlsx')
    # Load the data from /Dataset/Telco_customer_churn_demographics.xlsx
    demographics = pd.read_excel('../Dataset/Telco_customer_churn_demographics.xlsx')
    # rename the column to match the column name in the dataset
    compound.rename(columns={'CustomerID': 'Customer ID'}, inplace=True)
    # Join the two datasets on the column 'Customer ID'
    dataset1 = pd.merge(demographics, compound, on='Customer ID')
    my_columns = ['Gender_x', 'Age', 'Married',
              'Number of Dependents', 'Churn Value', 'Tenure Months', 'Churn Score', 'Monthly Charges', 'Customer ID', 'CLTV']

    dataset1 = dataset1[my_columns]
    # merge with services dataset
    dataset = pd.merge(services, dataset1, on='Customer ID')
    my_columns += ['Phone Service', 'Internet Service', 'Multiple Lines',
               'Online Security', 'Online Backup', 'Device Protection Plan', 'Premium Tech Support', 'Unlimited Data', 'Total Revenue', 'Referred a Friend']

    dataset = dataset[my_columns]

    # rename Gender_x to gender
    dataset.rename(columns={'Gender_x' : 'Gender'},inplace=True)
    # Load the data from /Dataset/Telco_customer_churn_status.xlsx
    status = pd.read_excel('../Dataset/Telco_customer_churn_status.xlsx')
    # -------------
    columns = ['Customer ID', 'Satisfaction Score', 'Churn Category']
    status1 = status[columns]
    # merge with dataset
    dataset = pd.merge(dataset, status1, on='Customer ID')
    # drop the columns 'Customer ID' and Churn Category if they exist
    churn_category = dataset['Churn Category']
    if 'Customer ID' in dataset.columns:
        dataset.drop(['Customer ID', 'Churn Category'], axis=1, inplace=True)
    
    # get the dummy variables for the categorical feature and store it in a new variable
    dataset = pd.get_dummies(dataset,drop_first=True)

    # rename features to remove _yes 
    if 'Married_Yes' in dataset.columns:
        dataset.rename(columns={'Married_Yes':'Married','Gender_Male': 'Gender','Phone Service_Yes':'Phone Service', 'Internet Service_Yes':'Internet Service', 'Multiple Lines_Yes':'Multiple Lines',
                        'Online Security_Yes':'Online Security', 'Online Backup_Yes':'Online Backup','Device Protection Plan_Yes':'Device Protection Plan',
                        'Premium Tech Support_Yes':'Premium Tech Support','Unlimited Data_Yes':'Unlimited Data','Referred a Friend_Yes':'Referred a Friend'}, inplace=True)
    
    # merging back the Churn Category feature
    dataset['Churn Category'] = churn_category

    # return the dataset
    return dataset