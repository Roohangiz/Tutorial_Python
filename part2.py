
"""
Created on Sun Sep 15 20:22:44 2024

@author: Roohi
"""
#%% Dictionary
car = {'Brand':'Ford', 'Model':'Mustang', 'Year':1965, 'Colors':['Red','Blue']}

# Print the value associated with the key 'Brand'
print(car['Brand'])

# Try to get the value for the key 'Price' (which does not exist)
# This will return None because 'Price' is not a key in the dictionary
print(car.get('Price'))

# Try to get the value for the key 'Price' with a default return value of 'No price'
# Since 'Price' doesn't exist, 'No price' will be returned
print(car.get('Price', 'No price')) 

# Update the value for the key 'Year' to 1964
car['Year'] = 1964
# Print the updated dictionary
print(car) 

# Add a new key-value pair 'Price': 'No information' to the dictionary
car['Price'] = 'No information'
# Print the updated dictionary
print(car)

# Use the update method to update multiple keys in the dictionary: 'Brand', 'Model', 'Year' and add a new key 'City'
car.update({'Brand': 'Chevrolet', 'Model': 'Corvette', 'Year': 1963, 'City':'Detroit'})
# Print the updated dictionary
print(car)

# Delete the key 'Price' from the dictionary
del car['Price']
print(car)

# Remove the key 'Colors' using the pop method
car.pop('Colors')
print(car)

# Print the number of key-value pairs in the dictionary
print(len(car))

# Print all the keys in the dictionary
print(car.keys())

# Print all the values in the dictionary
print(car.values())

# Print all key-value pairs in the dictionary as tuples
print(car.items())


# Loop through all the keys in the dictionary and print them
for key in car.keys():
    print(key)


# Loop through the dictionary and print each key and its corresponding value    
for key, value in car.items():
     print(key, '-------', value)   