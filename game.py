import random
from PIL import Image
import os


#! Put these in lists then for the decision: if option in list...
home_options = ["forest", "Cave", "Pond", "Mines"]

home_options = "Forest / Cave / Pond / Mines"
home_actions = "Eat / Move / Map / Build / Bag / Stats"
house_options = "Forest / Cave / Pond / Mines / Interior"
house_actions = "Eat / Move / Map / Bag / Stats"
interior_options = "Home"
interior_actions = "Eat / Move / Map / Sleep / Cook / Bag / Stats"
forest_options = "Home"
forest_actions = "Eat / Move / Map / Chop Wood / Bag / Stats"
pond_options = "Home"
pond_actions = "Eat / Move / Map / Fish / Bag / Stats"
mines_options = "Home"
mines_actions = "Eat / Move / Map / Mine / Bag / Stats"
cave_options = "Home / Mountain"
cave_actions = "Eat / Move / Map / Bag / Stats"
mountain_options = "Cave"
mountain_actions = "Eat / Move / Map / Bag / Stats"

# Environment


class Main:
    def __init__(self):
        self.day_number = 0
        self.available_weather = (
            40 * ["Sunny"]
            + 15 * ["Cloudy"]
            + 20 * ["Clear"]
            + 20 * ["Raining"]
            + 5 * ["Snowing"]
        )

        # defaults
        # player name in player class
        # some of these should be constants outside the class
        self.player_name = ""
        self.house_built = False
        self.game_ended = False
        self.zombie_beat = False
        self.weather = ""

    def intro(self):
        self.player_name = Player.character_name(self)

    def new_day(self):
        self.day_number += 1
        self.world = World(self.day_number, self.available_weather, self.player_name)
        player.player_health = 100
        player.player_energy = 150
        decision()


main = Main()


class Pockets:
    def __init__(self):
        self.inventory = []
        self.temp_inventory = []

    def print_inventory(self):
        # Magic python commands to print
        # __repr__ or __str__
        self.temp_inventory.clear()
        self.inventory.sort()
        if len(self.inventory) == 0:
            print("Your pockets are empty")
        else:
            for item in self.inventory:
                self.temp_inventory.append(item)
            for total in range(len(self.inventory)):
                for element in self.temp_inventory:
                    if self.temp_inventory.count(element) == 1:
                        print(element)
                        self.temp_inventory.remove(element)
                    else:
                        print(f"{element} x {self.temp_inventory.count(element)}")
                        for i in range(self.temp_inventory.count(element)):
                            self.temp_inventory.remove(element)

    # bag, drop, bag.drop rather than drop_item
    # bag class
    # item class (name, quantity)
    # player class
    # link all together

    def drop_item(self, item, drop_number: int = 1):
        if drop_number == 1:
            if item.endswith("s"):
                print(f"\n{item} have been removed")
            else:
                print(f"\n{item} has been removed")
            self.inventory.pop(self.inventory.index(item))
        else:
            if drop_number <= self.inventory.count(item):
                print(f"\n{item} x {drop_number} have been removed")
                for i in range(drop_number):
                    self.inventory.pop(self.inventory.index(item))
            else:
                print(
                    f"\n{item} x {self.inventory.count(item)} have been removed"
                    f" because you didn't have {drop_number} {item}!"
                )
                for i in range(self.inventory.count(item)):
                    self.inventory.pop(self.inventory.index(item))

    def add_item(self, item, add_number=1):
        if add_number == 1:
            if item.endswith("s"):
                print(f"\n{item} have been added to your inventory")
            else:
                print(f"\n{item} has been added to your inventory")
            self.inventory.append(item)
        else:
            print(f"\n{item} x {add_number} have been added to your inventory")
            for i in range(add_number):
                self.inventory.append(item)


inventory = Pockets()


class Location:
    def __init__(self):
        self.active_location = "Home"

    def current_location(self):
        return self.active_location


# classes in one section
# instances together in the seciton below

location = Location()
location.current_location()

# location property/attribute should be a property of player
# map should be a function/class method of the player which gets location
# (player.location)


class Map:
    def __init__(self):
        self.current_location = location.current_location()

    def view_map(self):
        match self.current_location:
            case "Forest":
                self.map_prefix = "forest_map"
            case "Home":
                if main.house_built:
                    self.map_prefix = "house_map"
                else:
                    self.map_prefix = "default_map"
            case "Interior":
                self.map_prefix = "interior_map"
            case "Mines":
                self.map_prefix = "mines_map"
            case "Pond":
                self.map_prefix = "pond_map"
            case "Mountain":
                self.map_prefix = "mountain_map"
            case "Cave":
                self.map_prefix = "cave_map"
            case _:
                self.map_prefix = "default_map"
        map_files = os.path.join(os.path.dirname(__file__), f"{self.map_prefix}.png")
        view_map = Image.open(map_files, "r")
        view_map.show()


# should be just name, health, energy


class Player:
    def __init__(self):
        self.player_name = "Player"
        self.player_health = 100
        self.player_energy = 150

    def character_name(self):
        # this should be in init
        # call functions in the init to populate it
        self.player_name = input("\nWhat is your name Adventurer?\n\n")
        print(f"\nI wish you luck on your future adventures {self.player_name}!\n")
        return self.player_name


player = Player()


class World:
    def __init__(self, day_number, available_weather, player_name):
        self.world_day_number = day_number
        self.world_weather = random.choice(available_weather)
        main.weather = self.world_weather
        # put this in player and call it with the world class
        if str(self.world_day_number).endswith("1"):
            print(
                f"\nGood morning {player_name}, it is your {self.world_day_number}st "
                f"day in the world! The weather today is {self.world_weather}.\n"
            )
        elif str(self.world_day_number).endswith("2"):
            print(
                f"\nGood morning {player_name}, it is your {self.world_day_number}nd "
                f"day in the world! The weather today is {self.world_weather}.\n"
            )
        elif str(self.world_day_number).endswith("3"):
            print(
                f"\nGood morning {player_name}, it is your {self.world_day_number}rd "
                f"day in the world! The weather today is {self.world_weather}.\n"
            )
        else:
            print(
                f"\nGood morning {player_name}, it is your {self.world_day_number}th "
                f"day in the world! The weather today is {self.world_weather}.\n"
            )


# function within the player class
# static methods
# class methods
# normal methods


def decision():
    while not main.game_ended:
        print(f"\nYou are currently in {location.active_location}\n")
        if location.active_location == "Home":
            if main.house_built:
                user_decision = input(
                    f"\nWhat would you like to do {main.player_name}? ({house_actions})\n\n"
                )
                match user_decision.lower():
                    case "move":
                        if location.active_location == "Home":
                            move_to = input(
                                f"\nWhere would you like to move to? ({house_options})\n\n"
                            )
                            match move_to.lower():
                                case "forest":
                                    location.active_location = "Forest"
                                case "cave":
                                    location.active_location = "Cave"
                                case "pond":
                                    location.active_location = "Pond"
                                case "mines":
                                    location.active_location = "Mines"
                                case "interior":
                                    location.active_location = "Interior"
                        else:
                            print("\nYou are lost!")
                    case "map":
                        print(location.active_location)
                        map = Map()
                        map.view_map()
                    case "eat":
                        if inventory.inventory.count("Cooked Fish") >= 1:
                            player.player_health += 20
                            if player.player_health >= 100:
                                player.player_health = 100
                            inventory.drop_item("Cooked Fish")
                        else:
                            print("\nYou don't have any food to eat!")
                    case "bag":
                        inventory.print_inventory()
                    case "stats":
                        print(f"\nHealth: {player.player_health}")
                        print(f"Energy: {player.player_energy}")
                    case _:
                        print("\nInvalid Option\n")

            else:
                user_decision = input(
                    f"\nWhat would you like to do {main.player_name}? ({home_actions})\n\n"
                )
                match user_decision.lower():
                    case "move":
                        if location.active_location == "Home":
                            move_to = input(
                                f"\nWhere would you like to move to? ({home_options})\n\n"
                            )
                            match move_to.lower():
                                case "forest":
                                    location.active_location = "Forest"
                                case "cave":
                                    location.active_location = "Cave"
                                case "pond":
                                    location.active_location = "Pond"
                                case "mines":
                                    location.active_location = "Mines"
                        else:
                            print("\nYou are lost!")
                    case "map":
                        print(location.active_location)
                        map = Map()
                        map.view_map()
                    case "eat":
                        if inventory.inventory.count("Cooked Fish") >= 1:
                            player.player_health += 20
                            if player.player_health >= 100:
                                player.player_health = 100
                            inventory.drop_item("Cooked Fish")
                        else:
                            print("\nYou don't have any food to eat!")
                    case "bag":
                        inventory.print_inventory()
                    case "build":
                        if (
                            inventory.inventory.count("Logs") >= 25
                            and inventory.inventory.count("Stone") >= 15
                        ):
                            inventory.drop_item("Logs", 25)
                            inventory.drop_item("Stone", 15)
                            print("\nYou have built a House!")
                            main.house_built = True
                            location.active_location = "Home"
                        else:
                            print(
                                "\nYou don't have enough materials, you need 25 Logs and 15 Stone!"
                            )
                    case "stats":
                        print(f"\nHealth: {player.player_health}")
                        print(f"Energy: {player.player_energy}")
                    case _:
                        print("\nInvalid Option\n")

        elif location.active_location == "Interior":
            user_decision = input(
                f"\nWhat would you like to do {main.player_name}? ({interior_actions})\n\n"
            )
            match user_decision.lower():
                case "move":
                    if location.active_location == "Interior":
                        move_to = input(
                            f"\nWhere would you like to move to? ({interior_options})\n\n"
                        )
                        match move_to.lower():
                            case "home":
                                location.active_location = "Home"
                    else:
                        print("\nYou are lost!")
                case "map":
                    print(location.active_location)
                    map = Map()
                    map.view_map()
                case "eat":
                    if inventory.inventory.count("Cooked Fish") >= 1:
                        player.player_health += 20
                        if player.player_health >= 100:
                            player.player_health = 100
                        inventory.drop_item("Cooked Fish")
                    else:
                        print("\nYou don't have any food to eat!")
                case "cook":
                    if inventory.inventory.count("Raw Fish") >= 1:
                        inventory.add_item("Cooked Fish")
                        inventory.drop_item("Raw Fish")
                    else:
                        print("\nYou don't have any raw food!")
                case "bag":
                    inventory.print_inventory()
                case "sleep":
                    main.new_day()
                case "stats":
                    print(f"\nHealth: {player.player_health}")
                    print(f"Energy: {player.player_energy}")
                case _:
                    print("\nInvalid Option\n")

        elif location.active_location == "Forest":
            user_decision = input(
                f"\nWhat would you like to do {main.player_name}? ({forest_actions})\n\n"
            )
            match user_decision.lower():
                case "move":
                    move_to = input(
                        f"\nWhere would you like to move to? ({forest_options})\n\n"
                    )
                    match move_to.lower():
                        case "home":
                            location.active_location = "Home"
                case "sleep":
                    main.new_day()
                case "chop wood":
                    if player.player_energy >= 10:
                        if main.weather == "Sunny":
                            inventory.add_item("Logs", 5)
                            if main.day_number != 1:
                                player.player_energy -= 10
                        else:
                            inventory.add_item("Logs", 3)
                            if main.day_number != 1:
                                player.player_energy -= 10
                    else:
                        print("\nYou don't have enough energy, you need to sleep!")
                case "bag":
                    inventory.print_inventory()
                case "eat":
                    if inventory.inventory.count("Cooked Fish") >= 1:
                        player.player_health += 20
                        if player.player_health >= 100:
                            player.player_health = 100
                        inventory.drop_item("Cooked Fish")
                    else:
                        print("\nYou don't have any food to eat!")
                case "map":
                    print(location.active_location)
                    map = Map()
                    map.view_map()
                case "stats":
                    print(f"\nHealth: {player.player_health}")
                    print(f"Energy: {player.player_energy}")
                case _:
                    print("\nInvalid Option\n")

        elif location.active_location == "Pond":
            user_decision = input(
                f"\nWhat would you like to do {main.player_name}? ({pond_actions})\n\n"
            )
            match user_decision.lower():
                case "move":
                    move_to = input(
                        f"\nWhere would you like to move to? ({pond_options})\n\n"
                    )
                    match move_to.lower():
                        case "home":
                            location.active_location = "Home"
                case "fish":
                    if player.player_energy >= 10:
                        if main.weather == "Raining":
                            inventory.add_item("Raw Fish", 2)
                            if main.day_number != 1:
                                player.player_energy -= 10
                        else:
                            inventory.add_item("Raw Fish", 1)
                            if main.day_number != 1:
                                player.player_energy -= 10
                    else:
                        print("\nYou don't have enough energy, you need to sleep!")
                case "bag":
                    inventory.print_inventory()
                case "eat":
                    if inventory.inventory.count("Cooked Fish") >= 1:
                        player.player_health += 20
                        if player.player_health >= 100:
                            player.player_health = 100
                        inventory.drop_item("Cooked Fish")
                    else:
                        print("\nYou don't have any food to eat!")
                case "map":
                    print(location.active_location)
                    map = Map()
                    map.view_map()
                case "stats":
                    print(f"\nHealth: {player.player_health}")
                    print(f"Energy: {player.player_energy}")
                case _:
                    print("\nInvalid Option\n")

        elif location.active_location == "Mines":
            user_decision = input(
                f"\nWhat would you like to do {main.player_name}? ({mines_actions})\n\n"
            )
            match user_decision.lower():
                case "move":
                    move_to = input(
                        f"\nWhere would you like to move to? ({mines_options})\n\n"
                    )
                    match move_to.lower():
                        case "home":
                            location.active_location = "Home"
                case "mine":
                    if player.player_energy >= 10:
                        if main.weather == "Cloudy":
                            inventory.add_item("Stone", 5)
                            if main.day_number != 1:
                                player.player_energy -= 10
                        else:
                            inventory.add_item("Stone", 3)
                            if main.day_number != 1:
                                player.player_energy -= 10
                    else:
                        print("\nYou don't have enough energy, you need to sleep!")
                case "bag":
                    inventory.print_inventory()
                case "eat":
                    if inventory.inventory.count("Cooked Fish") >= 1:
                        player.player_health += 20
                        if player.player_health >= 100:
                            player.player_health = 100
                        inventory.drop_item("Cooked Fish")
                    else:
                        print("\nYou don't have any food to eat!")
                case "map":
                    print(location.active_location)
                    map = Map()
                    map.view_map()
                case "stats":
                    print(f"\nHealth: {player.player_health}")
                    print(f"Energy: {player.player_energy}")
                case _:
                    print("\nInvalid Option\n")

        elif location.active_location == "Cave":
            user_decision = input(
                f"\nWhat would you like to do {main.player_name}? ({cave_actions})\n\n"
            )
            match user_decision.lower():
                case "move":
                    move_to = input(
                        f"\nWhere would you like to move to? ({cave_options})\n\n"
                    )
                    match move_to.lower():
                        case "home":
                            location.active_location = "Home"
                        case "mountain":
                            while not main.zombie_beat:
                                fight_choice = input(
                                    "\nThere is a dark shadow blocking the exit!"
                                    " As it moves closer you realise it is a member of the undead!"
                                    "\n\nFight or Flee?\n\n"
                                )
                                fight_choice = fight_choice.lower()
                                match fight_choice:
                                    case "fight":
                                        if main.weather == "Snowing":
                                            player.player_health -= 50
                                            health_check()
                                        else:
                                            player.player_health -= 25
                                        print(
                                            "\nThe zombie swipes at your face, but you manage to kick it"
                                            " to the ground and run past, you took some damage in the process!"
                                            " You hear a small sob as the zombie recedes somewhere within the cave"
                                        )
                                        health_check()
                                        main.zombie_beat = True
                                        location.active_location = "Mountain"
                                    case "flee":
                                        print("\nYou escaped the zombie just in time.")
                                        location.active_location = "Home"
                                        break
                            if main.zombie_beat:
                                location.active_location = "Mountain"
                            else:
                                location.active_location = "Home"
                case "bag":
                    inventory.print_inventory()
                case "eat":
                    if inventory.inventory.count("Cooked Fish") >= 1:
                        player.player_health += 20
                        if player.player_health >= 100:
                            player.player_health = 100
                        inventory.drop_item("Cooked Fish")
                    else:
                        print("\nYou don't have any food to eat!")
                case "map":
                    print(location.active_location)
                    map = Map()
                    map.view_map()
                case "stats":
                    print(f"\nHealth: {player.player_health}")
                    print(f"Energy: {player.player_energy}")
                case _:
                    print("\nInvalid Option\n")

        elif location.active_location == "Mountain":
            user_decision = input(
                f"\nWhat would you like to do {main.player_name}? ({mountain_actions})\n\n"
            )
            match user_decision.lower():
                case "move":
                    move_to = input(
                        f"\nWhere would you like to move to? ({mountain_options})\n\n"
                    )
                    match move_to.lower():
                        case "cave":
                            location.active_location = "Cave"
                case "bag":
                    inventory.print_inventory()
                case "eat":
                    if inventory.inventory.count("Cooked Fish") >= 1:
                        player.player_health += 20
                        if player.player_health >= 100:
                            player.player_health = 100
                        inventory.drop_item("Cooked Fish")
                    else:
                        print("\nYou don't have any food to eat!")
                case "map":
                    print(location.active_location)
                    map = Map()
                    map.view_map()
                case "stats":
                    print(f"\nHealth: {player.player_health}")
                    print(f"Energy: {player.player_energy}")
                case _:
                    print("\nInvalid Option\n")


# player.alive?
# then it will automatically run without needing to call it


def health_check():
    if player.player_health <= 0:
        print(
            "\nAfter a long struggle you finally succumb to your wounds and collapse.\n"
        )
        print("\nGame Over!")
        main.game_ended = True


# attributes of player

main.intro()
main.new_day()
decision()
