##############WEEKEND ACTIVITY- THEORETICAL JOURNEY########################################

# 1.What is Pickling and Unpickling in Python? Explain with the help of example.
        ### pickling and unpickling powerful algorithm for serializing and de-serializing a 
        # Python object structure.

dict_obj = {1:"Serdar", 2:"Riyaz",3:"Durbayev", 4:"John"}
import pickle

with open("pickle_dic.pickle","wb") as f:
        pickle.dump(dict_obj,f)

print(dict_obj)
del dict_obj
#print(dict_obj)

with open("pickle_dic.pickle","rb") as f:
        dict_obj=pickle.load(f)

print("Deserialized dictionary:", dict_obj )

# 2.How Memory Management is achieved in Python? Explain with the help of example.

#Fistly, memory management is handling by interprter itself in python. no programmer need do nothing about it.
#in Python two momery type or kind- stack memory and heep memory- stack memory is where all functions run, 
# also where referance veriable names sit and the other hand heap memory is where actuall data stored and keep untill
# their reference count to be zero when it happens periodically garbage collector come place and free the memory 
#from that unused data.

#when programmer create x variable and assign to it interger 10
#in heap memory alocatated place for inerger 10, in stack portion of memory be placed x reference variable name
# that references to number 10, reference counter now is one. if programmer create varriable y and assign to it 
# number 10( a same interger with x) and reference counter become two(2)
# when programmer assigns y and x a number integer 12, so now the data integer 10 reference counter is zero 
#so garbage collerter come and freed 10's memory place and delete 10


# 3.Write a Program In Python to explain Multithreading in Python.


# 4.What are the Collection in Python. Explain following terms with Example.
        #Collections in Python are containers that are used to store collections of data, 
        # for example, list, dict, set, tuple etc. These are built-in collections.
        # Several modules have been developed that provide additional data structures to store collections of data. 
        # One such module is the Python collections module.

#4.1 namedtuple()
        #Python supports a type of container like dictionaries called “namedtuples()” present in module, “collection“. 
        #Like dictionaries they contain keys that are hashed to a particular value. But on contrary,
        #it supports both access from key value and iteration, 
        #the functionality that dictionaries lack.

#4.2 Counter()

#A counter tool is provided to support convenient and rapid tallies. For example:

from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1
print(cnt)



#4.3 OrderedDict

#An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
#import collections 
#from collections import OrederedDict
#An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. 
# The only difference between dict() and OrderedDict() is that:
#OrderedDict preserves the order in which the keys are inserted. 
#A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order.
#By contrast, the order the items are inserted is remembered by OrderedDict.

#4.4 ChainMap

#ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
from collections import ChainMap
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)

#4.5 deque
#The deque is a list optimized for inserting and removing items.
from collections import deque
list = ["a","b","c"]
deq = deque(list)
print(deq)
deq.append("d")
deq.appendleft("e")
print(deq)
c="abcabcacbadscd"
print(deque(c))

# NOTE: Make sure to write at least one program on each and comment what each line of the code is doing.

# 5. 	Learn about PEP8 - How to write beautiful Python Code?
# 6. 	Difference between the pip, virtualenv, conda?

#In short, pip is a general-purpose manager for Python packages; 
# conda is a language-agnostic cross-platform environment manager. 
# For the user, the most salient distinction is probably this: 
# pip installs python packages within any environment; 
# conda installs any package within conda environments


####################WEEKEND ACTIVITY- GITHUB TASK####################################################
# (https://drive.google.com/file/d/1E8MY1ML_SsYDmN_MFwAgbApur_1OqqLQ/view?usp=sharing)
# 1.What is Version Control System and their types of tools available mentioned any top 5?.

#A version control system allows users to keep track of the changes in software development projects, 
#and enable them to collaborate on those projects. 
#Using it, the developers can work together on code and separate their tasks through branches.

#1. GitHub
# GitHub helps software teams to collaborate and maintain the entire history of code changes. 
# You can track changes in code, turn back the clock to undo errors and share your efforts with other team members.

# It is a repository to host Git projects. 
# For those wondering what is Git? It is an open source version control system that features local branching,
# multiple workflows, and convenient staging areas. Git version control is an easy to learn option and offers 
# faster operation speed.

# 2. GitLab
# GitLab comes with a lot of handy features like an integrated project, a project website, etc. 
# Using the continuous integration (CI) capabilities of GitLab, you can automatically test and deliver the code.

# You can access all the aspects of a project, view code, pull requests, and combine the conflict resolution.


# 3. PerForce
# Perforce delivers the version control capabilities through its HelixCore. 
# The HelixCore comes with a single platform for seamless team collaboration, 
# and support for both centralized and distributed development workflows.

# It is a security solution that protects the most valuable assets. 
# HelixCore allows you to track the code changes accurately and facilitates a complete Git ecosystem.

# 4. AWS CodeCommit
# AWS CodeCommit is a managed version control system that hosts secure and scalable private Git repositories. 
# It seamlessly connects with other products from Amazon Web Services (AWS) and hosts the code in secured AWS environments. 
# Hence, it is a good fit for the existing users of AWS.

# AWS integration also provides access to several useful plugins from AWS partners, which helps in software development.

# 5. Bitbucket
# Bitbucket is a part of the Atlassian software suite, so it can be integrated with other Atlassian services 
# including HipChat, Jira, and Bamboo. The main features of Bitbucket are code branches, 
# in-line commenting and discussions, and pull requests.

#It can be deployed on a local server, data center of the company, as well as on the cloud. 
# Bitbucket allows you to connect with up to five users for free. 
# This is good because you can try the platform for free before deciding to purchase.

# 2.What is the difference between Git and GitHub?
        #Git is a version control system that lets you manage and keep track of your source code history. 
        #GitHub is a cloud-based hosting service that lets you manage Git repositories. 
        # If you have open-source projects that use Git, then GitHub is designed to help you better manage them.

# 3.Answer the following question:
# PR is Version Control Systems
# Fork VS Commit
# Init VS Clone
# Branching and Merging


# 4.Create a Git Repositories using CLI and Console make sure to give them a name AssingmentUpload_Through_CLI and 
# AssignmentUpload_Through_Console respectively.cd 

# 5.Make sure to upload all your assignment into both of your repositories again using CLI and Console.
# 	HINT: Use following Commands for CLI
# git Init
# git add
# git commit -m “Message”
# git status
# git push
# git config --global user.name "FIRST_NAME LAST_NAME"
# git config --global user.email "MY_NAME@example.com"
# 6. 	Make sure to create three new branches and follow the instructions given below:
# Main Branch - Master
# First Branch - Dev ---> Copy of Master
# Second Branch - Test ---> Copy of Dev
# First Branch - Prod ---> Copy of Master
# Once you are done creating temp branches see how to delete them but make sure delete them only when the changes have been pushed to the master branch or any main branch.
