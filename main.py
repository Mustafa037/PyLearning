import random
from replit import clear

import hangman_words
chosen_word = random.choice(hangman_words.word_list)

word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art
print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
  
    if guess in guessed_letters:
      print(f"You have already guessed {guess}")
      continue

    guessed_letters.append(guess)
  
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:   
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")
        
    print(f"{' '.join(display)}")
  
    if "_" not in display:
        end_of_game = True
        print("You win.")
  
    print(hangman_art.stages[lives])
if end_of_game == True:
  print(f"it was {chosen_word}")

#tested changes in GitHub