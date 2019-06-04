from player import ComputerPlayer

def play_game(times):
    print("Welcome to Rock, Paper, Scissors! \nType your choice to play with CPU! \nAfter you're done, please type Finish.")
    player_lower = ''
    while player_lower != 'finish': # in range(times):
        player = str(input("Your choice? "))
        player_lower = player.lower()
        if player_lower not in ["rock", "paper", "scissors", "finish"]:
            print("Something is wrong, please try again!")
            player = str(input("Your choice? "))
            player_lower = player.lower()
        cp = ComputerPlayer(player_lower)
        CPU = cp.cpu_turn()
        print(cp.compare(CPU))
        print("\n------\n")

if __name__ == '__main__':
    play_game(1)