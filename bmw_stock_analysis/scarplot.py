import pandas as pd
import matplotlib.pyplot as plt
from seaborn import scatterplot
from warnings import filterwarnings

BMW = 'BMW_Data.csv'  # Replace with your actual file path
df = pd.read_csv(filepath_or_buffer=BMW, parse_dates=['Date'])
df['year'] = df['Date'].dt.year

filterwarnings(action='ignore', category=FutureWarning)

FIGSIZE = (12, 5)

plt.figure(figsize=FIGSIZE)
scatterplot(palette='viridis', s=5, data=df, x='Date', y='Volume', hue='year')

# Add title and labels
plt.title('BMW Daily Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')

# Customize the legend
plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))

# Add gridlines
plt.grid(True)

plt.show()