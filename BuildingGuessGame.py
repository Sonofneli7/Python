# Will have secret word, user tries to guess the word
# User keeps putting in guesses to try to guess
# put limit on how many guesses user will have

# variable: storing secret word
secret_word = "bee"

#variable to store user's response
guess = " "
guess_count = 0
guest_limit = 3
out_of_guesses = False
# Use WhileLoop
while guess != secret_word:
    # check that user has more guesses
    guess = input("Enter guess: ")
    guess_count += 1

print("You win!")