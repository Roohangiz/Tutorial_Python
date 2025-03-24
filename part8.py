"""
Created on Thu Feb 27 18:22:32 2025

@author: Roohi
"""
# try , except, else, finally

text1 = input("Your age:")              # Prompt the user to enter their age 
try:
    print("My age is", str(int(text1))) # Attempt to convert input to an integer and print it
except:
    print("Not a number")               # If conversion fails, print an error message
else:
    print("Thank you")                  # Executes only if no exception occurs
finally:
    print("Bye!")                       # Always executes, regardless of success or failure
  
    
text2 = input("Your age:")              # Prompt the user to enter their age 
txtfilename = input("Your filename:")   # Prompt the user to enter a filename
try:
    f = open(txtfilename)               # Attempt to open the specified file
    print("My age is", str(int(text2))) # Attempt to convert input to an integer and print it
except FileNotFoundError:
    print("Filename not correct")       # If the file does not exist, print an error message
except ValueError:
    print("Text must be integer")       # If age input is not a valid integer, print an error message
except Exception as e:
    print(e)                            # Catch any other unexpected exceptions and print the error message
else:
    print(f.read())                     # If no exception occurs, read and print the file content
finally:
    f.close()                           # Always close the file, even if an exception occurs

