#The previous example works with one variable.
#If we want to use this with a diffrent variale we would have to duplicate the function to make it work.

message = "H e l l o  W o r l d !"
message2 = "f o o"

def cut_spaces():
    return message.replace(" ", "")

def cut_spaces2():
    return message2.replace(" ", "")

print(cut_spaces())
print(cut_spaces2())

#This is not optimal: we use functions so we dont have to write the same code twice