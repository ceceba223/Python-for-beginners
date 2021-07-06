## make a function that adds to integers and returns the sum
## to see that it's working make it print out the sum of x = 8 and y = 6, and the sum of a = 3 and b = 6
#HINT: you can pass multiple arguments to a fuction by separating them with commas: function_name(argument1, argument2)


#first we define our 4 variables
x = 8
y = 6

a = 3
b = 6

def add(int1, int2):        #now we define a function called add that takes 2 arguments the frist and the second number we want to add
    return int1 + int2      #we return the sum of those 2 numbers

print(add(x, y))        #we call the function with 'x' and 'y' as the arguments and print out the results
print(add(a, b))        #we call the function again this time with the bvalues 'a' and 'b'

#btw this all was needless because python has a build in fuction which does exactly this the 'sum()' function