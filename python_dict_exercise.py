#  --------------------------- Python Dictionary exercise problems with solutions  -----------------------------  #


#  1. Write a Python script to add a key, value to a dictionary.
#  Sample Dictionary : {0: 10}
#  Expected Result : {0: 10, 1: 20, 2: 30}

def update_dict(key, val):
    dct = {0: 10}
    dct.update({1: 20})
    dct[2] = 30
    return dct


#  2. Write a Python script to concatenate the following dictionaries to create a new one.
dct1 = {1: 10, 2: 20}
dct2 = {3: 30, 4: 40}
dct3 = {5: 50, 6: 60}
#  Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def concatenate_dct(dct1, dct2, dct3):
    dct1.update(dct2)
    dct1.update(dct3)
    return dct1


# 3. Write a Python script to check whether a given key already exists in a dictionary.

def check_key(key):
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    if key in dct:
        return "Yes"
    else:
        return "No"


#  4. Write a Python program to iterate over dictionaries using for loops.

def loop_dct():
    dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    for ky, val in dct.items():
        print(ky, val)


#  5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form
#  (x, x*x).
#  Sample Dictionary ( n = 5) :
#  Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def mul_dct(n):
    dct = {}
    for i in range(1, n+1):
        dct.update({i: i*i})
        # dct[i] = i*i
    return dct


#  6. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the
#  values are the square of the keys.
#  Sample Dictionary
#  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

def square_dct():
    dct = {}
    for i in range(1, 16):
        dct.update({i: i*i})
        # dct[i] = i*i
    return dct


#  7. Write a Python script to merge two Python dictionaries.

def merge_dct(dcn1, dcn2):
    dcn1.update(dcn2)
    return dcn1


#  8. Write a Python program to sum all the items in a dictionary.

def sum_val_dct(dct):
    tot = sum(dct.values())
    return tot


#  9. Write a Python program to multiply all the items in a dictionary.

def mul_val_dct(dct):
    tot = 1
    for val in dct.values():
        tot *= val
    return tot


#  10. Write a Python program to remove a key from a dictionary.

def delete_key(dct, key):
    dct.pop(key)
    return dct


#  11. Write a Python program to map two lists into a dictionary.

def map_dct():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000','#008000', '#0000FF']
    color_dictionary = dict(zip(keys, values))
    return color_dictionary


#  12. Write a Python program to get the maximum and minimum values of a dictionary.

def max_min_dct():
    dct = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,}
    return max(dct.values()), min(dct.values())


#  13. Write a Python program to combine two dictionary by adding values for common keys.
#  d1 = {'a': 100, 'b': 200, 'c':300}
#  d2 = {'a': 300, 'b': 200, 'd':400}
#  Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def combine_dct():
    from collections import Counter
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    dct = Counter(d1) + Counter(d2)
    return dct


#  14. Write a Python program to create a dictionary from a string.
#  Note: Track the count of the letters from the string.
#  Sample string : 'data science'
#  Expected output: {'d': 1, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}

def word_count(word):
    dct = {}
    for val in word:
        dct[val] = word.count(val)
    # from collections import Counter
    # dct = Counter(word)
    return dct


#  15. Write a Python program to get the key, value and item in a dictionary.

def get_key_val():
    dct = {'d': 1, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}
    return dct.keys(), dct.values(), dct.items()


#  16. Write a Python program to check if multiple keys exist in a dictionary.

def check_multi_keys(dct):
    if len(dct) >=2:
        return 'Yes there are multiple keys'
    else:
        return 'No there are no multiple keys'


#  17. Write a Python program to create a dictionary from two lists without losing duplicate values.
#  Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
#  Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})

def dct_list(dct1, dct2):
    dct = {}
    for i, j in zip(dct1, dct2):
        dct[i] = {j}
    return dct


#  18. Write a Python program to replace dictionary values with their sums.

def sum_dct_val(dct):
    tot = sum(dct.values())
    return tot


#  19. Write a Python program to match key values in two dictionaries.
#  Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
#  Expected output: key1: 1 is present in both x and y

def dct_match(dct1, dct2):
    for i in dct1:
        if i in dct2 and dct1.get(i,False) == dct2.get(i, False):
            return f'{i}: {dct1[i]} is present in both dct1 and dct2'


#  20. Write a Python program to create a dictionary of keys x, y, and z where each key has as value of list from 11-20,
#  21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
#  {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#  'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#  'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
#  15
#  25
#  35

def list_dict():
    dct1 = {"x": [i for i in range(11, 21)]}
    dct2 = {"y": [i for i in range(21, 31)]}
    dct3 = {"z": [i for i in range(31, 41)]}
    return dct1['x'][4], dct2['y'][4], dct3['z'][4]


#  21. Write a Python program to drop empty items from a given dictionary.
#  Original Dictionary:
#  {'c1': 'Red', 'c2': 'Green', 'c3': None}
#  New Dictionary after dropping empty items:
#  {'c1': 'Red', 'c2': 'Green'}

def drop_empty_dict(dct):
    dct = {k: v for k, v in dct.items() if v}
    return dct


#  22. Write a Python program to filter a dictionary based on values.
#  Original Dictionary:
#  {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
#  Marks greater than 170:
#  {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

def fltr_dict(dct, val):
    dct = {k: v for k, v in dct.items() if v > val}
    return dct


#  23. Write a Python program to convert more than one list to a nested dictionary.
#  Original strings:
#  ['S001', 'S002', 'S003', 'S004']
#  ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
#  [85, 98, 89, 92]
#  Nested dictionary:
#  [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
#  {'S004': {'Saim Richards': 92}}]

def nested_dct():
    lst1 = ['S001', 'S002', 'S003', 'S004']
    lst2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
    lst3 = [85, 98, 89, 92]
    lst = []
    for l1, l2, l3 in zip(lst1, lst2, lst3):
        dct = {l1: {l2: l3}}
        lst.append(dct)
    return lst


#  24. Write a Python program to verify that all values in a dictionary are the same.
#  Original Dictionary:
#  {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
#  Check all are 12 in the dictionary.
#  True
#  Check all are 10 in the dictionary.
#  False

def chekc_dct_val(dct, val):
    cnt = 0
    for k in dct:
        if dct[k] == val:
            cnt += 1
        if cnt == len(dct):
            result = True
        else:
            result = False
    return result


#  25. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
#  Original list:
#  [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#  Grouping a sequence of key-value pairs into a dictionary of lists:
#  {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

def group_lst_dct():
    lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    dct = {}
    for i in lst:
        if i[0] in dct:
            dct[i[0]].append(i[1])
        else:
            dct[i[0]] = [i[1]]
    return dct


#  26. A Python dictionary contains List as a value. Write a Python program to clear the list values in the said
#  dictionary.
#  Original Dictionary:
#  {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
#  Clear the list values in the said dictionary:
#  {'C1': [], 'C2': [], 'C3': []}

def clear_dct_val():
    dct = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
    for i in dct:
        dct[i] = []
    return dct


#  27. Write a Python program to extract a list of values from a given list of dictionaries.
#  Original Dictionary:
#  [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
#  Extract a list of values from said list of dictionaries where subject = Science
#  [92, 94, 88]
#  Original Dictionary:
#  [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
#  Extract a list of values from said list of dictionaries where subject = Math
#  [90, 89, 92]

def extract_dct_val(dct, key):
    dct_val = []
    for i in dct:
        if i.get(key):
            dct_val.append(i.get(key))
    return dct_val


#  28. Write a Python program to find the length of a dictionary of values.
#  Original Dictionary:
#  {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#  Length of dictionary values:
#  {'red': 3, 'green': 5, 'black': 5, 'white': 5}
#  Original Dictionary:
#  {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
#  Length of dictionary values:
#  {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

def len_dct_val(dct):
    dct_val_len = {}
    for k, y in dct.items():
        dct_val_len[y] = len(y)
    return dct_val_len


#  29. Write a Python program to convert a dictionary into a list of lists.
#  Original Dictionary:
#  {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#  Convert the said dictionary into a list of lists:
#  [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
#  Original Dictionary:
#  {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
#  Convert the said dictionary into a list of lists:
#  [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

def dct_lst(dct):
    lst = [list(i) for i in dct.items()]
    return lst


#  30. Write a Python program to filter even numbers from a dictionary of values.
#  Original Dictionary:
#  {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
#  Filter even numbers from said dictionary values:
#  {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
#  Original Dictionary:
#  {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
#  Filter even numbers from said dictionary values:
#  {'V': [], 'VI': [], 'VII': [2]}

def dct_even_odd(dct):
    for k in dct:
        dct[k] = [i for i in dct[k] if i%2 == 0]
    return dct


#  31. Write a Python program to get the total length of all values in a given dictionary with string values.
#  Original dictionary:
#  {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
#  Total length of all values of the said dictionary with string values:
#  20

def total_val_len(dct):
    count = 0
    for d in dct:
        count += len(dct[d])
    return count


#  32. Write a Python program to check if a specific key and a value exist in a dictionary, then return true else false.
#  Original dictionary:
#  {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}

def check_key_val(dct, key, val):
    k = dct.keys()
    v = dct.values()
    if key in k and val in v:
        return True
    else:
        return False


#  33. Write a Python program to combine two or more dictionaries, creating a list of values for each key.
#  Sample Output:
#  Original dictionaries:
#  {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
#  {'x': 300, 'y': 'Red', 'z': 600}
#  Combined dictionaries, creating a list of values for each key:
#  {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}

def combine_dct(dct1, dct2):
    dct = {}
    for k in dct1:
        if k in dct2:
            dct[k] = [dct1[k], dct2[k]]
        else:
            dct[k] = [dct1[k]]
    return dct


#  34.Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
#  Sample Output:
#  Original list of dictionaries:
#  [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}]
#  Convert a list of dictionaries into a list of values corresponding to the specified key:
#  [18, 22, 20]

def convert_dct_val(lst, key):
    val = [i[key] for i in lst if key in i]
    return val


#  35. Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and
#  the elements of the second one serve as values. Each item in the first list must be unique and hashable.
#  Sample Output:
#  Original lists:
#  ['a', 'b', 'c', 'd', 'e', 'f']
#  [1, 2, 3, 4, 5]
#  Combine the values of the said two lists into a dictionary:
#  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def create_dct(lst1, lst2):
    # dct = {key: val for key, val in zip(lst1, lst2)}
    dct = {}
    for key, val in zip(lst1, lst2):
        dct[key] = val
    return dct


#  36. Write a Python program to transform a dictionary into a list of tuples.
#  Sample Output:
#  Original Dictionary:
#  {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
#  Convert the said dictionary to a list of tuples:
#  [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

def dct_lst_tup(dct):
    return dct.items()
if __name__ == "__main__":
    print(dct_lst_tup({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
                      ))
