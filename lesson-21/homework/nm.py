import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1['Average'] = df1[['Math','English','Science']].mean(axis=1)
print(df1)

top_student = df1.loc[df1['Average'].idxmax()]
print(top_student)

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1)

import matplotlib.pyplot as plt

subject_avgs = df1[['Math', 'English', 'Science']].mean()

plt.figure(figsize=(6, 4)) 
plt.bar(subject_avgs.index, subject_avgs.values, width=0.4)
plt.title("Average Grades per Subject")
plt.ylabel("Average Grade")
plt.xlabel("Subject")
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

df2['Total'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

df2[['Product_A_pct_change',
     'Product_B_pct_change',
     'Product_C_pct_change']] = (
    df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
).round(2)

plt.figure(figsize=(6, 4))  

plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_B'], marker='s', label='Product B')
plt.plot(df2['Date'], df2['Product_C'], marker='^', label='Product C')

plt.title('Sales Trends of Products Over Time')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()



import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

avg_salary = df3.groupby('Department')['Salary'].mean()
print(avg_salary)

most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("\n", most_experienced)

min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)
print("\n", df3)

import matplotlib.pyplot as plt

dept_counts = df3['Department'].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(dept_counts.index, dept_counts.values, color='skyblue', width=0.4)
plt.title('Number of Employees per Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()




import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

total_revenue = df4['Total_Price'].sum()
print("Total Revenue from all orders:", total_revenue)

product_totals = df4.groupby('Product')['Quantity'].sum()
most_ordered_product = product_totals.idxmax()
most_ordered_quantity = product_totals.max()

print(f"Most Ordered Product: {most_ordered_product} ({most_ordered_quantity} units)")


average_quantity = df4['Quantity'].mean()
print("Average Quantity Ordered:", round(average_quantity, 2))

import matplotlib.pyplot as plt

product_sales = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    product_sales, 
    labels=product_sales.index,  
    autopct='%1.1f%%',         
    startangle=90,               
    colors=['skyblue', 'lightgreen', 'salmon'],
    explode=(0.05, 0.05, 0.05) 
)
plt.title("Sales Distribution by Product")
plt.show()
