import os
import numpy as np
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings
from sklearn.metrics import mean_squared_error
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import timedelta


def predict_and_save_stock_graph(stock_symbol):
    # Pull data from Yahoo Finance
    data = yf.download(stock_symbol, start="2020-01-01", end="2023-12-31")

    # Feature Engineering
    for i in range(1, 6):
        data[f'Close_Lag_{i}'] = data['Close'].shift(i)
    data.dropna(inplace=True)
    features = [f'Close_Lag_{i}' for i in range(1, 6)]
    X = data[features]
    y = data['Close']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Linear Regression - Training 
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_predictions = lr_model.predict(X_test)
    lr_mse = mean_squared_error(y_test, lr_predictions)
    print(f"Linear Regression MSE: {lr_mse:.2f}")

    # Create future dates for prediction (from 2024 to 2025)
    last_date = data.index[-1]
    future_dates = [last_date + timedelta(days=i) for i in range(1, 365 * 1 + 1, 5)]

    # Initialize the first set of inputs for prediction
    last_actual_data = data.tail(len(features))

    # Predict future prices
    future_predictions = list(last_actual_data['Close'])  # Start with the last known values

    for i in range(len(future_dates)):
        # Using the last 5 known values for prediction
        input_data = future_predictions[-len(features):]

        if len(input_data) == len(features):
            prediction = lr_model.predict([input_data])[0]
            future_predictions.append(prediction)
        else:
            break

    # Create a DataFrame for predictions
    future_data = pd.DataFrame(index=future_dates[:len(future_predictions)-len(features)], data=future_predictions[len(features):], columns=['Close'])

    # Visualization
    plt.figure(figsize=(15, 7))
    plt.plot(data.index, data['Close'], label='Actual', color='blue', marker='o')
    plt.plot(future_data.index, future_data['Close'], label='Linear Regression Predicted', color='red', linestyle='dashed')
    plt.title(f'Actual vs Predicted Close Prices for {stock_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    # Define the path for saving the image
    image_folder = 'static/images'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    file_name = f'{stock_symbol}_prediction.png'
    image_path = os.path.join(image_folder, file_name)

    # Save the plot to the specified path and return
    plt.savefig(image_path)
    return image_path

# Example usage
predict_and_save_stock_graph("AAPL")  
