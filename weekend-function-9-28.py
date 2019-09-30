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
def sort_list(_list):
    _list.sort()
    print(_list)

_list=["Albert", "John", "Bernard", "Serdar", "Jessica", "Bruce", "Veronica", "Zebra", "Messi", "Ronaldo", "Kim Kardasyan"]

sort_list(_list)

# 5.Write a program that accepts sequence of lines as input and prints the lines after 
# making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def multi_line():
    print("Enter to UPPERCASE: ")
    _list=[]
    _bool=True

    while _bool:
        line=input(">")
        if line:
            _list.append(line.upper())
        else:
            _bool=False
  
    for i in _list:
        print(i)

multi_line()
   

# 6.Define a function that can receive two integral numbers in string form and 
# compute their sum and print it in console.
def _enter_number():
    _number=input("enter  two number seperated by comma:").split(",")
    res=int(_number[0])+int(_number[1])
    print(res)


_enter_number()


# 7.Define a function that can accept two strings as input and print the string
#  with maximum length in console. If two strings have the same length, then the function 
# should print all strings line by line.


# 8.Define a function which can generate and print a tuple where the value are square of
# numbers between 1 and 20.
def _tuple():
    res=tuple(i*i for i in range(1,20))
    print(res)

_tuple()

# 9.Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
def showNumber(limit):
    for i in range(limit):
        if i%2==0:
            print(i,"-- EVEN" )
        else:
            print(i,"-- ODD")

showNumber(20)

#           Higher order functions and exception handling-

# 1. Write a program which can filter() to make a list whose elements are even number 
# between 1 and 20 ( both included)

res = filter(lambda x:x%2==0,range(1,21))
print(list(res))
# 
# 2. Write a program which can map() and filter() to make a list whose elements 
# are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions
res=filter(lambda y: y%2==0 , list(map(lambda x:x**2, range(1,11))))
print(list(res))
# 
# 3. Write a function to compute 5/0 and use try/except to catch the exceptions
def _compute():
    try:
        5/0
    except:
        print("Undifened")

_compute()

# 4. Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
_list = [[1,2,3],[4,5],[6,7,8]]
new_list=[]
def extend_list(x,y):
    x.extend(y)
    return x
   
import functools
res=functools.reduce(extend_list,_list)
print(res)

# 5. Goal : Turn [1,2,3,4,5,6,7] to 1234567
_final= "".join([str(x) for x in res])
print(_final)


# 6. What is the output of the following codes:
# 6.1 def foo():
#     try:
#         return 1
#     finally:
#         return 2
# 
# k = foo()
# print(k)

##### Answer: finally block will execute no matter what



# 6.2 def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# 
# a()

##### Anwers: NameError: name 'f' is not defined




         
