# Import necessary libraries
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Read the dataset containing per capita income data
data = pd.read_csv("canada_per_capita_income.csv")

# Rename the column for better understanding
data.rename(columns={"per capita income (US$)": "income"}, inplace=True)

# Display the data to ensure it's loaded correctly
data

# Scatter plot to visualize the relationship between year and income
plt.scatter(data[["year"]], data.income, color="red")
plt.xlabel("Year (input)")
plt.ylabel("Income (output)")
plt.title("Year vs Income")
plt.show()

# Initialize the linear regression model
model = LinearRegression()

# Define input (year) and output (income) variables
input = data[["year"]]  # Year as input feature
output = data.income    # Income as output target

# Fit the linear regression model to the data
model.fit(input, output)

# Read the test data (you should have test.csv file in the same directory)
df = pd.read_csv("test.csv")

# Predict the income based on the test data (year)
predict = model.predict(df).astype("int")

# Display the predicted income
predict

# Manually calculate the predicted income for the year 2000 using the linear regression formula
# y = mx + b, where m = 828.46507522 and b = -1632210.7578554575
predicted_income_2000 = 828.46507522 * 2000 + -1632210.7578554575
predicted_income_2000  # Show the manually calculated predicted income for the year 2000

# Plot the data points and the linear regression line
plt.scatter(data[["year"]], data.income, color="red")  # Scatter plot of actual data points
plt.xlabel("Year (input)")
plt.ylabel("Income (output)")
plt.plot(data[["year"]], model.predict(data[["year"]]), color="blue")  # Regression line
plt.title("Year vs Income with Linear Regression Line")
plt.show()
