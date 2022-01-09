import random
from hangman_art import stages,logo
from hangman_words import word_list


print(logo)

chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')


display = ["_"]*len(chosen_word)
lives = len(stages) - 1
end_of_game = False
while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])

    if lives == 0:
        print("You lose")

    if "_" not in display:
        end_of_game = True
        print("you win")
