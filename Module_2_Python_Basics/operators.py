#  ------------------------------------ Python Operators and some examples -----------------------------------------  #
"""  Operators are used to perform operations on variables and values. These are standard symbols used for the purpose
of logical and arithmetic operations.

• OPERATORS: Are the special symbols. Eg- + , * , /, etc.
• OPERAND: It is the value on which the operator is applied.

Python have 7 types of operators:
• Arithmetic operators - Used to perform string/list/tuple concatenation and mathematical operations like addition,
                         subtraction, multiplication, division, floor division, modulus & exponent.
• Assignment operators - Used to assign values to variables. It can be used as increment/decrement operator also.
• Comparison operators - Used to compare values. It returns either True or False according to the condition.
• Logical operators - Used to perform logical conditions like AND, OR and NOT operations. It is used to combine
                      conditional statements.
• Identity/Special operators - is and is not are the identity operators both are used to check if two values are
                                located on the same part of the memory. Two variables that are equal do not imply that
                                they are identical.
• Membership operators - Used to test whether a value/variable is found in a sequence(string, list, tuple, set & dict).
• Bitwise operators - Act on bits and perform the bit-by-bit operations. These are used to operate on binary numbers.
"""


#  -------------------------------------------  Arithmetic operators  ----------------------------------------------  #
"""
+ - Used to perform string/list/tuple concatenation or addition of one or more numbers
• Addition will work for both integers and float values.
string + string will give single string by joining them
string + list/tuple/set/dict/int/float will throw error message
int + int/float will sum up the values
float + float/int will sum up the values
"""

first = "Hello Welcome "
second = "To Python World!"
print(first + second)  # joins both the string and prints single string message
print("1450" + "34343")  # it will join the values, not sum them


num1 = 100
num2 = 200
print(num1+num2)
print(num1+134.5343)
# print(first + num1)  # Integers/Float will not support any other data type for addition

lst = [10, 'abc', 100]
lst2 = ['mon', 'tue', 'wed']
print(lst + lst2)  # It will display as a single list value
# print(lst + num2)  # list will not support with any other data type for concatenation

tup = (10, 'abc', 100)
tup2 = ('mon', 'tue', 'wed')
print(tup + tup2)  # It will display as a single tuple value
# print(tup + num2)  # tuple will not support with any other data type for concatenation

st = {"abc", "hrf"}
st2 = {"hello", 10, 20}
# print(st + st2)  # set will not support + either same or different data type for addition/concatenation

dct = {"abc": 100}
dct2 = {"hello": 10}
# print(dct + dct2)  # dict will not support + either same or different data type for addition/concatenation

