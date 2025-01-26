import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/devoob/Downloads/tobedeleted/Data Analysis with Python/Page View Time Series Visualizer/fcc-forum-pageviews.csv', parse_dates=['date'])
df.set_index('date', inplace=True)

print(df.shape)
df_cleaned = df[
  (df['value'] >= df['value'].quantile(0.025)) & 
  (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    #copy to keep the original
    df_line = df_cleaned.copy()
    
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df_line.index, df_line['value'])
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df_cleaned.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = df_bar.plot(kind='bar', figsize=(10, 7)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df_cleaned.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month_name()
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    box1 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    box1.set_title('Year-wise Box Plot (Trend)')
    box1.set_xlabel('Year')
    box1.set_ylabel('Page Views')

    box2 = sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    box2.set_title('Month-wise Box Plot (Seasonality)')
    box2.set_xlabel('Month')
    box2.set_ylabel('Page Views')
    box2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    fig.savefig('box_plot.png')
    plt.show()
    return fig

line_plot = draw_line_plot()
bar_plot = draw_bar_plot()
box_plot = draw_box_plot()