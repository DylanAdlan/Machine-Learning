"""
iexplore

1.
correct syntax to create a Pandas DataFrame from a list named list1? 
list1 = [[1, 2, 3], [4, 5, 6] ]

answer = pd.DataFrame(list1)

2.
correct Pandas method for removing rows that contains empty cells from the DataFrame given below? 
irisdf = pd.read_csv("iris_data.csv")

answer = irisdf.dropna()

3. 
correct syntax to return the second row in a Pandas DataFrame

answer = df.loc[1]

4.
correct Pandas function for 
loading a CSV file by name "data.csv" into a DataFrame

asnwer = read_csv("data.csv")

5. 
correct Pandas method for returning(print) the last rows of the DataFrame given below? 
irisdf = pd.read_csv("iris_data.csv")

answer = irisdf.tail()

6.
correct method to fill empty cells with a new value in the DataFrame given below? 
irisdf = pd.read_csv("iris_data.csv")

answer = irisdf.fillna()

7.
correct syntax to return both the 
first row and the second row in a Pandas DataFrame?

answer = df.loc[[0,1]]

8.
correct syntax to return the first 5 rows of the DataFrame given below? 
irisdf = pd.read_csv("iris_data.csv")

answer = irisdf.head(5)

9.
correct method to plot (draw) diagrams from the data in a DataFrame?

answer = df.plot()

10.
When using the Pandas dropna() method, what argument allows you to 
change the original DataFrame instead of returning a new one?

answer = dropna(inplace = True)

ianalyse

1. 
Pandas Data Frames can be created from
- Numpy Arrays
- Dictionary of Lists
- List of Dictionaries

2.
Consider the iris.csv file given below 
sepal_length,sepal_width,petal_length,petal_width,species_type 
5.1,3.5,1.4,0.2,IrisSetosa 
4.9,3.0,1.4,0.2,IrisSetosa 
4.7,3.2,1.3,0.2,IrisSetosa 
5.0,3.3,1.4,0.2,IrisSetosa 
7.0,3.2,4.7,1.4,IrisVersicolor 
6.4,3.2,4.5,1.5,IrisVersicolor 
6.9,3.1,4.9,1.5,IrisVersicolor 
6.3,3.3,6.0,2.5,IrisVirginica 
5.8,2.7,5.1,1.9,IrisVirginica 
7.1,3.0,5.9,2.1,IrisVirginica 

Fill in the missing code to  
return (print) the last 3 rows of the DataFrame 

import pandas as pd 
df = pd.read_csv('iris.csv') 
print(_____)

answer = df.tail(3)

3.
What will the following code segment do? 
import pandas as pd df = pd.read_csv('iris.csv') 
df = df.drop(['petal_length', 'petal_width', 'species_type'], axis=1)

answer = Deletes the 3 columns having labels 
petal_length,petal_width,species_type from the Data Frame

4.
Fill in the missing code to return (print) the entire DataFrame

import pandas as pd 
df = pd.read_csv('iris.csv') 
print(_____)

answer = df.to_string()

5.
import pandas as pd 
data = [['Arun',21],['Bama',25],['Cecil',22]] 
df = pd.DataFrame(data,columns=['Name','Age']) 
print (df)

answer =  Name Age
        0  Arun 21
        1  Bama 25
        2  Cecil 22

6.
Pandas ___________function is used to 
split the data in dataframe into groups based on a given condition.

answer = groupby()

7.
What will the following code segment do? 
import pandas as pd 
df = pd.read_csv('iris.csv') 
print(df.shape)

answer = (10, 5) # refer to no.2

8.
Consider the statement given below. df['tax'] = 10 
Assume that the column by name 'tax' already exists 
in the data Frame by name df.

answer = Change all values of column tax to 10

9.
correct Features of Pandas DataFrames
- Potentially columns are of different types
- Can Perform Arithmetic operations on rows and columns
- Labeled axes (rows and columns)

10.
Fill in the missing code to return(print) the first row of a DataFrame 

import pandas as pd 
df = pd.read_csv('iris.csv') 
print(_____)

answer = df.loc[0]

"""

# idesign
# 1.

import pandas as pd

data = [[5.1,3.5,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisVersicolor"],
	[6.4,3.2,4.5,1.5,"IrisVersicolor"],
	[6.3,3.3,6.0,2.5,"IrisVirginica"],
	[5.8,2.7,5.1,1.9,"IrisVirginica"]]

#Fill in the code here

df = pd.DataFrame(data, columns= ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type'])
print(df)

#---------------------------------------------------------------------------------------------------

# 2.
import numpy as np
import pandas as pd

file_path = 'iris.csv'

# import CSV file as a DataFrame without header
df = pd.read_csv(file_path,  header=None)

# adding custom column names
df.columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']

# reset the index to ensure sequetial indexing
df = df.drop(index=0).reset_index(drop=True)

# print the DataFrame
print(df)

#---------------------------------------------------------------------------------------------------------

# 3. execute only 2 column[sepal_length and sepal_width] from iris_with_header csv file
import numpy as np
import pandas as pd

file_path = 'iris_with_header.csv'

# import CSV file as a DataFrame with header nut only use 2 header
df = pd.read_csv(file_path, usecols=['sepal_length', 'sepal_width'])
print(df)

#----------------------------------------------------------------------------------------------------------

# 4.
import numpy as np
import pandas as pd

file_path = 'iris_with_header.csv'

# import csv file as DataFrame
df = pd.read_csv(file_path)

# display the entire content
print("DataFrame")
print(df)

# display the Shape of the Data Frame
print("Shape")
print(df.shape)

# display the data types of the different columns in the Data Frame
print("Data Types")
print(df.dtypes)

# Display the number of columns under each data type in the Data Frame
print("Column Count under each dtype")
print(df.dtypes.value_counts())

# Display the Summary Statistics of the Data Frame
# count, mean, std, min, 25%, 50%, 75%, max
print("Summary Statistics")
print(df.describe())

#------------------------------------------------------------------------------------------------------------------------------

# 5.
import numpy as np
import pandas as pd

# Import the given CSV file as a Data Frame.
file_path = 'iris_with_header.csv'
df = pd.read_csv(file_path)

# Print the column names using columns attribute.
print("Column Names")
print(df.columns)

# Rename the column “species_type” to “SpeciesType”
df = df.rename(columns = {'species_type': 'SpeciesType'})

# Print the column names using columns attribute.
print("Column Names after renaming")
print(df.columns)

# Print the entire contents of the Data Frame
print("DataFrame")
print(df)

#---------------------------------------------------------------------------------------------------------------------------------

# 6.
import numpy as np
import pandas as pd

file_path = 'iris_with_header.csv'

# Load iris data from the input file.
df = pd.read_csv(file_path)

# Print the original Data Frame.
print("Original DataFrame")
print(df)

# Sort rows based on Sepal Length in ascending order and display the Data Frame.
df_sorted = df.sort_values(by='sepal_length')
print("Sorted DataFrame")
print(df_sorted)

#-------------------------------------------------------------------------------------------------------------------------------------
# iaccess

# 1.
#Merge DataFrames, Change column order

import pandas as pd

df1 = pd.DataFrame([["Anitha",7.8,8.9], ["Baskar",5.6,6.9]], columns = ["student_name","sem1_cgpa", "sem2_cgpa"])
df2 = pd.DataFrame([["Anitha","CSE"], ["Baskar","IT"]], columns = ["student_name","department"])

# Fill in the code here

# Print the First Data Frame
print("DataFrame1")
print(df1)

# Print the Second Data Frame
print("DataFrame2")
print(df2)

# Merge the 2 Data Frames and rearrange the columns in the order student_name , department , sem1_cgpa, sem2_cgpa
merged_df = pd.merge(df1, df2, on=['student_name'], how='inner')
merged_df = merged_df[['student_name', 'department', 'sem1_cgpa', 'sem2_cgpa']]
# Print the entire contents of the merged Data Frame
print("Merged DataFrame")
print(merged_df)

#----------------------------------------------------------------------------------------------------------------------------------------

# 2.

import numpy as np
import pandas as pd

# Import the given CSV file as a Data Frame.
file_path = 'iris_duplicates.csv'
df = pd.read_csv(file_path)

# Print the entire contents of the Data Frame
print("Original DataFrame")
print(df)

# Remove the Duplicate Rows from the Data Frame
df_no_duplicates = df.drop_duplicates()

# Print the entire contents of the Data Frame	
print("DataFrame after removing duplicates")
print(df_no_duplicates)	







