# Write a Python program to check whether a given string is a palindrome (ignore upper/lower case). 

# Input: Madam 

# Output: True 

 

# Input: python 

# Output: False 

string = str(input("Enter a string "))

reverse = string[::-1]

if string == reverse:
    print("string is a palindrome")
else:
    print("string is not a palindrome ")
