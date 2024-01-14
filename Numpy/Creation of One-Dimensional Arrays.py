# There is 6 ways to create an array in python

from numpy import *

# Method 1 - using array() - 1-Dimension only 
arr = array([1, 2, 3],int)
print(arr)

# Method 2 - using linspace() - Equal Spcaes
arr = linspace(1, 15, 4, int)
print(arr)

# Method 3 - using logspace() - No equal Spaces and numbers b/w 10^1 to 10^15
arr = logspace(1, 15, 2)
print(arr)

# Method 4 - using arange() - Equal Spaces b/w numbers
arr = arange(1, 17, 5)
print(arr)

# Method 5 - using zeros(size) - how many zeros you want!
arr = zeros(5, int)
print(arr)

# Method 6 - using ones(size) - how many ones you want!
arr = ones(12, int)
print(arr)
