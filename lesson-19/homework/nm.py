import pandas as pd
sales = pd.read_csv('sales_data.csv')
sales.head()

result = sales.groupby("Category", as_index=False).agg(
    total_quantity_sold=("Quantity", "sum"),
    average_price_per_unit=("Price", "mean"),
    max_quantity_single_transaction=("Quantity", "max")
)
print("\n", result)

top_selling_products = (
    sales.groupby(["Category", "Product"], as_index=False)["Quantity"]
      .sum()
      .loc[lambda x: x.groupby("Category")["Quantity"].idxmax()]
      .rename(columns={"Quantity": "total_quantity_sold"})
)
print("\n", top_selling_products)

highest_sales_date = (
    sales.assign(total_sales=sales["Quantity"] * sales["Price"])
          .groupby("Date", as_index=False)["total_sales"]
          .sum()
          .loc[lambda x: x["total_sales"].idxmax()]
)

print("\n", highest_sales_date)


import pandas as pd
cust_order = pd.read_csv('customer_orders.csv')
cust_order.head()

import pandas as pd

customers_20plus = (
    cust_order.groupby("CustomerID")
         .filter(lambda x: x["OrderID"].nunique() >= 20)
)
print("\n", customers_20plus)

high_spending_customers = (
    cust_order.groupby("CustomerID", as_index=False)
         .agg(avg_price_per_unit=("Price", "mean"))
         .loc[lambda x: x["avg_price_per_unit"] > 120]
)

print("\n", high_spending_customers)

less_than_5 = (
    cust_order
        .assign(total_price=cust_order["Quantity"] * cust_order["Price"])
        .groupby("Product", as_index=False)
        .agg(
            total_quantity=("Quantity", "sum"),
            total_price=("total_price", "sum")
        )
        .query("total_quantity >= 5")
)

print("\n", less_than_5)

import sqlite3
import pandas as pd

conn = sqlite3.connect("population.db")
cursor = conn.cursor()

cursor.execute("DROP VIEW IF EXISTS population_with_salary_band;")

cursor.execute("""
CREATE VIEW population_with_salary_band AS
SELECT
    id,
    first_name,
    last_name,
    email,
    gender,
    state,
    salary,
    CASE
        WHEN salary <= 200000 THEN 'till $200,000'
        WHEN salary BETWEEN 200001 AND 400000 THEN '$200,001 - $400,000'
        WHEN salary BETWEEN 400001 AND 600000 THEN '$400,001 - $600,000'
        WHEN salary BETWEEN 600001 AND 800000 THEN '$600,001 - $800,000'
        WHEN salary BETWEEN 800001 AND 1000000 THEN '$800,001 - $1,000,000'
        WHEN salary BETWEEN 1000001 AND 1200000 THEN '$1,000,001 - $1,200,000'
        WHEN salary BETWEEN 1200001 AND 1400000 THEN '$1,200,001 - $1,400,000'
        WHEN salary BETWEEN 1400001 AND 1600000 THEN '$1,400,001 - $1,600,000'
        WHEN salary BETWEEN 1600001 AND 1800000 THEN '$1,600,001 - $1,800,000'
        ELSE '$1,800,001 and over'
    END AS salary_category
FROM population;
""")

conn.commit()

cursor.execute("DROP TABLE IF EXISTS salary_category_summary;")
conn.commit()

cursor.execute("""
CREATE TABLE salary_category_summary AS
WITH ranked AS (
    SELECT
        salary_category,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY salary_category
            ORDER BY salary
        ) AS rn,
        COUNT(*) OVER (
            PARTITION BY salary_category
        ) AS cnt
    FROM population_with_salary_band
),
total_pop AS (
    SELECT COUNT(*) AS total_population
    FROM population_with_salary_band
)
SELECT
    r.salary_category,
    COUNT(*) AS population_count,
    ROUND(AVG(r.salary), 2) AS average_salary,
    ROUND(AVG(
        CASE
            WHEN r.rn IN ((r.cnt + 1) / 2, (r.cnt + 2) / 2)
            THEN r.salary
        END
    ), 2) AS median_salary,
    ROUND(
        COUNT(*) * 100.0 / t.total_population, 2
    ) AS population_percentage
FROM ranked r
CROSS JOIN total_pop t
GROUP BY r.salary_category;
""")

conn.commit()
df = pd.read_sql( "SELECT * FROM salary_category_summary ORDER BY salary_category;", conn ) 
df
