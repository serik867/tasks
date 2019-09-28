#1. Create a list of the 10 elements of four different types 
# of Data Type like int, string, complex and float.

_list = [1,2,"Serdar", "Durbayev", 2+5j,5-2j,23.23,22.34,45.5,10]


#2. CCreate a list of size 5 and execute the slicing structure 

_list_slice=[1,2,3,4,5]
print(_list_slice[1:3])
print(_list_slice[::-1])
print(_list_slice[::2])

#3. Write a program to get the sum and multiply of all the items in a given list.

def sum_multiply(_list,_number):
    for i in range(len(_list)):
        _list[i]=_list[i]*_number+_number
    
    return _list

print("Sum and Multiply by: ",sum_multiply([1,2,3,4,5,6,7,8,9], 3))
        


#4.Find the largest and smallest number from a given list.

def largest_smallest(_list):

    largest=0
    smallest=0
    for i in _list:
        if largest==0 and smallest==0:
            largest=i
            smallest=i
        elif largest<=i:
            largest=i
        elif smallest>=i:
            smallest=i
    
    return largest, smallest

print(largest_smallest([1,23,4,5,75,76,434,2323,656,7,1,4,5,45]))


#5.Create a new list which contains the specified numbers after 
# removing the even numbers from a predefined list. 
def even_list(_list):
    sort_list=[]
    for i in range(len(_list)):
        if _list[i] % 2!=0:
            sort_list.append(_list[i])
    
    return sort_list

print(even_list([1,2,3,4,6,7,8,6,4,3,2,1,10,12,12,24,45,56,67]))



#6.Create a list of first and last 5 elements where the values 
# are square of numbers between 1 and 30 (both included).

import random

_list=[]
for i in range(15):
    _list.append(random.randint(1,30)**2)

print(_list)


#7.	Write a program tp replace the last element in a list with another list.
#Sample data: [1,3,5,7,9,10],[2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]

_list1=[1,2,3,4,5,6,7,8,9,10]
_list2=[11,12,13,14]

_list1.remove(_list1[-1])
_list1.extend(_list2)
print(_list1)

#8.	Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}
a.update(b)
print(a)

#9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Sample data (n=5)
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

dict1={x:x*x for x in range(1,10)  }
print(dict1)

#10. Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number.

x=input("Enter numbers separeted by comma: " )
list1=x.split(",")
tuple1=tuple(list1)
print("list:", list1, "tuple :" ,tuple1 )
