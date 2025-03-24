"""
Created on Mon Feb 17 17:32:50 2025

@author: Roohi
"""
# if__name__ == '__main__'

# Running a user-defined module  named 'part7a'
import part7a    # Ensure that 'part7a.py' is in the same directory as the current file

# This function will work because it is defined globally in 'part7a.py'
part7a.function_Hello_En()

# This will NOT work when importing 'part7a' because 'function_Hello_Fa()' is defined inside 
# the if __name__ == '__main__': block. This means it only exists when 'part7a.py' is run directly 
# and is NOT available when imported as a module.
part7a.function_Hello_Fa()  # This will raise an AttributeError
