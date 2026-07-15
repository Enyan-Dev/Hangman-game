import random
from hangman_art import STAGES
from hangman_words import word_list


# 1. take one random word from the bowl.
chosen_word = random.choice(word_list)

# 2. create empty display plate
display = []
# 3. Fill the display with blanks for each letter in the chosen word
for letter in chosen_word:
    display.append("_")

game_over = False # game state tracking switch
lives = 6
# 4. Start the continuous loop
while not game_over:

    guess = input("Guess a letter: ").lower()

    # 5. looping through the word by its index positions
    for index in range(0,len(chosen_word)):
        letter = chosen_word[index]
# 6. swap the blank if the letter at this index matches the guess
        if letter == guess:
            display[index] = guess

    if guess not in chosen_word:
        lives = lives - 1
        print(f"Wrong guess! You lose a life. Lives remaining: {lives}")
        if lives == 0:
            print(STAGES[lives])
            print("GAME OVER! You ran out of lives.")
            print(f"The secret word was: {chosen_word}")
            break
    print(display)
    print(STAGES[lives])
    
    if "_" not in  display:
        game_over = True
        print("YOU WON, GAME OVER!!")

