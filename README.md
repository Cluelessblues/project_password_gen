## Password Ideas ##

Python script that generate a password based over a command line arguments

Command-line arguments include:

-n for numbers  

-a for lowercase letters

-A for uppercase letters

-S for special characters

These can be arguments can to concatenated to produce a combination of the three:

-naA would produce a password that randomly contains numbers, lowercase-letters and uppercase-letters.

Also the options for randomly generate words as passwords for my readable and memorable passwords.

-w command for words with produce a password contains words of a specific password length:

e.g -w 2 10 would produce two distinct words of the length 10:
    hello-world

If an incorrect Command-line argument is inputted then it would produce a help message:

"Incorrect input trying use -h or -help for more information"

Afterwards the passwords would be graded on their strength based on the length of the password generated.

Provide the user to regenerate a new password or save the password:

Saved passwords can be retrieved with a separated command.


Use ASCII art to customize the presentation of the newly generated password

The generated passwords are then saved to A CSV file that is encrypted by a master password on the initial usage of the program
The password on the CSV file can be change with a change password functions

can pass multiple csvs from either google or firefox and generate a single csv

