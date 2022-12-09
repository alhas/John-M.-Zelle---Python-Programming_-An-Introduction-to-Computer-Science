import string


def numerologist():

    name = input("Pelase enter your name: ").upper()

    letters = list(string.ascii_uppercase)
    value = 0

    print(name.split())


    for letter in name:
        value += ord(letter) - ord("A") + 1

    print(value)
        
    
numerologist()
