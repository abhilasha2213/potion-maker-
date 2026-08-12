import random 
ingredients = ["rose petals","moon dust","dragon scales","fairy tears","pixie dust"]

effects = [
    "makes you invisible❄️",
    "lets you fly🪽",
    "makes animals talk to you🐛",
    "gives you unlimited luck🥇",
    "turns your dreams into reality🌼"
]
print("WELCOME TO THE MAGIC LAB")
input("Press ENTER to continue: ")

ingredient = random.choice(ingredients)
effect = random.choice(effects)
print("Your ingredient: ",ingredient)
print("Effects: ",effect)