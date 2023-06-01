# format:
# protocol://[user[:password]@]hostname/[database_name]
import pandas as pd
from pydataset import data
from env import get_db_url


# Use your function to obtain a connection to the employees database.

url = get_db_url('employees')

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)

# Once you have successfully run a query:
# a. Intentionally make a typo in the database url. What kind of error message do you see?
url = get_db_url('employeez')


# b. Intentionally make an error in your SQL query. What does the error message look like?
pd.read_sql('SELECT # FROM employees LIMIT 5 OFFSET 50', url)

# Read the employees and titles tables into two separate DataFrames.
emp_df = pd.read_sql('SELECT * FROM employees', url)
tit_df = pd.read_sql('SELECT * FROM titles', url)


# How many rows and columns do you have in each DataFrame? Is that what you expected?
emp_df.shape
tit_df.shape


# Display the summary statistics for each DataFrame.
emp_df.describe()
tit_df.describe()


# How many unique titles are in the titles DataFrame?
tit_df['title'].nunique() #7


# What is the oldest date in the to_date column?
titles_df.to_date.min()

# What is the most recent date in the to_date column?
titles_df.to_date.max()


# Copy the users and roles DataFrames from the examples above.
# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users



roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# What is the result of using a right join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='inner')

# What is the result of using an outer join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)


# What happens if you drop the foreign keys from the DataFrames and try to merge them?
drop_key_users = users.drop(columns=['role_id'])
drop_key_roles = roles.drop(columns=['id'])

drop_key_users.merge(roles, users, how=inner, indicator=True)

# Load the mpg dataset from PyDataset.
from pydataset import data

mpg_df = data('mpg')
mpg_df

# Output and read the documentation for the mpg dataset.
mpg_df(show_docs = True)

# How many rows and columns are in the dataset?
mpg_df.shape

# Check out your column names and perform any cleanup you may want on them.
mpg_df = mpg_df.rename(columns={'trans': 'transmission', 'displ': 'displacement', 'drv': 'drive'})
mpg_df


# Display the summary statistics for the dataset.
mpg_df.describe()

# How many different manufacturers are there?
len(mpg_df.groupby('manufacturer').count()) # 15

# How many different models are there?
len(mpg_df.groupby('model').count()) # 38

# Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
mpg_df['mileage_difference'] = (mpg_df.hwy - mpg_df.cty)
mpg_df.head()

# Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
mpg_df['average_mileage'] = (mpg_df.hwy + mpg_df.cty) / 2
mpg_df

# Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
mpg_df['is_automatic'] = np.where(mpg_df['transmission'].str.contains('auto'), True, False)

# Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg_df['average_mileage'].max()

# Do automatic or manual cars have better miles per gallon?
mpg_df.groupby('is_automatic').average_mileage.agg(['mean'])

#  Use your get_db_url function to help you explore the data from the chipotle database.
url = get_db_url('chipotle')
orders_df = pd.read_sql('SELECT * FROM orders', url)

# What is the total price for each order?
orders_df['item_price'] = orders_df['item_price'].str.replace('$', '')

# What are the most popular 3 items?
orders_df['item_price'] = pd.to_numeric(orders_df['item_price'], errors='coerce')
orders_df['item_price']
orders_df.groupby('item_name').count().sort_values(by='id').tail(3)

# Which item has produced the most revenue?
pd.DataFrame(orders_df.groupby('item_name').sum()['total_per_item'].sort_values(ascending=False).head(1))

# Join the employees and titles DataFrames together.
url = get_db_url('employees')
employees_df = pd.read_sql('SELECT * FROM employees', url)
titles_df = pd.read_sql('SELECT * FROM titles', url)
employees_df, titles_df

employees_merge_df = employees_df.merge(titles_df, left_on='emp_no', right_on='emp_no', how='inner')
employees_merge_df.head()

# For each title, find the hire date of the employee that was hired most recently with that title.
employees_merge_df.groupby('title').hire_date.max()

# Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)
query = '''
SELECT t.title,
        de.emp_no,
        d.dept_name,
        t.to_date,
        t.from_date
FROM departments as d
JOIN dept_emp as de
ON emp_no = emp_no
JOIN title as t
ON emp_no = emp_no
'''

department_titles_df = pd.read_sql(dept_title, get_db_url('employees'))

department_titles_df.head()

pd.crosstab(current_emp_df.title, current_emp_df.dept_name)