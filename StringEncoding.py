import sys  
script, input_encoding, errors = sys.argv

def main(language, encoding, errors):
    line = language.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language, encoding, errors)

def print_line(line,encoding, errors):
    next_lang =  line.strip() #remove spaces in line
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes,"<====>", cooked_string)    


language_file = open("language.txt", encoding="utf-8")
main(language_file, input_encoding, errors)    

'''in o/p we have to enter 
python stringencoding.py utf-8 strict
utf-8 (unicode transformation format) is encoding type
strict is error type
errors r 3 types: ???? ji tell me'''