#import test function file
from bracket_input_class import *

#driver function
def main():
    input_method = Input
    #for keyboard interupt when running in shell
    try:
        input_method.user_input()
    except:
        #exception for when ctrl^c was entered during testing when choosing options
        print("Keyboard interupt")
main()
