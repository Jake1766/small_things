import random
main = True
roster = {}


def char_gen():
    name = name_gen()
    print('Your new hero is known as ' + str(name))
    stats = [random.randint(0, 3), random.randint(0, 3)]
    roster.update({name: stats})
    print(roster)


def name_gen():
    first_names = ['Splungy', 'Cocker', 'Wibble', 'Flan', 'Uncertain', 'Angry']
    last_names = ['Chris', 'Annete', 'Flibbler', 'Penelope', 'Ranch Dressing', 'Covid Bat']
    name = str(first_names[random.randint(0, 5)]) + ' ' + str(last_names[random.randint(0, 5)])
    return name


def input_handler(key_press):
    if key_press == 'f':
        fight()
    if key_press == 't':
        train()
    if key_press == 's':
        shop()
    if key_press == 'r':
        char_gen()
    if key_press == 'v':
        view_combatants()




while main:
    input_handler(input('Recruit: R\nView Combatants: V\nTrain: T\nShop: S\nFight: F\n:'))



