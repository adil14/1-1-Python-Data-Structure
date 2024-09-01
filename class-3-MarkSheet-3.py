# generate an authentication which will access chatbot. Chatbot must be created by you which will ask
# you your subjects and their marks and calculate your percentage and print a proper marksheet  with using
# ".format"
# "list"
# "dictionary"
# "if and nested if conditions"
# Then try with "While Loop"
# Then try Break the code into functions


dic = {}
list = []

# Authentication Part
a = input("Enter your name : ")
b = input("Enter your password")

dic.update({"username":a, "password":b})

if dic.get("username")==a and dic.get("password")==b:
     print("You are allowed to login")
else:
     print("Please enter correct user name or password")
# End of Authentication Part

# Chat Boot Part
c = input("Enter your message : ")
if c == "hello" or c == "hey" or c == "hi" or c == "salam":
     print(input("{} : Hi Please enter your subject : ".format(c)))
elif c == "Maths" or c == "Physics" or c == "Chemistry" or c == "Biology" or c == "English":
     print(input("{} : Please enter your Maths gain marks : ".format(c)))




# a = input("Enter your message : ")
# if a == "hello" or a == "hey" or a == "hi" or a == "salam":
#    print("{} : yo man".format(a))
# elif a == "who are you" or a == "your name" or a == "what do you do":
#    print("{} : I am NeuraSphare its a software house".format(a))
# elif a == "where are you from" or a == "your city":
#    print("{} : Karach".format(a))
# elif a == "how are you":
#    print("{} : Thank you, how can i help you ?".format(a))
#
# else:
#    print("Please enter correct question")