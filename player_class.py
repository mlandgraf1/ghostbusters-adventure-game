#Maureen Landgraf
from random import random
class Player:
    
    def __init__( self, name ):
        self.name = name
        self.protonEnergy = 100
        self.ghostsCollected = 0
        
    def getPlayerName( self ):
        return self.name
    
    def getProtonEnergy( self ):
        return self.protonEnergy
    
    def getGhostsCollected( self ):
        return self.ghostsCollected
    
    #collects random amount of ghosts
    def getGhosts( self ):
        r = random()
        self.ghostsCollected = self.getGhostsCollected()
        if r < 0.3:
            self.ghostsCollected = self.ghostsCollected + 3
            print("You caught 3 ghosts on this block! You've now caught {} ghosts.".format(self.ghostsCollected))
        elif r > 0.3 and r < 0.75:
            self.ghostsCollected = self.ghostsCollected + 5
            print("You caught 5 ghosts on this block! You've now caught {} ghosts.".format(self.ghostsCollected))
        else:
            self.ghostsCollected = self.ghostsCollected + 10
            print("You caught 10 ghosts on this block! You've now caught {} ghosts.".format(self.ghostsCollected))
        return self.ghostsCollected
    
    #collects 10 proton energy
    def getExtraEnergy( self ):
        self.protonEnergy = self.protonEnergy + 10
        print("You cut through a skyscraper and charged your proton pack. You now have {} energy in your proton pack!".format(self.protonEnergy))
        return self.protonEnergy
    
    # loses 3 proton energy
    def loseEnergy( self ):
        self.protonEnergy = self.protonEnergy - 3
        print("You stopped to get a slice of New York style pizza and your proton pack went off while reaching for your wallet.")
        print("You now only have {} energy in your proton pack.".format(self.protonEnergy))
        return self.protonEnergy
    
    def enemyAttacksPlayer( self ):
        self.protonEnergy = self.getProtonEnergy()
        r = random()
        if self.protonEnergy > 0:
            if self.protonEnergy <= 0:
                self.protonEnergy = 0
            if r < 0.45:
                self.protonEnergy = self.protonEnergy - 3
                print("You were hit! You spent 3 proton energy trying to defend yourself. You have {} proton energy remaining.".format( self.protonEnergy ))
            elif r >= 0.65 and r <= 0.85:
                self.protonEnergy = self.protonEnergy - 10
                print("You were hit! You spent 10 proton energy trying to defend yourself. You have {} proton energy remaining.".format(self.protonEnergy))
            elif r > 0.85 and r < 0.98:
                self.protonEnergy = self.protonEnergy - 5
                print("You were hit! You spent 5 proton energy trying to defend yourself. You have {} proton energy remaining.".format(self.protonEnergy))
            else:
                self.protonEnergy = self.protonEnergy - 20
                print("A devastating hit! You spent 20 proton energy trying to defend yourself. You have {} proton energy remaining.".format(self.protonEnergy))
        return self.protonEnergy