name_list = []
last_element = name_list[-1]
ticket_list = []
price_list = []
age_list = []
discount = []

def kill():
    while kill() == True:
        name_list.clear()
        SystemExit()

"""DEBUGGING - we are isolating the started definition and running it by itself - our desired output is that we can create a loop and then break it when the conditions are met"""

def age():
    age = int(input("hello {} how old are you? ".format(last_element)))  
    if (age < 16) or (age > 65):
        auckland_ticket = 37.80
        wellington_ticket = 40.60
        waikato_ticket = 41.30
        print("congratulations you will get a discount on our child and seniority policy!")
    return(auckland_ticket, wellington_ticket, waikato_ticket, age)
    tickets()
    
    if (age > 16) or (age <65):
        auckland_ticket = 54
        wellington_ticket = 58
        waikato_ticket = 59 
        return(auckland_ticket, wellington_ticket, waikato_ticket, age)
        tickets()
    if (age < 0) or (age > 122):
        print("invalid input")
def starter():
    starter = True
    while starter == True:
            #print(x)
            #name_list.clear()  Why are we clearing the name list?
            #name list
            Str_name = str(input("Hello welcome to waikato airlines!, what is your name? ")).strip().title()
            #name_list.append(Str_name)
            if len(Str_name) < 3 or len(Str_name) > 35:
                print("invalid input, name must be between 3 and 35 characters long.")
                #This part is working  L21 L22
                continue
            else:
                print("Acceptable length of username")
                if Str_name.isalpha() == True:
                    print("This is acceptable")
                    age()
                else:
                    print("Please use letters only")
                    continue
                print("""I am a debugging statement - All is well                                     """) 
            return Str_name
                      #print("error occured, retrying")
            continue
            break
print(starter())

def tickets(auckland_ticket, wellington_ticket, waikato_ticket, age, Str_name):
    last_element = name_list[-1]
    ticket = str(input("Hello {} Where will you flying today? (auckland, wellington, waikato) ".format(last_element)))
    if ticket == "auckland":
        print("enjoy your flight {}".format(last_element,))
        ticket_list.append({}, 54).format(last_element)
    elif ticket == "wellington":
        print("enjoy your flight {}".format(last_element))
        ticket_list.append({}, 58).format(last_element)
    elif ticket == "waikato":
        print("enjoy your flight {}".format(last_element))
        ticket_list.append({}, 59).format(last_element)
    else:
        print("invalid input")
        tickets()

def other_users(Str_name):
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
                print(name_list, discount, ticket_list, age_list)
                age()
        except:
            Str_name.isalpha() == False
            print("invalid input")
            continue
        return(Str_name)

def total(auckland_ticket, wellington_ticket, waikato_ticket, age, Str_name):
    ticket = {
        "Name": (Str_name),
        "age": (age) , 
        "destination": (ticket_list),
    }
    print (ticket)
if __name__ == "__main__":
    starter()
    age()
    tickets()
    other_users()
    total()