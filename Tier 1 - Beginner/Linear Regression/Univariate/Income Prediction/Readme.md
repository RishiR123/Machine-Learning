# **Salary Prediction using Linear Regression**

This project predicts salary based on experience, test scores, and interview scores using linear regression. It demonstrates the basic process of data cleaning, model training, prediction, and evaluation.

## **Overview**
-**Goal**: Predict the salary of an individual based on their experience, test score, and interview score.
-**Type**: Multivariate Regression
-Libraries Used:
  -**pandas**: For data manipulation and preprocessing.
  -**scikit**-learn: For building and evaluating the linear regression model.


## **How to Run**
1. Clone the repository and navigate into the project folder.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the model script `salary_predictor.py` to train and make predictions.

## **Requirements**
- Python 3.8+
- Libraries: `pandas`, `scikit-learn`




# Income Prediction using Linear Regression

This project uses linear regression to predict income based on the year using the "Canada Per Capita Income" dataset.

## **Project Overview**
In this project, we have used **linear regression** to predict income based on the year. We begin by visualizing the relationship between the year and income, fitting a linear regression model, and then predicting income for future years.

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

## **Requirements**
- `pandas`
- `scikit-learn`



To install the dependencies, run:
```bash
 pip install -r requirements.txt
```


## **Results**
The model uses linear regression to predict income based on experience and test scores. You can modify the input features (experience, test scores) in the script to test the model with different data points.

Stay tuned for updates as new features and improvements are added to this project!






