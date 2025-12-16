import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)
print("DataFrame after renaming columns:")
print(df, "\n")

print("First 3 rows of the DataFrame:")
print(df.head(3), "\n")

mean_age = df['age'].mean()
print("Mean age of the individuals:", mean_age, "\n")

print("Selected columns (first_name and city):")
print(df[['first_name', 'city']], "\n")

np.random.seed(0)  
df['salary'] = np.random.randint(40000, 100000, size=len(df))
print("DataFrame after adding 'salary' column:")
print(df, "\n")

print("Summary statistics of the DataFrame:")
print(df.describe())


import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)
print("Sales and Expenses DataFrame:")
print(sales_and_expenses, "\n")

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses, "\n")

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses, "\n")

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)



import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

expenses.set_index('Category', inplace=True)
print("Expenses DataFrame with Category as index:")
print(expenses, "\n")

max_expense = expenses.max(axis=1)
print("Maximum expense for each category:")
print(max_expense, "\n")

min_expense = expenses.min(axis=1)
print("Minimum expense for each category:")
print(min_expense, "\n")

avg_expense = expenses.mean(axis=1)
print("Average expense for each category:")
print(avg_expense)
