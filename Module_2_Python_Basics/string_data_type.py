#  --------- Primitive/Fundamental String data type, type conversion & there built-in methods with examples --------  #

"""
• string - Is used to represent collection of characters. Characters can be any alphabets, digits & special characters.
    • Example of strings are 'welcome to python', 'hello 123', '1947', '@#$$$' etc.
• type() - Is a built-in function, which tells what kind of data type the variable/value holds.
"""
#  ---------------------------------------  String data type  -------------------------------------------------  #
#  str() - Is a built-in method which is used to convert any values to string data type

month = "August"
print(month, type(month))

dob = '1-Sep-2022'
print(dob, type(dob))

email_id = "welcome_to_python@gmail.com"
print(email_id, type(email_id))

week = 7
print(week, type(week), 'Before converting to string')

con_week = str(week)
print(con_week, type(con_week), 'After converting to integer')

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(str(days), type(days))

iphone_cost = "799$"
print(iphone_cost, type(iphone_cost))

""" --------------------------------------- String Built-in methods ---------------------------------------------------
capitalize()   find()         isdecimal()    istitle()      partition()    rpartition()   swapcase()    
casefold()     format()       isdigit()      isupper()      removeprefix() rsplit()       title()       
center()       format_map()   isidentifier() join()         removesuffix() rstrip()       translate()   
count()        index()        islower()      ljust()        replace()      split()        upper()       
encode()       isalnum()      isnumeric()    lower()        rfind()        splitlines()   zfill()       
endswith()     isalpha()      isprintable()  lstrip()       rindex()       startswith()                 
expandtabs()   isascii()      isspace()      maketrans()    rjust()        strip()
--------------------------------------- End of String Built-in methods -------------------------------------------- """

'''
capitalize() - Returns a capitalized version of the string. More specifically, make the first character have upper 
 case and the rest lower case.
'''
message = 'WELCOME to python 3.9version!'
print('Original string: %s' % message)
print('After capitalization: %s' % message.capitalize())


'''
casefold() - Returns a version of the string suitable for caseless comparisons.
'''
casefld = 'Python WORLD!'
print(casefld.casefold())


'''
center() - Method centers given string in a given number of character space.
'''
cntr = "Python is awesome"
print(cntr.center(34))


'''
count() - Returns the number of occurrences of a substring in the given string.
'''
occr = "Python is awesome, isn't it?"
print("The count is:", occr.count("i"))


'''
encode() -
'''


'''
endswith() -
'''


'''
expandtabs() -
'''


'''
find() -
'''


'''
format() -
'''


'''
format_map() -
'''

'''
index() -
'''


'''
isalnum() -
'''


'''
isalpha() -
'''


'''
isascii() -
'''


'''
isdecimal() -
'''


'''
isdigit() -
'''


'''
isidentifier() -
'''


'''
islower() -
'''


'''
isnumeric() -
'''


'''
isprintable() -
'''


'''
isspace() -
'''


'''
istitle() -
'''


'''
isupper() -
'''


'''
join() -
'''


'''
ljust() -
'''


'''
lower() -
'''


'''
lstrip() -
'''


'''
maketrans() -
'''


'''
partition() -
'''


'''
removeprefix() -
'''


'''
removesuffix() -
'''


'''
replace() -
'''


'''
rfind() -
'''


'''
rindex() -
'''


'''
rjust() -
'''


'''
rpartition() -
'''


'''
rsplit() -
'''


'''
rstrip() -
'''


'''
split() -
'''


'''
splitlines() -
'''


'''
startswith() -
'''


'''
strip() -
'''


'''
swapcase() -
'''


'''
title() -
'''


'''
translate() -
'''


'''
upper() -
'''


'''
zfill() -
'''
#  ---------------------------------------  End of string data type -----------------------------------------------  #
