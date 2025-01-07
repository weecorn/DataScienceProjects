import pandas as pd
import matplotlib.pyplot as plt
from seaborn import lineplot
from warnings import filterwarnings
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import ta  # technical analysis package

BMW = 'BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

filterwarnings(action='ignore', category=FutureWarning)

# define default figure size
FIGSIZE = (12, 5)

# --- Bollinger Bands ---
df['Bollinger_High'] = ta.volatility.bollinger_hband(df['Adj_Close'], window=20, window_dev=2)
df['Bollinger_Low'] = ta.volatility.bollinger_lband(df['Adj_Close'], window=20, window_dev=2)
df['Bollinger_Mid'] = ta.volatility.bollinger_mavg(df['Adj_Close'], window=20)

# --- Limit the date range ---
# start_date = '2023-01-01' 
# end_date = '2023-12-31'
# df_filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
start_date = '2024-01-01' 
df_filtered = df[(df['Date'] >= start_date)]

plt.figure(figsize=FIGSIZE)
plt.plot(df_filtered['Date'], df_filtered['Adj_Close'], label='Adjusted Close', color='blue')
plt.plot(df_filtered['Date'], df_filtered['Bollinger_High'], label='Bollinger High', color='red', linestyle='dotted')
plt.plot(df_filtered['Date'], df_filtered['Bollinger_Mid'], label='Bollinger Mid', color='gray', linestyle='dotted')
plt.plot(df_filtered['Date'], df_filtered['Bollinger_Low'], label='Bollinger Low', color='green', linestyle='dotted')
plt.title('BMW Adjusted Close Price with Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()