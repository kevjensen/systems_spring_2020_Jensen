#!/usr/bin/python3


while True:
    usr_input = input("Please enter something that will produce an error to prove this program works as intended.\n")
    try:
        int_usr_input = int(usr_input)
        print("User input is: %d" % int_usr_input)
        break

    except:
        print("Invalid user entry.")

 

