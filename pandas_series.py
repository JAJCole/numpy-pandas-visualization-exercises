import pandas as pd
import numpy as np

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# from a list
my_series = pd.Series(fruits)


# from an array
my_array = np.array(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
# create series from array
my_series_1 = pd.Series(my_array)
type(my_series_1)


# from dictionary
labeled_series = pd.Series({'a' : 0, 'b' : 1.5, 'c' : 2, 'd': 3.5, 'e': 4, 'f': 5.5})
labeled_series


# from dataframe
sleep_df = data('sleepstudy')
sleep_df.head()


# Summary
# From a list, array, dictionary: - myseries = pd.Series(<list or array or dictionary>)
# From existing dataframe:

# myseries = df['col_for_series']
# myseries = df.col_for_series





# Exercises pt.1:

# Determine the number of elements in fruits.
my_series = pd.Series(fruits)
my_series.count()
my_series.value_counts()
my_series.describe()
# 17 elements in fruits


# Output only the index from fruits.
my_series.index


# Output only the values from fruits.
my_series.values


# Confirm the data type of the values in fruits.
my_series.dtype


# Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
my_series[:5]
my_series[-3:]
np.random.choice(my_series)
np.random.choice(my_series)
# OR
np.random.choice(my_series, 2)


# Run the .describe() on fruits to see what information it returns when called on a Series with string values.
my_series.describe()


# Run the code necessary to produce only the unique string values from fruits.
my_series.value_counts()



# Determine how many times each unique string value occurs in fruits.
# kiwi: 4, mango: 2 and the rest are one instance of occurance


# Determine the string value that occurs most frequently in fruits.
# kiwi


# Determine the string value that occurs least frequently in fruits.
# all but two have one occurance




# Exercises pt.2:

# Capitalize all the string values in fruits.
import pandas as pd
import numpy as np

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits.str.upper()


# Count the letter "a" in all the string values (use string vectorization).
# Use `isin()` to tell whether each value is in a set of known values. 
vowels = list('a')
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruit_series = pd.Series(fruits)
fruit_series
fruit_series.isin(vowels).value_counts()




# Output the number of vowels in each and every string value.

# Write the code to get the longest string value from fruits.

# Write the code to get the string values with 5 or more letters in the name.

# Find the fruit(s) containing the letter "o" two or more times.

# Write the code to get only the string values containing the substring "berry".

# Write the code to get only the string values containing the substring "apple".

# Which string value contains the most vowels?
