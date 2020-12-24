# Random password maker script
# make password from a random word and 4 random numbers
# make a list of possible words
# have the computer pick a random word from the list
# have the computer pick a random number from between 1000 and 10000
# have the compuer combine the two into a password

import random

wordsList = ["bomb", "annoy", "respect", "superb", "strengthen", "development", "tired", "trade", "influence", "underwear", "price", "secretive", "alluring", "knock", "needless", "forgetful", "lavish", "itchy", "bee", "tail", "interesting", "prick", "cushion", "agreement", "subsequent", "watch", "debt", "aware", "observant", "nasty", "white", "charge", "suggest", "panoramic", "deserted", "annoyed", "foot",
"tidy", "haunt", "cheerful", "animal", "spark", "stay", "blue", "towering", "marvelous", "unite", "answer", "lonely", "beneficial", "stove", "liquid", "office", "jealous", "known", "public", "queue", "abandoned", "analyze", "victorious", "sponge", "coffee","chairman", "Jaywatts"
]

words_item = random.choice(wordsList)
nums = random.randint(1000, 10000)

def pass_maker():
    print(words_item.capitalize() + str(nums))

pass_maker()
