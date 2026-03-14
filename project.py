import secrets
import string
import re,csv,sys

import pyperclip
from tabulate import tabulate
from help import help



numbers = string.digits

lower_letters = string.ascii_lowercase

upper_letter = string.ascii_uppercase

special_characters = string.punctuation

dictionary_list = []

command_dictionary = {"n" : numbers, "a" : lower_letters, "A" : upper_letter, "s" : special_characters}


def main():
    
    try:
        with open("passwords.csv") as file:
            read = csv.reader(file)
    except FileNotFoundError:
        with open("passwords.csv","w") as file:
            fieldnames = ["name","url","username","password"]
            write = csv.DictWriter(file,fieldnames = fieldnames)
            write.writeheader()





    while True:
        try:
            password = validate_parse()
        
        except IndexError:
             sys.exit("Incorrect argument try using -h or -help for more information")



        print(f"\nGenerated Password: {password}\n")
        print(password_strength(password))

        pyperclip.copy(password)
        
        answer = input("Save?\n")
        
        if answer == "yes":
    
            csv_savepassword(password)
            break
        
        elif answer != "no":
            continue


def csv_savepassword(s):
    name = input("Name of website: ")
    url = input("Website Url: ")
    username = input("Username: ")
    
    with open ("passwords.csv","a") as file:
        fieldnames = ['name','url','username','password']
        fileappend = csv.DictWriter(file,fieldnames = fieldnames)
        #fileappend.writeheader()
        
        passwordict ={'name':name, 'url':url, 'username':username, 'password':s}

        fileappend.writerow(passwordict)

def csv_command():
    try:
        with open(sys.argv[2]) as file:
            read = csv.DictReader(file)

    except EOFError:
        sys.exit()


    with open(sys.argv[2]) as file, open("passwords.csv","a") as writefile:
        fieldnames = ['name','url','username','password']
        
        reader = csv.DictReader(file)
        
        writer = csv.DictWriter(writefile,fieldnames = fieldnames)
        
        writer.writeheader()
        
       
        for row in reader:
            dict = {
                'name': row['name'],
                'url': row['url'],
                'username': row['username'],
                'password': row['password']
            }
            writer.writerow(dict)

     
#Function for password strength
def password_strength(s):
    if len(s) > 16:
        return("Password Strength: Strong")

    elif len(s) > 12:
        return("Password Strength: Weak")

    else:
        return("Password Strength: Vulnerable")


def csv_table():
    try:
        if sys.argv[2] == "w":
            with open("passwords.csv","w") as file:
            
                fieldnames = ['name','url','username','password']
                clear = csv.DictWriter(file, fieldnames = fieldnames)    
                clear.writeheader()

    except IndexError:
        table = []
        with open("passwords.csv") as file:
            read = csv.DictReader(file)
            for row in read:
                table.append(row)

        print(tabulate(table,headers="keys",tablefmt="grid"))




def validate_parse():
    #determine sys.argv output
    argument = "".join(sys.argv[1:])


    if match:= re.search("^-[naAs]{1,4}[0-9]{1,3}$",argument):
        while True:
            password = genpass()
            return(password)
    
    #regular expression to look for word argument
    elif match:= re.search(r"^-w(?P<count>[1-9]{1}$)",argument):
        return (random_pass_words(int(match.group("count"))))
    
    #regular expression to looking for help argument
    elif match:= re.search(r"^-h(elp)?$",argument):
        help()
        sys.exit()

    elif match:= re.search(r"^-t(able)?",argument):
        csv_table()
        sys.exit()
    
    elif match:= re.search(r"^-m$",sys.argv[1]):
        csv_command()
        sys.exit()



    else:
        sys.exit("Incorrect argument try using -h or -help for more information")

    
        
#function to generate random words for the password
def random_pass_words(s):
    with open("specialwords.txt") as file:
        
        dictionary_list = []
        
        dictionary_list += list(file)
        
        concatenated_words = ""
        
        for i in range(s):

            generated_str = str(secrets.choice(dictionary_list))

            concatenated_words += "-" + generated_str.strip("\n")
    
    return(concatenated_words.removeprefix("-").lower())


#function to randomize the addition of numbers and letter based on inputed numbers
def genpass():
    working_list = []

    for i in sys.argv[1][1:]:
        working_list += (command_dictionary[i])

    generated_password = ""
    for i in range(int(sys.argv[2])):
        generated_password += str(secrets.choice(working_list))



    return generated_password



if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt,EOFError):
        sys.exit()

