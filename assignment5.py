#1. Write a program in Python to allow the error of syntax to go in exception.
#  HINT: use SyntaxError
try:
    print "Serdar Durbayev"
except SyntaxError:
    print("I am in except block")


# 2. Write a program in Python to allow user to open a file by using argv module. 
# If the entered name is incorrect throw an exception and ask them to enter the name again. 
# Make sure to use read only mode. 

# 3. Write a program to handle an error if the user entered the number more than 
# four digits it should return “Please length is too short/long !!! Please provide only four digits” 


# 4. Create a login page backend to ask user to enter the UserEmail and password. 
# Make sure to ask Re-Type Password and if the password is incorrect give chance to enter 
# it again but it should not be more than 3 times.

# 5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand 
# Finally and Raise concept.


# 6. Read any file using Python File handling concept and return only the even length 
# string from the doc.txt file.
# Consider the content as: 
# 	Hello I am a file 
# 	Where you need to return the data string 
# 	Which is of even length 
# 	Make sure you return the content in 
# 	The same link as it is present.




# Open function modes in python:
# 
# The argument mode points to a string beginning with one of the following
#  sequences (Additional characters may follow these sequences.):

#  ``r''   Open text file for reading.  The stream is positioned at the
#          beginning of the file.

#  ``r+''  Open for reading and writing.  The stream is positioned at the
#          beginning of the file.

#  ``w''   Truncate file to zero length or create text file for writing.
#          The stream is positioned at the beginning of the file.

#  ``w+''  Open for reading and writing.  The file is created if it does not
#          exist, otherwise it is truncated.  The stream is positioned at
#          the beginning of the file.

#  ``a''   Open for writing.  The file is created if it does not exist.  The
#          stream is positioned at the end of the file.  Subsequent writes
#          to the file will always end up at the then current end of file,
#          irrespective of any intervening fseek(3) or similar.

#  ``a+''  Open for reading and writing.  The file is created if it does not
#          exist.  The stream is positioned at the end of the file.  Subse-
#          quent writes to the file will always end up at the then current
#          end of file, irrespective of any intervening fseek(3) or similar. 