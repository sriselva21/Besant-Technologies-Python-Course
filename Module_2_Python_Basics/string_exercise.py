#  ----------------------------------------- Exercise on String data type ------------------------------------------  #


""" Write a Python program to calculate the length of a string. """
# len() - Is a built function which is used to find length of sequences like list,str, tuple, set, dict (keys).
# len() does not support for number data type
msg = 'Welcome to Python!'
print('Length of the string {} is {}'.format(msg, len(msg)))


""" Write a Python program to count the number of given characters/word. """

message = "Hello welcome to python world"
print('Count of {} is {}'.format('l', message.count('l')))

print('Count of {} is {}'.format('hello', message.count("hello")))  # Python is a case-sensitive language.
print('Count of {} is {}'.format('Hello', message.count("Hello")))  # Hello is not same as hello (hello != Hello).
print('Count of {} is {}'.format('python', message.count("world")))


""" Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
Sample String : 'english'
Expected Result : 'ensh'
Sample String : 'god'
Expected Result : 'good'
"""

word = 'english'
print(word[0])  # [0] - Is known as indexing/slicing, we can pass only +ve int number, only one number at a time.
print(word[-1])  # [-1] - Is known as negative indexing/slicing, we can pass only -ve int number,
#  only one number at a time.

print(word[0], word[1])  # This will give zero and first position letters.

print(word[-2], word[-1])  # This will return the values in reverse order.

print(word[0]+word[1]+word[-2]+word[-1])  # Final output

gd = 'good'
print(gd[0]+gd[1]+gd[-2]+gd[-1])  # Final output

# 4. Write a Python program to get a string from a given string
# where all occurrences of its first char have been changed to '$',
# except the first char itself.
# Sample String : 'restart'
# Expected Result : '$esta$t'
# 5. Write a Python program to remove duplicate characters of a
# given string.
# 6. Write a Python program to add 'ing' at the end of a given
# string. If the given string already ends with 'ing' then add 'ly'
# instead.
# Sample String : 'abc'
# Expected Result : 'abcing'
#
# Sample String : 'string'
# Expected Result : 'stringly'
# 7. Write a Python program to count the occurrences of each
# word in a given sentence.
# 8. Write a Python script that takes input from the user and
# displays that input back in upper and lower cases.
# 9. Write a Python function to convert a given string to all
# uppercase if it contains at least 2 uppercase characters in the
# first 4 characters.
# 10. Write a Python program to remove a newline in Python.
# 11. Write a Python program to check whether a string starts with
# specified characters.
# 12. Write a Python program to strip a set of characters from a
# string.
# 13. Write a Python program to print the index of the character in
# a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
#
# 14. Write a Python program to convert a string in a list.
# 15. Write a Python program to count and display the vowels of a
# given text.