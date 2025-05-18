import random
def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
    choices = ['r', 's', 'p']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"It's a Tie!! Choice is {opponent}")

    if check_win(player, opponent):
        return print(f"Yay! you have won the game! Choice is {opponent}")

    if check_win(player, opponent) != True:
        return print(f"You lost! Choice is {opponent}")


def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True


rock_paper_scissors()