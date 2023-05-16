import numpy as np


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#How many negative numbers are there?
a[a < 0]
# 4


#How many positive numbers are there?
a[a > 0]
#5


#How many even positive numbers are there?
a[(a > 0) & (a % 2 == 0)]
# 3


#If you were to add 3 to each data point, how many positive numbers would there be?
a = a + 3
# 10 pos num


#If you squared each number, what would the new mean and standard deviation be?
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a = a ** 2
a.mean() # 74
a.std()  # 144.024


# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# BELOW IS CENTERING:
# I was recently asked about whether centering (subtracting the mean) a predictor variable in a regression model has the same effect as 
# standardizing (converting it to a Z score).  My response:
# They are similar but not the same.
# In centering, you are changing the values but not the scale.  So a predictor that is centered at the mean has new values–the entire scale 
# has shifted so that the mean now has a value of 0, but one unit is still one unit.  
# The intercept will change, but the regression coefficient for that variable will not.  
# Since the regression coefficient is interpreted as the effect on the mean of Y for each one unit difference in X, it doesn’t change when X is centered.
# And incidentally, despite the name, you don’t have to center at the mean.  It is often convenient, but there can be advantages of choosing a 
# more meaningful value that is also toward the center of the scale.
# But a Z-score also changes the scale.  A one-unit difference now means a one-standard deviation difference.  
# You will interpret the coefficient differently.  
# This is usually done so you can compare coefficients for predictors that were measured on different scales.  
# I can’t think of an advantage for doing this for an interaction.

# Center the dataset
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

mean = a.mean()
a = a - mean
print(a)
a.mean()


# Calculate the z-score for each data point. 
# Recall that the z-score is given by: z = (x - mean(x))/ std
# z = (a - a.mean()/a.std)

a = a - a.mean()
a = a / a.std()
print(a)
# Z-score: 
# [ 0.12403473  0.86824314  1.11631261  2.48069469 -0.62017367 -0.49613894
# -0.3721042  -0.3721042  -0.3721042  -1.11631261  0.         -1.24034735]



#
# Copy the setup and exercise directions from More Numpy Practice 
# into your numpy_exercises.py and add your solutions.
#




# import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
new_a = sum([i for i in a])
print(new_a)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_a = min([i for i in a])
print(min_a)


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max([i for i in a])
print(max_of_a)


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = mean([i for i in a])
print(mean_of_a)

mean_of_a = sum([i for i in a])/len(a)
print(mean_of_a)


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
import math
product_of_a = math.prod([i for i in a])
print(product_of_a)


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
square_of_a = [i**2 for i in a]
print(square_of_a)


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [i for i in a if i % 2 != 0]
print(odds_in_a)


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [i for i in a if i % 2 == 0]
print(evens_in_a)


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2