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

print(word[:2])  # This will print first two letters based on the index number
print(word[-2:])  # This will print last two letters based on the index number
print(word[:2]+word[-2:])  # Final output


gd = 'good'
print(gd[0]+gd[1]+gd[-2]+gd[-1])  # Final output
print(gd[:2])  # This will print first two letters based on the index number
print(gd[-2:])  # This will print last two letters based on the index number
print(gd[:2]+gd[-2:])  # Final output

d = 'dad'
print(d[:2]+d[-2:])  # Final output

""" Write a Python program to get first character from given string and change occurrence of the first character to $ 
except the first character.
Sample String : 'restart'
Expected Result : 'resta$t'
Sample String : 'good afternoon'
Expected Result : 'good afternoon'
"""

rpls = input("Enter the string: ")
print('First letter of given string is {}'.format(rpls[0]))
up_rpls = rpls[1:]  # Skips the first character and display remaining string
print(up_rpls)
up_rpls = up_rpls.replace(rpls[0], "$")  # Replaces the first letter occurrence to $, except first lettergoo
print(rpls[0]+up_rpls)

""" Write a Python program to remove duplicate characters of a given string."""


dup = input('Enter the string: ')
un_dup = set(dup)  # Set is a data type which excludes duplicate values or will not accept repeated values
un_dup = ''.join(un_dup)  # Join method is used to combine the sequence values like list,tuple
print(un_dup)


""" Write a Python program to add 'ing' at the end of a given string. If the given string already ends with 'ing' 
then add 'ly' instead.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'morning'
Expected Result : 'morningly'
"""

strng = input('Enter the word: ')
if strng.endswith('ing'):
    strng += 'ly'
else:
    strng +='ly'
print(strng)


""" Write a Python script that takes input from the user and displays that input back in upper and lower cases. """

lw = input("Enter the message: ")
print(lw.lower())


""" Write a Python program to check whether a string starts with specified characters."""

strng = "Welcome to python world"
if strng.startswith("Welcome"):
    print("starts with Welcome")
else:
    print("Starting word different")


""" Write a Python program to print the index of the character in a string.
Sample string: google
Expected output:
Current character g position at 0
Current character e position at 5
"""

# index or find method will return the position of letter/word.
# Tt will return the least position/first occurrence of the given letter has duplicate values.

msg = "google"
print(msg.index("g"))  # Index method finds index position of given letter/word, gives error if letter/word not found
print(msg.find("e"))   # Find method finds index position of given letter/word, returns -1 if letter/word not found


""" Write a Python program to convert a string in a list."""

strr = "Welcome to pycharm"
print(list(strr))  # list method will return individual letters in a list format
print(strr.split())  # split method will return individual words in a list format default,
print(strr.split("o"))  # If any letter/word passed into split, then split happens based on that


""" Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters 
in the first 4 characters."""


word = input("Enter the word: ")
up_count = 0
for i in word[:4]:
    if i.isupper() and up_count < 3:  # isupper returns true if letter is capital
        up_count += 1
if up_count >= 2:
    print("Contains upper case in first 4 letters", word.upper())
else:
    print("No upper case in first 4 letters", word.upper())



