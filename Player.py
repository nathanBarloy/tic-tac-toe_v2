# -*- coding: utf-8 -*-

import math
import numpy as np
from abc import ABC, abstractmethod
import random as rd

from TicTacToe import Variation

class Player(ABC) :
    """
    Abstract class representing a player

    Attributs :
        currentMoves : a list of pair that represents the move made for a state
        marker : the marker that the player uses (1 or -1)
    """
    def __init__(self, marker) :
        self.currentMoves = []
        self.marker = marker

    @abstractmethod
    def play(self, game) :
        pass

    def playHere(self, game, line, col) :
        """
        plays at the given position
        return True if the play was successful
        """
        if game.play(self.marker, line, col) :
            self.saveMove(game, line, col)
            return True
        return False

    def saveMove(self, game, line, column) :
        """
        Save a move in the currentMove list
        """
        move = np.zeros((3,3), dtype=int)
        move[line, column] = 1
        aux = game.board[line, column]
        game.board[line, column]=0
        self.currentMoves.append((game.board*self.marker, move))
        game.board[line, column]=aux

    
    def reset(self) :
        self.currentMoves = []



class HumanPlayer(Player) :
    """
    A human player

    Attributs :
        currentMoves : a list of pair that represents the move made for a state
        marker : the marker that the player uses (1 or -1)
    """
    def __init__(self, marker) :
        Player.__init__(self, marker)

    def play(self, game) :
        """
        Wait for the move of the player
        """
        self.terminalPlay(game)
    
    def terminalPlay(self, game) :
        """
        play through the terminal
        """
        validMove = False
        while not validMove :
            choice = 0
            entry = input("Enter your move on the numpad :")
            try :
                choice = int(entry)
            except ValueError :
                print("Please enter an integer")
                continue
            except :
                raise

            if choice>0 and choice<=9 :
                choice-=1
                line = 2-choice//3
                col = choice%3
                if game.play(self.marker, line, col) :
                    self.saveMove(game, line, col)
                    validMove = True
                else :
                    print("You can't play here")
            else :
                print("Please enter an integer between 1 and 9")

    


class LearningPlayer(Player) :
    """
    A computer player, that use his experience to play

    Attributs :
        currentMoves : a list of pair that represents the move made for a state
        marker : the marker that the player uses (1 or -1)
        experience : a dictionary that gives the moves done for a given state
    """
    def __init__(self, marker, learning = True, exp={}) :
        Player.__init__(self, marker)
        self.experience = exp
        self.learning = learning

    def addPositivExperience(self, experiences, init_coeff, coeff=1) :
        """
        add a list of new experiences to the experience of the IA

        Parameters :
            experiences : a list of pair that represents new experiences
        """
        for i in range(len(experiences)) :
            exp = experiences[i]
            tot_coeff = (init_coeff + 2*i)*coeff
            self.addExperienceVariation(exp[0], exp[1]*tot_coeff)
    
    def addNegativExperience(self, experiences, init_coeff, coeff=1) :
        """
        add a list of new experiences to the experience of the IA

        Parameters :
            experiences : a list of pair that represents new experiences
        """
        for i in range(len(experiences)) :
            exp = experiences[i]
            tot_coeff = (init_coeff + 2*i)*coeff
            self.addExperienceVariation(exp[0], exp[1]*(-tot_coeff))
    
    def addExperienceVariation(self, board, move) :
        """
        add a new experience to the already existing experiences

        Parameters :
            board : the 3*3 board of the new experience
            move : the 3*3 moe representing the new move
        """
        eqMoves = Variation.getEquivalentMoves(board, move)
        boardCopy = board.copy()
        boardList = Variation.toString(boardCopy)
        #initial board
        if boardList in self.experience :
            for m in eqMoves :
                np.add(self.experience[boardList], m, out=self.experience[boardList], casting="unsafe")
            return
        # 3 rotations
        for _ in range(3) :
            boardCopy = np.rot90(boardCopy)
            for i in range(len(eqMoves)) :
                eqMoves[i] = np.rot90(eqMoves[i])
            boardList = Variation.toString(boardCopy)
            if boardList in self.experience :
                for m in eqMoves :
                    np.add(self.experience[boardList], m, out=self.experience[boardList], casting="unsafe")
                return
        #mirror
        Variation.mirror(boardCopy)
        for i in range(len(eqMoves)) :
                Variation.mirror(eqMoves[i])
        boardList = Variation.toString(boardCopy)
        if boardList in self.experience :
            for m in eqMoves :
                np.add(self.experience[boardList], m, out=self.experience[boardList], casting="unsafe")
            return
        #3 rotations
        for _ in range(3) :
            boardCopy = np.rot90(boardCopy)
            for i in range(len(eqMoves)) :
                eqMoves[i] = np.rot90(eqMoves[i])
            boardList = Variation.toString(boardCopy)
            if boardList in self.experience :
                for m in eqMoves :
                    np.add(self.experience[boardList], m, out=self.experience[boardList], casting="unsafe")
                return
        #the board was not in the experiences
        self.experience[boardList] = np.zeros((3,3), int)
        for m in eqMoves :
            np.add(self.experience[boardList], m, out=self.experience[boardList], casting="unsafe")
    

    def getExperience(self, board) :
        """
        get the stored experience for the given board

        Return :
            the experience as a 3*3 matrix
            the positions of the board after doing the transforms to get the experience
        """
        boardCopy = board.copy()
        positions = np.array([[(0,0), (0,1), (0,2)],
                              [(1,0), (1,1), (1,2)],
                              [(2,0), (2,1), (2,2)]])

        boardList = Variation.toString(boardCopy)
        #initial board
        if boardList in self.experience :
            return (self.experience[boardList], positions)
        # 3 rotations
        for _ in range(3) :
            boardCopy = np.rot90(boardCopy)
            positions = np.rot90(positions)
            boardList = Variation.toString(boardCopy)
            if boardList in self.experience :
                return (self.experience[boardList], positions)
        #mirror
        Variation.mirror(boardCopy)
        Variation.mirror(positions)
        boardList = Variation.toString(boardCopy)
        if boardList in self.experience :
            return (self.experience[boardList], positions)
        #3 rotations
        for _ in range(3) :
            boardCopy = np.rot90(boardCopy)
            positions = np.rot90(positions)
            boardList = Variation.toString(boardCopy)
            if boardList in self.experience :
                return (self.experience[boardList], positions)
        #the board was not in the experiences
        return (np.zeros((3,3)), positions)


    def getMove(self, game) :
        """
        compute the best move for the given board
        """
        emptyPlaces = game.getEmptyPlaces()
        experience, positions = self.getExperience(game.board*self.marker)
        if np.count_nonzero(experience)==0 : #if there is no experience
            possibleMoves = emptyPlaces
        else :
            chosenMoves = []
            maxVal = np.amax(experience)
            for i in range(3) :
                for j in range(3) :
                    if experience[i,j]==maxVal :
                        chosenMoves.append((positions[i,j][0], positions[i,j][1]))
            possibleMoves = [value for value in chosenMoves if value in emptyPlaces]
        if not possibleMoves :
            possibleMoves = emptyPlaces
        return rd.choice(possibleMoves)



    def play(self, game) :
        #if not self.connect3(game) and not self.defend3(game) :
            line, col = self.getMove(game)
            game.play(self.marker, line, col)
            self.saveMove(game, line, col)

    
    def connect3(self, game) :
        """
        play a move that makes you win immediatly if it exists

        Return True if the move was made
        """
        gameCopy = game.copy()
        for pos in game.getEmptyPlaces() :
            gameCopy.play(self.marker, *pos)
            if gameCopy.winner!=0 :
                game.play(self.marker, *pos)
                return True
            gameCopy.board[pos[0], pos[1]] = 0
        return False
    
    def defend3(self, game) :
        """
        play a move that prevent an immediat lose if it exists

        Return True if the move was made
        """
        gameCopy = game.copy()
        for pos in game.getEmptyPlaces() :
            gameCopy.play(self.marker*(-1), *pos)
            if gameCopy.winner!=0 :
                game.play(self.marker, *pos)
                return True
            gameCopy.board[pos[0], pos[1]] = 0
        return False



class AlphaBetaPlayer(Player) :
    """
    A computer player, that use the alpha-beta algorithm to play

    Attributs :
        currentMoves : a list of pair that represents the move made for a state
        marker : the marker that the player uses (1 or -1)
        experience : a dictionary that gives the moves done for a given state
    """
    def __init__(self, marker, maxDepth) :
        Player.__init__(self, marker)
        self.maxDepth = maxDepth

    
    def play(self, game) :
        (line, col) = self.getMove(game)
        game.play(self.marker, line, col)
        self.saveMove(game, line, col)
    
    def getMove(self, game) :
        _, coord = self.alphabeta(game, (self.marker==-1), -math.inf, math.inf, self.maxDepth)
        return coord

    def alphabeta(self, game, minimizing, alpha, beta, depth) :
        """
        the min-max algorithm with alpha-beta prunning
        """
        if game.isEnded() :
            return (game.winner*depth, None)
        if depth<=0 :
            return (0,None)
        elif minimizing :
            v = math.inf
            playCoord = None
            possibleCoords = game.getEmptyPlaces()
            for coord in rd.sample(possibleCoords, len(possibleCoords)) :
                game.play(-1, *coord)
                newVal, _ = self.alphabeta(game, False, alpha, beta, depth-1)
                if v > newVal :
                    v = newVal
                    playCoord = coord
                if alpha >= v :
                    game.reverse(*coord)
                    return (v, playCoord)
                beta = min(beta, v)
                game.reverse(*coord)
        else :
            v = -math.inf
            playCoord = None
            possibleCoords = game.getEmptyPlaces()
            for coord in rd.sample(possibleCoords, len(possibleCoords)) :
                game.play(1, *coord)
                newVal, _ = self.alphabeta(game, True, alpha, beta, depth-1)
                if v < newVal :
                    v = newVal
                    playCoord = coord
                if beta <= v :
                    game.reverse(*coord)
                    return (v, playCoord)
                alpha = max(alpha, v)
                game.reverse(*coord)
        return (v, playCoord)



class RandomPlayer(Player) :
    """
    A player who plays randomly
    """
    def __init__(self, marker) :
        Player.__init__(self, marker)
    
    def play(self, game) :
        """
        plays randomly in the game
        """
        (line, col) = rd.choice(game.getEmptyPlaces())
        game.play(self.marker, line, col)
        self.saveMove(game, line, col)