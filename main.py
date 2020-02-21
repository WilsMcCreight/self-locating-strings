import os # To read files with
import sys # For the exit command

file_name = "./pi1000000.txt" # INPUT :: Insert the path to your own text file containing the number to scan
starting_index = 1 # INPUT :: Insert the index you want our counting to begin with (The index of the tens place)

if starting_index < 0 or int(starting_index) != startind_index:
    print("Error: Invalid starting_index")
    sys.exit()

with open(file_name) as f: # Save the contents of the file to the variable 'digits'
    digits = f.read()


for i in range(len(digits)): # Strip the leading digits up until the decimal point, leaving just the decimal digits
    if digits[i] == '.':
        break
digits = digits[i+1:]


for i in range(len(digits)):
    number = str(i + starting_index)
    slice = digits[i:i+len(number)]
    # print(slice)
    if number == slice:
        print(number)
