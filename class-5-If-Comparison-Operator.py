
#Example 1
a = 33
b = 200
if b > a:
    print("b is greater than a")

#Example 2
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#Example 3
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


#Example 4
a = 200
b = 33
if b > a:
    print("b is greater than a")


#Example 5 one line statment
if a > b: print("a is greater than b")


#Example 6 one line statment
a = 2
b = 330
print("A") if a > b else print("B")


#Example 7 Using AND
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")