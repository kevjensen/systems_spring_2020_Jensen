#!/usr/bin/python3

import random

class Player:
    def __init__(self, name, usr_type, game, position=0, money=1500):
        self.name = name
        self.position = position
        self.money = money
        self.usr_type = usr_type
        self.game = game
        self.properties_owned = []
        self.dice1 = None
        self.dice2 = None
        self.dicesum = None

    def dice_roll(self):
        dbl_count = 0
        # roll dice1; use random number example from Nate's video
        self.dice1 = random.randrange(1, 6)
        # roll dice2
        self.dice2 = random.randrange(1, 6)
        # roll total (so we know how much they have to pay on certain tiles)
        self.dicesum = self.dice1 + self.dice2
        self.position = self.position + self.dicesum
        # move player's position on board
        if self.position > 39:
            self.position = self.position - 40
            if self.position == 0:
                self.money += 200
                print("{0} landed on Go. You receive $100.".format(self.name))
            else:
                print("{0} passed Go. Received $100.".format(self.name))
                self.money += 100
        print("You rolled a {0} and a {1} for a total of {2}.".format(self.dice1, self.dice2, self.dicesum))
        for game_dict in self.game.tiles:
            if game_dict['location'] == self.position:
                print("{0}'s location is {1}".format(self.name, game_dict['name']))
        self.property_interaction()
        while self.dice1 == self.dice2:
            dbl_count = dbl_count + 1
            if dbl_count == 3:
                print("You have rolled 3 straight doubles. Turn over.")
                break
            print("You rolled doubles! Roll again")
            # roll dice1; use random number example from Nate's video
            self.dice1 = random.randrange(1, 6)
            # roll dice2
            self.dice2 = random.randrange(1, 6)
            # roll total (so we know how much they have to pay on certain tiles)
            self.dicesum = self.dice1 + self.dice2
            if self.position > 39:
                self.position = self.position - 40
                if self.position == 0:
                    self.money += 200
                    print("{0} landed on Go. You receive $200.".format(self.name))
                else:
                    print("{0} passed Go. Received $100.".format(self.name))
                    self.money += 100
            self.position = self.position + self.dicesum
            # move player's position on board
            print("You rolled a {0} and a {1} for a total of {2}.".format(self.dice1, self.dice2, self.dicesum))
            for game_dict in self.game.tiles:
                if game_dict['location'] == self.position:
                    print("{0}'s location is {1}".format(self.name, game_dict['name']))
            self.property_interaction()

    def character_info(self):
        for game_dict in self.game.tiles:
            if game_dict['location'] == self.position:
                print("{0} has ${1}\nOwns: {2}\nIs located on: {3}\n".format(self.name, self.money, self.properties_owned,
                                                                         game_dict['name']))

    def end_game_status(self):
        if self.money < 0:
            print("{0} has lost! They've run out of money.".format(self.name))
            for players in range(len(self.game.playerlist)):
                if self.name == self.game.playerlist[players].name:
                    self.game.playerlist.remove(self.game.playerlist[players])
                    break
        if len(self.game.playerlist) == 1:
            print("{0} has won the game!".format(self.game.playerlist[0].name))
            return True
        return False

    def property_interaction(self):
        for game_dict in self.game.tiles:
            if game_dict['location'] == self.position:
                for players in self.game.playerlist:
                    # Some of these conditionals may seem superfluous, but to keep the game from crashing I had to
                    # place these extra conditionals
                    if game_dict['name'] == "Go To Jail!":
                        print("Property cannot be purchased.")
                        break
                    if game_dict['name'] == "Go":
                        break
                    if game_dict['group'] == "chill":
                        print("Property cannot be purchased.")
                        if game_dict['name'] == "Income Tax":
                            print("{0} landed on {1}. They must pay {2}".format(self.name, game_dict['name'], game_dict['base_rent']))
                            self.money = self.money - int(game_dict['base_rent'])
                            break
                        if game_dict['name'] == "Luxury Tax":
                            print("{0} landed on {1}. They must pay {2}".format(self.name, game_dict['name'],
                                                                                game_dict['base_rent']))
                            self.money = self.money - int(game_dict['base_rent'])
                            break
                        break
                    if game_dict['owner'] is None and game_dict['type'] == "property" or game_dict[
                        'type'] == "railroad" or \
                            game_dict['type'] == "utility":
                        if self.usr_type == "human":
                            purchase_input = input(
                                "The property {0} has no owner. It is of type {2}. Would you like to purchase {0} for ${1}? Y/N\n".format(
                                    game_dict['name'], game_dict['cost'], game_dict['type']))
                            if purchase_input == "Y":
                                if self.money > int(game_dict['cost']):
                                    game_dict['owner'] = self.name
                                    self.money = self.money - int(game_dict['cost'])
                                    self.properties_owned.append(game_dict['name'])
                                    break
                                else:
                                    print("Insufficient funds.")
                                    break
                        elif self.usr_type == "bot":
                            if game_dict['owner'] != None:
                                break
                            elif self.money > int(game_dict['cost']):
                                game_dict['owner'] = self.name
                                self.money = self.money - int(game_dict['cost'])
                                self.properties_owned.append(game_dict['name'])
                                print("{0} purchased {1} which is of type {2}".format(self.name, game_dict['name'],
                                                                                      game_dict['type']))
                                break
                            elif self.money < int(game_dict['cost']):
                                break
                    if players.name == game_dict['name'] and players.name != self.name and game_dict['type'] == "property" or game_dict['type'] == "railroad" or \
                        game_dict['type'] == "utility":
                            if game_dict['owner'] == self.name:
                                break
                            if game_dict['name'] == "Electric Company" or game_dict['name'] == "Water Works":
                                print("{0} is owned by {1}. You must pay {2}".format(game_dict['name'], players.name,
                                                                                     self.dicesum * 4))
                                self.money = self.money - (self.dicesum * 4)
                                players.money = players.money + (self.dicesum * 4)
                                break
                            else:
                                print("This property is owned by {0}. You must pay {1}".format(game_dict['owner'],
                                                                                               game_dict['base_rent']))
                                # print("TEST: {0} should equal {1}".format(int(game_dict['base_rent']), game_dict['base_rent']))
                                self.money = self.money - int(game_dict['base_rent'])
                                players.money = players.money + int(game_dict['base_rent'])
                                break
                    if game_dict['owner'] is not None and game_dict['type'] == "property" or game_dict['type'] == "railroad" or \
                        game_dict['type'] == "utility":
                        if game_dict['owner'] == self.name:
                            break
                        if game_dict['name'] == "Electric Company" or game_dict['name'] == "Water Works":
                            print("{0} is owned by {1}. You must pay {2}".format(game_dict['name'], players.name,
                                                                                 self.dicesum * 4))
                            self.money = self.money - (self.dicesum * 4)
                            players.money = players.money + (self.dicesum * 4)
                            break
                        else:
                            print("This property is owned by {0}. You must pay {1}".format(game_dict['owner'],
                                                                                           game_dict['base_rent']))
                            # print("TEST: {0} should equal {1}".format(int(game_dict['base_rent']), game_dict['base_rent']))
                            self.money = self.money - int(game_dict['base_rent'])
                            players.money = players.money + int(game_dict['base_rent'])
                            break

    def take_turn(self):
        self.character_info()
        input("Please hit 'enter' to roll.\n")
        self.dice_roll()
        return self.end_game_status()


class Game:
    def __init__(self):
        self.playerlist = []
        self.tiles = [{'name': 'Go', 'cost': 0, 'location': 0, 'type': 'pass', 'base_rent': 2, 'group': None},
                      {'name': 'Mediterranean Avenue', 'cost': 60, 'location': 1, 'type': 'property', 'base_rent': 2,
                       'group': 'brown', 'owner': None},
                      {'name': 'Community Chest', 'cost': 0, 'location': 2, 'type': 'chest', 'base_rent': 0,
                       'group': 'chill'},
                      {'name': 'Baltic Avenue', 'cost': 60, 'location': 3, 'type': 'property', 'base_rent': 4,
                       'group': 'brown', 'owner': None},
                      {'name': 'Income Tax', 'cost': 0, 'location': 4, 'type': 'chest', 'base_rent': 100,
                       'group': 'chill'},
                      {'name': 'Reading RR', 'cost': 200, 'location': 5, 'type': 'railroad', 'base_rent': '25',
                       'group': 'white', 'owner': None},
                      {'name': 'Oriental Avenue', 'cost': '100', 'location': 6, 'type': 'property', 'base_rent': '6',
                       'group': 'blue', 'owner': None},
                      {'name': 'Chance', 'cost': 0, 'location': 7, 'type': 'chance', 'base_rent': 0, 'group': 'chill'},
                      {'name': 'Vermont Avenue', 'cost': '100', 'location': 8, 'type': 'property', 'base_rent': '6',
                       'group': 'blue', 'owner': None},
                      {'name': 'Connecticut Avenue', 'cost': '120', 'location': 9, 'type': 'property', 'base_rent': '8',
                       'group': 'blue', 'owner': None},
                      {'name': 'Jail', 'cost': 0, 'location': 10, 'type': 'chest', 'base_rent': 0, 'group': 'chill'},
                      {'name': 'St. Charles', 'cost': '140', 'location': 11, 'type': 'property', 'base_rent': '10',
                       'group': 'purple', 'owner': None},
                      {'name': 'Electric Company', 'cost': '150', 'location': 12, 'type': 'utility', 'base_rent': '1',
                       'group': 'utility', 'owner': None},
                      {'name': 'States Avenue', 'cost': '70', 'location': 13, 'type': 'property', 'base_rent': '10',
                       'group': 'purple', 'owner': None},
                      {'name': 'Virginia Avenue', 'cost': '160', 'location': 14, 'type': 'property', 'base_rent': '12',
                       'group': 'purple', 'owner': None},
                      {'name': 'Pennsylvania RR', 'cost': '200', 'location': 15, 'type': 'railroad', 'base_rent': '25',
                       'group': 'white', 'owner': None},
                      {'name': 'St. James', 'cost': 180, 'location': 16, 'type': 'property', 'base_rent': '14',
                       'group': 'orange', 'owner': None},
                      {'name': 'Community Chest', 'cost': 0, 'location': 17, 'type': 'chest', 'base_rent': 0,
                       'group': 'chill'},
                      {'name': 'Tennessee Avenue', 'cost': '180', 'location': 18, 'type': 'property', 'base_rent': '14',
                       'group': 'orange', 'owner': None},
                      {'name': 'New York', 'cost': 200, 'location': 19, 'type': 'property', 'base_rent': '16',
                       'group': 'orange', 'owner': None},
                      {'name': 'Free Parking', 'cost': 0, 'location': 20, 'type': 'parking', 'base_rent': 0,
                       'group': 'chill'},
                      {'name': 'Kentucky Avenue', 'cost': '220', 'location': 21, 'type': 'property', 'base_rent': '18',
                       'group': 'red', 'owner': None},
                      {'name': 'Chance', 'cost': 0, 'location': 22, 'type': 'chance', 'base_rent': 0, 'group': 'chill'},
                      {'name': 'Indiana Avenue', 'cost': '220', 'location': 23, 'type': 'property', 'base_rent': '18',
                       'group': 'red', 'owner': None},
                      {'name': 'Illinois Avenue', 'cost': '240', 'location': 24, 'type': 'property', 'base_rent': '20',
                       'group': 'red', 'owner': None},
                      {'name': 'B&O RR', 'cost': 200, 'location': 25, 'type': 'property', 'base_rent': '25',
                       'group': 'white', 'owner': None},
                      {'name': 'Atlantic Avenue', 'cost': '260', 'location': 26, 'type': 'property', 'base_rent': '22',
                       'group': 'yellow', 'owner': None},
                      {'name': 'Ventnor Avenue', 'cost': '260', 'location': 27, 'type': 'property', 'base_rent': '22',
                       'group': 'yellow', 'owner': None},
                      {'name': 'Water Works', 'cost': '150', 'location': 28, 'type': 'property', 'base_rent': '1',
                       'group': 'utility', 'owner': None},
                      {'name': 'Marvin Gardens', 'cost': 280, 'location': 29, 'type': 'property', 'base_rent': '24',
                       'group': 'yellow', 'owner': None},
                      {'name': 'Go To Jail!', 'cost': 0, 'location': 30, 'type': 'gotojail', 'base_rent': 0,
                       'group': 'jail'},
                      {'name': 'Pacific Avenue', 'cost': '300', 'location': 31, 'type': 'property', 'base_rent': '26',
                       'group': 'green', 'owner': None},
                      {'name': 'North Carolina', 'cost': 300, 'location': 32, 'type': 'property', 'base_rent': '150',
                       'group': 'green', 'owner': None},
                      {'name': 'Community Chest', 'cost': 0, 'location': 33, 'type': 'chest', 'base_rent': 0,
                       'group': 'chill'},
                      {'name': 'Pennsylvania Avenue', 'cost': '320', 'location': 34, 'type': 'property',
                       'base_rent': '28', 'group': 'green', 'owner': None},
                      {'name': 'Short Line', 'cost': 200, 'location': 35, 'type': 'property', 'base_rent': '25',
                       'group': 'white', 'owner': None},
                      {'name': 'Chance', 'cost': 0, 'location': 36, 'type': 'chance', 'base_rent': 0, 'group': 'chill'},
                      {'name': 'Park Place', 'cost': '350', 'location': 37, 'type': 'property', 'base_rent': '35',
                       'group': 'darkblue', 'owner': None},
                      {'name': 'Luxury Tax', 'cost': 0, 'location': 38, 'type': 'tax', 'base_rent': 75,
                       'group': 'chill'},
                      {'name': 'Boardwalk', 'cost': '400', 'location': 39, 'type': 'property', 'base_rent': '50',
                       'group': 'darkblue', 'owner': None}]


def main():
    # Declare game variables
    monopoly = Game()

    # Get number of players, type, name, and append them to the game player list
    while True:
        num_players = int(input(("How many players (2-4)?\n")))
        if (num_players > 4 or num_players < 2):
            print("Invalid number of players.")
        else:
            break

    for players in range(num_players):
        while True:
            type_input = input("Is Player {0} a 'human' or 'bot'?\n".format(players + 1))
            if type_input == "bot":
                players = Player("Bot {0}".format(players + 1), "bot", monopoly)
                monopoly.playerlist.append(players)
                break
            if type_input == "human":
                players = Player(input("Please enter your name\n"), "human", monopoly)
                monopoly.playerlist.append(players)
                break
            else:
                print("Invalid input. Try again.")
    game_state = False

    while game_state == False:
        for players in monopoly.playerlist:
            print("It is {0}'s turn".format(players.name))
            game_state = players.take_turn()


if __name__ == "__main__":
    main()
