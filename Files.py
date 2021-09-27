'''from sys import argv
script, filename = argv

txt = open(filename)
print(f"here is your file {filename}.")

print(txt.read())

print("type the filename again:")
file_again = input("> ") # here why " >" is used. how it takes filename
txt_again = open(file_again)
print(txt_again.read())'''


from sys import argv

script, filename = argv

print(f" we are going to erase {filename}.")
print("If you don't want that , hit CRTL-c(^c).")
print("if you do want that, hit RETURN.")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file.")
target.truncate()

print("type 3 lines")
line1 = input("line1: ")
line2 = input("line2:")
line3 = input("line3:")

print("im gng to write these to file")

target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")

print("open the file again:")
file_again = input("> ")
txt = open(file_again)
print(txt.read())


print("and finally. close it")

target.close()
