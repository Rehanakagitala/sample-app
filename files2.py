'''from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying the {from_file} to {to_file}.")

in_file = open(from_file)
indata = in_file.read() #or in_file = open(from_file).read() is  used but we should not use close() function to in_file bcoz here after reading the file is automatically closed

print(f"The input file is {len(indata)} bytes long")

print(f"does the output file {exists(to_file)}:")
# here the file is already taken then y exists is false in output

print("ready,hit return to continue, CTRL-C to abort.")
input()
# why should we mention empty input wt is neccesity

out_file = open(to_file, 'w')
out_file.write(indata)

#print(f"open the file again{out_file}") # why this code does't run
#file_again = open(out_file)
#print(file_again.read())

print("alright, all done.")

out_file.close()
in_file.close()'''


'''# FUNCTIONS AND VARIABLES

def cheese_and_cake(count, boxes):
    print(f"you have {count} cheese")
    print(f"we have no.of {boxes}.")
    print("party")

print("numbers directly")    
cheese_and_cake(10, 20)

print("or, through varaibles")
value = int(input("enter  only numbers"))
value1 = 50
cheese_and_cake(value,value1)

print("we can do math inside")
cheese_and_cake(30+50, 50-10)

print("we can combine value and variables")
cheese_and_cake(value+20, value1-10)'''


# FUNCTIONS AND FILES


from sys import argv
script, filename = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)

    #f.seek(10) here o/p: First print the whole file:lets print 3 lines 1 ld  2 how r u   3 im gd. all o/p is same but in first line it removes 8 character means it works on bytes not on lines


def print_a_line(line_count, f):
    print(line_count, f.readline())
    end = " "  # removes double /n spaces between lines after reading data
    
current_file = open(filename)
print("First print the whole file:")

print_all(current_file)

print("now lets rewind")

rewind(current_file)

print("lets print 3 lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# i want to add data to file in runtime
print("open the file again")
target = open(filename, 'w')

value1 = input("enter value1:")
value2 = input("enter value2:")
value3 = input("enter value3:")

print("now i write the data to file:")

target.write(value1) 

'''here adding data in runtime  lines by line, but data entered is stored in single line. And also only one previous runtime data is taken not all runtime data?? and also my writen data in input1.txt file is gne???? only at runtime data that entered recently is stored in input.txt'''??

target.write(value2)
target.write(value3)

#print("open the file again:")
#file_again = input("> ")
#txt = open(file_again)
#print(target.read())# why the code is not performed
''' i want to see the data that i added in runtime?'''

target.close()  

