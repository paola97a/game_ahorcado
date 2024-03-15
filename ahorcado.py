"""
Exercise 5.
The program choose one secret word and it show to player only a serie og guiones
that represent the amount of letters of word. The player in every turn would shoose
a letter and if the letter is found in the word the programa show him the places
where appears. But if the player say a letter that is not found in the secret word 
he will lost. 
"""

from random import choice

def get_letter(my_food):
    """
    From a letter validates if is in the word, the lives of game are six, 
    when the letter is not in the word the player lost a live if not the player 
    has opportunity to win.
    """
    list_food = list(my_food)
    list_key = [i for i in range(len(list_food))]
    combination = {k:v  for k, v in zip(list_key, list_food)}
    list_icon = ['_' for i in range(len(list_food))]
    list_letters =[]
    aux = 7

    jump = 1
    while jump<=6:
        letter = input("Enter a letter: ").lower()
        while letter.isalpha() is not True:
            print("Please Enter a letter! ")
            letter = input("Enter a letter: ").lower()
        list_letters.append(letter)
        for i in list_letters:
            for key, value  in combination.items():
                if value == i:
                    pos = key
                    list_icon[pos] = i
        print(f"{list_icon}\n")         
        if list_icon.count(letter) == 0:
            list_letters.remove(letter)
            jump += 1
            print(f"Your lives are: {aux-jump}")
        elif list_icon.count('_') == 0:
            print('!!! YOU WIN !!')
            break


def get_food():
    """
    Method that show the init game.
    """
    random_food= ['chocolate', 'amazorca', 'carnederes', 'tocino', 'huevofrito',
                  'manzana', 'banana', 'aguacate', 'mango']
    my_food = choice(random_food)
    print("----------------------------------------------------------------")
    print("|                      Welcome to AHORCADO!!                   |")
    print("----------------------------------------------------------------")
    print("!!This word is a food!!\n")
    icon = ['_' for i in range(len(list(my_food)))]
    print(icon)
    return my_food


food = get_food()
get_letter(food)
