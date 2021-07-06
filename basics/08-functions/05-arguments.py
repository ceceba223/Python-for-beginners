message = "H e l l o  W o r l d !"
message2 = "f o o"

#               🡳 This is an argument it's a variable that we need to provide whenn we call the function 
def cut_spaces(text):                       
    return text.replace(" ", "")
#           🡱 The argument that we passed to the function can be used as an variable in the function


#befor the brackets after the function name where empty: print(cut_spaces())
#                   🡳 Now we put th argument that we need to provide in these brackets
print(cut_spaces(message))
print(cut_spaces(message2))

#print(cut_spaces("P y t h o n"))
#                       🡱 We can also pass a value directly and not as a variable 

#you can pass multiple arguments to a fuction by separating them with commas: def function_name(argument1, argument2):
#remmber to provide all necessary arguments when calling the function: function_name(argument1, argument2)
#if you don't do this you will see an error of this kind:

#function_name() missing 1 required positional argument: 'argument2'

#or if you privide to many arguments:

#function_name() takes 2 positional arguments but 3 were given
