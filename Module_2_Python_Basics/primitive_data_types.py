#  ---------- Primitive/Fundamental data types, type conversion & there built-in methods with examples -------------  #

"""
Fundamental or Primitive Data Types in Python
• integer number - Whole number from -∞ to +∞ are integer numbers. Example: 45, -90, 89, 1171 are integer numbers.
• floating point number - Is used to represent floating/decimal point numbers. Ex: 4.5, -9.0, 81.71
• complex number - It has two parts, real part and imaginary part.
    Complex numbers are represented as A+Bi or A+Bj, where A is real part and B is imaginary part.
• boolean - Is used to represent logical True and False. True hold value as 1 and False as 0.
• string - Is used to represent collection of characters. Characters can be any alphabets, digits & special characters.
    • Example of strings are 'welcome to python', 'hello 123', '1947', '@#$$$' etc.
• type() - Is a built-in function, which tells what kind of data type the variable/value holds.
"""


#  ---------------------------------------  Integer data type  -------------------------------------------------  #
#  int() - Is a built-in method which is used to convert the values from int, str and float to integer data type
year = 2022
print(year, type(year))

temperature = -9
print(temperature, type(temperature))

amount = 46579
print(amount, type(amount))

#  Integer has a built method to convert the values from int, str and float to integer data type
mobile = '9845098450'
print(mobile, type(mobile), 'Before converting to integer')

mob = int(mobile)
print(mob, type(mob), 'After converting to integer')

weight = 57.46
print(weight, type(weight), 'Before converting to integer')
converted_weight = int(weight)
print(converted_weight, type(converted_weight), 'After converting to integer')

#  ---------------------------------------  End of integer data type -----------------------------------------------  #

#  ---------------------------------------  Float data type  -------------------------------------------------  #
#  float() - Is a built-in method which is used to convert the values from int, str and float to float data type
percentage = 72.45
print(percentage, type(percentage))

pi_value = 3.141592653589793
print(pi_value, type(pi_value))

balance = -465.545
print(balance, type(balance))

#  Float has a built method to convert the values from int, str and float to float data type
marks = '98.45'
print(marks, type(marks), 'Before converting to float')

con_marks = float(marks)
print(con_marks, type(con_marks), 'After converting to float')

lucky_number = 57
print(lucky_number, type(lucky_number), 'Before converting to float')
con_lucky_number = float(lucky_number)
print(con_lucky_number, type(lucky_number), 'After converting to float')

#  ---------------------------------------  End of float data type -----------------------------------------------  #

#  ---------------------------------------  Complex data type  -------------------------------------------------  #
#  complex() - Is a built-in method which is used to convert values to complex data type
cmp = 3+4j
print(cmp, type(cmp))

num1 = 67
num2 = 34
cmp_num = complex(num1,num2)
print(cmp_num, type(cmp_num))

#  ---------------------------------------  End of complex data type -----------------------------------------------  #


#  ---------------------------------------  Boolean data type  -------------------------------------------------  #
#  bool() - Is a built-in method which is used to convert the values from str and bool to boolean data type
#  True - 1, False - 0
happy = True
print(happy, type(happy))

sad = False
print(sad, type(sad))

#  Boolean has a built method to convert the values from str and bool to boolean data type
yes = "true"
print(yes, type(yes), 'Before converting to bool')

con_yes = bool(yes)
print(con_yes, type(yes), 'After converting to bool')

add = True + True
print(add, type(add), 'Before converting to bool')

sub = False + True
print(sub, type(sub), 'After converting to bool')

#  ---------------------------------------  End of boolean data type -----------------------------------------------  #
