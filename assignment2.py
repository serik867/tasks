#1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

x=33

if x%5==0 and x%3==0:
    print("Consultadd Python Training") 
elif x%3==0:
    print("Consultdd")
elif x%5==0:
    print("Python Training")
else:
    pass

#2. Write a program in Python to perform the following operator based task:

_operator = int(input(" Enter 1 for Addition \n Enter 2 for Subtraction \n Enter 3 for Division \n Enter 4 for Multiplacation \n Enter 5 for Average:\n"))
if 0 < _operator < 5:
    print("0<operator<5")
    _first=int(input("Enter first number: "))
    _second=int(input("Enter second number: "))
    if _operator == 1:
        if _first+_second <0:
           print("Oops option 1 is returning the negative number", _first+_second)
        else:
            print(_first+_second)
    elif _operator == 2:
        if _first-_second <0:
           print("Oops option 2 is returning the negative number", _first-_second)
        else:
            print(_first-_second)
    elif _operator == 3:
        if _first/_second <0:
           print("Oops option 3 is returning the negative number", _first/_second)
        else:
            print(_first/_second)
    elif _operator == 4:
        if _first*_second <0:
           print("Oops option 4 is returning the negative number", _first*_second)
        else:
            print(_first*_second)
    else:
        print("Something wrong with 0<opeartor<5 part of if statement" )

       
elif _operator == 5:
    print("operator = 5")
    _first=int(input("Enter first number: "))
    _second=int(input("Enter second number: "))
    _first2=int(input("Enter third number: "))
    _second2=int(input("Enter forth number: "))
    if (_first+_second+_first2+_second2)/4 <0:
           print("Oops option 5 is returning the negative number", (_first+_second+_first2+_second2)/4)
    else:
        print((_first+_second+_first2+_second2)/4)

else:
    print("Enter valid number")

#3.Write a program in Python to implement the given flowchart:


a,b,c = 10,20,30
avg=(a+b+c)/3
print("avg: ", avg)

if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
elif avg>a and avg>b:
    print("avg is higher than a,b")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just bigger than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")
else:
    print("a,b,c less than avg ")


#4.Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”

while True:
    _entered = int(input("Enter either negative or positive number:"))
    #print(_entered)
    if _entered<0:
        break
    elif _entered>0:
        print("Good Going")
        continue

print("It's over")

#5. Write a program in Python which will find all such numbers which are divisible    
# by 7 but are not a multiple of 5, between 2000 and 3200.
_list=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        _list.append(i)
    else:
        continue

print(_list)


#6.What is the output of the following code examples?

def check_output():
    x=123 
    for i in range(100,x,2):
   	    print("First output: ", i)

    i = 0
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
        else:
            print("Second output:","error")

    count = 0
    while True:
        print("Third output",count)
        count += 1
        if count >= 5:
            break

check_output()

#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#  Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for i in range(6):
    if i!=3:
        print(i)
        continue

#8. Write a program that accepts a string as an input from user and 
# calculate the number of digits and letters.

_input = input("Enter Leter and number: ")
_digit_count=0
_letter_count=0

for i in _input:
    if i.isnumeric():
        _digit_count+=1
    elif i.isalpha():
        _letter_count+=1
    else:
        continue

print(" Letter: ", _letter_count, " and Digits:", _digit_count)

