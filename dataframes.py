import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)



#

# Copy the code from the lesson to create a dataframe full of student grades.
df


# Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing_english']= df['english'] >= 70
df


# Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values('passing_english')


# Sort the english grades first by passing_english and then by student name. 
# All the students that are failing english should be first, and within the students that are 
# failing english they should be ordered alphabetically. The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
df.sort_values(['passing_english', 'name'], ascending =(True, True))



# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(['passing_english','english'], ascending = (True,True))


# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = (df['english'] + df['math'] + df['reading'])/3
df


# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
# How many rows and columns are there?
from pydataset import data
mpg_df = data('mpg')
mpg_df

# What are the data types of each column?
mpg_df.describe
mpg_df.dtypes


# Summarize the dataframe with .info and .describe
mpg_df.info()
mpg_df.describe()


# Rename the cty column to city.
mpg_df = mpg_df.rename(columns={'cty':'city'})


# Rename the hwy column to highway.
mpg_df = mpg_df.rename(columns={'hwy':'highway'})


# Do any cars have better city mileage than highway mileage?
(mpg_df['city'] > mpg_df['highway']).any()
# answer: false/no


# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg_df['mileage_difference'] = mpg_df['highway'] - mpg_df['city']
mpg_df

# Which car (or cars) has the highest mileage difference?
mpg_df['mileage_difference','manufacturer'].max()

# Which compact class car has the lowest highway mileage? The best?
mpg_df

mpg_df.sort_values('mileage_difference').tail(1)

mpg_df.sort_values(['mileage_difference'], ascending=False)

# Create a column named average_mileage that is the mean of the city and highway mileage.
# Which dodge car has the best average mileage? The worst?

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data('mammals')
mammals

# How many rows and columns are there?
mammals.info()
# 2 columns and 62rows

# What are the data types?
mammals.dtype()


# Summarize the dataframe with .info and .describe
mammals.info()
mammals.describe()

# What is the the weight of the fastest animal?
# What is the overal percentage of specials?
# How many animals are hoppers that are above the median speed? What percentage is this?
