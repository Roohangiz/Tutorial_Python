"""
Created on Thu Jan 30 17:28:17 2025

@author: Roohi
"""
#%% Packages

# Built-in packages

# Importing the math module for mathematical operations
import math
# Printing the value of Pi (3.141592653589793)
print(math.pi)

# Importing the os module to work with file paths
import os
# Define a file name
file_name = "Nature.jpg"
# Get the absolute path of the file
abs_path = os.path.abspath(file_name)
print("Absolute Path:", abs_path)
# Check if the file exists
if os.path.exists(file_name):
    print(f"{file_name} exists.")
else:
    print(f"{file_name} does not exist.")
    
    

# Not Built-in packages (External packages)

# Importing NumPy for numerical computations
import numpy as np
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
# Calculate and print the mean of the array
print("Mean:", np.mean(arr))



# Create a package (Custom module)

# Importing a user-defined package named 'MyPackage'
import MyPackage
# Call a function from MyPackage (assumed to be a function that adds numbers)
print(MyPackage.fun_add_numbers(2, 3))
