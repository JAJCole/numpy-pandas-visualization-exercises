# format:
# protocol://[user[:password]@]hostname/[database_name]


# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
# pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


def get_db_url(un, hn, pw, db):
    return 


# Use your function to obtain a connection to the employees database.

# Once you have successfully run a query:

# a. Intentionally make a typo in the database url. What kind of error message do you see?

# b. Intentionally make an error in your SQL query. What does the error message look like?

# Read the employees and titles tables into two separate DataFrames.

# How many rows and columns do you have in each DataFrame? Is that what you expected?

# Display the summary statistics for each DataFrame.

# How many unique titles are in the titles DataFrame?

# What is the oldest date in the to_date column?

# What is the most recent date in the to_date column?
