# Players have to guess a word with a minimum of penalties.
# Each turn, a player suggests a letter:
# ✓ if the word contains it, each occurrence of the letter is revealed;
# ✓ if the word does not contain it, the player gets 1 penalty.
# At any time, the player can propose a full word:
# ✓ if the word is the one to be guessed, the player wins:
# ✓ else, the player gets 5 penalties.
# If the number of penalties exceeds 12, the player looses

# avoir un mot, le décomposer sur chaque lettre
# si le mot dépasse

import random
from english_words import get_english_words_set

def checkloose(number: int):
    if(number <= 0):
        return True
    return False

# Récupération d'un mot aléatoire en anglais
def hasard(values: list, length_wanted: int):
    words = [word for word in values if len(word) == length_wanted]
    return random.choice(words) if words else None

# Décomposition du mot
def each_strings(word: str):
    lenString = len(word)
    finalString = []
    for i in range(0, lenString):
        finalString.append("_")
        i =+ 1
    return finalString


# fonction récupération d'une liste de mot
def words_from_txt(file):
    with open(file, encoding='utf-8') as f:
        return set(m.strip().lower() for m in f if m.strip())
# Liste de mots en anglais / fraçais
englishWords = get_english_words_set(['gcide'], lower=True)
frenchWords = words_from_txt("frenchwords.txt")

# choix de la langue
language = input("Choose your language (en/fr) : ")
languageChoosen = ""
if(language == "en"):
    languageChoosen = englishWords
elif(language == "fr"):
    languageChoosen = frenchWords
else: 
    print("Unknown language")

# choix de la difficulté
choose = int(input("Choose the length of the word : "))

# mot unique trouvé
englishWordFind = hasard(list(languageChoosen), choose)
# stockage du mot dans un tableau par caractère
englishWordArray = []
for i in range(0, len(englishWordFind)):
    englishWordArray.append(englishWordFind[i])
# génération du même mot mais version caché
hiddenWord = each_strings(englishWordFind)



# Tant que le mot final n'égal pas le mot trouvé, continuer
lives = 12
badLetter = []
cheating_mode = False
attempt = 0
print(f"the word is : {englishWordFind} (cheating mode activated ahahahahah)")
print(f"{"".join(hiddenWord)} / {lives} lives")
while(lives > 0):
    guess = input("Guess a letter/word : ")
    
    # print(len(guess))
    if(len(guess) >= 2):
        if(guess == englishWordFind):
            print(f"Well done ! The word was {englishWordFind}")
            print(f"Finded in {attempt} attempt\n")
            break
        else:
            lives -= 5
            attempt += 1
            print("Not a good word ! -5 lives !!!! SO BAD !!!\n")
    else:
        # parcourir toute la liste du mot trouvé
        # si son guess == à un indice du mot trouvé
        # alors remplacer dans hiddenWord la lettre par guess sur l'index correct
        for i in range(0, len(englishWordArray)):
            if(guess == englishWordArray[i]):
                hiddenWord[i] = guess
        # comparer si le guess est au moins 1 fois dans la liste
        if guess not in englishWordArray:
            if guess not in badLetter:
                badLetter.append(guess)
                lives -= 1
                attempt += 1
                print(f"\nBooouh failed ! Not in this word :c")
                print(f"{attempt} attempt")
                print(f"Bad letters : {" ".join(badLetter)}\n")
            elif(guess in badLetter):
                attempt += 1
                print(f"You already said {guess}, are u dumb ?")
        if(hiddenWord == englishWordArray):
            print(f"\nWell done ! The word was {englishWordFind}")
            print(f"Finded in {attempt} attempt\n")
            break
        elif(checkloose(lives)):
            print("\nYou loose ! So bad...")
            print(f"The word was {englishWordFind}")
            print(f"Tried in {attempt} attempts\n")
            break
        else:
            print(f"{"".join(hiddenWord)} / {lives} lives\n")
            

