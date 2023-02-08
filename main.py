import random
import art
import astro_word_list

stages = art.stages
words = astro_word_list.words
word = random.choice(words)
word_len = len(word)

print(
  "Welcome to Astro-Hangman... \n\nRules: \n-You have 6 chances to guess the word \n-If you repeat the letters lives won't be cut-off\n"
)

print(f"It is a {word_len} letters word\n")

display = []
for i in word:
  display.append("_")
print(*display)

print("\n")

end_of_game = False
lives = 6
guesses = []

while not end_of_game:
  guess = input("Guess a letter : ").lower()

  if guess in guesses:
    print(f"you have already guessed {guess}")
  elif guess in word:
    print("You got it right...")
    for j in range(word_len):
      if word[j] == guess:
        display[j] = word[j]
  else:
    lives -= 1
    print(f"The letter '{guess}' is not in the given word...")
  print("\n")
  print(*display)
  print("\n")

  print("These are the guessed letters :")
  guesses.append(guess)
  print(*guesses)

  print(stages[lives])

  if lives == 0:
    end_of_game = True
    print(f"You lose, the word given was '{word}'")
  if "_" not in display:
    end_of_game = True
    print(f"You win, with {lives} lives remaining!")
