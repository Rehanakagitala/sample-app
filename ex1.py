'''print('i could love this program')
print("i love this")
#print('i dont run')
print('hens', 25 + 30 / 6)
print("roosters", 100 - 25 * 3 % 4)
print(3 + 2 + 1 -5 +4 % 2 -1 / 4 + 6)
print(3 + 2 < 5 -7)
print("is it greater?" , 5 > -2)
print("is it less or equal", 5 <= -2)'''

#excersice-2

'''cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven
print("There are ", cars, "cars avaliable")
print("we can transport", car_pool_capacity, "people today.")
print("we need to put about", average_passenger_per_car, "in each car")'''

'''my_name = 'rehana'
my_age = 35
my_height = 74
my_weight = 180 #lbs
my_hair = "brown"

print(f"let's talk about {my_name}.")# here two ways give value to statement
print("she is", my_height, "inches tall")
print(f"she is {my_age} old")
print(f"she got {my_hair} hair")
total = my_age + my_height + my_weight
print(total)'''


'''print("mary has a little {}".format("lamb")) 

{ here within statement we add data through format and empty parameters
or we define the value already and then in print (f"statement {declared value} statement")
or after defining value in print("statement",declared name,"statement")  }

print("." * 10) #print 10 times

end1 = "a"
end2 = "r"
end3 = "a"
end4 = "a"
end5 = "r"
print(end1 + end2)
print(end3 + end4 + end5)'''

#excersice-3

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("try your",
"own text here",
"maybe a poem",
"or a song about fear"))
print(""" hello world, how r you.
how to you do??.
missing me.
love me. """)

'''#excersice-4

tabby_cat = "\t i'm tabbed in."
persian_cat = "I'm split\n on a line"
backslash_cat = "I'm \\ a\\ cat."
fat_cat = """ I'll do a list:
\t* cat food
\t* Fishes
\t* Catnip\n\t* Grass """
cat = "hashim\b jaraar\b love\b\b\b\b you" #here \b just move cursor back and remove data check the output is :hashi jaraa you


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(cat)
print("python is hard language \r java ") # here  after \r the data is moved to starting sentence output: java is hard language 
print("python is hard language \r java c++ c#") # here  after \r the data is moved to starting sentence output: java c++ c#rd language '''
