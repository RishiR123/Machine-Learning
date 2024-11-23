
# Radiation Level Prediction Based on Environmental Factors

This project predicts radiation levels using synthetic data based on environmental factors such as temperature, humidity, altitude, and distance from the source. A regression model is trained on this data to make predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Project Overview

This project generates synthetic data and uses a regression model to predict radiation levels. The environmental factors considered include:
- Temperature (°C)
- Humidity (%)
- Altitude (meters)
- Distance from the source (km)

The radiation level is calculated using a simplistic formula:
```
Radiation Level = 0.5 * (Altitude / 100) + (5 / Distance) + Noise
```

## Requirements

The following Python packages are required to run the project:

- numpy
- pandas
- scikit-learn
- matplotlib

You can install the dependencies using:
```
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
```
git clone <repository-url>
```
2. Navigate to the project directory:
```
cd radiation-level-prediction
```

## Usage

1. Run the script to generate synthetic data, train the model, and visualize the results:
```
python radiation_prediction.py
```

2. The script outputs a scatter plot comparing the actual vs predicted radiation levels.

## Results

The model's performance is visualized using a scatter plot, where the actual radiation levels are plotted against the predicted values. A diagonal reference line represents perfect predictions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
