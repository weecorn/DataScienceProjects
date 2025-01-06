import pandas as pd
import matplotlib.pyplot as plt
from seaborn import lineplot
from warnings import filterwarnings

BMW = 'bmw_stock_analysis/BMW_Data.csv'
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

filterwarnings(action='ignore', category=FutureWarning)

FIGSIZE = (12, 5)
plt.figure(figsize=FIGSIZE)
lineplot(palette='magma', data=df, x='Date', y='Adj_Close', hue='year')

# Add title and labels
plt.title('BMW Stock Adjusted Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')

# Customize the legend
plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))  # Move legend outside

# Add gridlines
plt.grid(True)

plt.show()