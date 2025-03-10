from random import choice

# Ahorcado


# Generate a magic word and lifes
def generate_secret_word():

    animals = [
        "tiger",
        "elephant",
        "dog",
        "cat",
        "lyon",
        "whales",
        "dolphin",
        "bat",
        "bear",
        "bull",
        "buffalo",
    ]
    secret_word = choice(animals)
    secret_word_list = list(secret_word)

    # Generate visible word
    visible_word = []
    for letter in secret_word:
        visible_word.append("-")

    return secret_word, secret_word_list, visible_word


# Validate letter
def enter_letter():
    letter = "-"
    while not ((letter > "a" and letter < "z") or (letter > "A" and "Z")):
        letter = input("Enter a letter: ")
    return letter


def validate_letter(letter, letter_entered):
    for l in letter_entered:
        if letter in letter_entered:
            return True
    return False


# Check letter
def check_letter(letter, lifes, visible_word, secret_word):
    letter = letter.lower()
    flag = False
    for index, l in enumerate(secret_word):
        if letter == l:
            visible_word[index] = letter
            flag = True
    if flag == False:
        lifes -= 1
    return visible_word, lifes


# Check word
def check_word(word):
    for letter in word:
        if letter == "-":
            return False  # Word is not completed

    return True  # Word is completed


# Main

# Generate word
secret_word, secret_word_list, visible_word = generate_secret_word()

# Generate lifes
lifes = 6

# Generate list of letter that the user enter
letters_entered = []

while lifes > 0:
    print(f"You have {lifes} lifes remain")
    print(visible_word)
    letter = enter_letter()
    if validate_letter(letter, letters_entered) == True:
        print(f"You already entered '{letter}'")
        continue
    else:
        letters_entered.append(letter)
    visible_word, lifes = check_letter(letter, lifes, visible_word, secret_word)
    if check_word(visible_word) == True:
        break
    else:
        pass

if lifes > 0:
    print(f"Congrulations the word was {secret_word}")
else:
    print(f"Good try, the word was {secret_word}")
