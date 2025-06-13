# factorial function

def factorial(a):
    if a < 2:
        return 1
    else:
        return a * factorial(a-1)

a = int(input("Enter a number: "))
p = factorial(a)
print ("Factorial of", a," is", p)
