
def use_dict():
    string1= "serdar serdar communitttttyyyy riiiiyyyyaaazzzzz"

    letter=dict()
    string1 = "".join(string1.split())

    for i in string1:
        if i not in letter:
            letter[i]=1
        else:
            letter[i]=letter[i]+1

    print(letter)

use_dict()



   


