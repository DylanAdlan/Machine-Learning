'''
iexplore

1.
Which function in the scipy.optimize submodule is used to minimize a function using the downhill simplex algorithm?
- scipy.optimize.fmin

2.
What is the purpose of the scipy.interpolate submodule?
- Interpolation and smoothing functions

3.
Which function in the scipy.stats submodule is used to generate random numbers from a normal distribution?
- scipy.stats.norm

4.
What is the purpose of the scipy.optimize submodule?
- optimization algorithms

5.
What is the purpose of the scipy.linalg submodule?
- Linear algebra operations

6.
Which function in the scipy.linalg submodule is used to compute the eigenvalues and eigenvectors of a square matrix?
- scipy.linalg.eig

7.
What is the primary purpose of the scipy.stats submodule?
- Statistical functions and probability distributions

8.
What is the primary purpose of the SciPy library in Python?
- Scientific computing and technical computing

9.
Which function in the scipy.interpolate submodule is used to perform 1-D interpolation?
- scipy.interpolate.interp1d

10.
Which of the following is NOT a submodule of the SciPy library?
- scipy.plot

ianalyse

1.
What is the purpose of the scipy.ndimage submodule?
- Image processing and analysis

2.
What is the primary purpose of the scipy.cluster submodule?
- Clustering algorithms

3.
Which function in the scipy.io submodule is used to load MATLAB data files?
- scipy.io.loadmat

4.
Which function in the scipy.spatial submodule is used to compute the distance between two points in space?
- scipy.spatial.distance.euclidean

5.
Which function in the scipy.cluster submodule is used to perform hierarchical clustering?
- scipy.cluster.hierarchy

6.
What is the purpose of the scipy.special submodule?
- Special mathematical functions

7.
Which function in the scipy.special submodule is used to compute the gamma function?
- scipy.special.gamma

8.
What is the purpose of the scipy.spatial submodule?
- Spatial data analysis and algorithms

9.
Which function in the scipy.ndimage submodule is used to apply a Gaussian filter to an image?
- scipy.ndimage.gaussian_filter

10.
What is the purpose of the scipy.io submodule?
- Input and output operations for various file formats


# '''
# # idesign
# # 1.

# import numpy as np
# from scipy.special import exp10, sindg, cosdg

# # input exponenet value
# exp_val = int(input("Enter the exponent value:\n"))

# # calculate 10 raised to the power of exponent
# result_exp10 = exp10(exp_val)
# print(f"10 raised to the power of {exp_val} : {result_exp10}")

# # input degree
# degree = float(input("Enter the angle in degrees:\n"))

# # find sine and cosine of the degree
# sin_val = sindg(degree)
# cos_val = cosdg(degree)

# print(f"Sine of {degree} degrees: {sin_val}")
# print(f"Cosine of {degree} degrees: {cos_val}")

# # # 2.

# import numpy as np
# from scipy.stats import linregress

# x = input("Enter the values of x separated by spaces: ").split()
# y = input("Enter the values of y separated by spaces: ").split()

# x = np.array([float(number) for number in x])
# y = np.array([float(number) for number in y])

# # perform linear regression
# stats = linregress(x,y)

# slope, intercept, r_val, prob, std_error = stats

# # calculate R-squared value
# r_squared = r_val ** 2

# print(f"Slope: {slope}")
# print(f"Intercept: {intercept}")
# print(f"R-squared: {r_squared}")
# print(f"p-value: {prob}")
# print(f"Standard error: {std_error}")

# 3.

# # import root function from scipy.optimize module ( to find roots)
# import numpy as np
# from scipy.optimize import root

# # define the equation function
# def equation(x):
#     return (x ** 3) - (2 * x) -5

# # get initial guess form the user
# x0 = float(input("Enter initial guess: "))

# # find root using scipy.optimize.root
# result = root(equation, x0)
# print("Root:", result.x)

# # 4.

# import numpy as np
# from scipy.integrate import dblquad

# function = input("Enter the function to be integrated in terms of x and y:\n")
# min_x = int(input("Enter the lower limit for x:\n"))
# max_x = int(input("Enter the upper limit for x:\n"))
# min_y = int(input("Enter the lower limit for y:\n"))
# max_y = int(input("Enter the upper limit for y:\n"))

# funct = lambda y, x:eval(function) # eval function execute string function and substitute to actual value

# result, error = dblquad(funct, min_x, max_x, lambda x: min_y, lambda x: max_y)

# print(f"Result of dblquad integration: {result}")
# print(f"Error estimate: {error}")

#--------------------------------------------------
# iaccess

import numpy as np
from scipy.fft import fft, ifft

numbers = input("Enter the sequence (comma-separated values): \n").split(",")

numbers = np.array([float(number) for number in numbers])

result_fft = fft(numbers)

result_ifft = ifft(result_fft)

print(f"Fourier Transform of the sequence: {result_fft}")
print(f"Inverse Fourier Transform of the transformed sequence: {result_ifft}")

            