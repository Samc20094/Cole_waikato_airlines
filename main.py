
global name_list
global age
name_list = []
ticket_list = []
discount = []

def kill():
    while kill() == True:
        SystemExit()


def starter():
    global Str_name
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
                age()
                
        except: 
            Str_name.isalpha() == False
            print("invalid input")
            continue
            return Str_name


def age():
    age = int(input("hello {} how old are you? "))
    if (age <16 or age >65):
        print("congratulations you will get a discount on our child and seniority policy!")
        discount.append(age)
        tickets()
    if (age <1 or age >100):
        print("invalid input")


def tickets():
    last_element = name_list[-1]
    auckland_ticket = 54
    wellington_ticket = 58
    waikato_ticket = 59    
    ticket = str(input("Hello {} Where will you flying today? (auckland, wellington, waikato) ".format(last_element)))
    if ticket == "auckland":
        print("okay {} that will be ${}".format(last_element, auckland_ticket))
        ticket_list.append(54)
        otherusers()
    elif ticket == "wellington":
        print("okay {} that will be ${}".format(last_element, wellington_ticket))
        ticket_list.append(58)
        otherusers()

    elif ticket == "waikato":
        print("okay {} that will be ${}".format(last_element, waikato_ticket))
        ticket_list.append(59)
        otherusers()
        
    else:
        print("invalid input")
        tickets()


def otherusers():
    extras = str(input("will there be any other travelers? "))
    if extras == "no":
        total()
        
    while extras == "yes":
        try:
            Str_name = input("what is their name? ")
            name_list.append(Str_name)
            if len(Str_name) < 3 or len(Str_name)> 35:
                print("invalid input")
                continue
            if Str_name.isalpha() == True:
                print(name_list, discount)
                tickets()
        except:
            Str_name.isalpha() == False
            print("invalid input")
            continue
            return Str_name
    

def total():
    for item in discount:
        if(item[1] < 25):
            item [1] in ticket_list (1-0.31)
    print("okay your total will be {}".format( ticket_list))
    
    
if __name__ == "__main__":
    starter()

        
