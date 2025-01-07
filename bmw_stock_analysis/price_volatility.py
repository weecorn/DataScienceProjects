import pandas as pd
import matplotlib.pyplot as plt
from seaborn import lineplot
from warnings import filterwarnings
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import ta   # technical analysis package

BMW = 'BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

filterwarnings(action='ignore', category=FutureWarning)

# define default figure size
FIGSIZE = (12, 5)

# --- Line plot with adjusted closing price over time ---
plt.figure(figsize=FIGSIZE)
lineplot(palette='magma', data=df, x='Date', y='Adj_Close', hue='year')
plt.title('BMW Stock Adjusted Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

# --- Candlestick chart for daily price movements ---
df_ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

fig, ax = plt.subplots(figsize=FIGSIZE)
candlestick_ohlc(ax, df_ohlc.values, width=0.6, colorup='green', colordown='red')
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.title('BMW Daily Candlestick Chart')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# --- Volume traded over time ---
plt.figure(figsize=FIGSIZE)
plt.bar(df['Date'], df['Volume'], color='blue')
plt.title('BMW Daily Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()

# --- Moving averages ---
df['MA50'] = df['Adj_Close'].rolling(window=50).mean()
df['MA200'] = df['Adj_Close'].rolling(window=200).mean()

plt.figure(figsize=FIGSIZE)
plt.plot(df['Date'], df['Adj_Close'], label='Adjusted Close')
plt.plot(df['Date'], df['MA50'], label='50-Day MA')
plt.plot(df['Date'], df['MA200'], label='200-Day MA')
plt.title('BMW Adjusted Close Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# --- Bollinger Bands ---
df['Bollinger_High'] = ta.volatility.bollinger_hband(df['Adj_Close'], window=20, window_dev=2)
df['Bollinger_Low'] = ta.volatility.bollinger_lband(df['Adj_Close'], window=20, window_dev=2)
df['Bollinger_Mid'] = ta.volatility.bollinger_mavg(df['Adj_Close'], window=20)

plt.figure(figsize=FIGSIZE)
plt.plot(df['Date'], df['Adj_Close'], label='Adjusted Close')
plt.plot(df['Date'], df['Bollinger_High'], label='Bollinger High')
plt.plot(df['Date'], df['Bollinger_Mid'], label='Bollinger Mid')
plt.plot(df['Date'], df['Bollinger_Low'], label='Bollinger Low')
plt.title('BMW Adjusted Clsoe Price with Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()