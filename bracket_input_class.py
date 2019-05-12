from bracket_test_class import *

class Input():
    
    #open and read from file
    #NOTE TO SELF WHEN ADDING TO THIS FUNCTION: strip white space off line or the size will be off
    def read_input_file():
        #define class variable
        test = Tests
        #define variables to assign values to
        number_of_strings = 0
        list_of_brackets = []
        
        #collect filename
        file_name = input("What file are you opening for input: ")

        #open file
        with open(file_name, "r") as file:
            #define variable to help with reading
            first_line = True

            #read each line of the file and assign values accordingly
            for line in file:
                #read first line
                if first_line:
                    first_line = False
                    number_of_strings = int(line)
                    print("Number of string: ", number_of_strings)
                        
                    #check preset paramaters
                    if test.test_size(number_of_strings):
                        print("Number of strings is too large")
                        return
                    
                #every other line after the first    
                else:
                    #check preset paramaters checking
                    if test.test_size(len(line.rstrip())) or test.odd_even_test(len(line.rstrip())):
                        print("Invalid string size.")
                        #print(len(line.rstrip()))
                    else:
                        print("String: ", line.rstrip())
                        #strip white space to avoid null character being detected an error is detected when testing the string
                        list_of_brackets.append(line.rstrip())
        print('\n')                
        #test bracket list if condition is met
        if number_of_strings == len(list_of_brackets):
            for line in list_of_brackets:
                test.balance_test(line)
        else:
            print("\nSize and number of strings does not match")
            print("This can happen if the string you entered has an odd length, too short or too long, or there was an incorrect character.")
            print("Please check contents of file and try again.")

    #collect manual input
    def manual_input():
        #delcare class variables to call other class functions
        test = Tests
        
        #declare list to hold strings
        bracket_list = []
        
        #collect number of strings
        number_of_strings = input("Enter number of strings: ")

        #test paramaters
        if test.test_size(int(number_of_strings)):
            print("Invalid number of strings")
            return

        i = 0
        #collect strings
        while i != int(number_of_strings):
            string = input("String: ")
            if test.test_size(len(string)) or test.odd_even_test(len(string)):
                print("Invalid string size.")
                continue
            else:
                bracket_list.append(string)
            i += 1
            
        print('\n')
        
        #test strings and print results
        for line in bracket_list:
            test.balance_test(line)

    #collect user input and call apporpriate functions
    def user_input():
        #define class variables
        input_method = Input
        
        #prompt for and collect input
        #set as loop so user can perform operation as many times as desired and if error gives chance to retry
        while True:
            print("Would you like to manually input strings, open a file collect input, or exit program?")
            print("    Option 1: manual input")
            print("    Option 2: file input")
            print("    Option 3: exit program\n")
            option = input("Option: ")

            #function call based on option
            #manual input
            if option == '1':
                try:
                    input_method.manual_input()
                    print('\n')
                except:
                    print("Error in collecting input")
                    print('\n')
            #file input        
            elif option == '2':
                try:
                    input_method.read_input_file()
                    print('\n')
                except:
                    print("Error in reading from file.")
                    print('\n')
            #quit program
            elif option == '3':
                break
            
            else:
                print("Invalid Option")
                print('\n')