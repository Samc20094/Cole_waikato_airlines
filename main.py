
ticket_list = []

def kill():
    while kill() == True:
        SystemExit()


def starter():
    global Str_name
    global name_list
    name_list = []
    starter = True
    while starter == True:
        try:
            name_list.clear()
            Str_name = str(input("Hello welcome to waikato airlines!, what is your name? ")).strip().title()
            name_list.append(Str_name)
            if len(Str_name) < 3 or len(Str_name)> 35:
                print("invalid input")
                continue
            if Str_name.isalpha() == True:
                tickets()
        except: 
            Str_name.isalpha() == False
            print("invalid input")
            continue
            return Str_name
            

def tickets():
    
    auckland_ticket = 54
    wellington_ticket = 58
    waikato_ticket = 59
    ticket = str(input("Hello {} Where will you flying today? (auckland, wellington, waikato) ".format(Str_name)))
    if ticket == "auckland":
        print("okay {} that will be ${}".format(Str_name, auckland_ticket))
        otherusers()
    elif ticket == "wellington":
        print("okay {} that will be ${}".format(Str_name, wellington_ticket))
        otherusers()

    elif ticket == "waikato":
        print("okay {} that will be ${}".format(Str_name, waikato_ticket))
        otherusers()
        
    else:
        print("invalid input")
        tickets()

def otherusers():
    extras = str(input("will there be any other travelers? "))
    if extras == "no":
        print("okay goodbye")
        kill()
    while extras == "yes":
        try:
            str(input("what is their name? "))
            name_list.append(Str_name)
            if len(Str_name) < 3 or len(Str_name)> 35:
                print("invalid input")
                continue
            if Str_name.isalpha() == True:
                print(name_list)
                tickets()
        except:
            Str_name.isalpha() == False
            print("invalid input")
            continue
            return Str_name
    



    
if __name__ == "__main__":
    starter()

        
