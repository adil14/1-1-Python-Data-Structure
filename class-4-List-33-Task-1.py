# Generate a list of item containing 10 subjects.
#
# Only print 1 and 2 subject
#
# delete last subject
# Add two more subjects after index[3]

subjects = ["Maths", "Physics", "Chemistry", "Computer Science", "Statistics", "Elecronics", "Mechanics", "Economics", "Accounting", "Business"]
print(subjects)
print(subjects[-10:-8])

subjects.pop()
print(subjects)

# subjects.extend(["HTML"])
# print(subjects)

subjects[4:1] = ["Python", "Java"]
print(subjects)




# a = list(range(10))
# print(a)
# a[4:1] = range(10, 20)
# print(a)



#a = list(str(range(subjects)))
#a[4:1] = range("Biology", "Anatomy")
#print(a)



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)





