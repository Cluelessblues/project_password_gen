def help():
    print("""available options:

        -n ---numbers: numbers argument to include numbers 0-9 in password string

        -a ---alphalowercase: lower case letters argument to include lower case letters from a-z

        -A ---alphauppercase: uppercase letters argument to include uppercase letters from A-Z

        These argument must be followed by an integar (example: -n 10) = 43097322354 
        to indicate the length of the password.


        These arguments can be used together to increase complexity of your password
        Example: -naA 9
        Generates: 123ABCabc
    
        -w ---words: generates random password using familiar words for a more memorable password 
                     Note: argument must include an integar from 0-9 to indicate the amount of words
                    to be used in generated password.""")
