# 1. Print the second item in the Books list
# 2. Change the value from "Maths" to "Computer", in the Books list.
# 3. Use the append method to add "History" to the Books list.
# 4. Use the insert method to add "Geography" as the second item in the Books list
# 5. Use the remove method to remove "Geography" from the Books list.

Books = ["Science", "Maths", "English"]
print(Books[1])

Books[1]= "Computer"
print(Books)

Books.append("History")
print(Books)

Books.insert(1, "Geography")
print(Books)

Books.remove("Geography")
print(Books)

print("hi") 