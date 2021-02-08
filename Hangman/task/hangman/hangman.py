import random
import string


def print_word(word_to_guess, covered):
    print("\n" + "".join("-" if c in covered else c for c in word_to_guess))


def ask_letter():
    _str = input("Input a letter: ")
    if len(_str) != 1:
        print("You should input a single letter")
    elif _str not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
    else:
        return _str


def game_play():
    word = random.choice(words)

    word_letters = frozenset(word)
    covered_letters = set(word)
    guessed_letters = set()

    tries_cnt = 8

    while tries_cnt:
        print_word(word, covered_letters)
        answer = ask_letter()
        if not answer:
            continue

        if answer in guessed_letters:
            print("You've already guessed this letter")
        else:
            guessed_letters.add(answer)
            if answer not in word_letters:
                print("That letter doesn't appear in the word")
                tries_cnt -= 1
            else:
                covered_letters.discard(answer)
                if not covered_letters:
                    break

    if not covered_letters:
        print(f"You guessed the word {word}!")
        print("You survived!")
    else:
        print("You lost!")
    print()


words = 'python', 'java', 'kotlin', 'javascript'
random.seed()
print("""H A N G M A N""")

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "exit":
        break
    if menu == "play":
        game_play()
