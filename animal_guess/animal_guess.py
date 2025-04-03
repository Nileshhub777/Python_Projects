def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, please try the guess again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is :", answer)


score = 0
print("Guess the Animal !!")
guess1 = input("Which bear lives at North Pole ? ")
check_guess(guess1, "Polar bear")
guess2 = input("Which is fastest land animal in the world ? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the largest animal ? ")
check_guess(guess3, "Blue Whale")
print("Your Score is : " + str(score))