# 0 1 1 2 3 5 8 13 21 34 ...
# 0+1 = 1
# 1+1 = 2
# 1+2 = 3
# ...
# 13+21 = 34

x = 0
y = 1
z = 0

for i in range(10):
    print(x+y)
    z = x+y
    x = y
    y = z