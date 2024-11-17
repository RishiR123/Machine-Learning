# **Income Prediction - Univariate Project**

This project predicts income based on a single feature, using experience and test scores. It demonstrates basic machine learning techniques, including data preprocessing, linear regression, and model evaluation.

## **Overview**
- **Goal**: Predict the income of an individual based on their experience and test scores.
- **Type**: Univariate Regression
- **Libraries Used**:
  - `pandas`: For data manipulation and preprocessing.
  - `scikit-learn`: For building and evaluating the linear regression model.
  - `matplotlib`: For data Vizualization


## **How to Run**
1. Clone the repository and navigate into the project folder.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the model script `salary_predictor.py` to train and make predictions.

## **Requirements**
- Python 3.8+
- Libraries: `pandas`, `scikit-learn` , `matplotlib`


**minimal explanation**

# Income Prediction using Linear Regression

This project uses linear regression to predict income based on the year using the "Canada Per Capita Income" dataset.

## **Project Overview**
In this project, we have used **linear regression** to predict income based on the year. We begin by visualizing the relationship between the year and income, fitting a linear regression model, and then predicting income for future years.

## **Explanation**

### **Data Visualization**
We start by visualizing the data using a scatter plot. The plot helps us observe the relationship between the year (input) and income (output). From the visualization, we can see that there is a linear trend, which suggests that linear regression is an appropriate model for this task.

### **Model Training**
The model is trained using the **Linear Regression** algorithm. We use the year as the input feature (independent variable) and income as the target (dependent variable). The model learns the relationship between the year and income to make predictions.

### **Prediction**
Once the model is trained, we use it to predict income for new input data. The model generates predictions for income based on the year input.

### **Manual Calculation**
In addition to the model's predictions, we manually calculate the predicted income for specific years using the formula of linear regression:  
**y = mx + b**, where `m` is the slope and `b` is the intercept.

### **Plotting the Regression Line**
After training the model, we plot the regression line along with the data points. The regression line helps us visually verify how well the model fits the data. A good fit means that the line closely follows the trend of the data points.

### **Model Evaluation**
The model’s performance is evaluated using **R-squared (R²)**, a statistical measure that tells us how well the regression model explains the variation in the target variable. An R² value close to 1 indicates that the model explains most of the variance in the data, while a value closer to 0 suggests that the model does not explain much of the variance.

## **Dataset**
The project uses the following datasets:
- **canada_per_capita_income.csv**: Contains the data for the year and corresponding per capita income.
- **test.csv**: Contains test data for which income predictions are made.

## **Requirements**
- `pandas`
- `scikit-learn`
- `matplotlib`


To install the dependencies, run:
```bash
 pip install -r requirements.txt
```

Run the model: You can run the model training and prediction script by executing:

```bash
Tier 1 - Beginner/Linear Regression/Univariate/Income Prediction/Income_predictor.py

```

## **Results**
The model uses linear regression to predict income based on experience and test scores. You can modify the input features (experience, test scores) in the script to test the model with different data points.

Stay tuned for updates as new features and improvements are added to this project!






