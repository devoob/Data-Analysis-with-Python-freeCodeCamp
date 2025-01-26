import pandas as pd

#define the column names based on the sample data
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]

df = pd.read_csv('/Users/devoob/Downloads/tobedeleted/Data Analysis with Python/Demographic Data Analyzer/adult/adult.data', header=None, names=column_names)

# strip leading and trailing spaces from all string columns
string_columns = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'salary']
df[string_columns] = df[string_columns].apply(lambda x: x.str.strip())


df.dropna(inplace=True)

print(df.head())
#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
race_count = df['race'].value_counts()
#What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 2)
#What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(df[df.education=='Bachelors'].size / df.size * 100, 2)
#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_advanced_education_50k = round(advanced_education[advanced_education.salary == '>50K'].size / advanced_education.size * 100, 2)
#What percentage of people without advanced education make more than 50K? ~ means not in
lower_education = df[~df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_lower_education_50k = round(lower_education[lower_education.salary == '>50K'].size / lower_education.size * 100, 2)
#What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()
#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
salary_of_50k = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)
#What country has the highest percentage of people that earn >50K and what is that percentage?
more_50k = df[df.salary == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
highest_earning_country_percentage = more_50k.idxmax()
#Identify the most popular occupation for those who earn >50K in India
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

print(race_count)
print(average_age_men)
print(percentage_bachelors, '%')
print(percentage_advanced_education_50k, '%')
print(percentage_lower_education_50k, '%')
print(min_work_hours)
print(salary_of_50k, '%')
print(highest_earning_country_percentage)
print(top_IN_occupation)