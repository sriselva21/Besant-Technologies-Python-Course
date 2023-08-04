#  --------------------------- Python Set exercise problems with solutions  -----------------------------  #


#  1. Write a Python program to create a set.

def create_set():
    s = set(["hello", "world", "welcome"])
    return s


#  2. Write a Python program to iterate over sets.

def iterate_sets():
    s = {1, 2, 3, 'foo', 'bar'}
    for i in s:
        print(i, end=' ')


#  3. Write a Python program to add member(s) to a set.

def add_set_val(val):
    s = {1, 2, 3, 'foo', 'bar'}
    s.add(val)
    return s


#  4. Write a Python program to remove item(s) from a given set.

def remove_set(val):
    s = {1, 2, 3, 'foo', 'bar'}
    s.remove(val)
    return s


#  5. Write a Python program to remove an item from a set if it is present in the set.

def delete_set(val):
    s = {1, 2, 3, 'foo', 'bar'}
    if val in s:
        s.remove(val)
        return s
    else:
        return f'{val} not present in set'


#  6. Write a Python program to create an intersection of sets.

def intersection_set():
    set1 = {"hello", "welcome", "bye"}
    set2 = {"bye", "good", "super"}
    return set1.intersection(set2)


#  7. Write a Python program to create a union of sets.

def set_union():
    set1 = {"hello", "welcome", "bye"}
    set2 = {"bye", "good", "super"}
    return set1.union(set2)


#  8. Write a Python program to create set difference.

def set_difference():
    set1 = {"hello", "welcome", "bye"}
    set2 = {"bye", "good", "super"}
    return set1.difference(set2)


#  9. Write a Python program to create a symmetric difference.

def set_symmetric_difference():
    set1 = {"hello", "welcome", "bye"}
    set2 = {"bye", "good", "super"}
    return set1.symmetric_difference(set2)


#  10. Write a Python program to check if a set is a subset of another set.

def set_subset():
    set1 = {"hello", "welcome", "bye"}
    set2 = {"bye", "good", "super"}
    return set1.issubset(set2)


#  11. Write a Python program to create a shallow copy of sets.

def shallow_set():
    set1 = {"hello", "welcome", "bye"}
    new_set1 = set1.copy()
    return new_set1


#  12. Write a Python program to remove all elements from a given set.

def remove_all_set():
    set1 = {"hello", "welcome", "bye"}
    set1.clear()
    return set1


#  13. Write a Python program that uses frozensets.

def frozen_sets():
    fz_set = frozenset({"hello", "welcome", "bye"})
    return fz_set


#  14. Write a Python program to find the maximum and minimum values in a set.

def max_min_set_val():
    val = {1, 2, 33, -1, 400}
    return max(val), min(val)


#  15. Write a Python program to find the length of a set.

def len_set(val):
    return len(val)


#  16. Write a Python program to check if a given value is present in a set or not.

def check_set_val(st, val):
    if val in st:
        return f'Yes {val} present in set {st}'
    else:
        return f'No {val} not present in set {st}'


#  18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.

def check_superset(set1, set2):
    print(set1.issuperset(set1))
    print(set1.issuperset(set2))


#  19. Write a Python program to find elements in a given set that are not in another set.

def check_set(set1, set2):
    return set1.difference(set2)


#  20. Write a Python program to remove the intersection of a second set with a first set.

def set_intersection(set1, set2):
    return set2.intersection(set1)
