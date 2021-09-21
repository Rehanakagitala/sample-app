#find
str1 = "this is a string"
'is' in str1
'me' in str1
str1.find('is')
str1.find('me')
str1.find('is',5)

str2 = "one two three"
str2[0:2]
str2[:4]
str2[6:]

#replace

str3 = "here are a string"
corrected_str3 = str3[:5] + "is" + str3[8:]# here 1 ways to replace the strings
print(corrected_str3)
corrected_str4 = str3.replace("are","is")# 2nd way
print(corrected_str4)


#reverse
str1 = "hello world"
str2 = str1[::-1]
str3 = str1[::-2]
str4 = str1[::-3]
print(str2) #dlrow olleh output
print(str3) #drwolh
print(str4) #dooe ??can't find y by me

#trim
str1 = "Space    world"
str2 = str1.strip() #doubt
print(str2)

#upper, lower
str1 = "hello jaraar"
print(str1.upper())
str2 = "HELLO"
print(str2.lower())

#converting to numbers
hex1 = int ("ae", 16)
hex1
int1 = int ("by", 2)# doubt
int1
float1 = float(input("bt"))#here im enter input method
print(float1)

#iterating over characters of a string
str1 = "0123456789"
i = 0
for i in range(10): #error
print(str1[i], " and ")

#Statistics on text
str1 = 'hello world'
len(str1)
min(str1) # output is ' ' don't know y doubt
max(str1)#here through alphabets range the max value is defined
str1.count('z') # 0 is output
str1.count("w")

#encoding unicode
ustr1 = Unicode("hello")# here unicode is not taken , shown error
ustr2 = u'Hello'
ustr1 == ustr2  1`

ustr1.encode("utf-8")

#translation
str1 = "hello world"
translate_table = str1.maketrans("abcd", "efgh") #hello worlh
translate_table2 = str1.maketrans("ello", "234h")  # h244h whr4d here only replace
str1.translate(translate_table)
str1.translate(translate_table2)
str1.translate(str1.maketrans("abcd", "efgh"))  # here 2 ways to add maketrans
str1.translate(str1.maketrans({'l':None, 'w':None})) #heo ord makes l and w delete
