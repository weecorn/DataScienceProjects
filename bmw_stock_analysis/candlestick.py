import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import ta

BMW = 'BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

# --- Prepare data for candlestick chart ---
df_ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# --- Calculate RSI ---
df['RSI'] = ta.momentum.rsi(df['Adj_Close'], window=14)

# --- Create a figure and axes for the main plot with candlestick and RSI ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# --- Candlestick chart on the first subplot ---
candlestick_ohlc(ax1, df_ohlc.values, width=0.6, colorup='green', colordown='red')
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.set_ylabel('Price')
ax1.grid(True)

# --- RSI on the second subplot ---
ax2.plot(df['Date'], df['RSI'], color='purple', label='RSI')
ax2.axhline(70, color='red', linestyle='--', linewidth=0.5)  # Overbought level
ax2.axhline(30, color='green', linestyle='--', linewidth=0.5)  # Oversold level
ax2.set_ylabel('RSI')
ax2.legend(loc='upper left')
ax2.grid(True)

plt.xlabel('Date')
plt.suptitle('BMW Candlestick Chart with RSI')
plt.show()

# --- Create a separate figure and axes for the June 2023 candlestick chart ---
fig_june, ax_june = plt.subplots(figsize=(12, 5))

# --- Filter data for June 2023 ---
df_june = df[(df['Date'] >= '2023-06-01') & (df['Date'] <= '2023-06-30')]
df_june_ohlc = df_june[['Date', 'Open', 'High', 'Low', 'Close']]
df_june_ohlc['Date'] = df_june_ohlc['Date'].map(mdates.date2num)

# --- Candlestick chart for June 2023 ---
candlestick_ohlc(ax_june, df_june_ohlc.values, width=0.6, colorup='green', colordown='red')
ax_june.xaxis_date()
ax_june.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax_june.set_ylabel('Price')
ax_june.grid(True)

plt.xlabel('Date')
plt.title('BMW Candlestick Chart - June 2023')
plt.show()