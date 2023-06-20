
name_list = []
ticket_list = []


    
def starter():
    global Str_name
    starter = True
    while starter == True:
        try:
            name_list.clear()
            Str_name = str(input("Hello welcome to waikato airlines!, what is your name? ")).strip().title()
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
    ticket = str(input("Hello {} Where will you flying today? (auckland, wellington, waikato)".format(Str_name)))
    ticket_list.append
    if ticket == "auckland":
        print("okay {} that will be ${}".format(Str_name, auckland_ticket))
    elif ticket == "wellington":
        print("okay {} that will be ${}".format(Str_name, wellington_ticket))
    elif ticket == "waikato":
        print("okay {} that will be ${}".format(Str_name, waikato_ticket))
    else:
        print("invalid input")
        tickets()

    
if __name__ == "__main__":
    starter()

        
