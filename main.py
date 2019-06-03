from player import ComputerPlayer

def play_game(times):
    for i in range(times):
        print("1 - Rock \n2 - Paper\n3- Scissors\n")
        player = str(input("Your choice? "))
        player_lower = player.lower()
        cp = ComputerPlayer(player_lower)  # cria o objeto da classe ComputerPlayer
        CPU = cp.play()  # escolhe um valor pra cpu
        print(cp.compare(CPU))
        print("\n------\n")


if __name__ == '__main__':
    print("Rock, paper, scissors!")
    play_game(3)
