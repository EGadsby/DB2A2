import pandas as pd
import sqlite3
import os

# Set the current working directory to the "relation" folder
os.chdir('./Relations')

# Read the CSV files into pandas DataFrames
works_df = pd.read_csv('workson.csv')
salaries_df = pd.read_csv('salary.csv')
employees_df = pd.read_csv('employee.csv')
supervise_df = pd.read_csv('supervise.csv')
department_df = pd.read_csv('department.csv')
project_df = pd.read_csv('project.csv')
male_df = pd.read_csv('male.csv')
female_df = pd.read_csv('female.csv')

# Create an SQLite database connection
conn = sqlite3.connect(':memory:')  # Use ':memory:' to create an in-memory database

# Load the DataFrames into SQLite as tables
works_df.to_sql('workson', conn, index=False)
salaries_df.to_sql('salary', conn, index=False)
employees_df.to_sql('employee', conn, index=False)
supervise_df.to_sql('supervise', conn, index=False)
department_df.to_sql('department', conn, index=False)
project_df.to_sql('project', conn, index=False)
male_df.to_sql('male', conn, index=False)
female_df.to_sql('female', conn, index=False)


# Define SQL queries
queries = [
     """
    SELECT female.Name
    FROM female
    INNER JOIN workson ON female.name = workson.name
    INNER JOIN supervise ON supervise.subordinate = female.name
    WHERE workson.PROJECT = 'computerization'
    AND workson.effort = 10
    AND supervise.supervisor = "jennifer";
    """,
    """
    SELECT salary.employee_name
    FROM salary
    INNER JOIN department ON department.employee_name = salary.employee_name
    WHERE salary > 40000
    AND department.department = "research";
    """,
    """
    SELECT employee.EMPLOYEE_NAME
    FROM employee
    EXCEPT
    SELECT supervise.subordinate
    FROM supervise;
    """,
    """
    SELECT workson.NAME
    FROM workson
    WHERE PROJECT = 'productx'
    AND EFFORT >= 20;
    """
]




def main():
    #get number of total transactions, which is always 3




# Execute the queries and display the results
    for i, query in enumerate(queries, 1):
        print(f"Query {i}:")
        result = pd.read_sql_query(query, conn)
        print(result)
        print()

main()
