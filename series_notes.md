[Series vs DF]:
series: rows, no columns
Df: rows and columns

[Creating_Series]:
# 1. List
my_series = pd.series(my_list)
# 2. Array
my_array = np.array([1,2,3])
my_series = pd.Series(my_array)
# 3. Dictionary
labeled_series = pd.Series({'A':1, 'B':2, 'C':3})
# 4. DF
my_df = data('data_storage')


[Series_Attributes]:
.astype, 
.index, 
.values,
.dtype
.name
.size
.shape

[Series_Methods]:
.describe()
.head(), .tail(), .sample()
.value_counts(), .count(), .sort_values()
.sort_index, .any(), .all(), .isin()
.apply()


[Plotting]
import matplotlib.pyplot as plt
what_to_plot.plot(kind=*)
plt.title('*')



[DataFrames]:
pd.DataFrame({'A':1,'B':2,'C':3})
or
pd.DataFrame([[2,3,4],[6,8,9]])

[Methods]:
df.info(), df.describe(), .head/tail(), 
df.rename(columns={'':''}), .drop('')
[Attributes]:
.index, .shape, .dtypes
