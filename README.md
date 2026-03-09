# MTN Churn Intelligence System
*Predictive Retention & Customer Insight for Telecom  Growth*
![MTN Icon](https://upload.wikimedia.org/wikipedia/commons/2/29/MTN-Logo.png)
## Project Overview 
This project addresses a critical business challenge for **MTN Nigeria** as an increasing churning rate poses as an obstacle to business sustenance. This end-to-end system moves beyond static analysis to providing real-time prediction tool for identifying at-risk customers while focusing on the roll-out of 5G services and regional market pressures. 

### Business Goals
* Identification  of at-risk high-value customers before they switch to competitors.
* Identification of regional factors for churning
* Recommendation of a specific retention offer based on individual customer data usage and tenure.

### The Dataset
The project makes use of the **Kaggle's Q1 2025 MTN Nigeria Customer Churn Dataset** which includes 
* Service Metrics such as 5G router adoption, data plan types, average signal strength*
* Demographics such as Customer location, tenure and age group.
* Sentiment such as customer interaction logs and satisfaction score.

## Key Features
### 1. Exploratory Data Analysis

Comprehensive visuals were created using **Seaborn** and **Plotly** for revealing:
* Churn by Geography: Heatmap showing high-churn hotspots.
* Feature Correlation: showing customer loyalty
* Sentiment Analysis: For insights into customer review.

### 2. Predictive Modeling

An optimized XGBoost classifier for identifying churn patterns using:
* Metrics such as Recall and F1-Score to ensure not missing-out of at-risk customers.
* SHAP Values for the expalnation of why the model predicted a specific customer would churn

### 3. Automated Alerting System

A Python-based workflow is created for filtering high-value customers and the triggering of an automated alert when a satisfaction score drops below a specific threshold. 

### 4. Live Deployment 

A web-based dashboard is created for stakeholders for the:
* Computation of customer stats and performing some toogling based on tenure, data usage and complaints.
* Generation of real-time churn risk percentage for the recommendation of "Retention Action".

## Tech Stack
* Language: SQL and Python
* Libraries: Pandas, Sckitlearn, Matplotlib and Streamlit
* Deployment: Streamlit Cloud and Github


## Task Six: Model Selection and Building
The choice model for this project covers three main philosophies of classification, which includes Linearity, Geometric and Tree-based modeling. Overfitting in machine learning occurs when a model performed well at learning noise/random patterns in the training data and cannot generalize to new or unseen data. Signs of overfitting includes model accuracy score on training data to be at 99% but 70% on test data.
### The choice models for this project and their reasons are:
* Logistic Regression: To act as the baseline model as it is faster and higly interpretable
* Support Vector Machine: For helping to find the boundaries between churners and non-churners in high dimensional space.
* Random Forest: For tackling overfitting and handling the mix of categorical and numerical data, as they create many decision trees and average them
* XGBoost: It is the state of the art model for tabular churn data as it creates decision trees squentially and with each new tree correcting the errors of the previous one


## Task Nine: Business Intelligence Recommendation
The XGBoost modeling and SHAP result is telling us that:
* 1. The South West is the strongest driver for retention and the service standard here are blueprint for other regions
  2. Age is a strong predictor as younger customers are more likely to leave and so there is need for a youth-centric data bundles or social media driven loyalty rewards.
  3. Long-term "Loyal" vintage customers have shown higher churn than new ones. this suggests older customers feel neglected compared to new sign-ups.
  4. Customers using Broadband MiFi devices are more stable than SIM users and so there is need to incentivize SIM users in high-risk zones to help upgrade to MiFi or 5G routers.
