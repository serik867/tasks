#1. Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

def reverse_str(_str):
    return _str[::-1]

print(reverse_str("Serdar Durbayev 1234567"))

# 2. Write a function that accepts a string and calculate the number of upper case 
# letters and lower case letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_lower(_str):
    upper_case=len(list(filter(lambda x:x.isupper(),_str)))
    lower_case=len(list((filter(lambda x:x.islower(),_str))))
    return "upper case: ", upper_case, "Lower case: ", lower_case

print(upper_lower("LasdSDASDASASasdas"))

# 3. Create a function that takes a list and return a new list with unique elements of the first list.
def unique_list(list1):
    return list(set(list1))

print(unique_list([1,1,2,2,3,4,53,53,34,34,12,23,12,23,]))

# 4.Write a program that accepts a hyphen-separated sequence of words as input and 
# prints the words in a hyphen-separated sequence after sorting them alphabetically.

# 5.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT




# 6.Define a function that can receive two integral numbers in string form and 
# compute their sum and print it in console.

# 7.Define a function that can accept two strings as input and print the string
#  with maximum length in console. If two strings have the same length, then the function 
# should print all strings line by line.


# 8.Define a function which can generate and print a tuple where the value are square of
#  numbers between 1 and 20.

# 9.Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# Higher order functions and exception handling-
#  Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions
# Write a function to compute 5/0 and use try/except to catch the exceptions
# Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#  Goal : Turn [1,2,3,4,5,6,7] to 1234567 

#  What is the output of the following codes:
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# 
# k = foo()
# print(k)

# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# 
# a()


         
