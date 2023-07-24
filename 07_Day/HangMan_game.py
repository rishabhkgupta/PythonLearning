from replit import clear
import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = list(random.choice(word_list))
word_length = len(chosen_word)
lives = 6

print(f"The chossen world is {chosen_word}")
print(logo)  

display = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    if guess in display:
        print(f"You have already guessed {guess}")
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, That is not in the World. You lose a lift")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost, No more Life left")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("congratulations! You Won")

    print(stages[lives])
        
    

