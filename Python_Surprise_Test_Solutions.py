#  --------------------------- Python Surprise Test Solutions  -----------------------------  #

#  Exercise 1: Reverse a given string.
#  Output: "semaJ"

str1 = input("Enter the string: ")  # "James"
print(str1[::-1])


#  Exercise 2: Change special #  symbol with * in the following string.
#  Output: '*  Jon is @developer & musician**'

str1 = '#  Jon is @developer & musician##'
print(str1.replace("#", "*"))


#  Exercise 3: Write a program to create a new string made of an input string’s first, middle, and last character.
#  Output: "Tpe"

str1 = "Tuple"
print(len(str1))
print(str1[0] + str1[2] + str1[-1])


#  Exercise 4: Sort Descending order of a list in Python.
#  Output: [500, 400, 300, 200, 100]

list1 = [100, 200, 300, 400, 500]
list1.sort(reverse=True)  # reverse keyword is optional, set True for descending order & False for ascending order
print(list1)


#  Exercise 5: Concatenate two lists index-wise.
#  Output: ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
output = []

if len(list1) == len(list2):
    for i in range(len(list1)):
        output.append(list1[i]+list2[i])
print(output)


#  Exercise 6: Write a program in Python to count lower, upper, numeric and special characters in a string.
#  Expected output: Numeric - 2, Lower - 8, Upper - 3, Special - 2

Numeric = Lower = Upper = Special = 0
msg = "@pyThOnlobb!Y34"

for i in msg:
    if i.isupper():
        Upper += 1
    elif i.islower():
        Lower += 1
    elif i.isdigit():
        Numeric += 1
    else:
        Special += 1
print(f'Numeric - {Numeric}, Lower - {Lower}, Upper - {Upper}, Special - {Special}')


#  Exercise 7: Turn every item of a list into its square.
#  Output: [1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]
print([i*i for i in numbers])


#  Exercise 8: Slice list into 3 equal list and reverse them.
#  sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#  list 1 [11, 45, 8]
#  After reversing it [8, 45, 11]
#  list 2 [23, 14, 12]
#  After reversing it [12, 14, 23]
#  list 3 [78, 45, 89]
#  After reversing it [89, 45, 78]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

list1 = sample_list[:3]
print('sample_list', sample_list)
print('Sliced list1', list1)
list1.reverse()
print('Reversed list1', list1, "\n")

list2 = sample_list[3:6]
print('sample_list', sample_list)
print('Sliced list2', list2)
list2.reverse()
print('Reversed list2', list2, "\n")

list3 = sample_list[6:]
print('sample_list', sample_list)
print('Sliced list3', list3)
list3.reverse()
print('Reversed list3', list3, "\n")


#  Exercise 9: Add new item to list after a specified item.
#  Output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(list1[2])
print(list1[2][2])
list1[2][2].append(7000)
print(list1)


#  Exercise 10: Replace list’s item with new value if found.
#  Output: [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    list1[list1.index(20)] = 200
    print(list1)


#  Exercise 11: Add a list of elements to a set.
#  Output: {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)  # use add method for single values & update method for multiple values
print(sample_set)


#  Exercise 12: Access value 20 from the tuple.
#  Output: 20

tuple1 = ("Orange", 20, [10, 30], (5, 15, 25))
print(tuple1[1])


#  Exercise 13: Remove all occurrences of a specific item from a list.
#  Output: [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]

new_list1 = [i for i in list1 if i != 20]  # Creating new list by skipping the value 20
print(new_list1)

# Deleting the value 20, the list1 values gets updated after deletion
for i in list1:
    if i == 20:
        list1.remove(20)
print(list1)


#  Exercise 14: Write a program to sum all the elements of a list.
#  Output: Sum of list items 26

given = [2, 3, 2, 4, 7, 8]
print(sum(given))


#  Exercise 15: Write a program to append data of the second list to the first list.
#  Output: [23, 24, 25, 26, 27, 28, 29, 30]

list1 = [23, 24, 25, 26]
list2 = [27, 28, 29, 30]
list1.extend(list2)
print(list1)


#  Exercise 16: Remove items from set1 that are common to both set1 and set2.
#  Output: {10, 20}
#
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.difference(set2), set1)  # it shows the difference from set1 & still set1 value remains unchanged
print(set1.difference_update(set2), set1)  # it takes the difference from set1 & updates set1 values


#  Exercise 17: Create a tuple with single item 50

tp = (100,)
tpp = "hello",
print(type(tp), type(tpp))


#  Exercise 18: Write a program to print only keys of a dictionary.
#  Output: dict_keys([0, 1, 2])

dct = {0: "Value 1", 1: "Value 2", 2: "Value 3"}
print(dct.keys())


#  Exercise 19: Write a program in Python to display the Factorial of a number.
#  Input : 5
#  Output : Factorial is 120

val = 1
for i in range(1, 6):
    val *= i
print(val)


#  Exercise 20: Return a new set of identical items from two sets.
#  Output: {40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set1.intersection(set2)  # intersection finds the common values between two sets
print(new_set)


#  Exercise 21: Write a program in Python to reverse a word.
#  Input a word to reverse : python
#  Output: nohtyp

print("python"[::-1])


#  Exercise 22: Write a program to print multiplication table of a given number.

for i in range(1, 11):
    print(f'{5} * {i} = {5*i}')


#  Exercise 23: Write a program to separate positive and negative number from a list.
#  Output: Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]

x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
pos = []
neg = []
for i in x:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)
print(pos, neg)


#  Exercise 24: Write a program to modify the first item (22) of a list inside a following tuple to 222.
#  Output: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)  # tuple cannot modify, but list values inside a tuple can be changed
lst = tuple1[1]
print(lst)
tuple1[1][0] = 222
print(tuple1)


#  Exercise 25: Write a program to sum all the values of a dictionary.
#  Output: 500

dict1 = {'key1': 200, 'key2': 300}
print(sum(dict1.values()))  # values or keys method returns list type


#  Exercise 26: Write a program to check whether a given key exists in a dictionary or not.

dict1 = {'key1': 200, 'key2': 300}

if "key1" in dict1:
    print("Yes key present")
else:
    print("key not present")


#  Exercise 27: Write a program to get only unique items from two sets.
#  Output: {70, 40, 10, 50, 20, 60, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))


#  Exercise 28: Write a program to check whether a given value is present then delete those values.
#  Given value = 56

list_val = [10, 40, 56, 5, "hello"]
tuple_val = (10, 40, 56, 5, "hello")
set_val = {10, 40, 56, 5, "hello"}
dct_val = {"a": 10, "b": 40, "c": 56, "d": "hello"}

if 56 in list_val:
    list_val.remove(56)
    print(list_val)

tup = tuple()
for i in tuple_val:
    if i != 56:
        tup += (i, )
print(tup)

if 56 in set_val:
    set_val.remove(56)
    print(set_val)

for k in dct_val.copy():
    if dct_val[k] == 56:
        dct_val.pop(k)
print(dct_val)


#  Exercise 29: Write a program to delete random value from set.

sett = {100, 200, 300}
sett.pop()
print(sett)


#  Exercise 30: Write a program to delete a value from set if the value is present, if not return the message value
#  not present.
#  After deleting 200: {100, 300}
#  After deleting 700: "Value 700 is not present in the set"

sett = {100, 200, 300}
val = int(input("Enter the value to delete: "))
if val in sett:
    sett.remove(val)
    print(sett)
else:
    print(f'Value {val} is not present in the set')


#  Exercise 31: Write a program to delete a key from dictionary, if key is not present then return zero.
#  after deleting key 'black': {'yellow': 1, 'blue': 2, 'orange': 3, 'red': 1}
#  after deleting key 'green': zero

dct = {'yellow': 1, 'blue': 2, 'orange': 3, 'black': 4, 'red': 1}
ky = input("Enter the key to delete: ")
print(dct.pop(ky, 'zero'))  # In pop/get we can set default value, if key not present then it wil consider default value
