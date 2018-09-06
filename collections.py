
#Exercise 1
#Create a list a which contains the first three odd positive integers and a list b which contains the first three even positive integers.
#Create a new list c which combines the numbers from both lists (order is unimportant).
#Create a new list d which is a sorted copy of c, leaving c unchanged.
#Reverse d in-place.
#Set the fourth element of c to 42.
#Append 10 to the end of d.
#Append 7, 8 and 9 to the end of c.
#Print the first three elements of c.
#Print the last element of d without using its length.
#Print the length of d.

"""a = [1, 3, 5]
b = [2, 4, 6]
c = a + b
c[3] = 42
c.extend([7, 8, 9])
d = list(reversed(sorted(c)))
d.append(10)
print(c[:3])
print(d[-1])
print(len(d))"""


#Exercise 2
#Create a tuple a which contains the first four positive integers and a tuple b which contains the next four positive integers.
#Create a tuple c which combines all the numbers from a and b in any order.
#Create a tuple d which is a sorted copy of c.
#Print the third element of d.
#Print the last three elements of d without using its length.
#Print the length of d.

"""a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
d = tuple(sorted(c))
print(d[2])
print(d[-3:])
print(len(d))"""


#Exercise 3
#Create a set a which contains the first four positive integers and a set b which contains the first four odd positive integers.
#Create a set c which combines all the numbers which are in a or b (or both).
#Create a set d which contains all the numbers in a but not in b.
#Create a set e which contains all the numbers in b but not in a.
#Create a set f which contains all the numbers which are both in a and in b.
#Create a set g which contains all the numbers which are either in a or in b but not in both.
#Print the number of elements in c.

"""a = {1, 2, 3, 4}
b = {1, 3, 5, 7}
c = a | b
d = a - b
e = b - a
f = a & b
g = a ^ b
print(g)"""


#Exercise 4
#Create a range a which starts from 0 and goes on for 20 numbers.
#Create a range b which starts from 3 and ends on 12.
#Create a range c which contains every third integer starting from 2 and ending at 50.

"""a = range(20)
b = range(3, 13)
c = range(2, 51, 3)"""


#Exercise 5
#Create a dict directory which stores telephone numbers (as string values), and populate it with these key-value pairs:
#    Name 	Telephone number
#    Jane Doe 	+27 555 5367
#    John Smith 	+27 555 6254
#    Bob Stone 	+27 555 5689
#Change Jane’s number to +27 555 1024
#Add a new entry for a person called Anna Cooper with the phone number +27 555 3237
#Print Bob’s number.
#Print Bob’s number in such a way that None would be printed if Bob’s name were not in the dictionary.
#Print all the keys. The format is unimportant, as long as they’re all visible.
#Print all the values.

"""directory = {"Jane Doe":"+27 555 5367", "John Smith":"+27 555 6254", "Bob Stone":"+27 555 5689"}
directory["Jane Doe"] = "+27 555 1024"
directory.update({"Anna Cooper":"+27 555 3237"})
print(directory.get("Bob Stone"))
print(directory.keys())
print(directory.values())"""


#Exercise 6
#Convert a list which contains the numbers 1, 1, 2, 3 and 3, and convert it to a tuple a.
#Convert a to a list b. Print its length.
#Convert b to a set c. Print its length.
#Convert c to a list d. Print its length.
#Create a range which starts at 1 and ends at 10. Convert it to a list e.
#Create the directory dict from the previous example. Create a list t which contains all the key-value pairs from the dictionary as tuples.
#Create a list v of all the values in the dictionary.
#Create a list k of all the keys in he dictionary.
#Create a string s which contains the word "antidisestablishmentarianism". Use the sorted function on it. What is the output type? Concatenate the letters in the output to a string s2.
#Split the string "the quick brown fox jumped over the lazy dog" into a list w of individual words.

"""l = [1, 1, 2, 3, 3]
a = tuple(l)
b = list(a)
print(len(b))
c = set(b)
print(len(c))
d = list(c)
print(len(d))
e = list(range(1, 11))
directory = {"Jane Doe":"+27 555 5367", "John Smith":"+27 555 6254", "Bob Stone":"+27 555 5689"}
t = list(directory.items())
v = list(directory.values())
k = list(directory.keys())
s = sorted("antidisestablishmentarianism")
s2 = ("".join(s))
w = list("the quick brown fox jumped over the lazy dog".split(" "))
print(w)"""


#Exercise 7
#Create a list a which contains three tuples. The first tuple should contain a single element, the second two elements and the third three elements.
#Print the second element of the second element of a.
#Create a list b which contains four lists, each of which contains four elements.
#Print the last two elements of the first element of b.

"""a = [(1), (2, 3), (4, 5, 6)]
print(a[1][1])
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(b[0][-2:])"""