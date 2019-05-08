# ASWWU Web Coding Challenge
This project accepts user input in the form of manual input, or in the form of a file input. The user is prompted for what style of input they would like or if they want to quit the program (for looping purposes) and then the program proceeds based on the option chosen by the user. This program was written for easy integration into other programs.
## What you need
The following is what you need to run the project.
```
Python 3.7.3
```
#### Helpful Links
[Python Downloads](https://www.python.org/downloads/)
## Before compiling the code with Python
```
Unzip the file with the source code
    -For ease of use, place correctly formatted input file in the same file as the source code
        (instructions on formatting input files after instruction on how to run program)
```
## How to run program
```
If using the provided 'bracket_test_main.py' file to run the program, do one of the following:
    -double click the 'bracket_test_main.py' file
    -right click the 'bracket_test_main.py' file, select 'open with' option, and select python
    -Running in shell:
        navigate to directory where file is placed and run the following command:
            python bracket_test_main.py

If using other program here is how to integrate it
    -add the following lines to your program(where most applicable):
    
        from bracket_input class import *
        
        input_method = Input
        
        input_method.user_input()
    BE SURE TO PLACE PYTHON FILES FOR 'bracket_input_class' and 'bracket_test_class' IN THE SAME FILE
```
## Constraints on Input
```
The number of strings to be entered in should not be more than 1000 or less than 1
 
The length of strings entered should not be longer than 1000 characters or less than 1 character
    -strings with an odd length (ex. 5) will not be accepted by the program
     
The only characters accepted will be as follows: [, ], (, ), {, }
 
The program will validate user input and deal with errors accordingly
```
## How to format input file
The input file should follow the form of the first line containing the number of strings to be checked, and the following lines containing the strings to be checked (1 string per line). Incorrectly formatted input files will not have their contents checked.
#### Example input file
```
3
{[()]}
{[(])}
{{[[(())]]}}
```
#### Sample Program output
```
Number of string:  3
String:  {[()]}
String:  {[(])}
String:  {{[[(())]]}}
 
 
YES
NO
YES
```
## Choosing an Option
This program takes three options. The option to enter input manually, use a file for input, or to quit the program. If one of the first two options is chosen the program will loop until the third option is chosen. Depending on the option chosen follow the prompts.
#### Choosing Option 1
```
Would you like to manually input strings, open a file collect input, or exit program?
    Option 1: manual input
    Option 2: file input
    Option 3: exit program
 
Option: 1
Enter number of strings: [example_number_of_strings]
```
##### Sample manual input with output
```
Enter number of strings: 3
String: {[()]}
String: {[(])}
String: {{[[(())]]}}


YES
NO
YES
```

#### Choosing Option 2
```
Would you like to manually input strings, open a file collect input, or exit program?
    Option 1: manual input
    Option 2: file input
    Option 3: exit program
 
Option: 2
What file are you opening for input: test.txt
```
#### Choosing Option 3
```
Would you like to manually input strings, open a file collect input, or exit program?
    Option 1: manual input
    Option 2: file input
    Option 3: exit program
 
Option: 3
```
## Deployment in other programs
This program works with other programs as it does not return any values, but instead displays output. To deploy in another program follow the instructions listed above under 'How to run program.'