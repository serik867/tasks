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

#6.2 FIXED ONE
    i = 0
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
        else:
            print("Second output:","error")


#6.2 HAVE ERRORS:

    """
    i = 0
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
    else:
        print(“error”)

    """

#6.3 FIXED 
    count = 0
    while True:
        print("Third output",count)
        count += 1
        if count >= 5:
            break

#6.3 HAVE ERROR

"""

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break

"""

check_output()
#abive check code, fix errors, however answer for question no:6 is below:---->
# Answers for question: 6.1 :TypeError: 'int' object is not iterable
# 6.2 AS I SEE THERE IS TWO ERROR: 6.2.1   
#   print(“error”)
#               ^
#SyntaxError: invalid character in identifier
#6.2.2 INDENTATION ERRROR: ELSE BLOCK HAVE TO INDENTED
#
#6.3 NameError: name 'Break' is not defined




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

# 9. Read the two parts of the question below: 
# 9.1 Write a program such that it asks users to “guess the lucky number”. 
# If the correct number is guessed the program stops, otherwise it continues forever. 
# 9.2 Modify the program so that it asks users whether they want to guess again each time. 
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question 
# whether they want to continue guessing. The program stops if the user guesses the correct 
# number or answers “no”. ( The program continues as long as a user has not answered “no” and 
# has not guessed the correct number)

import random

def guess_number():
    _number=random.randint(0,20)
    print(_number)

    while True:
        _answer=input("Guess the lucky number-Enter number between 0 to 20:")
        if _answer.isdigit and int(_answer)==_number:
            print(" Congratulation!!! You find the number")
            break
        elif _answer.isdigit and int(_answer)!=_number:
            _answer = input("No rigth! like to play again: Yes/No: ")
            if _answer.capitalize()=="Yes":
                continue
            elif _answer.capitalize()=="No":
                break
            else:
                print("Sorry do not caght it!!")
                continue
        else:
            break

guess_number()       

#10 and 11. Write a program that asks five times to guess the lucky number. 
# Use a while loop and a counter, such as

def five_guess():

    _count = 1
    _number=random.randint(0,20)
    print("random number:", _number)

    while _count <= 5:
        _answer=int(input("Guess the lucky number-Enter number between 0 to 20:"))
        _count+=1
        print("guess count",_count)
        if _answer==_number:
            print("Good Guess")
            break
        elif _answer != _number and _count!=6:
            print("Try again")
        else:
            print("Sorry but that was not very successful. It's over!!!")


print("Here starts five_guess------ ")

five_guess()