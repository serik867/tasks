# 1.Write a program to Python find the values which is not divisible 3 
# but is should be a multiple of 7. Make sure to use only higher order function.

_list= [1,2,35,21,49,14,28,29,31,63,42,56,63,70]
res = filter(lambda x: x%3!=0 and x%7==0,_list)
print(list(res))

# 2.Write a program in Python to multiple the element of list by itself using traditional 
# function and pass the function to map to complete the operation.
def multiple(a):
    return a*a

res2=map(multiple,_list)
print(list(res2))

# 3.Write a program to Python find out the character in a string which is uppercase using 
# list comprehension.
str1="Serdar Durbayev Python Learn and so Happy!!!"
res3=[x for x in str1 if x.isupper()]
print(res3)

# 4.Write a program to construct a dictionary from the two lists containing the names 
# of students and their corresponding subjects. The dictionary should maps the students 
# with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. 
# HINT-Use Zip function also
student = ['Smith', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

#zip
res4=dict(zip(student,capital))
print(res4)

#dict comprehension
res41={k:v for k,v in zip(student,capital)}
print(res41)

#for loops
dict1=dict()
for k,v in zip(student,capital):
    dict1[k]=v

print(dict1)
# 5.Learn More about Yield, next and Generators

# 6.Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

# 7.Write any example on decorators.

# 8.Learn about What is FRONT END and its Technologies and Tools

# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mentioned the name of companies using those 5 technologies individually
