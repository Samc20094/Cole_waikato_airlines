passenger_data = []
import os
import time
            
def clear_console():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def age():
    last_element = passenger_data[-1]["Name"]
    age = int(input("Hello {} how old are you? ".format(last_element)))
    
    if 16 <= age <= 65:
        auckland_ticket = 54
        wellington_ticket = 58
        waikato_ticket = 59
        print("You are eligible for standard ticket prices.")
        time.sleep(2)
        clear_console()
    elif 0 <= age < 16 or age > 65:
        auckland_ticket = 37.80
        wellington_ticket = 40.60
        waikato_ticket = 41.30
        print("Congratulations! You will get a discount on our child and seniority policy!")
        time.sleep(2)
        clear_console()
    else:
        print("Invalid age.")
        return None
    
    ticket_prices = {
        "auckland": auckland_ticket,
        "wellington": wellington_ticket,
        "waikato": waikato_ticket
    }
    
    tickets(ticket_prices, age)

def starter():
    Str_name = str(input("Hello, welcome to Waikato Airlines! What is your name? ")).strip().title()
    
    if len(Str_name) < 3 or len(Str_name) > 35:
        print("Invalid input, the name must be between 3 and 35 characters long.")
        return
    
    if Str_name.isalpha() == True:
        passenger_data.append({"Name": Str_name})
        age()
    else:
        print("Please use letters only")

def tickets(ticket_prices, age):
    last_element = passenger_data[-1]["Name"]
    ticket = input("Hello {} Where will you be flying today? (auckland, wellington, waikato) ".format(last_element)).strip().lower()

    if ticket in ticket_prices:
        print("Enjoy your flight, {}".format(last_element))
        passenger_data[-1]["Age"] = age
        passenger_data[-1]["Destination"] = ticket
        passenger_data[-1]["Ticket Price"] = ticket_prices[ticket]
    else:
        print("Invalid input, please select auckland, wellington, or waikato.")
        tickets(ticket_prices, age)

def other_users():
    extras = input("Will there be any other travelers? (yes/no) ").strip().lower()
    
    if extras == "yes":
        while extras == "yes":
            time.sleep(2)
            clear_console()
            Str_name = input("What is their name? ").strip().title()
            if len(Str_name) < 3 or len(Str_name) > 35:
                print("Invalid input")
            elif Str_name.isalpha() == True:
                passenger_data.append({"Name": Str_name})
                age()
            else:
                print("Please use letters only")
            
            extras = input("Will there be any other travelers? (yes/no) ").strip().lower()
    elif extras != "no":
        print("Invalid input, please answer with 'yes' or 'no'.")
        other_users()

def total():
    total_price = 0
    print("Passenger details:")
    for idx, passenger in enumerate(passenger_data):
        total_price += passenger["Ticket Price"]
        print("Passenger {}: {}".format(idx + 1, passenger))
    
    print("Total price for all tickets: ${:.2f}".format(total_price))

if __name__ == "__main__":
    starter()
    other_users()
    total()
