#  --------------------------- Python List exercise problems with solutions  -----------------------------  #


#  1. Write a Python program to sum all the items in a list.

def sum_list(lst):
    total = sum(lst)  # sum is built-in method, sum is a function which adds the value
    return total


def lst_sum(lst):
    total = 0
    for i in lst:
        total += i  # using + (increment operator) to update the total value by adding the iterating value
    return total


#  2. Write a Python program to multiply with same numbers which present in a list.

def lst_mul(lst):
    mul_lst = [i * i for i in lst]
    return lst, mul_lst


#  3. Write a Python program to get the largest number from a list.

def lst_max(lst):
    return max(lst)  # max is pre-defined function, which finds the highest number from a sequence.


def max_lst(lst):
    highest = lst[0]
    for i in lst:
        if i > highest:
            highest = i
    return highest


#  4. Write a Python program to get the smallest number from a list.

def lst_min(lst):
    return min(lst)  # min is pre-defined function, which finds the lowest number from a sequence.


def min_lst(lst):
    lowest = lst[0]
    for i in lst:
        if i < lowest:
            lowest = i
    return lowest


#  5. Write a Python program to count the number of strings from a given list of strings and return only strings whose
#  length is 2 or more and the first and last characters are the same.
#  Sample List: ['mom', 'dad', 'son', 'daughter', 'malayalam']
#  Excepted Output: ['mom', 'dad', 'malayalam]

def string_count(lst):
    new_lst = []
    for i in lst:
        if len(i) > 1 and i[0] == i[-1]:
            new_lst.append(i)
    return new_lst


#  6. Write a Python program to remove duplicates from a list.
#  Sample List : [2, 55, 1, 22, 4, 4, 2, 3, 2, 1]
#  Expected Result : [1, 2, 3, 4, 22, 55]

def remove_duplicate(lst):
    return list(set(lst))


def duplicate_lst(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return sorted(new_lst)


#  7. Write a Python program to check if a list is empty or not.

def check_lst_empty(lst):
    if lst:
        return f'List is not empty {lst}'
    else:
        return f'List is empty {lst}'


def empty_lst_check(lst):
    if not lst:
        return f'List is empty {lst}'
    else:
        return f'List is not empty {lst}'


#  8. Write a Python program to clone or copy a list.

def clone_lst(lst):
    original = lst
    clone = original.copy()  # copy is a pre-defined list method, it copies the value of the list to new variable
    return original, clone


#  9. Write a Python program to find the list of words that are longer than n from a given list of words.

def words_lst(n, lst):
    new_lst = []
    for i in lst:
        if len(i) > n:
            new_lst.append(i)
    return new_lst


#  10. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_lst(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True


#  11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#  Sample List : ['Red', 'Red', 'White', 'Black', 'Pink', 'Yellow']
#  Expected Output : ['Red', 'White', 'Black']

def rmv_lst_inx(lst):
    inx = (0, 4, 5)
    new_lst = []
    for lst_inx, i in enumerate(lst):  # enumerate returns the index and value of each element from sequences.
        if lst_inx not in inx:
            new_lst.append(i)
    return new_lst


#  12. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def rmv_even(lst):
    new_lst = [i for i in lst if i % 2 != 0]
    return new_lst


#  13. Write a Python program to generate and print a list of the first and last 2 elements where the values are
#  square numbers between 1 and 30 (both included).

def square():
    lst = [i * i for i in range(1, 6)]
    return lst, lst[:2], lst[-2:]


#  14. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers
#  are prime otherwise False.
#  Sample Data:
#  ([0, 3, 4, 7, 9]) -> False
#  ([3, 5, 7, 13]) -> True
#  ([1, 5, 3]) -> False


#  15. Write a Python program to generate all permutations of a list in Python.

def lst_methods():
    lst = [10, 20, 30]
    new_lst = lst.copy()  # copies the lst values to new_lst
    lst.append([30])  # adds 30 to the existing lst list
    lst.count(30)  # finds number 30 how many times repeated
    lst.extend([20, 20, 40])  # adds the values existing lst list without [ ]
    lst.index(10)  # finds the value 10 index location, it will give least/first index value
    lst.insert(1, 1000)  # to insert value at specific index/position 1 - index, hello - value
    lst.pop()  # deletes last item default
    lst.pop(0)  # deletes the position value 0 - index value
    lst.remove(20)  # deletes the value 20, it will delete least/first index value
    lst.reverse()  # reverse the values inside the list
    lst.sort()  # arranges the value in ascending order, it will sort only when list have same data types (numbers/str)
    lst.sort(reverse=True)  # arranges the value in descending order, give False to get in ascending order
    lst.clear()  # deletes all values from the list and will return empty list
    return lst


#  16. Write a Python program to access the index of a list.

def inx_access(lst, inx):
    return inx, lst.index(inx)


#  17. Write a Python program to convert a list of characters into a string.

def str_lst(lst):
    stng = ''.join(lst)
    return stng


#  18. Write a Python program to calculate the difference between the two lists.

def diff_lst(lst1, lst2):
    diff_list1_list2 = list(set(lst1) - set(lst2))
    diff_list2_list1 = list(set(lst2) - set(lst1))
    total_diff = diff_list1_list2 + diff_list2_list1
    return total_diff


#  19. Write a Python program to append a list to the second list.

def appnd_lst(lst):
    wk_end = ["Saturday", "Sunday"]
    wk_end.append(lst)
    return wk_end


#  20. Write a Python program to select an item randomly from a list.

import random


def ran_lst(lst):
    random_item = random.choice(lst)
    return random_item


#  21. Write a Python program to find the second-smallest number in a list.

def small_num(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[0]


#  22. Write a Python program to get unique values from a list.

def unique_lst(lst):
    lst = list(set(lst))
    return lst


#  23. Write a Python program to count the number of elements in a list within a specified range.

def rng_lst(start, end):
    lst = range(start, end)
    return len(lst)


#  24. Write a Python program to check whether a list contains a sublist.

def sub_lst(lst):
    for i in lst:
        if type(i) == list:
            msg = f'Yes there is a sub-list {i}'
        else:
            msg = "No sub-list present"
    return msg


#  25. Write a Python program to find common items in two lists.
#  Sample input: ["Red", "Green", "Orange", "White"], ["Black", "Green", "White", "Pink"]
#  Sample output: ['Green', 'White']

def common_lst(lst1, lst2):
    new_lst = []
    for i in lst1:
        if i in lst2:
            new_lst.append(i)
    return new_lst


#  26. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
#  Sample list : ['p', 'q']
#  n =5
#  Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

def concat_lst(lst, n):
    new_lst = []
    for i in lst:
        for j in range(1,n+1):
            new_lst.append(i+ str(j))
    return new_lst


#  27. Write a Python program to convert a list of multiple integers into a single integer.
#  Sample list: [11, 33, 50]
#  Expected Output: 113350

def cnvrt_lst(lst):
    new_lst = ""
    for i in range(len(lst)):
        new_lst += str(lst[i])
    return int(new_lst)


#  28. Write a Python program to insert an element before each element of a list.
# Sample List:  ['Red', 'Green', 'Black']
# Excepted List:  ['c', 'Red', 'c', 'Green', 'c', 'Black']

def lst_insert(lst, char):
    new_lst = []
    for i in lst:
        new_lst.append(char)
        new_lst.append(i)
    return new_lst


#  29. Write a Python program to convert a list to a list of dictionaries.
#  Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
#  Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
#  {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def color_code(color,code):
    new_lst = []
    for i, j in zip(color, code):
        new_lst.append({"color_name": i, "color_code": j})
    return new_lst


#  30. Write a Python program to compute the difference between two lists.
#  Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
#  Expected Output:
#  Color1-Color2: ['white', 'orange', 'red']
#  Color2-Color1: ['black', 'yellow']

def lst_diff(lst1, lst2):
    lst1_diff = []
    lst2_diff = []
    for i in lst1:
        if i not in lst2:
            lst1_diff.append(i)
    for j in lst2:
        if j not in lst1:
            lst2_diff.append(j)
    return lst1_diff, lst2_diff


#  31. Write a Python program to replace the last element in a list with another list.
#  Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#  Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

def replace_lst(lst1, lst2):
    lst1 = lst1[:len(lst1)-1] + lst2
    return lst1


#  32. Write a Python program to insert a given string at the beginning of all items in a list.
#  Sample list : [1,2,3,4], string : emp
#  Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

def insert_lst(lst, char):
    for inx, val in enumerate(lst):
        lst[inx] = char + str(val)
    return lst


#  33. Write a Python program to iterate over two lists simultaneously.

def iterate_lst(lst1, lst2):
    for l1, l2 in zip(lst1, lst2):
        print(l1, l2)


#  34. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
#  Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
#  Expected Output: [10, 11, 12]

def max_lst(num):
    return max(num, key=sum)


#  35. Write a Python program to extend a list without appending.
#  Sample data: [10, 20, 30]
#  [40, 50, 60]
#  Expected output : [40, 50, 60, 10, 20, 30]

def extend_lst(lst1, lst2):
    lst2.extend(lst1)
    return lst2


#  36. Write a Python program to find items starting with a specific character from a list.
#  Expected Output:
#  Original list:
#  ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
#  Items start with a from the said list:
#  ['abcd', 'abc', 'acjd']
#  Items start with d from the said list:
#  ['dagfa']
#  Items start with w from the said list:
#  []

def find_item(lst, char):
    new_lst = []
    for i in lst:
        if i.startswith(char):
            new_lst.append(i)
    return new_lst


#  37. Write a Python program to split a given list into 2 parts where length of the first part of the list is given.
#  Original list:
#  [1, 1, 2, 3, 4, 4, 5, 1]
#  Length of the first part of the list: 3
#  Splited the said list into two parts:
#  ([1, 1, 2], [3, 4, 4, 5, 1])

def split_lst(lst, length):
    return lst[:length], lst[length:]


#  38. Write a Python program to remove the K'th element from a given list, and print the updated list.
#  Original list:
#  [1, 1, 2, 3, 4, 4, 5, 1]
#  After removing an element at the kth position of the said list:
#  [1, 1, 3, 4, 4, 5, 1]

def remove_lst(lst, index):
    lst.pop(index)
    return lst


#  39. Write a Python program to insert an element at a specified position into a given list.
#  Original list:
#  [1, 1, 2, 3, 4, 4, 5, 1]
#  After inserting an element at kth position in the said list:
#  [1, 1, 12, 2, 3, 4, 4, 5, 1]

def add_lst(lst, index, val):
    lst.insert(index, val)
    return lst


#  40. Write a Python program to extract a given number of randomly selected elements from a given list.
#  Original list:
#  [1, 1, 2, 3, 4, 4, 5, 1]
#  Selected 3 random numbers of the above list:
#  [4, 4, 1]

def random_lst(lst, num):
    import random
    return random.sample(lst, num)


#  41. Write a Python program to round every number in a given list of numbers and print the total sum multiplied by
#  the length of the list.
#  Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
#  Result:
#  243

def round_lst_sum(lst):
    lst = [round(i) for i in lst]
    return sum(lst) * len(lst)


#  42. Write a Python program to round the numbers in a given list,
#  print the minimum and maximum numbers and multiply the numbers by 5.
#  Print the unique numbers in ascending order.
#  Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
#  Minimum value: 4
#  Maximum value: 22
#  Result:
#  20 25 45 55 60 70 80 90 110

def round_num(lst):
    lst = [round(i) for i in lst]
    small_num = min(lst)
    big_num = max(lst)
    result = [i*5 for i in lst]
    result.sort()
    return small_num, big_num, result


#  43. Write a Python program to create a 3X3 grid with numbers.
#  3X3 grid with numbers:
#  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

def multi_dimension():
    lst = [[j for j in range(1,4)] for i in range(3)]
    return lst


#  44. Write a Python program to Zip two given lists of lists.
#  Original lists:
#  [[1, 3], [5, 7], [9, 11]]
#  [[2, 4], [6, 8], [10, 12, 14]]
#  Zipped list:
#  [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]


def zip_lst(lst1, lst2):
    ziplst = []
    for i, j in zip(lst1, lst2):
        ziplst.append(i+j)
    return ziplst


#  45. Write a Python program to count the number of lists in a given list of lists.
#  Original list:
#  [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
#  Number of lists in said list of lists:
#  4
#  Original list:
#  [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
#  Number of lists in said list of lists:
#  3

def count_nested_lst(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count +=1
    return count


#  46. Write a Python program to find a list with maximum and minimum lengths.
#  Original list:                                       #  Original list:
#  [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]         #  [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
#  List with maximum length of lists:                   #  List with maximum length of lists:
#  (3, [13, 15, 17])                                    #  (4, [1, 34, 5, 7])
#  List with minimum length of lists:                   #  List with minimum length of lists:
#  (1, [0])                                             #  (1, [12])

def max_min_lst_len(lst):
    max_lst = 0, []
    min_lst = 1, []
    for i in lst:
        if len(i) >= max_lst[0]:
            max_lst = len(i), i
        if len(i) <= min_lst[0]:
            min_lst = len(i), i
    return min_lst, max_lst


#  47. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
#  Original list:
#  ['Python', 3, 2, 4, 5, 'version']
#  Maximum and Minimum values in the said list:
#  (5, 2)

def max_min_lst(lst):
    max_val = max(i for i in lst if isinstance(i, int))
    min_val = min(i for i in lst if isinstance(i, int))
    return max_val, min_val


#  48. Write a Python program to find the difference between consecutive numbers in a given list.
#  Original list:
#  [1, 1, 3, 4, 4, 5, 6, 7]
#  Difference between consecutive numbers of the said list:
#  [0, 2, 1, 0, 1, 1, 1]
#  Original list:
#  [4, 5, 8, 9, 6, 10]
#  Difference between consecutive numbers of the said list:
#  [1, 3, 1, -3, 4]

def lst_diff(lst):
    result = [b-a for a, b in zip(lst[:-1], lst[1:])]
    return result


#  49. Write a Python program to count integers in a given mixed list.
#  Original list:
#  [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
#  Number of integers in the said mixed list:
#  6

def count_lst_int(lst):
    count =0
    for i in lst:
        if isinstance(i, int):
            count += 1
    return count


#  50. Write a Python program to find the item with the most occurrences in a given list.
#  Original list:
#  [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
#  Item with maximum occurrences of the said list:
#  2

def max_occurrences(nums):
    max_val = 0
    result = nums[0]
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i
    return result


#  51. Write a Python program to access multiple elements at a specified index from a given list.
#  Original list:
#  [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
#  Index list:
#  [0, 3, 5, 7, 10]
#  Items with specified index of the said list:
#  [2, 4, 9, 2, 1]

def specified_index_lst(lst, inx_lst):
    result = [lst[i] for i in inx_lst]
    return result


#  52. Write a Python program to reverse strings in a given list of string values.
#  Original lists:
#  ['Red', 'Green', 'Blue', 'White', 'Black']
#  Reverse strings of the said given list:
#  ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

def reverse_string_lst(lst):
    result = [i[::-1] for i in lst]
    return result


#  53. Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
#  Original list:
#  [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
#  Range: 8 , 10
#  Sum of the specified range:
#  29

def sum_rang_lst(lst, start, end):
    result = sum(lst[start: end+1])
    return result


#  54. Write a Python program to reverse each list in a given list of lists.
#  Original list of lists:
#  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#  Reverse each list in the said list of lists:
#  [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]

def reverse_lst(lst):
    for i in lst:
        i.sort(reverse = True)
    return lst


#  55. Write a Python program to find the first even and odd number in a given list of numbers.
#  Original list:
#  [1, 3, 5, 7, 4, 1, 6, 8]
#  First even and odd number of the said list of numbers:
#  (4, 1)

def find_first_even_odd(lst):
    even = odd = 0
    for i in lst:
        # import ipdb; ipdb.set_trace()
        if i%2 == 0 and even == 0:
            even = i
        elif i%2 != 0 and odd == 0:
            odd = i
    return even, odd


#  56. Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
#  Original list:
#  [19, 'red', 1, 'green', 'blue', 10, 'white', 'green', 12]
#  Sort the said mixed list of integers and strings:
#  [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

def sort_mixed_list(lst):
    num = []
    chars = []
    for i in lst:
        if isinstance(i, str):
            chars.append(i)
        elif isinstance(i, int):
            num.append(i)
    num.sort()
    chars.sort()
    result = num + chars
    return result


#  57. Write a Python program to sort a given list of strings(numbers) numerically.
#  Original list:
#  ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
#  Sort the said list of strings(numbers) numerically:
#  [-500, -12, 0, 4, 7, 12, 45, 100, 200]

def sort_str_list(lst):
    result = [int(i) for i in lst]
    result.sort()
    return result


#  58. Write a Python program to remove a specific item from a given list of lists.
#  Original list of lists:
#  [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)'
#  , 'rgb(255,255,0)', 'rgb(128,128,0)']]
#  Remove 1st list from the given list of lists:
#  [['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb(128,0,0)', 'rgb(255,255,0)',
#  'rgb(128,128,0)']]
#  Remove 2nd list from the given list of lists:
#  [['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
#  Remove 4th list from the given list of lists:
#  [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']]

def remove_nested_list(lst, inx):
    for i in lst:
        i.pop(inx)
    return lst


#  59. Write a Python program to remove empty lists from a given list of lists.
#  Original list:
#  [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
#  After deleting the empty lists from the said lists of lists
#  ['Red', 'Green', [1, 2], 'Blue']

def remove_empty_lst(lst):
    result = [val for val in lst if val]
    return result


#  60. Write a Python program to sum a specific column of a list in a given list of lists.
#  Original list of lists:
#  [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
#  Sum: 1st column of the said list of lists:
#  12
#  Sum: 2nd column of the said list of lists:
#  15
#  Sum: 4th column of the said list of lists:
#  9

def sum_nested_list(lst, inx):
    result = []
    for i in lst:
        result.append(i[inx])
    return sum(result)


#  61. Write a Python program to get the frequency of elements in a given list of lists.
#  Original list of lists:
#  [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
#  Frequency of the elements in the said list of lists:
#  {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

def count_nested_list(lst):
    result = []
    for i in lst:
        result.extend(i)
    from collections import Counter
    return Counter(result)


#  62. Write a Python program to extract every first or specified element from a given two-dimensional list.
#  Original list of lists:
#  [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
#  Extract every first element from the said given two dimensional list:
#  [1, 4, 7]
#  Extract every third element from the said given two dimensional list:
#  [3, 6, 9]

def extract_nested_list(lst, inx):
    result = []
    for i in lst:
        result.append(i[inx])
    return result


#  63. Write a Python program to remove specific words from a given list.
#  Original list:
#  ['red', 'green', 'blue', 'white', 'black', 'orange']
#  Remove words:
#  ['white', 'orange']
#  After removing the specified words from the said list:
#  ['red', 'green', 'blue', 'black']

def remove_words(list1, remove_words):
    for word in list1:
        if word in remove_words:
            list1.remove(word)
            print(word)
    return list1


#  64. Write a Python program to reverse a given list of lists.
#  Original list:
#  [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
#  Reverse said list of lists:
#  [['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
#  Original list:
#  [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
#  Reverse said list of lists:
#  [[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]

def reverse_nested_list(lst):
    lst.reverse()
    return lst


#  65. Write a Python program to find the maximum and minimum values in a given list within a specified index range.
#  Original list:
#  [4, 3, 0, 15, 3, 0, 2, 3, 4, 2, 4, 3, 5]
#  Index range:
#  3 to 8
#  Maximum and minimum values of the said given list within index range:
#  (5, 0)

def find_max_min_inrange(lst, start, end):
    return max(lst[start:end]), min(lst[start:end])


#  66. Write a Python program to check if a given element occurs at least n times in a list.
#  Original list:
#  [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
#  Check if 3 occurs at least 4 times in a list:
#  True
#  Check if 0 occurs at least 5 times in a list:
#  True
#  Check if 8 occurs at least 3 times in a list:
#  False

def count_list(lst, val, cnt):
    if lst.count(val) >= cnt:
        return True
    else:
        return False


#  67. Write a Python program to join two given list of lists of the same length, element wise.
#  Original lists:
#  [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
#  [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
#  Join the said two lists element wise:
#  [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
#  Original lists:
#  [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
#  [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
#  Join the said two lists element wise:
#  [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

def join_two_lst(lst1, lst2):
    new_lst = []
    for val1, val2 in zip(lst1, lst2):
        new_lst.append(val1+val2)
    return new_lst


#  68. Write a Python program to add two given lists of different lengths, starting on the left.
#  Original lists:
#  [2, 4, 7, 0, 5, 8]
#  [3, 3, -1, 7]
#  Add said two lists from left:
#  [5, 7, 6, 7, 5, 8]
#  Original lists:
#  [1, 2, 3, 4, 5, 6]
#  [2, 4, -3]
#  Add said two lists from left:
#  [3, 6, 0, 4, 5, 6]

def sum_two_lst(lst1, lst2):
    new_lst = []
    for val1, val2 in zip(lst1, lst2):
        new_lst.append(val1+val2)
    return new_lst



#  69. Write a Python program to split a given list into specified-sized chunks.
#  Original list:
#  [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
#  Split the said list into equal size 3
#  [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
#  Split the said list into equal size 4
#  [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
#  Split the said list into equal size 5
#  [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]

def split_list(lst, inx):
    result = list((lst[i:i+inx] for i in range(0, len(lst), inx)))
    return result


#  70. Write a Python program to convert a given list of strings into a list of lists.
#  Original list of strings:
#  ['Red', 'Maroon', 'Yellow', 'Olive']
#  Convert the said list of strings into list of lists:
#  [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

def split_list_str(lst):
    result = []
    for i in lst:
        result.append([j for j in i])
    return result


#  71. Write a Python program to convert a given list of strings and characters to a single list of characters.
#  Original list:
#  ['red', 'white', 'a', 'b', 'black', 'f']
#  Convert the said list of strings and characters to a single list of characters:
#  ['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']

def join_list_str(lst):
    result = []
    for i in lst:
        for j in i:
            result.append(j)
    return result


#  72. Write a Python program to insert an element in a given list after every nth position.
#  Original list:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#  Insert a in the said list after 2 nd element:
#  [1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
#  Insert b in the said list after 4 th element:
#  [1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]

def insert_lst(lst, val, inx):
    lst.insert(lst.index(inx) + 1, val)
    return lst


#  73. Write a Python program to merge some list items in a given list using the index value.
#  Original lists:
#  ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#  Merge items from 2 to 4 in the said List:
#  ['a', 'b', 'cd', 'e', 'f', 'g']
#  Merge items from 3 to 7 in the said List:
#  ['a', 'b', 'c', 'defg']

def join_lst(lst, start, end):
    new_lst = lst[:start] + ''.join(lst[start:end]).split() + lst[end:]
    return new_lst


#  74. Write a Python program to add a number to each element in a given list of numbers.
#  Original lists:
#  [3, 8, 9, 4, 5, 0, 5, 0, 3]
#  Add 3 to each element in the said list:
#  [6, 11, 12, 7, 8, 3, 8, 3, 6]
#  Original lists:
#  [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
#  Add 0.51 to each element in the said list:
#  [3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]

def add_num_lst(lst, num):
    result = [i+num for i in lst]
    return result
