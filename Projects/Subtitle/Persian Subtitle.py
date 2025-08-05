"""
Created on Thu Jan 30 23:10:03 2025

@author: Roohi
"""
#%% Persian Subtitle

# Import the OS module to interact with the operating system (like file paths)
import os
# Import the GoogleTranslator class from deep_translator for language translation
from deep_translator import GoogleTranslator

# Define the file path where the subtitle file is located
filepath = "C:/Roohi/Git/Tutorial_Python/Projects"
# Name of the subtitle file we want to translate
filename = "English.srt"

# List of numbers, which helps to identify subtitle timing lines (e.g., "00:00:01,500 --> 00:00:04,000")
nums= ['0','1','2','3','4','5','6','7','8','9']

# Initialize the translator with source language as 'en' (English) and target language as 'fa' (Farsi)
translator = GoogleTranslator(source="en", target="fa") 
 
# Combine the file path and file name to create the full path to the subtitle file
# And Open the subtitle file in read mode with UTF-8 encoding (to handle any special characters properly)
with open(os.path.join(filepath, filename),'r', encoding='utf-8') as f:
    sub_lines = f.readlines()    # Read all the lines from the subtitle file into a list
# Generate and Open the output file path and the output file in write mode with UTF-8 encoding to avoid character encoding issues
with open(os.path.join(filepath, "Farsi.srt"),'w', encoding='utf-8') as f:
    for line_en in sub_lines:    # Loop through each line in the subtitle file
        if line_en[0] in nums:   # If the line starts with a number, it's a timestamp line (e.g., "1", "2", etc.)
            f.write(line_en)     # Write the timestamp line unchanged to the output file
        elif line_en == '\n':    # If the line is empty (i.e., just a blank line)
            f.write('\n')        # Write an empty line to the output file
        else:
            line_fa = translator.translate(line_en) # Translate the line from English to Farsi
            f.write(line_fa)                        # Write the translated Farsi line to the output file

# Print a success message indicating the translation is complete and where the output is saved
print(f"✅ Translation complete! Saved as: {filepath}")
    

    
