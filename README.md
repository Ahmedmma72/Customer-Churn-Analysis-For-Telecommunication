# Telecommunication Churn Analysis

## 📝 Table of Contents

- [Overview](#about)
- [Dataset](#dataset)
- [Tools &amp; Technologies](#tools)
- [Questions Answered](#questions)

## 🚩Overview `<a name = "about"></a>`

Customer churn is a major concern for telecommunications companies, as retaining existing customers is more cost-effective than acquiring new ones. The goal of this project is to analyze customer data, identify factors contributing to customer churn, and develop a predictive model to help the company reduce customer churn rates. Based on the insights gained, we will propose targeted marketing strategies and customer retention initiatives.

## 📊 Dataset `<a name = "dataset"></a>`
You can find the dataset we used for this project here:
`<br>`
[IBM Watson Analytics Sample Dataset - Telco Customer Churn]( https://www.kaggle.com/datasets/ylchang/telco-customer-churn-1113)

## 💻Tools & Technologies `<a name = "tools"></a>`

- **Python**
- **Jupyter Notebook**  
- **seaborn**
- **pandas**
- **sklearn**
- **tableau**

## 🧾 Questions Answered `<a name= "questions"></a>`

The project is divided into questions each in a separate folder inside which the code is found in a jupyter notebook. Each notebook is typically divided into 3 to 4 sections:
1. Question statement and Expectations
2. Exploratory Data Analysis
3. Model Building
4. Results Interpretation
   
We have the following types of questions to answer:

|Question Type | No. Questions|
|:---:|:---:|
|Descriptive | 2 |
|Exploratory |1 |
|Inferential | 4 |
| Predictive | 5 |
|Total |12 |

### Descriptive Questions

1. What is the distribution of customers across different Internet service types? and the churn rate for each type?
2. What is the distribution of customers across different payment methods, and which payment methods are associated with lower churn rates?

### Exploratory Question

3. What are the factors that affect customer satisfaction?

### Inferential Questions

4. Does customer churn depend on the customer contract segment?
5. Are customers with contracts of the type Month-to-Month more likely to churn? (ie. the churn proportion is higher for customers with Month-to-Month contracts by more than 25% than the other contract types)
6. Are customers with online security features less likely to churn? (i.e, churn proportion of customers without online security features are higher than those with security features by more than 25%)
7. Does the distribution of Internet types follow (70%   20%  10%) for DSL, Cable and Fiber respectively ?

### Predictive Questions

8. How well can we predict customer churn based on demographic features (gender, SeniorCitizen, Partner, and Dependents)?
9. Can we predict customer churn based on billing information (Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, and TotalCharges)?
10. What are the best predictors of Churn Value?
11. Are there any specific services or products that are more commonly associated with each reason category for churn? then, How well can we predict the churn reason category based on the services and products that a customer has?
12. Can we predict whether a customer will refer a friend or not ?













