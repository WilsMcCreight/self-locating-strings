import os # To read files with
import re # Regular expressions to preprocess strings

file_name = "./pi1000000.txt" # Insert the path to your own text file containing the number to scan

with open(file_name) as f: # Save the contents of the file to the variable 'digits'
	digits = f.read()

#digits = re.sub(r'.*\.', '', digits) # Strip the leading digits up until the decimal point, leaving just the decimal digits


for i in range(len(digits)):
    if digits[i] == '.':
        break
digits = digits[i+1:]


for i in range(len(digits)):
    number = str(i + 1)
    slice = digits[i:i+len(number)]
    # print(slice)
    if number == slice:
        print(number)
