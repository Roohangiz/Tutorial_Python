"""
Created on Thu Nov 14 18:49:12 2024

@author: Roohi
"""
#%% Loops

# Define a list of numbers from 1 to 7
Numbers =[1, 2, 3, 4, 5, 6, 7]

# Loop through each number in the 'Numbers' list and print it
for num in Numbers:
    print(num)

# Loop through 'Numbers' and print each number until reaching the number 6
# When 'num' equals 6, 'break' stops the loop    
for num in Numbers:
    if num == 6:
        break
    print(num)

# Loop through 'Numbers' and print each number except 6
# When 'num' equals 6, 'continue' skips printing it, moving to the next number
for num in Numbers:
    if num == 6:
        continue
    print(num)
  
# Define two lists, 'Items' and 'Colors'   
Items = ['Shirt' ,'Skirt', 'Pants']   
Colors = ['Turquoise' ,'Pink', 'Purple']

# Nested loop to combine each item in 'Items' with each color in 'Colors'
# Prints each item-color combination
for item in Items:
    for color in Colors:
        print(item, '----', color)
        
# Initialize x with 5 and loop 3 times
# In each iteration, multiply 'x' by itself and print the result        
x = 5
for i in range(3):
    x = x*x
    print(x)
    
# Initialize x and y with 5, then loop 3 times
# In each iteration, multiply 'y' by 'x' and print the result    
x = 5
y = x
for i in range(3):
    y = x*y
    print(y)   
    
# Initialize x with 5, then use a while loop that runs while x is less than 60
# Print x, and if x equals 40, print "It's done!" and break out of the loop
# Increase x by 5 in each iteration    
x = 5
while x < 60:
    print(x)
    if x == 40:
        print("It's done!")
        break
    x+=5

# Initialize x with 5, then use an infinite while loop
# Print x, and if x equals 40, print "It's done!" and break out of the loop
# Increase x by 5 in each iteration    
x = 5
while True:
    print(x)
    if x == 40:
        print("It's done!")
        break
    x+=5