import pandas as pd
import sklearn.linear_model

# Function to load and clean the data
def load_and_clean_data(filename):
    data = pd.read_csv(filename)

    # Map 'experience' values to numeric equivalents
    exp = {"five": 5, "two": 2, "seven": 7, "three": 3, "ten": 10, "eleven": 11}
    data["experience"] = data.experience.map(exp)

    # Fill missing values in 'experience' and 'test_score'
    data["experience"].fillna(data["experience"].median(), inplace=True)
    data["test_score(out of 10)"].fillna(data["test_score(out of 10)"].mean(), inplace=True)

    return data

# Function to train the linear regression model
def train_model(data):
    model = sklearn.linear_model.LinearRegression()
    model.fit(data[["experience", "test_score(out of 10)", "interview_score(out of 10)"]], data["salary($)"])
    return model

# Function to make predictions
def make_prediction(model, experience, test_score, interview_score):
    return model.predict([[experience, test_score, interview_score]])

# Function to display model coefficients and intercept
def display_model_details(model):
    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)

# Main execution flow
if __name__ == "__main__":
    # Load and clean the data
    data = load_and_clean_data("hiring.csv")

    # Train the model
    model = train_model(data)

    # Display model details
    display_model_details(model)

    # Make a prediction for a new set of inputs
    prediction = make_prediction(model, 7, 8, 9)
    print("Prediction for experience=7, test_score=8, interview_score=9:", prediction)

    # Manual prediction using the model's coefficients
    manual_prediction = 2823.76559304*7 + 1329.00027432*8 + 2929.14459978*9 + 11842.306307731225
    print("Manual Prediction:", manual_prediction)
