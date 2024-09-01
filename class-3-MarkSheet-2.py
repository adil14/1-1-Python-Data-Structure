maths_gain = eval(input("Enter maths gain number = "))
maths_total = eval(input("Maths total number = "))
maths_percentage = maths_gain*maths_total/100
print("MATHS {} {}".format(maths_percentage,"%"))

physics_gain = eval(input("Enter physics gain number = "))
physics_total = eval(input("Physics total number = "))
physics_percentage = physics_gain*physics_total/100
print("PHYSICS {} {}".format(physics_percentage,"%"))

chemistry_gain = eval(input("Enter chemistry gain number = "))
chemistry_total = eval(input("Chemistry total number = "))
chemistry_percentage = chemistry_gain*chemistry_total/100
print("CHEMISTRY {} {}".format(chemistry_percentage,"%"))

biology_gain = eval(input("Enter biology gain number = "))
biology_total = eval(input("Biology total number = "))
biology_percentage = biology_gain*biology_total/100
print("BIOLOGY {} {}".format(biology_percentage,"%"))

english_gain = eval(input("Enter English gain number = "))
english_total = eval(input("English total number = "))
english_percentage = english_gain*english_total/100
print("ENGLISH {} {}".format(english_percentage,"%"))

total_percentage = (maths_gain + physics_gain + chemistry_gain + biology_gain + english_gain)*100/500
print("You Obtain Total : {} {}".format(total_percentage,"%"))


if total_percentage >= 90 and total_percentage <= 100:
    print("You got A+ grade")
elif total_percentage >= 80 and total_percentage <= 90:
    print("You got A grade")
elif total_percentage >= 70 and total_percentage <= 80:
    print("You got B grade")
elif total_percentage >= 60 and total_percentage <= 70:
    print("You got C grade")
else:
    print("You are fail")



# generate an authentication which will access chatbot. Chatbot must be created by you which will ask you your subjects and their marks and calculate your percentage and print a proper marksheet  with using
# ".format"
# "list"
# "dictionary"
# "if and nested if conditions"
# Break the code into functions


# dic = {}
# list = []
#
# a = input("Enter your name : ")
# b = input("Enter your password")
#
# dic.update({"username":a, "password":b})
#
# if dic.get("username")==a and dic.get("password")==b:
#     print("You are allowed to login")
# else:
#     print("Please enter correct user name or password")
#
# c = input("Enter your message : ")
# if c == "hello" or c == "hey" or c == "hi" or c == "salam":
#     print(input("{} : Please enter your subject : ".format(c)))