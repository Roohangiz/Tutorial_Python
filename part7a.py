"""
Created on Mon Feb 17 17:32:50 2025

@author: Roohi
"""
# if__name__ == '__main__'

# This function is always available, whether the script runs directly or is imported    
def function_Hello_En():
    print("Hello")

# This checks if the script is being run directly or imported as a module
if __name__ == '__main__':
    print("Direct")
    # Defining a function inside the if-block (not recommended unless necessary)
    def function_Hello_Fa():
       print("سلام")  # This prints "Hello" in Persian
else:
    print("Indirect") # This will print if the script is imported as a module
 
print(__name__)