import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ta

BMW = 'BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

# --- Calculate the daily price change ---
df['Price_Change'] = df['Adj_Close'].diff() 

# --- Plot the daily price change ---
plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Price_Change'], color='blue', label='Daily Price Change')
plt.title('BMW Daily Price Change')
plt.xlabel('Date')
plt.ylabel('Price Change')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Add a horizontal line at 0
plt.legend()
plt.grid(True)
plt.show()

# --- Histogram of daily price changes ---
plt.figure(figsize=(12, 5))
plt.hist(df['Price_Change'].dropna(), bins=50, color='purple', alpha=0.7) 
plt.title('Histogram of BMW Daily Price Changes')
plt.xlabel('Price Change')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# --- Scatter plot of Volume vs. Price Change ---
plt.figure(figsize=(12, 5))
plt.scatter(df['Volume'], df['Price_Change'], color='green', alpha=0.5)
plt.title('Scatter Plot of Volume vs. Price Change')
plt.xlabel('Volume')
plt.ylabel('Price Change')
plt.grid(True)
plt.show()



