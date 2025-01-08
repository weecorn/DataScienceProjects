import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ta  # technical analysis package

BMW = 'BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

# Calculate the daily percentage change
df['Daily_Return'] = df['Adj_Close'].pct_change() * 100

# Calculate the 50-day rolling volatility
df['Volatility_50D'] = df['Daily_Return'].rolling(window=50).std()

# Plot the rolling volatility
plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Volatility_50D'], color='orange', label='50-Day Rolling Volatility')
plt.title('BMW 50-Day Rolling Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility (%)')
plt.legend()
plt.grid(True)
plt.show()

# Create subplots to compare price and volatility
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Price subplot
ax1.plot(df['Date'], df['Adj_Close'], color='blue', label='Adjusted Close Price')
ax1.set_ylabel('Price')
ax1.legend(loc='upper left')
ax1.grid(True)

# Volatility subplot
ax2.plot(df['Date'], df['Volatility_50D'], color='orange', label='50-Day Rolling Volatility')
ax2.set_ylabel('Volatility (%)')
ax2.legend(loc='upper left')
ax2.grid(True)

plt.xlabel('Date')
plt.suptitle('BMW Price and Volatility')
plt.show()