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
# Would it be reasonable to predict species based on sepal width and sepal length? For this, you'll visualize two numeric columns through the lense of a categorical column.
# Which features would be best used to predict species?
