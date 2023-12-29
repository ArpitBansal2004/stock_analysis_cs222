import requests
import csv
from datetime import datetime, timedelta

# Alpha Vantage API key
api_key = 'EX0PX7Y0QFSFK7TI'

# Define the stock symbol
symbol = 'AAPL'

# Define the date range for the past 20 years
end_date = datetime.now()
start_date = end_date - timedelta(days=20 * 365)  # 20 years

# Initialize an empty list to store data
all_data = []

# Calculate the number of years to cover with each API request
years_per_request = 5

# Calculate the number of API requests needed
num_requests = (end_date.year - start_date.year) // years_per_request + 1

# Loop through the API requests
for i in range(num_requests):
    
    # Calculate the start and end years for the current request
    request_start_year = start_date.year + i * years_per_request
    request_end_year = min(start_date.year + (i + 1) * years_per_request, end_date.year)
    
    # Construct the API URL for monthly data for the current request
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={api_key}&datatype=json'
    
    # Make an HTTP GET request to fetch the data
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Check if the data was retrieved successfully
        if 'Monthly Adjusted Time Series' in data:
            monthly_data = data['Monthly Adjusted Time Series']
            
            # Filter data for the current request's years
            filtered_data = {date: info for date, info in monthly_data.items() if
                             int(date.split('-')[0]) >= request_start_year and
                             int(date.split('-')[0]) <= request_end_year}
            
            # Append the filtered data to the list
            all_data.extend(filtered_data.items())
        else:
            print(f"No data found for years {request_start_year}-{request_end_year}")
    else:
        print(f"Error fetching data for years {request_start_year}-{request_end_year}")

# Create and write data to a CSV file
with open(f'{symbol}_historical_data_20_years.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header row
    csv_writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    
    # Write data rows
    for date, info in all_data:
        row = [date, info['1. open'], info['2. high'], info['3. low'], info['4. close'], info['6. volume']]
        csv_writer.writerow(row)

print(f"Historical data for {symbol} (past 20 years) saved to {symbol}_historical_data_20_years.csv")
