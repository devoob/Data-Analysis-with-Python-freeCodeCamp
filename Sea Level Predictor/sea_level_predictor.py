import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('/Users/devoob/Downloads/tobedeleted/Data Analysis with Python/Sea Level Predictor/epa-sea-level.csv')
print(df.head())

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level (Without Regression)')
plt.savefig('sea_level_rise (without).png')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')

slope, intercept, r_value, p_value, std_err = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years = range(1880, 2051)
plt.plot(years, slope * years + intercept, color='red', label='Best Fit Line (1880-2050)')

df_2000 = df[df['Year'] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = stats.linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
years_2000 = range(2000, 2051)
plt.plot(years_2000, slope_2000 * years_2000 + intercept_2000, color='black', label='Best Fit Line (2000-2050)')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level (With Regression)')
plt.legend()

plt.savefig('sea_level_rise.png')
plt.show()