#LIST 
'''#ADDING
my_list = [3,4,6,8,"string",2.7,10]
print(my_list)
print(type(my_list)) # all data structures r objects of class o/p:<class 'list'>

my_list.append([32,"xyx"]) #takes values as 1 in list. how many values can b entered
print(my_list)
my_list.extend([23,98])
print(my_list)
my_list.insert(3, "jaraar") #insert data at 3 position remember list start at 0
print(my_list)

#DELECTING
my_list = [3, 4, 6, 8, "string", 2.7, 10]
del my_list[2] #del through index and it just delete
print(my_list)
my_list.pop(2) #del through position and it shows the value that is deleted 
print(my_list)
my_list.remove(4) #remove through name or number
print(my_list)
my_list.clear()
print(my_list)

#Accessing
my_list = [2,43,56,89,9,"abcd"]
print(my_list[4])
print(my_list[1:3])# start from my_list[1]=43 and end at 89 o/p:[43,56] the cursor stop before the end
print(my_list[::-1]) #o/p:[abcd,9,89,56,43,2] gives reverse string
print(my_list[::-2]) #o/p:[abcd, 89,43] takes reverse starting value and skip 1 value
print(my_list[::-3]) #o/p:[abcd,56] skips 2 vlaues
# print(my_list[::-0]) error not taken

print(len(my_list)) # shows length

my_value = [2,4,15,6,7,15,7,15,15,15]
print(my_value.index(15))# show the index
print(my_value.count(15))# show how many times the value exists'''

#SETS
#here we can enter duplicate data but in o/p it doesn't show duplicates. it takes only one value
# doubt: how to delete in sets??? ans:remove and pop. DEL not works in sets
#no append and insert operations in sets ONLY add()
#doubt: how to access sets??

'''my_set = {3,5,7,1,8}
print(type(my_set)) # here set is an obj of class o/p: <class 'set'>

my_set.add(56) #takes only 1 arg. 
print(my_set)
my_set.remove(5)# remove the value through its name
print(my_set)
my_set.pop() #here pop doesn't take any arguments. it delets starting numbers
print(my_set)
my_set.add(23)
my_set.add(53)
print(my_set)
my_set.pop()
print(my_set)

#UNION IN SETS
my_set1 = {7,8,2,5,6}
my_set2 = {5,6,9,1,0}
print(my_set1.union(my_set2), "--------" ,my_set1 | my_set2)

#Intersection
print(my_set1.intersection(my_set2), "-------" , my_set1 & my_set2 )

#Difference
print(my_set1.difference(my_set2), "-------" , my_set1 - my_set2) 
# it del common data and print only my_set1 data
#doubt : but the o/p should be {7,8,2} like this order but the o/p is {8,2,7} why??? changes in data position doesn't make any change in o/p why??

#Symetric_Difference

my_set1 = {23,45,78,96,96,"abc"}
my_set2 = {54,96,"abc", 87,5.9}
print(my_set1.symmetric_difference(my_set2),"-------", my_set1 ^ my_set2)
#del common data and show the remaining 2 sets data
#doubt: but not in order. the o/p is not in order it takes randomly position and display?????
#if we give simple data, o/p is in ascending order

my_set1.clear()
print(my_set1)'''

#TUPLE
#here the values r immutable, we can't change,add,remove the values once they r entered. but we can do this by trick. first change the tuple into list and then made changes and then convert into same tuple name

'''my_tuple = (1,3,5,"rehana","abc",4,6,7,7)
print(my_tuple)

name = ("rehana") 
print(type(name)) # its a string "type"

name = ("rehana",)
print(type(name)) #its a tuple type is obj of class
print(type(my_tuple)) #here tuple is an object of class o/p:<class 'tuple'>

#Access
for x in my_tuple:
    print(x)

print(my_tuple[3])
print(my_tuple[-1])
print(my_tuple[:])# print the complete tuple
print(my_tuple[2:5]) #o/p: {5,"rehana","abc"} start at 2 and end at 5(not included)
print(my_tuple[-4:-1])

#adding tuple
my_tuple1 = my_tuple + (95,8,"xyz")
print(my_tuple1)
my_tuple1 += (3,7,8)
print(my_tuple1)
#my_tuple1[2] = 3  It shows error bcoz we  can't change values in tuple

my_tuple2 = (1,2,3,["abc", "xyz"])
my_tuple2[3][0] = "eng"
print(my_tuple2) #here the data is stored in list form in tuple, so changes possible

print(my_tuple2.count(2))
print(my_tuple2.index(["eng", "xyz"]))# shows index position'''

#Convertion of tuple into list and made changes

'''thistuple = tuple(("abc","xyz","banana","cherry"))
#DOUBT: here in cmd line tuple constructor takes but in terminal it doesn't take y??
print(thistuple)'''

'''#replacing in the tuple 
x = ("abc", "xyz", "ghi")
y = list(x)
y[1] = "kiwi"
x = tuple(y)  # doubt:cmd line takes but terminal say no
print(x)
#trough cmd line we can addd data to tuple'''

'''#adding in the tuple
# 1)
a = ("apple","banana","cherry")
y = list(a)
y.append("orange") 
#in list append([2,4]) but in tuple append(). not in set
a = tuple(y)
print(a)

#2)adding tuple to tuple
tuple1 = ("apple", "banana", "cherry")
x = ("strawberry",)  #its a tuple with 1 item
#creating with 1 or many item,remember to include , after after the item otherwise its not included as tuple
tuple1 += x
print(tuple1)

#Removing items
y = list(tuple1)
y.remove("cherry")
tuple1 = tuple(y)
print(tuple1)

#delete the tuple
del tuple1
print(tuple1)# here shows error bcoz tuple1 is empty now '''


#unpacking,Loop,mutiple the tuple,union  the tuple
'''fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(red)
print(yellow)
#number of varaibles must match the number of vlaues in tuple

fruits1 = ("apple", "banana", "cherry", "rasperry","strawberry")
(green, yellow, *red) = fruits1 #we can assign multiple vlaues to 1 variable with *
print(green)
print(red)

#LOOP through a tuple
fruits1 = ("apple", "banana", "cherry", "rasperry", "strawberry")
for i in fruits1 :
    print(i)

#Loop through index number
for i in range(len(fruits1)):
    print(fruits1[i])

#only union of 2 tuples, no intersction,difference,symmetric_difference
fruits2 = ("mango","guava","apple")
print(type(fruits2))
x = fruits1 + fruits2
print(x)

#multiply same tuple 2 times
z = fruits2 * 2
print(z)'''

#DICTIONARY




