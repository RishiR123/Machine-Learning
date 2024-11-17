import pandas as pd
import sklearn.linear_model

# Load the dataset
data = pd.read_csv("hiring.csv")

# Create a dictionary to map experience as strings to numbers
exp = {"five": 5, "two": 2, "seven": 7, "three": 3, "ten": 10, "eleven": 11}

# Convert the 'experience' column to numerical values using the mapping
data["experience"] = data.experience.map(exp)

# Fill any missing values in the 'experience' column with the median value
data["experience"].fillna(data["experience"].median(), inplace=True)

# Fill any missing values in the 'test_score' column with the mean value
data["test_score(out of 10)"].fillna(data["test_score(out of 10)"].mean(), inplace=True)

# Initialize the Linear Regression model
model = sklearn.linear_model.LinearRegression()

# Fit the model using the relevant columns: experience, test_score, and interview_score to predict salary
model.fit(data[["experience", "test_score(out of 10)", "interview_score(out of 10)"]], data["salary($)"])

# Print the model's coefficients and intercept
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

# Make a prediction for a new set of inputs (e.g., experience=7, test_score=8, interview_score=9)
prediction = model.predict([[7, 8, 9]])
print("Prediction for experience=7, test_score=8, interview_score=9:", prediction)

# Manual prediction using the model's coefficients
manual_prediction = 2823.76559304*7 + 1329.00027432*8 + 2929.14459978*9 + 11842.306307731225
print("Manual Prediction:", manual_prediction)
