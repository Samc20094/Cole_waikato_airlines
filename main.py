import os
import time
name_list = []


    
def starter():
    Str_name = [] 
    starter = True
    while starter == True:
        name_list.clear()
        print("*=*" * 8)
        # print('*=' * 14) # HAG
        Str_name = str(input("Hello welcome to waikato airlines!, what is your name? ")).strip().title()
        if len(Str_name) < 3 or len(Str_name)> 35:
            print("invalid input")
            continue
        if Str_name.isalpha() == True:
            print("Hello {} Where will you flying today? (aukland, wellington, waikato)".format(Str_name))
            print('*=*=' * 9)
        if Str_name.isalpha() == False:
            print("invalid input")
            continue


if __name__ == "__main__":
        starter()
        
