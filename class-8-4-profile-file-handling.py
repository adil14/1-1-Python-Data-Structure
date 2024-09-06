f = open("class-8-3-profile.txt", "r") 
print(f.read())

f = open("class-8-3-profile.txt", "r")
print(f.readline())



f = open("class-8-3-profile.txt", "r") 
print(f.readline(4))
    

f = open("class-8-3-profile.txt", "r")
for x in f:
    print(x)

f = open("class-8-1-demofile.txt", "a")
f.write("Now the file has more content !!")
f.close()

f = open("class-8-1-demofile.txt", "r")
print(f.read())

f = open("class-8-1-demofile.txt", "w")
f.write("Woops !!! I have deleted the content")
f.close()

f = open("class-8-1-demofile.txt", "r")
print(f.read())

import os 
os.remove("class-8-1-demofile.txt")




