#Exercise 1
#Create a function called func_a, which prints a message.
#Call the function.
#Assign the function object as a value to the variable b, without calling the function.
#Now call the function using the variable b.

"""def func_a():
    print("message")
def b():
    func_a()
b()"""


#Exercise 2
#Create a function called hypotenuse, which takes two numbers as parameters and prints the square root of the sum of their squares.
#Call this function with two floats.
#Call this function with two integers.
#Call this function with one integer and one float.

"""import math
def hypotenuse(a, b):
    result = math.sqrt(a*a + b*b)
    print(result)

hypotenuse(4.5, 8.2)
hypotenuse(3, 10)
hypotenuse(2.5, 9)"""


#Exercise 3
#Rewrite the hypotenuse function from exercise 2 so that it returns a value instead of printing it. Add exception handling so that the function returns None if it is called with parameters of the wrong type.
#Call the function with two numbers, and print the result.
#Call the function with two strings, and print the result.
#Call the function with a number and a string, and print the result.

"""import math
def hypotenuse(a, b):
    try:
        result = math.sqrt(a*a + b*b)
        return result
    except TypeError:
        return ("Can't be executed.")   

print(hypotenuse(20, 40))
print(hypotenuse("abc", "def"))
print(hypotenuse(20, "def"))"""


#Exercise 4
#Write a recursive function which calculates the factorial of a given number. Use exception handling to raise an appropriate exception if the input parameter is not a positive integer, but allow the user to enter floats as long as they are whole numbers.

"""def factorial(n):
    if n <= 0:
        print (n * factorial(n-1))

factorial(4)"""

"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial(4)"""


#Exercise 4
#Write a function called calculator. It should take the following parameters: two numbers, an arithmetic operation (which can be addition, subtraction, multiplication or division and is addition by default), and an output format (which can be integer or floating point, and is floating point by default). Division should be floating-point division.
#The function should perform the requested operation on the two input numbers, and return a result in the requested format (if the format is integer, the result should be rounded and not just truncated). Raise exceptions as appropriate if any of the parameters passed to the function are invalid.
#Call the function with the following sets of parameters, and check that the answer is what you expect:
#            2, 3.0
#            2, 3.0, output format is integer
#            2, 3.0, operation is division
#            2, 3.0, operation is division, output format is integer

def calculator(a, b, operation="addition", output = float):
    if output == int:
        output = round(output)
    if operation == "subtraction":
        output = a - b
        return output
    if operation == "multiplication":
        return a*b
    if operation == "division":
        return a / b
    else:
        return a + b

calculator(8, 4, "subtraction")

