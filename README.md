Multi-Series Time Series Forecasting with Prophet

This script forecasts values for multiple time series data present in a CSV file.

Requirements:

pandas
prophet
matplotlib
How to Use:

Data Preparation:

Replace "your_data.csv" in the script with the actual filename and path to your CSV file.
Ensure your data has two columns:
A date column named "date_column" formatted as dates (e.g., YYYY-MM-DD).
Each additional column represents a separate time series you want to forecast.
Run the Script:

Bash

python multi_series_forecasting.py
Output:

The script generates a plot visualizing the predicted values for each time series in your data. The x-axis represents the date, and the y-axis represents the predicted values. Each time series has its own line in the plot with a corresponding legend entry.

Additional Notes:

The script uses the Prophet library's default model parameters. You can explore the Prophet documentation for customization options.
The script predicts for the next future_periods (currently set to 12) based on the frequency specified (set to 'M' for monthly). Adjust these values as needed.
Further Development:

Implement functionalities to save the forecasts to a file.
Allow users to specify model parameters through script arguments.
