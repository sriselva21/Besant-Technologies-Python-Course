#  ---------------------Print Function - To display the message/values passed into the print function---------------  #
print("Hello World!")  # It prints single value

print("python", 12, -3, 45.6)  # It prints multiple different values in a single line

# Print function using format function
print("Collection of fruits name {} ".format(['apple', 'grapes', 'orange']))

print("First value {} Second Value {}".format(100, 200))  # Values are passed based on  default position into strings

print("Second value {1} First Value {0}".format(100, 200))  # Values are passed based on position numbers into strings

# Values are passed based on key names into strings
print("Second value {secn} First Value {firs}".format(firs=100, secn=200))

#  ---------------------------------------  End of Print Function -------------------------------------------------  #


#  ---------------------------------------  Comments Section -------------------------------------------------  #

# hash comments
#  print(" this is a comment statement") This entire line will skip while execution of the file.

print("this is line will execute till half of line")  # This line will execute till print function only

# Line number 26 to 28 & 30 will be skipped for execution
#  print(1000)
#  print(50,50,343)

# Doc String - Documentation String/ Multiple Line comments
'''
Using print() we can write our first program (“Hello World!”). Print function displays the specified message to the 
screen, or other standard output device.
Example: print(“Hello World!”)

'''

#  ---------------------------------------  End of Comments Section ------------------------------------------------  #
