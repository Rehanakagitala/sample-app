'''from sys import argv

script, first, second, third = argv

print("the script is called", script)
print("your first name is avaliable", first)
print("your second name is avaliable", second)
print("your third name is avaliable", third)'''

'''run this program in cmd prompt
here counting start from argv[0]=script(file name),argv[1]=first value. if we give 2 value here is exception
D:\Jaza Juwairiya\python\examples>python ex3.py first
Traceback (most recent call last):
File "ex3.py", line 3, in <module>
script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 2)'''


'''here if we 4 values it doesn't take
D:\Jaza Juwairiya\python\examples>python ex3.py first red 3 5
Traceback (most recent call last):
File "ex3.py", line 3, in <module>
script, first, second, third = argv
ValueError: too many values to unpack (expected 4)'''

from sys import argv

script, user_name, kid_name = argv
prompt = ">"
print(f"hi {user_name} mother of {kid_name}, im the {script} script.")
print(f"do u like my name {user_name}?")
likes = input(prompt)
print(f"do u like my name {kid_name}?")
xyz = input(prompt)
print(f"where do u live {user_name}")
lives = input(prompt)

print(f"""so you said {likes} me, you live in {lives}.nice""")