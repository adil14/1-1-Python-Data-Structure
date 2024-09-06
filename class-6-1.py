pi = 3.14
radius = float(input("Please enter the radius of a sphare : "))
while radius <= 0 :
    radius = float(input("OO please enter radius of sphare : "))
volume = (4/3) * pi * radius * radius * radius 
surface_area = 4 * pi * radius * radius

print("Volume is : ", volume) 
 

print("Surface Area is : ", surface_area)


population = int(input("please enter the population o f the country : ")) 
land_area = int(input("please enter the land area : "))

while population <= 100 and land_area <= 200 :
    population = int(input(" please enter more than 100 population : "))
    land_area = int(input("please enter more than 200 land area : "))
population_density = population / land_area 

print("population density is : ", population_density)


