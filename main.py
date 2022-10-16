import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)


display = []
for _ in range(word_length):
    display += "_"

guessed_words = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if (guess not in chosen_word) and (guess not in guessed_words):

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"Chosoen word is {chosen_word}")
    if guess not in guessed_words:
        guessed_words.append(guess)
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
