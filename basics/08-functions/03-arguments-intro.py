message = "H e l l o  W o r l d !"

def cut_spaces():                       #this function removes all spaces in the string
    return message.replace(" ", "")     #we can manage data within fuctions like this

print(cut_spaces())                     #we  print the string after all spaces have been cut out