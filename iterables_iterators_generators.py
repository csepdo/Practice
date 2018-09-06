
#Exercise 4
#Create a tuple of month names and a tuple of the number of days in each month (assume that February has 28 days). Using a single for loop, construct a dictionary which has the month names as keys and the corresponding day numbers as values.
#Now do the same thing without using a for loop.

"""months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
days_of_moths = ("31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31")
for i in zip(months, days_of_moths):
    print(i)

year = dict(zip(months, days_of_moths))
print(year)"""


#Exercise 5
#Create a string which contains the first ten positive integers separated by commas and spaces. Remember that you can’t join numbers – you have to convert them to strings first. Print the output string.
#Rewrite the calendar program from exercise 3 using nested comprehensions instead of nested loops. Try to append a string to one of the week lists, to make sure that you haven’t reused the same list instead of creating a separate list for each week.
#Now do something similar to create a calendar which is a list with 52 empty sublists (one for each week in the whole year). Hint: how would you modify the nested for loops?

"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = (", ".join(str(number) for number in numbers))
print(a)

weeks = (WEEK_1, WEEK_2, WEEK_3, WEEK_4)

months = (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST,
SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER)

calendar = [[[] for w in range(4)] for m in range(months)]

calendar[JULY][WEEK_2].append("Go on holiday!")
print(calendar[JULY][WEEK_2])


calendar = [[] for w in range(4) for m in range(12)]"""


#Exercise 6
#Write a program which repeatedly prompts the user for an integer. If the integer is even, print the integer. If the integer is odd, don’t print anything. Exit the program if the user enters the integer 99.
#Some programs ask the user to input a variable number of data entries, and finally to enter a specific character or string (called a sentinel) which signifies that there are no more entries. For example, you could be asked to enter your PIN followed by a hash (#). The hash is the sentinel which indicates that you have finished entering your PIN.
#Write a program which averages positive integers. Your program should prompt the user to enter integers until the user enters a negative integer. The negative integer should be discarded, and you should print the average of all the previously entered integers.
#Implement a simple calculator with a menu. Display the following options to the user, prompt for a selection, and carry out the requested action (e.g. prompt for two numbers and add them). After each operation, return the user to the menu. Exit the program when the user selects 0. If the user enters a number which is not in the menu, ignore the input and redisplay the menu. You can assume that the user will enter a valid integer:
#   -- Calculator Menu --
#    0. Quit
#    1. Add two numbers
#    2. Subtract two numbers
#    3. Multiply two numbers
#    4. Divide two numbers

"""while True:
    number = int(input("Please enter an integer: "))
    if number % 2 == 0:
        print(number)
    elif number == 99:
        break"""

"""numbers = []
while True:
    number = int(input("Please enter numbers: "))
    if number < 0:
        break
    numbers.append(number)
average = str(sum(numbers)/len(numbers))
print("Average: " + average)"""

"""menu = "   -- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers"

selection = None

while selection != 0:
    print(menu)
    selection = int(input("Select an option: "))

    if selection not in range(5):
        print("Invalid option: %d" % selection)
        continue

    if selection == 0:
        continue

    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number: "))

    if selection == 1:
        result = a + b
    elif selection == 2:
        result = a - b
    elif selection == 3:
        result = a * b
    elif selection == 4:
        result = a / b

    print("The result is: " + str(result) + "\n")"""


#Exercise 7
#Modify the example above to include type conversion of the properties: age should be an integer, height and weight should be floats, and name and surname should be strings.

"""person = {}
properties = [("name", str), ("surname", str), ("age", int), ("height", float), ("weight", float)]

for prop, p_type in properties:
    person[prop] = p_type(input("Please enter your %s: " % prop))
print(properties)"""