'''def string_name(str1):
    if len(str1) < 2:
        return ' '

    return str1[0:2] + str1[-2:]  
    # here -2 takes last 2 values if str1[:-2] then o/t: w3w3resour w3 if str1[-2:] then o/t: w3ce   w3w3

print(string_name("w3resource"))
print(string_name("w3"))  
print(string_name("w"))'''


'''#replace the character into $ 
def string_count(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char+str1[1:]
    return str1

print(string_count("resource") )'''

'''# swaping starting 2 characters of 2 strings ex:abc xyz output:xyc abz
def swap_method(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b

str1 = input("enter value")  # abc
str2 = input("enter another value")  # xyz
print(swap_method(str1, str2))'''

'''# adding ing to the last 2 digits of string   if ing is already added then add ly in last
def add_string(str1):
    length = len(str1)
    if length > 2 :
        if str1[-3:] == 'ing':
            str1 += "ly"
        else:
            str1 += "ing"
    return str1


print(add_string('abc'))
print(add_string('ab'))'''


'''# find first occurence of substring "not" and "poor" in given string and replace with "good

def snot_poor(str1):
    snot = str1.find("not")
    spoor = str1.find("poor")
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], "good")
        return str1
            
    else:
        
        return str1

abc = input("enter sentence") #input ex:the lyrics r not that poor output is "The lyrics r good"

print(snot_poor(abc))'''


'''#finding longest string in given string

def longest_word(word_list):
    word_len = []
    for n in word_list:
        word_len.append((len(n),n))     
        
    #list[0] ={3, "php"}, list[1] = {9, "excersice"}, list[3]={7 ,"backend"}
    
    word_len.sort()
    
    # sorting in ascending list[0] ={3, "php"}, list[1] = {7, "backend"}, list[3]={9 ,"excersice"}
    
    return word_len[-1][0], word_len[-1][1]     
    
    # so longest word stored in last list so word_len[-1][0] = 9, word_len[-2][0] = 7, word_len[-3][0] = 3

result = longest_word(["PHP","Excersice","Backend"])
print("longest_string", result[1])
print("length of Longest string", result[0])'''


#removing nth character from nonempty string

def remove_character(str, n):
    first_character = str[:n] #doubt
    last_character = str[n+1:]
    return first_character + last_character
abc = input("enter string")
x = input("enter removed character")
print(remove_character(abc, x))
#print(remove_character('python', 3))
#print(remove_character('python', 4))