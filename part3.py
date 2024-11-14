
"""
Created on Thu Nov 14 16:26:13 2024

@author: Roohi
"""
#%% Conditions

# Define a variable 'condition' and set it to True. If the condition is true, print 'T'
condition = True
if condition:
    print('T')
   
# Define a variable 'X' with a value of 20. Check if X equals 20, print 'True', otherwise print 'False'
X = 20   
X = 20
if X == 20:
    print('True')
else:
    print('False')
    
# Define three variables: Name, Language, and Online
# Check if Name is 'Roohi', Language is 'Python', and Online is True. 
# If all conditions are met, print a checkmark (✔), otherwise print 'X'    
Name = 'Roohi'
Language = 'Python'
Online = True
if Name == 'Roohi' and Language == 'Python' and Online:
    print('\u2713')
else:
    print('X')
  
# Check if Name is 'Roohi', Language is 'Java', and Online is True. 
# Since Language is 'Python', this condition will fail, so it should print 'X'    
if Name == 'Roohi' and Language == 'Java' and Online:
    print('\u2713')
else:
    print('X')

# Check if Name is 'Roohi' OR Language is 'Java' AND Online is True.
# Since Name is 'Roohi', the condition will pass, so it should print a checkmark (✔)
if Name == 'Roohi' or Language == 'Java' and Online:
    print('\u2713')
else:
    print('X') 
  
# Define a variable 'Y' and check its range.
# If Y is less than 200, print 'Increase'.
# If Y is between 200 and 250 (exclusive of 200), print "It's Ok".
# Otherwise, print 'Decrease'.    
Y = 237
if Y < 200:
    print('Increase')
elif 200 < Y < 250:
    print("It's Ok")
else:
    print('Decrease')
    
# Demonstrate identity and equality in Python
# Define 'a' and 'b' with the same value and compare them    
a = 200
b = a
print(a == b)  # Check if a is equal to b (True)
print(a is b)  # Check if a is the same object as b (True)
print(id(a))   # Print memory ID of 'a'
print(id(b))   # Print memory ID of 'b'

# Define 'c' and 'd' with the same value but check if they refer to the same object in memory
c = 700
d = 700
print(c == d)  # Check if c is equal to d (True)
print(c is d)  # Check if c is the same object as d (may be False, as higher values may create separate objects)
print(id(c))   # Print memory ID of 'c'
print(id(d))   # Print memory ID of 'd'


