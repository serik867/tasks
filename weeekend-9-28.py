#1.Create a list of the 10 elements of four different types of
#  Data Type like int, string, complex and float.
combined_list = [23,24,"Serdar", 2+5j, 454.45]
print(combined_list)

#2. 	Create a list of size 5 and execute the slicing structure 
list1=list(range(5)) # I work with python3
print(list1[2:4])
print(list1[:2:-1])
print(list1[:4:2])

#3. 	Create a list of given structure and run 
#  0    1   2   3   4               5                         6  7  8  
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#Access list [1, 2, 3, 4]
print(x[5][:4])

#Access list [600,  700]
print(x[6:8])

#Access list [100, 300, 500, 600, 800]
print(x[::2])

#Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print([x[::-1]])

#Access list [10]
print(x[5][5][0])

#Access list [ ]
del x[:]
print(x)

#4. 	Create a list of thousand number using range and xrange and see the difference between each other.
#### range create list and use memory---> print(range(1000))
#### xrange create xrange object, more meory optimized ---> print(xrange(1000)) --- two of the is for python2 
#### in Python3 range already an object which means it works as a xrange in python2 - memory optimization

#5. How Tuple is beneficial as compare to the list?

"""
- Tuples are stored in a single block of memory. 
 Tuples are immutalbe so, It doesn't require extraspace to store new objects.
- Lists are allocated in two blocks: the fixed one with all the Python object information and
 a variable sized block for the data.
- It is the reason creating a tuple is faster than List.
- It also explains the slight difference in indexing speed is faster than lists,
 because in tuples for indexing it follows fewer pointers.

Advantages using tuples:
-- Tuples is that they use less memory where lists use more memory
-- We can use tuples in a dictionary as a key but it's not possible with lists
-- We can access element with an index in both tuples and lists
Disadvantages of tuples
-- We cannot add an element to tuple but we can add element to list.
-- We can't sort a tuple but in a list we can sort by calling "list.sort()" method.
-- We can't remove an element in tuple but in list we can remove element
-- We can't replace an element in tuple but you can in a list
"""

#6. Write a program in Python to iterate through the list of numbers in the range of 1,100 and
#  print the number which is divisible by 3 and a multiple of 2.
list2= [ x for x in range(1,100) if x%3==0 and x%2==0 ]
print(list2)

#7. Write a program in Python to reverse a string and print only the vowel alphabet if 
# exist in the string with their index.
_str ="Serdar Durbayev python Learning and having fun"
Vowels = "aeuioAEUIO"
reverse_str = _str[::-1]
print(reverse_str)
res = [[x,reverse_str.index(x)] for x in reverse_str if x in Vowels]
print(res)


#8. Write a program in Python to iterate through the string “hello my name is abcde” and 
# print the string which has even length of word.
_str = "hello my name is abcde Serdar Durbayev Python"
_list= _str.split()

res = [x for x in _list if len(x)%2==0]
print(res)

res1= list(filter(lambda x: not len(x) % 2, _list))
print(res1)

#9. Write a program in python to print the pair of numbers whose sum is equal 
# to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]

res=[[x[i],x[j]] for i in range(len(x)) for j in range(len(x)-1) if x[i]+x[j]==8]
print(res)

#10. 	Write a program in Python to complete the following task:
#Create two different list as in even_list and odd_list
even_list = list(range(0,20,2))
print(even_list)

odd_list = list(range(1,20,2))
print(odd_list)
#Ask user to enter the number in the range of 1,50 and make sure if the entered number 
# is even append it to the even_list and if the entered number is odd append it to the odd list.

def add_list():
    _input=int(input("Enter number between 1-50:"))
    if _input%2==0:
        even_list.append(_input)
        print("Add to Even list", even_list)
    else:
        odd_list.append(_input)
        print("Add to odd list", odd_list)

#Keep that in mind you can only add 5 items in each list
i=0
while i<5:
    add_list()
    i+=1

#Make sure once you entered the total 5 element calculate the sum of the list and 
# return the maximum out of the list.
import functools
res_even = functools.reduce(lambda x,y:x+y, even_list)
res_odd = functools.reduce(lambda x,y:x+y, odd_list)
result = lambda x,y: x if (x>y) else y
print("Result ", result(res_even,res_odd))

# 11. Write a program to find out the occurrence of a specific word from an alphanumeric statement.
# Example: 12abcbacbaba34ab  
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
_str1= "12abcabcbacbacbacbadededcbacb2323abcacbacb"
str_dict = dict()
y=1
count=0

for i in _str1:
    count+=1
    if i.isalpha() and i not in str_dict:
        str_dict[i]=y
    elif i.isalpha() and i in str_dict:
        str_dict[i]=str_dict[i]+1

print(str_dict)
    




# 12. Generate and print another tuple whose values are even numbers 
# in the given tuple (1,2,3,4,5,6,7,8,9,10).
tuple1=(1,2,3,4,5,6,7,8,9,10)
res=tuple([ x for x in tuple1 if x%2==0])
print(res)