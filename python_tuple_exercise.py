#  --------------------------- Python Tuple exercise problems with solutions  -----------------------------  #


#  1. Write a Python program to create an empty tuple.

def create_tuple():
    tp = tuple()
    return tp


#  2. Write a Python program to create a tuple with different data types.

def tuple_val():
    tp = (10, -3, 4.5, "tuple data type", [1, 2, 3], (19, 12), {1, 2, "a"}, {"name": "dell"})
    return tp


#  3. Write a Python program to create a tuple with one item.

def single_tuple():
    tp = 10,
    tup = ("hello",)
    return tp, tup


#  4. Write a Python program to unpack a tuple into several variables.

def unpack_tuple():
    name, email, mobile = "Google", "gmail.com", 98450
    return name, email, mobile


#  5. Write a Python program to add an item to a tuple.

def add_tuple_val():
    tup = 12, 13, -55
    tup = tup + (9, "hello")
    new_tup = tup[:2] + (15, 20, 25) + tup[4:]
    return tup, new_tup


#  6. Write a Python program to convert a tuple to a string.

def tuple_str():
    tup = ("mon", "tue", "wed")
    char = ','.join(tup)
    return char


#  7. Write a Python program to get the last 4th element from given tuple.

def get_tuple_val(tup):
    if len(tup) >=4:
        return tup[-4]
    else:
        return "Total tuple values is less than or not equal to 4"


#  8. Write a Python program to find repeated items in a tuple.

def duplicate_tuple(tup):
    val = [(i,tup.count(i)) for i in tup if tup.count(i) > 1]
    return val


#  9. Write a Python program to check whether an element exists within a tuple.

def find_tuple(tup, val):
    if val in tup:
        return f'Yes value {val} is within tuple'
    else:
        return f'No value {val} is not within tuple'


#  10. Write a Python program to convert a list to a tuple.

def lst_tup(lst):
    tup = tuple(lst)
    return tup


#  11. Write a Python program to remove an item from a tuple.

def remove_tuple():
    tup = (1, 4, '44', 11, 5, 44)
    removed_val = "44"
    tup = tup[:2]+tup[3:]
    return tup


#  12. Write a Python program to slice a tuple.

def tuple_slice():
    tup = (1, 4, '44', 11, 5, 44)
    print(tup[2:])
    print(tup[:5])
    print(tup[2:10])
    print(tup[:])


#  13. Write a Python program to find the index of an item in a tuple.

def find_index():
    tup = (1, 4, '44', 11, 5, 44)
    for i in tup:
        print(i, tup.index(i))


#  14. Write a Python program to find the length of a tuple.

def len_tuple(val):
    return len(val)


#  15. Write a Python program to replace the last value of tuples in a list.
#  Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#  Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

def replace_tup(lst_tup):
    lst_tup = [i[:-1] + (100, ) for i in lst_tup]
    return lst_tup


#  16. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
#  Original Tuple:
#  (4, 3, 2, 2, -1, 18)
#  Product - multiplying all the numbers of the said tuple: -864
#  Original Tuple:
#  (2, 4, 8, 8, 3, 2, 9)
#  Product - multiplying all the numbers of the said tuple: 27648

def cal_tup_pro(tup):
    val = 1
    for i in tup:
        val *= i
    return val


#  17. Write a Python program to check if a specified element appears in a tuple of tuples.
#  Original list:
#  (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
#  Check if White presenet in said tuple of tuples!
#  True
#  Check if White presenet in said tuple of tuples!
#  True
#  Check if Olive presenet in said tuple of tuples!
#  False

def check_val_tuple(tup, val):
    for i in tup:
        if val in i:
            return True
        else:
            return False


#  18. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
#  Original list of tuples:
#  [(1, 2), (2, 3), (3, 4)]
#  Sum of all the elements of each tuple stored inside the said list of tuples:
#  [3, 5, 7]
#  Original list of tuples:
#  [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
#  Sum of all the elements of each tuple stored inside the said list of tuples:
#  [9, -1, 7, 8]

def sum_tuple(tup):
    t = [sum(i) for i in tup]
    return t


#  19. Write a Python program to convert a given list of tuples to a list of lists.
#  Original list of tuples: [(1, 2), (2, 3), (3, 4)]
#  Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
#  Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
#  Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

def list_tuple(tup):
    t = [list(i) for i in tup]
    return t


#  20. Write a Python program to convert a given list of tuples to set.
#  Original list of tuples: [(1, 2), (2, 3), (3, 4)]
#  Convert the said list of tuples to a list of lists: [{1, 2}, {2, 3}, {3, 4}]
#  Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
#  Convert the said list of tuples to a list of lists: [{1, 2}, {2, 3, 5}, {3, 4}, {2, 3, 4, 2}]

def set_tuple(tup):
    t = [set(i) for i in tup]
    return t
