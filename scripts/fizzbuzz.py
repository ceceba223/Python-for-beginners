# FizzBuzz is a simple kids game. You count up but everytime the number id a multiple of 3 you instead say fizz.
# And everytime it's a multiple of 5 you say buzz. When both is the case (e.g. 15) you say FizzBuzz.

for i in range(100):
    if i % 3 == 0 and i % 5 ==0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)