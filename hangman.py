from os import system
import requests
import hangmanFunc as custom

# Fetching random word using API (Starts Here):
wordLink = requests.get("https://random-word-api.herokuapp.com/word")
wordJson = wordLink.json()
chosen_word = wordJson[0].upper()
# Ends Here --------------------^


blanked = []
display = custom.mask(chosen_word)
liveConsumed = 0

while True:
    system("cls")
    print(custom.title())
    print(custom.cutbody(liveConsumed))
    print(f"Lives Remaining: {6 - liveConsumed}")
    print("Word: ", end="")
    print(custom.lstToStr(display))

    # Break Cases to exit infinite loop
    if custom.lstToStr(display) == chosen_word:
        print("You Win!")
        break
    elif liveConsumed == 6:
        print(f"Actual Word: {chosen_word}")
        print("HANGED!!! You Lose...")
        break

    # Prompting user to guess the alphabets in chosen word untill they run out of lives
    # Or have correctly guessed the word
    guess = input("Your guess: ").upper()
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = chosen_word[position]

    # Incrementing number of wrong guesses
    if guess not in chosen_word:
        liveConsumed += 1