from player import ComputerPlayer

def play(times):
    for i in range(times):
        player_choose = input("1 - Rock \n2 - Paper\n3- Scissors\n")
        cp = ComputerPlayer()
        print(cp.play())
        print("\n------\n")


if __name__ == '__main__':
    print("Rock, paper, scissors!")
    play(3)
