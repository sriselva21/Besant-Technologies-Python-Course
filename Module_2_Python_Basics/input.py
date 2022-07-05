#  --------------------- Input/Output Function - To get & display the values received from user. Variables ---------- #

email_id = input("Enter your email id")
print(email_id)

first_name = input("Enter the first name")
last_name = input("Enter the last name")
print("My name is {} {}".format(first_name, last_name))

#  ---------------------------------------  End of Input/Output Section --------------------------------------------  #


#  ------------------------------------  Naming Variables, Swapping Variables -----------------------------------  #
"""
Rules to name a variables
. Variable names should have a combination of letters, integer number (0 to 9) or an underscore (_).
• Create a name that makes sense.
• If variable name is lengthy, use underscore to separate them (first_name).
• Your first letter should not be number, You can use underscore or character.
• Python does not support special symbols like !, @, #, $, %, etc for naming variables except underscore character (_).
• Numbers can used to name a variable, but we can use from second letter/position.
• Variable can have any kind of value or a reference of another variable name.
"""

name = "Python Programing"

_emp = "Python world"

full_name = "Technology"

emp2 = "React Scripting language"

lng3name = "HTML"

# Assigning 3 different variables in a single line
first, second, third = 1000, "Programming", True
print(first, second, third)

# Assigning 3 different variables with same value in a single line, Later you can update individual variables
car = truck = train = "Diesel"
print('car, truck and train runs on {} Note: All variables prints same value'.format(car, truck, train))

car = "Battery"
train = "Electricity"
print('car runs on {}, truck runs on {} and train runs on {} Note: Some variables got updated with '
      'new value'.format(car, truck, train))

# Swapping variables
rupee = 5000
dollar = 76
print("Before swapping variable values -- Rupees is {} and Dollar is {}".format(rupee, dollar))
rupee, dollar = dollar, rupee
print("After swapping variable values -- Rupees is {} and Dollar is {}".format(rupee, dollar))

#  ---------------------------------------  End of Variables Section --------------------------------------------  #
