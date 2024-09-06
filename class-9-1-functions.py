def my_function():
    print("hello from a function")
my_function()

def my_function_second(fname):
    print(fname + "Reference : ")
my_function_second("Email")
my_function_second("Tobias")
my_function_second("Linus")

def my_function_third(fname, lname):
    print(fname + " " + lname)
my_function_third("Adil", "Ather")

def my_function_fourth(*kids):
    print("The youngest child is : " + kids[2])
my_function_fourth("Email", "Tobias", "Linus")


# Arbitratri function
def my_function_fifth(*pakistaniname):
    print("My name is :" + pakistaniname[0])
    print("My name is :" + pakistaniname[1])
    print("My name is :" + pakistaniname[2])
    print("My name is :" + pakistaniname[3])
    print("My name is :" + pakistaniname[4])
my_function_fifth("Adil", "Ather", "Imran", "Khan", "Jon")


def my_function_sixth(*pakistaniname):
    for i in range(5):
        print(pakistaniname[i])

my_function_sixth("Adil", "Ather", "Imran", "Khan", "Jon")


def my_function_seventh(child3, child2, child1):
    print("The youngest child is : " + child3)
my_function_seventh(child1= "Adil", child2= "Ather", child3= "Imran")

def my_function_eighth(**kid):
    print("His last name is : " + kid["lname"])
my_function_eighth(fname = "Adil", lname = "Ather")


def my_function_ninth(country = "Norway"):
    print("I am from : " + country)

my_function_ninth("Sweden")
my_function_ninth("Japan")
my_function_ninth()
my_function_ninth("India")



def my_function_tenth(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "Cherry"]
my_function_tenth(fruits)

def my_function_eleventh(x):
    return 5 * x

print(my_function_eleventh(3))
print(my_function_eleventh(5))
print(my_function_eleventh(9))

