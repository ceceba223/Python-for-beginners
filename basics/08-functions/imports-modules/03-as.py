from module import add as alias     #when you import a function with a realz long name you can use the "import * as *" statement to set an alias

x = 8
y = 6

a = 3
b = 6

print(alias(x, y))
print(alias(a, b))