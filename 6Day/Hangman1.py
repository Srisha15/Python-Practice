import random
import hangman_art
import hangman_words

print(hangman_art.logo)
lives = 6
comp_ch = random.choice(hangman_words.word_list)
#print(comp_ch)
placeholder = ""
for _ in range(len(comp_ch)) :
    #print("_", end="")
    placeholder += "_"
print("Word to guess :" + placeholder)

game_over = False
letter_list = []
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess= input("\nGuess a word:").lower()

    if guess in letter_list:
            print(f"You have already entered {guess}\n")
    display = ""
   

    for letter in comp_ch:
        if letter == guess:
            display += letter
            letter_list.append(letter)
        elif letter in letter_list:
            display += letter
        else:
            display += "_"
    print("Word to guess :" + display)


    if guess not in comp_ch:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"IT WAS f{comp_ch}!\n")
            print("***********************YOU LOSE**********************")

    print(hangman_art.stages[lives])

    if "_" not in display:
        game_over = True
        print("***********************YOU WIN**********************")
    


