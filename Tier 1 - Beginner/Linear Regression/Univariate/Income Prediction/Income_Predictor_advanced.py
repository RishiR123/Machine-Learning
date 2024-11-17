import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def load_data(file_path):
    data = pd.read_csv(file_path)
    data.rename(columns={'per capita income (US$)': 'income'}, inplace=True)
    return data

def train_model(data):
    input_data = data[['year']]
    output_data = data['income']
    model = LinearRegression()
    model.fit(input_data, output_data)
    return model

def make_predictions(model, test_data):
    predictions = model.predict(test_data)
    return predictions.astype('int')

def plot_data(data, model):
    plt.scatter(data[['year']], data['income'], color='red')
    plt.xlabel('year(input)')
    plt.ylabel('income(output)')
    plt.plot(data[['year']], model.predict(data[['year']]), color='blue')
    plt.title('Linear Regression Fit: Income vs Year')
    plt.show()

def main():
    data = load_data('canada_per_capita_income.csv')
    model = train_model(data)
    test_data = pd.read_csv('test.csv')
    predictions = make_predictions(model, test_data)
    print(predictions)
    plot_data(data, model)

if __name__ == "__main__":
    main()
