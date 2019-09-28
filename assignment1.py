
#1.Create three variables in a single line and assign different 
#values to them and make sure their data types are different.
#Like one is int, another one is float and last one is string.

_int1 = 14
_float1 = 14.5
_string1 = "Assignment1"

int1,float1,string1= 14,14.5,"Assignment1"
print(int1,float1,string1)

#2.Create a variable of value type complex and swap it with another variable whose value is an integer.

_complx = 5+2j
_int2 =7
print(_complx,_int2)

_int2, _complx = int(_complx.real),complex(_int2,_complx.imag)

print(_complx,_int2)

#3.Swap two numbers using third variable as result name and do the same task without using any third variable.

x = 14
y = 41

#First Option
temp = x
x=y
y=temp
#print("x is", x, "y is", y)

#Second Option

k=66
l=77

k,l=l,k
#print("k is", k, "l is", l )

#4.Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

#python2 is commented due to not work on python3
#print eval(raw_input("enter the value: "))

#python3 is commented due to work faster with below code
#print(input("Enter the value: "))


#5.Write a program to complete the task given below:
#5.1 Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable  call z.
_number1= int(input("Enter first number between 1-10: "))
_number2 = int(input("Enter second number between 1-10: "))
z=_number1 + _number2
#print(z)

#5.2 Use z for adding 30 into it and print the final result by using variable result.
print(z+30)

#6.Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is : int/float/string/etc

print(type(input("Enter number: ")))

#7.Create Variable using CamelCase, LadderCase and UPPERCASE.
FirstVar="Hello World"
secondVar="Hello World"
THIRD_VAR="Hello World"

#8.Yes it is Change because "a" reference different place in memory, different data type (also class type)
a=12
print(type(a))
print(id(a))

a="serdar"
print(type(a))
print(id(a))