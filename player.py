from random import randint

class Player():

    def __init__(self, player_choice):
        self.player_choice = player_choice

    def compare(self, cpu_choice):

        if self.player_choice.lower() == "rock":
            if cpu_choice == "rock":
                return "Empate! A CPU escolheu {}".format(cpu_choice)
            if cpu_choice == "paper":
                return "Vitória da CPU! A CPU escolheu {}".format(cpu_choice)
            if cpu_choice == "Scissors":
                return "Vitória do Jogador! A CPU escolheu {}".format(cpu_choice)

        elif self.player_choice.lower() == "paper":
            if cpu_choice == "rock":
                return "Vitória do Jogador! A CPU escolheu {}".format(cpu_choice)
            if cpu_choice == "paper":
                return "Empate! A CPU escolheu {}".format(cpu_choice)
            if cpu_choice == "scissors":
                return "Vitória da CPU! A CPU escolheu {}".format(cpu_choice)

        elif self.player_choice.lower() == "scissors":
            if cpu_choice == "rock":
                return "Vitória da CPU! A CPU escolheu {}".format(cpu_choice)
            if cpu_choice == "paper":
                return "Vitória do Jogador! A CPU escolheu {}".format(cpu_choice)
            if cpu_choice == "scissors":
                return "Empate! A CPU escolheu {}".format(cpu_choice)


class ComputerPlayer(Player):

    '''
        Retorna uma escolha aleatória entre as 3 possíveis
        Dica: use a propriedade self.choice e a função randint da biblioteca random
    '''
    def play(self):
        choices = ["rock", "paper", "scissors"]
        cpu_choice = choices[randint(0,2)]
        return cpu_choice

