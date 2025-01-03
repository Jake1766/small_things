import random

class Character:
    def __init__(self):
        self.stats = {
            'strength' : 0,
            'agility': 0,
            'endurance': 0,
            'intelligence': 0
        }

        self.inventory = []



class Main:
    # constructor
    def __init__(self):
        self.running = True
        self.daily_options = '\n1. Train\n2. Shop\n3. Explore\n4. View Character\n5. View Inventory/Equipment:'

    # Utility

    def rand_int(self, max):
        output = random.randint(0, max)
        return output

    def on_start(self):
        print('welcome...')
        self.player_gen()

    def player_gen(self):
        player = Character()
        for key in player.stats:
            player.stats[key] = self.rand_int(5)

    def daily_choice(self, choice):
        if choice == 1:
            self.daily_train()
        if choice == 2:
            self.daily_shop()
        if choice == 3:
            self.daily_explore()

    def daily_train(self):
        pass

    def daily_shop(self):
        pass

    def daily_explore(self):
        pass

    def main_loop(self):
        self.on_start()
        while self.running:
            self.daily_menu()

    def daily_menu(self):
        print(self.daily_options)
        choice = input('What will you do today?\n: ')
        self.daily_choice(choice)



game = Main()
game.main_loop()