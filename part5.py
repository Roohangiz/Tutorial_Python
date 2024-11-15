"""
Created on Thu Nov 14 20:48:30 2024

@author: Roohi
"""
#%% Function

# Define a simple function that prints "car color"
def car_color_print():
    print('car color')
 # Call the function to display the message   
car_color_print()
    
# Define a function that returns a string "car color" instead of printing it
def car_color_print():
    message = 'car color'
    return message
# Call the function, store the returned value in 'msg', and print it
msg = car_color_print()
print(msg)
# Calls the function directly and prints its return value
print(car_color_print())


# Define a dictionary mapping numbers to car colors
car_colors  = {1:'blue', 2:'red', 3:'green'}
# Define a function that takes a number as input and returns the corresponding car color
def car_color_print(num):
    car_color = car_colors[num]         # Get the car color from the dictionary
    message = 'car color:' + car_color  # Create a formatted string with the car color
    return message
# Another version of the function using f-strings for cleaner formatting
car_colors  = {1:'blue', 2:'red', 3:'green'}
def car_color_print(num):
    car_color = car_colors[num]         # Get the car color from the dictionary
    return f'car color: {car_color}'    # Return the formatted string directly
# Call the function with the input 2 and print the result
print(car_color_print(2))


# Define a function that accepts variable-length positional and keyword arguments
def car_info(*args, **kwargs):
    print(args)                         # Print the tuple of positional arguments
    print(kwargs)                       # Print the dictionary of keyword arguments

# Define a list of cities and a dictionary of car specifications    
Cities = ['New York', 'Paris']  
Specs = {'Brand' : 'Ford', 'Model' : 'B-Max'} 
# Call the function, unpacking the list into positional arguments and the dictionary into keyword arguments 
car_info(*Cities, **Specs)
