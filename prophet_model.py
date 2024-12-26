import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load your time series data into a DataFrame
# Replace 'your_data.csv' with the actual filename/path
data = pd.read_csv('your_data.csv')

# Check the structure of your data
print(data.head())

# Initialize an empty dictionary to store the Prophet models
prophet_models = {}

# Iterate over each column (assuming they are all time series data)
for column in data.columns:
    # Prepare the data for Prophet (renaming columns to 'ds' and 'y')
    df = data[['date_column', column]].rename(columns={'date_column': 'ds', column: 'y'})

    # Initialize Prophet model
    model = Prophet()

    # Fit the model
    model.fit(df)

    # Store the model in the dictionary
    prophet_models[column] = model

# Define the number of periods for future prediction
future_periods = 12  # Example: predict the next 12 months

# Initialize an empty DataFrame to store the forecasts
forecasts = pd.DataFrame()

# Iterate over each column and make predictions
for column, model in prophet_models.items():
    # Make future dataframe for prediction
    future = model.make_future_dataframe(periods=future_periods, freq='M')

    # Make predictions
    forecast = model.predict(future)

    # Append the forecasted values to the forecasts DataFrame
    forecasts[column] = forecast['yhat']

# Plot the forecasts
plt.figure(figsize=(10, 6))
for column in forecasts.columns:
    plt.plot(forecasts.index, forecasts[column], label=column)
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Forecasted Values')
plt.legend()
plt.show()
