# Salary Prediction using Linear Regression
-This project predicts salary based on experience, test scores, and interview scores using linear regression. It demonstrates the basic process of data cleaning, model training, prediction, and evaluation.

# Project Overview
-**Goal**: Predict the salary of an individual based on their experience, test score, and interview score.
-**Type**: Multivariate Regression
-**Libraries Used**:
  -**pandas**: For data manipulation and preprocessing.
  -**scikit-learn**: For building and evaluating the linear regression model.

## **Explanation**

### **Data Preprocessing**
The dataset is preprocessed by mapping experience values to numerical values and filling missing data in the 'experience' and 'test_score' columns using the median and mean, respectively. This ensures that the data is clean and ready for model training.

### **Model Training**
The model is trained using the **Linear Regression** algorithm. The input features (independent variables) are `experience`, `test_score`, and `interview_score`, and the target (dependent variable) is `salary`. The model learns the relationship between these features and salary to make predictions.

### **Prediction**
Once the model is trained, it can predict salary for any new set of input data (experience, test score, and interview score). We also demonstrate manual salary prediction using the regression coefficients.

### **Manual Calculation**
In addition to using the model for predictions, we manually calculate the predicted salary using the formula for linear regression:  
**y = mx1 + mx2 + mx3 + b**, where `m` are the coefficients for each feature, and `b` is the intercept.

### **Model Evaluation**
The model's performance can be evaluated by inspecting the model coefficients and intercept. However, for a more comprehensive evaluation, we could look at **R-squared (R²)**, which measures how well the model explains the variation in salary.



