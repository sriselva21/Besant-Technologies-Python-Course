#  ------------------------------------ Python Flow Controls and some examples --------------------------------------  #
"""  Decision-making is required when we want to execute a code only if certain condition is satisfied. In python, we
use if, elif and else statement for decision-making. loops are used to iterate over a sequence (list, tuple, string)
or other iterable objects. Iterating over a sequence is called traversal. while loop in Python is used to iterate over
a block of code as long as the test expression (condition) is true.

Python have 3 types of if conditions:
• if  - The condition returns true when the 'if-condition' is correct, or it will return false.
• elif (else if) - Is used to check multiple ,conditions at a time for a value
• else - Is used when the 'if or elif conditions' fails.
Indentation means there should be 1-tab or 4 or 8 empty/blank spaces after the colon (:) symbol, Indentation are used
when we write if, elif, else, while, def, for, try, except keywords.
Indentation should be applied after every if, elif, else conditions
"""


#  -------------------------------------------  if condition  ----------------------------------------------  #
"""
Syntax --->  if logic/condition:
Example ---> if "100" == 100:
                print("yes")
"""

num = 100
if num == 100:  # here the if condition checks whether the value of variable "num" is equal to 100
    print("Value of num is 100")  # if the value matches, the print statement will execute, if not it will not print

# There is no any condition written, In this case it will check if the variable is holding a value or not.
if num:  # here the if condition becomes true when num has some value, it becomes false when num is empty value or None
    print(num)  # the variable num having value, So its print that value

info = ""
if info:  # here the info variable has empty value,So the if condition becomes false, and it won't go to print statement
    print(info)  # the variable info having empty value

data = None
if data:  # here the data variable has empty value,So the if condition becomes false, and it won't go to print statement
    print(data)  # the variable data having empty value

#  ---------------------------------------  End of if condition  -----------------------------------------------  #


#  -------------------------------------------  else condition  ----------------------------------------------  #
"""
Syntax --->  else logic/condition:
Example ---> if 100 == 10:
                print("yes its 100")
             else:
                print("No its not 100")
In else part we cannot write any conditions, there can be only one else condition for a if/elif condition
"""

num = 100
if num == 100:  # here the if condition checks whether the value of variable "num" is equal to 100
    print("Value of num is 100")  # if the value matches, the print statement will execute, if not it will go to else
else:
    print("Value of num is not equal to 100")  # if condition becomes false,then this print statement will execute

# There is no any condition written, In this case it will check if the variable is holding a value or not.
if num:  # here the if condition becomes true when num has some value, it becomes false when num is empty value or None
    print(num)  # the variable num having value, So its print that value
else:
    print(num, "is having empty value")  # this print will execute when the if condition becomes false

info = ""
if info:  # here the info variable has empty value,So the if condition becomes false, and it won't go to print statement
    print(info)  # the variable info having empty value
else:
    print("info is having empty value")  # this print will execute when the if condition becomes false

data = None
if data:  # here the data variable has empty value,So the if condition becomes false, and it won't go to print statement
    print(data)  # the variable data having empty value
else:
    print("data value is none")  # this print will execute when the if condition becomes false

#  ---------------------------------------  End of else condition  -----------------------------------------------  #


#  -------------------------------------------  elif condition  ----------------------------------------------  #
"""
Syntax --->  elif logic/condition:
Example ---> if 100 == 10:
                print("yes its 100")
             elif "hello" == "hello":
                print("True ")
elif cannot be your first if condition
you can multiple of elif conditions, But it will stop checking when any one conditions becomes true 
"""

num = 10
if num == 100:  # here the if condition checks whether the value of variable "num" is equal to 100
    print("Value of num is 100")  # if the value matches, the print statement will execute, if not it will go to else
elif num == 10:  # here the if above condition fails then only this condition can be checked
    print("Value of num is 10")  # if the value matches, the print statement will execute, if not it will go to else
else:
    print("Value of num is not equal to 100")  # if condition becomes false,then this print statement will execute


# There is two elif condition written, In this case it will stop at first elif itself.
data = 12345
if data == 100:  # here the if condition checks whether the value of variable "data" is equal to 100
    print("Value of num is 100")  # if the value matches, the print statement will execute, if not it will go to else
elif data == 12345:  # here the if above condition fails then only this condition can be checked
    print("Value of data is 12345")  # if the value matches, the print statement will execute, if not it will go to else
elif type(data) == int:
    print("data is integer value")  # the print statement will not execute until above two if condition becomes false


# There is two elif condition and one else written, In this case it will stop at last else.
data = "hello"
if data == 100:  # here the if condition checks whether the value of variable "data" is equal to 100
    print("Value of num is 100")  # if the value matches, the print statement will execute, if not it will go to else
elif data == 12345:  # here the if above condition fails then only this condition can be checked
    print("Value of data is 12345")  # if the value matches, the print statement will execute, if not it will go to else
elif type(data) == int:
    print("data is integer value")  # the print statement will not execute until above two if condition becomes false
else:
    print(data)  # this print statement will execute when all the if/elif conditions becomes false


#  ---------------------------------------  End of elif condition  -----------------------------------------------  #


#  -------------------------------------------  Nested if condition  ----------------------------------------------  #
num = 10
if num == 10:  # here the if condition checks whether the value of variable "num" is equal to 10
    if type(num) == int:  
        print('yes it 10 and integer type')  # if above 2 condition is true then only print statement can be executed


num = 10
if num == 10:  # here the if condition checks whether the value of variable "num" is equal to 10
    if type(num) == str:  
        print('yes it 10 and integer type')  # if above 2 condition is true then only print statement can be executed
    else:
        print('yes it 10, but not an integer type')  # if 2 condition is false then only print statement can be executed


num = "abc"
if num == 10:  # here the if condition checks whether the value of variable "num" is equal to 10
    if type(num) == int:  
        print('yes it 10 and integer type')  # if above 2 condition is true then only print statement can be executed
    else:
        print('yes it 10, but not an integer type')  # if 2 condition is false then only else statement can be executed
else:
    print("if condition failed")  # Main if condition is false then only this else statement can be executed
    
#  ---------------------------------------  End of Nested if condition  --------------------------------------------  #


"""
Python have 2 types of loop conditions:
• for  - Iterating over a sequence of values like str, list, tuple, set, dict (keys only), Iteration limit is known.
• while  - Keep on iterating until the condition becomes true, Iteration limit is unknown.
for loop cannot be applied for numbers(int, float values), boolean data type. 
"""


#  -------------------------------------------  for condition  ----------------------------------------------  #
"""
Syntax --->  for variable in sequence: logic/condition:
Example ---> for val in "good morning":
                print(val)
"""

msg = "Welcome to python world"

#  I want to print each letters from the variable msg
for val in msg:  # here val is new variable, it can be anything name, but don't give the name which already exists.
    print(val)  # it starts printing each letter continuously and stops when all letters printed from the msg.

lst = ["hello", 1212, "welcome", [1, 2], (19, 12, "good")]
#  I want to print each item from the variable lst
for ll in lst:
    print(ll)


tup = ("morning", "welcome", [1, 2], (19, 12, "good"))
for p in tup:
    print(p)


st = {"a", "b", "c", 1, 2}
for s in st:
    print(s)

dct = {"a": 100, "b": 1000}
for dc in dct:
    print(dc)

#  ---------------------------------------  End of for condition  -----------------------------------------------  #
