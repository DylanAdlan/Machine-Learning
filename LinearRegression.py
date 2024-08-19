'''
iexplore

1.
List methods to reduce heteroscedasticity (i a issue occured bila variance of residuals/ errors not constant across all levels of independent variables)

answer: 

- Logarithmising the data
- Using weighted linear regression
- Attach weights directly related to the magnitude of the dependent variable.

2. 
Statement 1:Decreasing the bias increases the variance. (True)
Statement 2:Decreasing the variance increases the bias. (True)

3.
Multicollinearity occurs when some of the
- independent variables are highly positively correlated with each other.
- Independent variables are highly negatively correlated with each other.

4.
Linear regression is a
- Statistical algorithm
- Machine Learning Algorithm

5.
A random variable is said to be heteroscedastic when different subpopulations have different variabilities (standard deviation).
- when different subpopulations have different standard deviation.
- when different subpopulations have different variabilities.

6.
three main assumptions in a linear regression model.
- There is a linear relationship between the dependent and independent variables.
- The independent variables are measured without error.
- It is assumed that the residual terms have the same (but unknown) variance

7.
If the training error and true error (cross-validating error) converge to the same value and the corresponding value of the error is high, it indicates that the model is ____________ 
and is suffering from ____________bias.
- underfitting,high

8.
The production cost of a company for each year are shown in the table below. x(year):2016 2017 2018 2019 2020 y(cost):12 19 29 37 45 Find the least square regression line y = a x + b. Value of a and b are ___________ and _____________.
- 0.605 ,0.263


9.
List the assumptions impacting the tradeoff between underfitting and overfitting.
- The polynomial degree

10.
If strong relationship between X and Y exists then _______________________.
- Correlation coefficient = 0.9

ianalyse
1.
Which metric is used in measuring individual impact of variables in a model?
- P-value

2.
A variable has high p-value. We dropped it. What happens to R-square?
- it will not be impacted

3.
In the equation of a straight line, Y = mX + c the term, m is the: 
- slope

4.
If the slope of the regression line is calculated to be 2.5 and the intercept 16 then the value of Y when X is 4 is:
- 26

5.
If the p-value of a variable in the regression model is 0.65, what should we do?
- Keep this variable and drop closest variable with similar p-value

6.
Two variable have same p-value in a regression line. What does that indicate?
- It indicates nothing about the relation of the variables

7.
R-Square value of a regression model is 0.85
- Good model. 15% un explained variance

8.
A multiple regression model has the form: y = 2 + 3x1 + 4x2. As x1 increases by 1 unit (holding x2 constant), y will
- increase by 3 units

9.
For a multiple regression model, SST = 200 and SSE = 50. The multiple coefficient of determination is
- 0.75

10.R2 is the mathematical notation for:
- The Co-efficient of Determination

#---------------------------------------------------------
#cth cari covariance using numpy library

# 1

import numpy as np

# Example data
X = [10, 15, 20, 25, 30]
Y = [5, 10, 15, 20, 25]

# Calculate covariance
covariance = np.cov(X, Y)[0, 1]
print(covariance)


'''
'''# idesign

#2.

import numpy as np

size = int(input())

x = []
y = []

for i in range(size):
    value_x, value_y = input().split(",")
    x.append(int(value_x))
    y.append(int(value_y))

correlation_coef = np.corrcoef(x,y)[0,1]

print(f"Correlation Coefficient: {correlation_coef:.2f}")
'''
#3.

# import numpy as np

# number = input().split()
# number = list(map(int, number))
# numbers = np.array(number)

# mean_num = np.mean(numbers)
# print(f"{mean_num:.1f}")

# #4

# import numpy as np

# num1 = input().split()
# num2 = input().split()

# num1 = list(map(int, num1))
# num2 = list(map(int, num2))


# correlation = np.corrcoef(num1, num2)[0,1]
# print(round(correlation, 2))


#5.
import numpy as np

# input 2 list of numbers
x = input().split()
y = input().split()

# make them into integer
x = list(map(float, x))
y = list(map(float, y))

# find mean
mean_x = np.mean(x)
mean_y = np.mean(y)

# find standard deviation
std_x = np.std(x)
std_y = np.std(y)

# find correlation
correlation = np.corrcoef(x,y)[0,1]

# find slope
slope = correlation * (std_y / std_x)


# find intercept
intercept = mean_y - (slope * mean_x)

# execute all
print("Mean of x =", mean_x)
print("Mean of y =", mean_y)
print(f"SD of x = {round(std_x, 3)}")
print(f"SD of y = {round(std_y, 3)}")
print(f"Correlation of x and y = {round(correlation, 3)}")
print(f"Scope = {round(slope,3)}")
print(f"Intercept = {round(intercept, 3)}")

#------------------------------------------------

# iaccess

#1.

# to find a r, correlation coefficient by covariance and variance is covariance / (square root(var x * var y))
# import library
import numpy as np

covariance = float(input())

var_x = float(input())
var_y = float(input())

coefficient = covariance /( (var_x * var_y)**(1/2))
print(round(coefficient, 3))

# 2.

import numpy as np

number = input().split()


numbers = list(map(int, number))
numbers = np.array(numbers)

# find standard deviation using 
std_dev = np.std(numbers)
print(round(std_dev, 2))





