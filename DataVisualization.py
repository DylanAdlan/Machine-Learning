"""
iexplore

1.
- used to visualize a trend in data over intervals of time.
- often drawn chronologically.

answer = line chart

2.
Tableau Online has a storage limit of over 100 tera bytes

answer = False

4.
types of visualizations in Matplotlib
- line plot 
- scatter plot
- histogram plot
- box plot
- bar chart
- pie chart

5.
Tableau Product that not free of cost
- Tableau Desktop

6.
python package used for 2D graphics?
- matplotlib.pyplot

7.
Tableau Software is an American computer software company 
headquartered in____________
- Seattle

8.
_____ represents categorical data with rectangular bars. 
Each bar has a height corresponds to the value it represents.
- Bar chart

9.
Which of the following is circular graphic and 
is divided into slices to illustrate numerical proportion?
- Pie chart

10.
Tableau cannot be used without having a good programming knowledge

# ianalyse
1.
______ method inside the file is used to display your plot.
- plt.show()

2.
_______________can be used to apply a required view to the existing data 
in the worksheet
- Show Me

3.
Tableau Desktop can be installed only in
- Windows Os and Mac OS

4.
A user-defined grouping of measures in the data source is called as ____________
- Bin

5.
A card to the left of the view, where you can drag fields to control 
mark properties such as type, color, size, shape, label, tooltip, and detail
- Mark Cards

6.
A field of clear-cut information is called as ________________
- Measures

7.
_______ is a management software for installing python packages.
- pip

8.
assign labels to those respective x and y axes
- plt.xlabel
- plt.ylabel

9.
make a bar chart using Matplotlib?
- plt.bar()

10.
- To make a pie chart with Matplotlib, we can use the plt.pie() function. (True)
- The autopct parameter allows us to display the percentage value using the Python string formatting. (True)


"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()


plt.style.use('classic')
fig = plt.figure()
ax = plt.axes()

# video 1


'''
6.

7.

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips', cache=True, data_home='\temp')


# plot histogram
sns.histplot(data= tips, x = "total_bill", kde=True)
# kde(Kernel Density estimate) = the curve on the histogram (to represent smoothed estimate of data's distribution)

plt.savefig('splot2.png')


8.

import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips', cache=True, data_home='\temp')

sns.countplot(data=data, x="day", hue="sex", palette='magma')
# save plot to a file
plt.savefig('splot6.png')



'''
# iaccess

'''
1.# iacess
#1.

# import module
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# read data
data = pd.read_csv("Medals.csv")

team_name = data['Team']
total_medal = data['Total']

#create plot
plt.figure()
plt.plot(team_name, total_medal, linestyle="solid")

# set labels and title
plt.xlabel('Team Name')
plt.ylabel('Total Number of Medals')
plt.title('Team-wise Total Medal Data')
plt.savefig('plot1.png')



2.

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load dataset
data = sns.load_dataset('tips', cache=True, data_home='\temp')

# intialize color palette for the graph
palette = {"Thur": "#1f77b4", "Fri": "#ff7f0e", "Sat": "#2ca02c", "Sun": "#d62728"}

# Customize the appearance of outliers
flierprops = dict(marker='D', markerfacecolor='grey', markeredgecolor='black')

# create plot( boxplot)
sns.boxplot(data=data, x="day", y="total_bill", palette=palette, flierprops=flierprops)

# save the plot
plt.savefig('splot8.png')


'''