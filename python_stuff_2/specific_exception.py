#!/usr/bin/python3


while True:
    usr_input = input("Please enter something that will produce an error to prove this program works as intended.\n")
    try:
        int_usr_input = int(usr_input)
        print("User entry is: %d" % int_usr_input)
        break

    except ValueError:
        print("Please input something of type int.")
    except Exception as err:
        print("A different exception occurred. Error is %s" % (type(err), str(err))

