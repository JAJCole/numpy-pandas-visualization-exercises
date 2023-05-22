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

fruit_series.str.count('a')


# Output the number of vowels in each and every string value.
fruit_series.str.count('a|e|i|o|u')


# Write the code to get the longest string value from fruits.
max(fruit_series, key = len)


# Write the code to get the string values with 5 or more letters in the name.
fruit_series[fruit_series.str.len() >= 5]


# Find the fruit(s) containing the letter "o" two or more times.
fruit_series[fruit_series.str.count('o') > 1]


# Write the code to get only the string values containing the substring "berry".
fruit_series[fruit_series.str.contains('berry')]


# Write the code to get only the string values containing the substring "apple".
fruit_series[fruit_series.str.contains('apple')]


# Which string value contains the most vowels?
fruit_series.str.count('[aeiou]').max()
# index 5 is honeycrisp apple

fruit_series


# Exercises pt.3:
# Use pandas to create a Series named letters from the following 
# string. The easiest way to make this string into a Pandas series 
# is to use list to convert each individual letter into a single 
# string on a basic Python list.


pt_3_letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
pt_3_list = list(pt_3_letters)
pt_3_series = pd.Series(pt_3_list)

pt_3_series


letters = pd.Series(list(pt_3_letters))
letters

# Which letter occurs the most frequently in the letters Series?
letters.value_counts().max()



# Which letter occurs the Least frequently?
letters.value_counts().min()


# How many vowels are in the Series?

def is_vowel(text):
    return text in ['a','e','i','o','u']

letters.str.lower().apply(is_vowel).sum()


# How many consonants are in the Series?
def is_conso(text):
    return text not in ['a','e','i','o','u']

letters.str.lower().apply(is_conso).sum()
   
# Create a Series that has all of the same letters but uppercased.
upper_series = letters.str.upper()
upper_series

# Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters.value_counts().head(6).plot(kind="bar")


