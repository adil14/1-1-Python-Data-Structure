# inheritence
class human:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def myfun(self):
        print("Hello my name is : " + self.name)
p1 = human("Ahmed",35)
print(p1)
p1.myfun()


# encapsulation with making objects
class person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    def printname(self):
        print(self.firstname, self.lastname)
x = person("Adil", "Ather")
x.printname()


//class person:
//    def __init__(self, Fname, Lname, age, address):
//        self.firstname = Fname
//        self.lastname = Lname
//        self.age = age
//        self.address = address
//    def printname(self):
//        print(self.firstname, self.lastname, self.age, self.address)
//
//class student(person):
//    pass
//
//y = student("Adil", "Ather", 54, "A")
//y.printname()



class person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, Fname, Lname):
        person.__init__(Fname, Lname)

y = student("Adil", "Ather")
y.printname()

