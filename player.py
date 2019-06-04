from random import randint

class Player():

    def __init__(self, player_choice):
        self.player_choice = player_choice

    def compare(self, cpu_choice):

        if self.player_choice.lower() == "rock":
            if cpu_choice == "rock":
                return "Tie! CPU chose {}.".format(cpu_choice)
            if cpu_choice == "paper":
                return "CPU wins! CPU chose {}.".format(cpu_choice)
            if cpu_choice == "Scissors":
                return "Player wins! CPU chose {}.".format(cpu_choice)

        elif self.player_choice.lower() == "paper":
            if cpu_choice == "rock":
                return "Player wins! CPU chose {}.".format(cpu_choice)
            if cpu_choice == "paper":
                return "Tie! CPU chose {}.".format(cpu_choice)
            if cpu_choice == "scissors":
                return "CPU wins! CPU chose {}.".format(cpu_choice)

        elif self.player_choice.lower() == "scissors":
            if cpu_choice == "rock":
                return "CPU wins! CPU chose {}.".format(cpu_choice)
            if cpu_choice == "paper":
                return "Player wins! CPU chose {}.".format(cpu_choice)
            if cpu_choice == "scissors":
                return "Tie! CPU chose {}.".format(cpu_choice)


class ComputerPlayer(Player):
    def cpu_turn(self):
        choices = ["rock", "paper", "scissors"]
        cpu_choice = choices[randint(0, 2)]
        return cpu_choice

