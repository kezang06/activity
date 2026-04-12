name = input("Enter your name: ")
for i in name:
    print(i)

li = ["Python programming", "Python fundamentals", "Python interview questions"]
for x in li:
    print(x)

lenli = len
for x in range(lenli(li)):
    print(li[x])

tupleli = tuple(li)
for x in range(lenli(tupleli)):
    print(tupleli[x])

setli = set(li)
for x in setli:
    print(x)

tup = ("John Smith", "Jane Doe", "Alice Johnson")
for x in tup:
    print(x)

set1 = {10, 30,20}
for x in set1:
    print(x)

Bookdetails = dict({"Python Programming": "John Smith","Python Fundamentals": "Alice Johnson", "Python Interview "
"Questions": "Jane Doe"})
for keys in Bookdetails:
    print(keys, Bookdetails[keys])

for i in range(4):
    for j in range(i):
        print("*", end="")
    print()

for x in range(6):
    for y in range(x):
        print(y+1, end="")
    print()

for i in range(6,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        for j in range(rows):
            print("*", end=" ")


