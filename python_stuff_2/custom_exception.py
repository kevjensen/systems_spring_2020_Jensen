#!/usr/bin/python3

class PurpleError(Exception):
    def __init__(self, description= "You typed the word 'Lilac', which triggers this error."):
        self.description = description

class DogAteHomeworkError(Exception):
    def __init__(self, description="Ruh roh Scooby Doo, you triggered an error!"):
        self.description = description

def throw_purple_error():
    raise PurpleError("Lilacs are terrible for the purpose of this exerciste.")

def throw_dog_error():
    raise DogAteHomeworkError("Ruh Roh Scooby Doo. This is not an appropriate input.")

def user_input():
    ui = input("Type something here: use Scooby and Lilac to test error functions.\n")
    if ui == "Lilac":
        throw_purple_error()
    if ui == "Scooby":
        throw_dog_error()
    return ui
    

try:
    ui = user_input()

except PurpleError as p:
    print(p)

except DogAteHomeworkError as e:
    print(e)

try:
    print("You typed '%s' and did not trigger an error." % ui)

except NameError:
    print("Your entry was invalid, so this part of the code will also throw an error! You've broken two things with one mistake!!")
