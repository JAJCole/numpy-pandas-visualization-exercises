import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


# Use seaborn's load_dataset function to load the iris database 
# to answer the following questions:
iris_db = sns.load_dataset('iris')
iris_db

# What does the distribution of petal lengths look like?
avg_y = iris_db['petal_length'].mean()
iris_db['petal_length'].std()

sns.relplot(x='species',y='petal_length',data=iris_db)


# Is there a relationship between petal length and petal width?
sns.relplot(data = iris_db, x = 'petal_length', y = 'petal_width', hue = 'species')
# seems length and width of petals are pos. correlated


# Would it be reasonable to predict species based on sepal width and sepal length? 
# For this, you'll visualize two numeric columns through the lense of a categorical column.
sns.relplot(data = iris_db, x = 'sepal_length', y = 'sepal_width', hue = 'species')
# Doesnt seem to be reasonable


# Which features would be best used to predict species?
sns.boxplot(y = 'petal_width', x = 'species', data = iris_db)
# Seems the range of petal width is the best predictor



# Load the anscombe dataset from seaborn. Use pandas to group the data by the dataset column, 
# and calculate summary statistics for each dataset. What do you notice?
ans_db = sns.load_dataset('anscombe')
ans_db
ans_db.groupby('dataset').describe()
# notice count, mean, std and other aggregates/descriptive functions are similar if not the same



# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
sns.relplot(data = ans_db, x = 'x', y = 'y', col = 'dataset')


# Load the InsectSprays dataset from pydataset and read it's documentation. 
# Create a boxplot that shows the effectiveness of the different insect sprays.
from pydataset import data

bug_db = data('InsectSprays')
bug_db

sns.boxplot(y = 'count', x= 'spray', data = bug_db)


# Load the swiss dataset from pydataset and read it's documentation. 
# Create visualizations to answer the following questions:
swiss = data('swiss')
swiss
# for doc: data('swiss', show_doc=True)

# Create an attribute named is_catholic that holds a boolean value of whether or not the 
# province is Catholic. (Choose a cutoff point for what constitutes catholic)
swiss['is_catholic'] = swiss.Catholic > 55
sw

# Does whether or not a province is Catholic influence fertility?
sns.boxplot(x = 'is_catholic', y = 'Fertility', data = swiss)
# would seem so

    
# What measure correlates most strongly with fertility?
sns.pairplot(data = swiss.iloc[:, :-1])

swiss.corr().Fertility
# looks like military examination and education are neg. correlated to fert. lower the scores, more kids


# Load the chipotle dataset from SQL, create a bar chart that shows the 4 most popular items 
# and the revenue produced by each.


