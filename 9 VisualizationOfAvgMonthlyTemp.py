# Problem Statement 
# Develop a program to read a CSV file containing daily temperature data with columns like 'Date' and 'Temperature'. 
# Perform data analysis to compute the average temperature for each month. 
# Visualize the average monthly temperatures using a line chart.

import pandas as pd
import matplotlib.pyplot as plt

def compute_average_monthly_temperatures (file_path):
    df pd.read_csv(file_path, parse_dates=['Date'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['YearMonth'] = df ['Date'].dt.to_period('M')
    monthly_avg_temp = df.groupby('YearMonth') ('Temperature'].mean()
    return monthly_avg_temp

def visualize_average_monthly_temperatures (monthly_avg_temp):
    plt.figure(figsize=(10, 6))
    monthly_avg_temp.plot(kind='line', marker='o')
    plt.title('Average Monthly Temperature')
    plt.xlabel('Month')
    plt.ylabel('Average Temperature')
    plt.grid(True)
    plt.show()

file_path= input("Enter the path to the CSV file containing temperature data: ")

monthly_avg_temp = compute_average_monthly_temperatures (file_path)

visualize_average_monthly_temperatures (monthly_avg_temp)

