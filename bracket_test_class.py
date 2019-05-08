class Tests():
    
    #test size of number of integers or 
    def test_size(size):
        #variables for size constraints
        MAX_SIZE = 10**3
        MIN_SIZE = 1
        if size > MAX_SIZE or size < MIN_SIZE:
            return True
        else:
            return False

    #test for odd length
    def odd_even_test(size):
        if (size % 2) == 0:
            return False
        else:
            return True
        
    #test string of brackets
    def balance_test(bracket_string):
        #declare variables
        bracket_list = []
        
        #loop to iterate through string
        for char in bracket_string:
            
            #Append bracket to list if open bracket
            if char == '{' or char == '[' or char == '(':
                bracket_list.append(char)
                
            #if closing bracket check list and clear the last character if balanced
            #if not balanced return false
            elif char == '}' or char == ']' or char == ')':
                if char == '}' and bracket_list[-1] == '{':
                    bracket_list.pop(-1)
                elif char == ']' and bracket_list[-1] == '[':
                    bracket_list.pop(-1)
                elif char == ')' and bracket_list[-1] == '(':
                    bracket_list.pop(-1)
                else:
                    print("Is Balanced: NO")
                    return
            #if an unknown character is found return
            else:
                print("Character entered in string is not a bracket.")
                return

        #if the bracket list is empty and there have been no errors, return true
        #if not empty return false
        if len(bracket_list) == 0:
            print("Is Balanced: YES")
        else:
            print("Is Balanced: NO")
