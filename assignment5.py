#1. Write a program in Python to allow the error of syntax to go in exception.
#  HINT: use SyntaxError



# 2. Write a program in Python to allow user to open a file by using argv module. 
# If the entered name is incorrect throw an exception and ask them to enter the name again. 
# Make sure to use read only mode. 
from sys import argv

nameOfProgram,fileName = argv

while True:
    try:
        with open(fileName,"r") as f:
            content=f.read()
            print(content)  
        break
    except:
        try_again=input("File name is not correct. Do you want to try again.(Y/N): ")
        if try_again=='Y':
            fileName=input("Enter correct filename:")
        else:
            break


# 3. Write a program to handle an error if the user entered the number more than 
# four digits it should return “Please length is too short/long !!! Please provide only four digits” 

number=input("Please enter four digit number only: ")
while True:
    try:
        
        if len(number)!=4:
            raise ValueError("Please length is too short/long !!! Please provide only four digits:")
        else:
            print(number)
        break
    except ValueError as ve:
        number=input(ve)


# 4. Create a login page backend to ask user to enter the UserEmail and password. 
# Make sure to ask Re-Type Password and if the password is incorrect give chance to enter 
# it again but it should not be more than 3 times.
email=input("Please enter your email: ")
password=input("Please enter pasworrd: ")
count=1
while count<3:
    try:
        if email=="serdar@gmail.com" and password=="12345":
            print("Welcome your home,Boss")
            break
        else:
            count+=1
            raise ValueError("NOT Correct email or password. Please try again")
    except ValueError as ve:
        print(ve)
        email=input("Please enter your email: ")
        password=input("Please enter pasworrd: ")


# 5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand 
# Finally and Raise concept.


# 6. Read any file using Python File handling concept and return only the even length 
# string from the doc.txt file.
# Consider the content as: 

with open("doc.txt", "r") as fh:
    content =fh.read()
    #print(content)
    for word in content.split(" "):
        #print(word)
        if len(word)%2==0:
            print(word)





 