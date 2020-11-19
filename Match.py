# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from TicTacToe import TicTacToe

class Match() :
    """
    A class that allows you to play TicTacToe game

    Attributes :
        game : a TicTacToe object
        mode : the mode of the game (must be 'hvh', 'hvc' or 'cvc')
        players : a pair of Player
        firstPlayer : the first player of the current match (must be 0 or 1)
        turn : the index of the current Player (must be 0 or 1)
        wins : a list that contains the results of the games
    """

    def __init__(self, player1, player2) :
        self.game = TicTacToe()
        self.firstPlayer = 0
        self.turn = 0
        self.players = [player1, player2]
        self.wins = []
    
    def start(self, n=1) :
        """
        Start a new match

        Parameters :
            n : number of games in the match
        """
        for _ in range(n) :
            #print(f"{i+1}/{n}")
            self.newGame()
            self.learn()
            self.firstPlayer = 1-self.firstPlayer
            self.game.reset()
            self.players[0].reset()
            self.players[1].reset()

    def newGame(self) :
        """
        A new game of tic-tac-toe
        """
        self.turn = self.firstPlayer
        while self.game.winner==0 and not self.game.isFull() :
            #print(self.game)
            self.players[self.turn].play(self.game)
            self.turn = 1-self.turn
        #print(self.game)
        self.wins.append(self.game.winner)
    
    def learn(self) :
        """
        Learns the experience that the players have
        """
        init_coeff = 10-self.game.turn
        loser_bias = init_coeff%2
        winner_bias = 1-loser_bias
        if type(self.players[1]).__name__=='LearningPlayer' and self.players[1].learning :
            human = self.players[0]
            computer = self.players[1]
            if self.game.winner==1 :
                computer.addPositivExperience(human.currentMoves, init_coeff+winner_bias)
                computer.addNegativExperience(computer.currentMoves, init_coeff+loser_bias)
                computer.addExperienceVariation(computer.currentMoves[-1][0],human.currentMoves[-1][1]*9)
            if self.game.winner==-1 :
                computer.addPositivExperience(computer.currentMoves, init_coeff+winner_bias)
                computer.addNegativExperience(human.currentMoves, init_coeff+loser_bias)
                computer.addExperienceVariation(human.currentMoves[-1][0],computer.currentMoves[-1][1]*9)
        
        if type(self.players[0]).__name__=='LearningPlayer' and self.players[0].learning :
            human = self.players[1]
            computer = self.players[0]
            if self.game.winner==-1 :
                computer.addPositivExperience(human.currentMoves, init_coeff+winner_bias)
                computer.addNegativExperience(computer.currentMoves, init_coeff+loser_bias)
                computer.addExperienceVariation(computer.currentMoves[-1][0],human.currentMoves[-1][1]*9)
            if self.game.winner==1 :
                computer.addPositivExperience(computer.currentMoves, init_coeff+winner_bias)
                computer.addNegativExperience(human.currentMoves, init_coeff+loser_bias)
                computer.addExperienceVariation(human.currentMoves[-1][0],computer.currentMoves[-1][1]*9)
    

    def showGraph(self) :
        """
        Shows the graphs of win of the players
        """
        n = len(self.wins)
        x = [i for i in range(n)]
        plt.figure()
        plt.plot(x,np.cumsum(self.wins))
        plt.grid(True)
        plt.show()


