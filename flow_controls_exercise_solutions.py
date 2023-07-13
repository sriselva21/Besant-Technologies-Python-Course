#  --------------------------- Python Flow Controls exercise problems with solutions  -----------------------------  #


#  1 Write a python program to find those numbers which are divisible by 7 between 1500 and 2700.

num = range(1500, 2701)
for i in num:
    if i % 7 == 0:
        print(i)


#  2 Write a python program that accepts a word or a letter from the user and reverse it.

word = input("Enter the word to see reverse of it: ")
print(word[::-1])


#  3 Write a python program to count the number of even and odd numbers from a series of numbers.

series = range(1, 10)
even = odd = 0
for i in series:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Total even numbers count is {}, odd numbers count is {}".format(even, odd))


#  4 Write a python program that prints each item and its corresponding type from the following list.

lst = [10, "hello", 44.56, [10, "welcome"], (1, 9.5, "time"), {"a", "b", 12, -2.3}, {"name": "Tony", "emp": "Marvel"}]
for item in lst:
    print(item, type(item))


#  5 Write a python program that prints all the numbers from 0 to 6 except 3 and 6.

numb = range(7)
for nb in numb:
    if nb in [3, 6]:
        continue
    print(nb)


#  6 Write a python program that accepts a string and calculate the number of digits and letters in it.

stng = input("Enter the string to check if it contains digit or not: ")
nom = chr = 0
for h in stng:
    if h.isalpha():
        chr += 1
    elif h.isdigit():
        nom += 1
print("Total letters count is {}, numbers count is {}".format(chr, nom))


#  7 Write a python program to check whether an alphabet is a vowel or not.

vowels = ("a", "e", "i", "o", "u")
inp = input("Enter the string to check if it contains vowels or not: ")
for v in inp:
    if v in vowels:
        print("yes {} is a vowel letter".format(v))


#  8 Write a python program to create the multiplication table (from 1 to 10) of a number.

table = int(input("Enter the number to view the tables : "))  # input values always considered as string, so used int
for n in range(1, 11):
    print(f'{table} * {n} = {table*n}')  # here f indicates formatted string, So no need of using format function.

#  9 Write a python program with all if conditions(if, elif, else) and loop (for, while, break and continue statements)

#  if, elif, else
val = 100
if val != 100:
    print("Yes val is not equal to 100")
elif val > 1000:
    print("Yes val is greater than 1000")
elif val == "1000":
    print("Yes val is equal than 1000")
else:
    print("None of the above conditions are correct")

# while loop
while val <= 110:
    print(val)
    val += 2
else:
    print("while loop condition failed and stooped")

# for loop
for lt in [10, "hello", 44.56, [10, "welcome"], (1, 9.5, "time"), {"a", 12, -2.3}, {"name": "Tony", "emp": "Marvel"}]:
    print(lt)
