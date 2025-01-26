import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/devoob/Downloads/tobedeleted/Data Analysis with Python/Medical Data Visualizer/medical_examination.csv')
df.head()
df.shape
#print(df.shape)

df['BMI'] = df['weight'] / (df['height']/100)**2
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
#print(df.head())

def draw_cat_plot():
    #melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    #print(df_cat)

    #groupby
    df_cat['total'] = 1 
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count() 
    #print(df_cat)
    df_cat.rename(columns={'total': 'counts'}, inplace=True)

    #catplot
    fig1 = sns.catplot(x='variable', y='counts', hue='value', col='cardio', kind='bar', data=df_cat)

    return fig1
fig = draw_cat_plot()
plt.show()

def draw_heat_map():
    #cleaning
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
    fig = plt.gcf()

    return fig

fig_heat = draw_heat_map()
plt.show()
w