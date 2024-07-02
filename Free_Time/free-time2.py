import random

# Room class
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.linked_rooms = {}

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")

    def get_item(self):
        return self.items.pop() if self.items else None

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s Inventory: " + ', '.join(self.inventory))
        else:
            print(f"{self.name}'s Inventory is empty.")

# Game setup
def create_rooms():
    kitchen = Room("Kitchen", "A place where you cook food.", ["knife"])
    dining_hall = Room("Dining Hall", "A place where you eat.", ["fork"])
    ballroom = Room("Ballroom", "A place where you dance.", ["crown"])
    library = Room("Library", "A place where you read books.", ["book"])

    kitchen.link_room(dining_hall, "east")
    dining_hall.link_room(kitchen, "west")
    dining_hall.link_room(ballroom, "north")
    ballroom.link_room(dining_hall, "south")
    ballroom.link_room(library, "east")
    library.link_room(ballroom, "west")

    return kitchen, dining_hall, ballroom, library

def play_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    kitchen, dining_hall, ballroom, library = create_rooms()
    current_room = kitchen

    while True:
        current_room.get_details()
        player.show_inventory()

        command = input("Enter command (move [direction] / take item / quit): ").lower().strip()

        if command.startswith("move"):
            direction = command.split()[1]
            if direction in current_room.linked_rooms:
                current_room = current_room.linked_rooms[direction]
            else:
                print("You can't go that way!")
        elif command == "take item":
            item = current_room.get_item()
            if item:
                player.add_item(item)
                print(f"You took the {item}.")
            else:
                print("There's nothing to take.")
        elif command == "quit":
            break
        else:
            print("Invalid command.")

    print("Thanks for playing!")

# Main function
if __name__ == "__main__":
    play_game()
