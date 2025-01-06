import pandas as pd

BMW = 'bmw_stock_analysis/BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year
print(df.head())

print(df.tail())

print(df[['Adj_Close', 'Close', 'High', 'Low', 'Open', 'Volume']].corr())


