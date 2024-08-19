"""
iexplore

1.
purpose of a validation dataset in Machine Learning
- To test the model's performance on unseen data and tune hyperparameters.

2.
In supervised learning, what is the role of the model?
- The model is provided with labeled data and learns to 
make predictions or decisions based on that data.

3.
What is Machine Learning?
- A field of artificial intelligence that focuses on developing algorithms 
that can learn from and make predictions or decisions based on data.

4.
Which of the following is an example of a hyperparameter in 
a Machine Learning algorithm?
- The learning rate in a gradient descent algorithm.

5.
What is the primary goal of unsupervised learning?
- To discover patterns or structures in data without labeled examples.

6.
classification problem in Machine Learning
- Recognizing handwritten digits (e.g., classifying a digit as 1, 2, 3, etc.).

7.
What type of learning is used when training a self-driving car to navigate 
without explicit instructions?
- Reinforcement Learning

8.
What is overfitting in Machine Learning?
- When a model performs well on the training data but poorly on unseen data.

9.
What is the main difference between regression and classification in Machine Learning
- Regression predicts continuous values, while classification predicts categories or labels.

10.
key type of Machine Learning
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

ianalyse

1.
What is an example of a binary classification problem in concept learning?
- Recognizing handwritten digits (e.g., classifying a digit as 1 or not 1).

2.
In supervised learning, what is the role of labeled examples in concept learning?
- Labeled examples are used to train the model to recognize and generalize concepts.

3.
What is the bias-variance trade-off in concept learning?
- The trade-off between a model's ability to fit the training data (low bias) 
and its ability to generalize to new data (low variance).

4.
What is an example of an unsupervised learning problem in concept learning?
- Clustering news articles into topics.

5.
In concept learning, what is feature engineering?
- The practice of designing and selecting relevant features from the data to 
improve the performance of a machine learning model.

6.
What is the primary goal of concept learning in unsupervised learning?
- To discover patterns or structures in data without labeled examples.

7. What is the primary goal of concept learning?
- To learn to classify or categorize objects based on their features.

8.
What is the "noisy data" problem in concept learning?
- Data that is full of random errors or irrelevant information, making it challenging to extract meaningful patterns.

9.
What is the primary challenge in reinforcement learning?
- Balancing the exploration-exploitation trade-off.

10. 
What is concept learning in the context of Machine Learning?
- Learning to recognize and understand abstract concepts or categories from data.

"""
#----------------------------------------------------------------------------
# idesign
#1. Creating Ranges in numpy

# Write a Python program to create  1-D arrays using arange function defined in numpy library.
# Get the number ranges from user and create a numpy array.

import numpy as np

start = int(input("Enter Starting Number:\n"))
end = int(input("Enter Ending Number:\n"))
print("Array")
print(np.arange(start, end+1))

#2. 
import numpy as mp
import pandas as pd

data = pd.read_csv("training_data.csv")

# remove a row that have duplicate values
data.drop_duplicates(inplace=True) # no need to put axis as it represent row
print("Dataset after removing duplicate rows:")
print(data)

# remove a column that have duplicate values
cols_to_drop = data.columns[data.nunique() == 1] # see for column yg value duplicate

# drop identified column
data.drop(cols_to_drop, axis=1, inplace=True)

print("Dataset after removing columns with a single value:")
print(data)

#3.

import pandas as pd

# Load the dataset from a CSV file
data = pd.read_csv("dataset.csv")

# Calculate the total number of records
num_records = len(data)

# Calculate the number of records containing 'golf'
count_golf = (data['recreation'] == 'golf').sum()

# Calculate the unconditional probability of 'golf'
golf_probability = count_golf / num_records
print(f"Unconditional probability of golf: = {golf_probability:.2f}")

# Calculate the conditional probability of 'single' given 'medRisk'
count_records = ((data['status'] == 'single') & (data['credit_worthiness'] == 'medRisk')).sum()
count_medRisk = (data['credit_worthiness'] == 'medRisk').sum()
probability = count_records / count_medRisk
print(f"Conditional probability of single given medRisk: = {probability:.2f}")

# 4.

'''
DF Shape
(100, 13)

DF Column Types
make              object
model             object
year               int64
selling_price      int64
km_driven          int64
fuel              object
seller_type       object
transmission      object
owner             object
mileage_kmpl     float64
engine_cc        float64
max_power_bhp    float64
seats            float64
dtype: object

Top 5 rows
make                   model  year  selling_price  km_driven    fuel  \
0   Maruti         Swift Dzire VDI  2014         450000     145500  Diesel   
1    Skoda  Rapid 1.5 TDI Ambition  2014         370000     120000  Diesel   
2    Honda      City 2017-2020 EXi  2006         158000     140000  Petrol   
3  Hyundai       i20 Sportz Diesel  2010         225000     127000  Diesel   
4   Maruti         Swift VXI BSIII  2007         130000     120000  Petrol   

seller_type transmission         owner  mileage_kmpl  engine_cc  \
0  Individual       Manual   First Owner         23.40     1248.0   
1  Individual       Manual  Second Owner         21.14     1498.0   
2  Individual       Manual   Third Owner         17.70     1497.0   
3  Individual       Manual   First Owner         23.00     1396.0   
4  Individual       Manual   First Owner         16.10     1298.0   

max_power_bhp  seats  
0          74.00    5.0  
1         103.52    5.0  
2          78.00    5.0  
3          90.00    5.0  
4          88.20    5.0  


'''
#Import the required libraries
import pandas as pd
pd.set_option('display.max_columns',100)
import matplotlib.pyplot as plt  
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

#Load the dataset
data = pd.read_csv("vehicle_data_1.csv")

df = pd.DataFrame(data)

print("DF Shape")
print(df.shape)

print("Data Types")
print(df.dtypes)

print("Top 5 rows")
print(df.head())


#create df of numeric features only.
numeric_features = data.select_dtypes(exclude='object').columns
# atau numeric_features = data.select_dtypes(include=['int64', 'float64']).columns


#Step 4 : Plot  Histogram for all numeric features (Use sns.histplot())
#(Set title as "Histogram" .Save in file uahistogram.png)
plt.figure(figsize = (15,15))
plt.suptitle('Histogram')
for i, feature in enumerate(numeric_features):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uahistogram.png')
plt.clf()

#Step 5 : Plot KDE plot for all numeric features (Use sns.kdeplot())
#(Set title as "KDE Plot" .Save in file uakdeplot.png)
plt.figure(figsize = (15,15))
plt.suptitle('KDE Plot')
for i, feature in enumerate(numeric_features):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uakdeplot.png')
plt.clf()

#Step 6 : Plot Rug Plot for all numeric features (Use sns.rugplot())
#(Set title as "Rug Plot" .Save in file uarugplot.png)
plt.figure(figsize = (15,15))
plt.suptitle('Rug Plot')
for i, feature in enumerate(numeric_features):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uarugplot.png')
plt.clf()

#Step 7 : Plot Box Plot for all numeric features (Use sns.boxplot())
#(Set title as "Box Plot" .Save in file uaboxplot.png)
plt.figure(figsize = (15,15))
plt.suptitle('Box Plot')
for i, feature in enumerate(numeric_features):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uaboxplot.png')
plt.clf()

#Step 8 : Plot Violin Plot for all numeric features (Use sns.violinplot())
#(Set title as "Violin Plot" .Save in file uaviolinplot.png)
plt.figure(figsize = (15,15))
plt.suptitle('Violin Plot')
for i, feature in enumerate(numeric_features):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uaviolinplot.png')
plt.clf()

#Step 9 : Plot Strip Plot for all numeric features (Use sns.stripplot())
#(Set title as "Strip Plot" .Save in file uastripplot.png)
plt.figure(figsize = (15,15))
plt.suptitle('Strip Plot')
for i, feature in enumerate(numeric_features):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uastripplot.png')
plt.clf()

#Categorical Features Plots
#create df of categoric features only.
categorical_features = data.select_dtypes(include = ['object']).columns

#Create df of categorical features where the number of unique values is less than 10




#Step 10 : Plot Count Plot for all Categoric features (Use sns.countplot())
#(Set title as "Count Plot" .Save in file uacountplot.png)
plt.figure(figsize = (10,10))
plt.suptitle('Count Plot')
for i, feature in enumerate(categorical_features):
    plt.subplot(2,2, i+1)
    sns.countplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uacountplot.png')
plt.clf()

#Step 11 : Plot Pie Charts for all Categoric features (Use plt.pie()) 
plt.figure(figsize = (10,10))
plt.suptitle('Pie Chart')
for i, feature in enumerate(categorical_features):
    plt.subplot(2,2, i+1)
    data[feature].value_counts().plot.pie(autopct="%.0f%%")
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uapiechart.png')
plt.clf()

# corrected
import pandas as pd
pd.set_option('display.max_columns', 100)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Load the dataset
data = pd.read_csv("vehicle_data_1.csv")
df = pd.DataFrame(data)

# Step 1: Shape or Dimensions of the DataFrame
print("DF Shape")
shape = df.shape
print(shape)

# Step 2: Explore Data Types of the various columns
print("DF Column Types")
data_type = df.dtypes
print(data_type)

# Step 3: Explore data by displaying 5 rows
print("Top 5 rows")
five_rows = df.head(5)
print(five_rows)

# Numerical Features Plots
num_cols = data.select_dtypes(include=['float64', 'int64']).columns

# Set size of figure
cols = 3
rows = 3

# Step 4: Plot Histogram for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle("Histogram")
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.histplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uahistogram.png")
plt.clf()

# Step 5: Plot KDE plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('KDE Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.kdeplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uakdeplot.png')
plt.clf()

# Step 6: Plot Rug Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Rug Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.rugplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uarugplot.png')
plt.clf()

# Step 7: Plot Box Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Box Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.boxplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uaboxplot.png')
plt.clf()

# Step 8: Plot Violin Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Violin Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.violinplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uaviolinplot.png')
plt.clf()

# Step 9: Plot Strip Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Strip Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.stripplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uastripplot.png')
plt.clf()

# Categorical Features Plots
cat_cols = data.select_dtypes(include=['object']).columns
cat_cols = [col for col in cat_cols if data[col].nunique() < 10]

# Step 10: Plot Count Plot for all categoric features
fig = plt.figure(figsize=(10, 10))
plt.suptitle("Count Plot")
for i, col in enumerate(cat_cols):
    ax = fig.add_subplot(2, 2, i + 1)
    sns.countplot(x=data[col], ax=ax)
#plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uacountplot.png")
plt.clf()

# Step 11: Plot Pie Charts for all categoric features
fig = plt.figure(figsize=(10, 10))
plt.suptitle("Pie Chart")
for i, col in enumerate(cat_cols):
    ax = fig.add_subplot(2, 2, i + 1)
    data[col].value_counts().plot.pie(autopct="%.0f%%", ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uapiechart.png")
plt.clf()
#--------------------------------------------------------
# iaccess

#1.

import numpy as np
from scipy import stats

size = int(input("Enter the number of elements:"))

print("Enter the elements:")
elements = input().split()

# convert from string to integer and keep in list
numbers = list(map(int, elements))

if len(numbers) != size:
    print("The numbers are not match with the size")
else:
    # convert elements to numpy array
    data = np.array(numbers)

    # calculate mean
    mean_value = np.mean(data)

    # calculate median
    median_value = np.median(data)

    # calculate standar deviation
    std_value = np.std(data)

    # calculate mode
    mode_value = stats.mode(data)
    # print(mode_value) akn execute mode value and berapa byk dia ada

print("Mean:", mean_value)
print("Median:", median_value)
print(f"Standard Deviation: {std_value:.4f}")
print(f"Mode: {mode_value.mode[0]}")

#------------------------------------------------------------

#2. Calculate MSE, mean squared error

import numpy as np

actual_values= input("Enter actual values\n").split(",")
predict_values = input("Enter predicted values\n").split(",")

# convert list into float
list_actual_values = list(map(float, actual_values))
list_predict_values = list(map(float, predict_values))

print("List of Actual Values\n", list_actual_values)
print("List of Predicted Values\n", list_predict_values)

y_actual = np.array(list_actual_values)
y_predict = np.array(list_predict_values)

# calculate the Mean Squared Error (MSE)
mse = np.mean((y_actual - y_predict) ** 2)

# round MSE to two decimal places
round_mse = round(mse, 2)

print(f"MSE\n {round_mse}")
   












