import os # To read files with
import re # Regular expressions to preprocess strings

file_name = "./pi1000000.txt" # INPUT :: Insert the path to your own text file containing the number to scan
starting_index = 1 # INPUT :: Insert the index you want our counting to begin with (The index of the tens place)

with open(file_name) as f: # Save the contents of the file to the variable 'digits'
	digits = f.read()

#digits = re.sub(r'.*\.', '', digits) # Strip the leading digits up until the decimal point, leaving just the decimal digits


for i in range(len(digits)):
    if digits[i] == '.':
        break
digits = digits[i+1:]


for i in range(len(digits)):
    number = str(i + starting_index)
    slice = digits[i:i+len(number)]
    # print(slice)
    if number == slice:
        print(number)
