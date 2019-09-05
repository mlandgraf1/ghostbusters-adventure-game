#Maureen Landgraf
from random import random
class Enemy:
    def __init__( self, name, enemyHealth ):
        self.name = name
        self.enemyHealth = enemyHealth
        
    def getEnemyName( self ):
        return self.name
    
    def getEnemyHealth( self ):
        return self.enemyHealth
    
    #introduces enemy
    def getEnemyInfo( self, name ):
        if self.name == "Gozer":
            self.enemyIntro = print("It’s Gozer! If this monster asks you if you're a god, you'd better say yes!")
        elif self.name == "Zuul":
            self.enemyIntro = print("It’s Zuul! He may look dog-like but you wouldn't want him as a pet!")
        elif self.name == "Stay-Puft Marshmallow Man":
            self.enemyIntro = print("It’s the Stay-Puft Marshmallow Man! He’ll ruin the taste of marshmallows forever!")
        else:
            self.name == "Slimer"
            self.enemyIntro = print("It’s Slimer! He’ll eat your dinner and soak you with ectoplasm!")
        return self.enemyIntro
        
    def playerAttacksEnemy( self ):
        self.enemyHealth = self.getEnemyHealth()
        #self.getEnemyInfo(self.getEnemyName())
        print("{} currently has {} health.".format(self.getEnemyName(), self.getEnemyHealth()))
        r = random()
    
        if self.enemyHealth > 0:
            if r < 0.4:
                self.enemyHealth = self.enemyHealth - 10
                print("You shot {} with your proton pack, reducing their health by 10! They have {} health remaining.".format(self.getEnemyName(), self.enemyHealth))
            elif r >= 0.4 and r < 0.85:
                self.enemyHealth = self.enemyHealth - 20
                print("You shot {} with your proton pack, reducing their health by 20! They have {} health remaining.".format(self.getEnemyName(), self.enemyHealth))
            else:
                self.enemyHealth = self.enemyHealth - self.enemyHealth
                print("CRITICAL HIT! Your proton pack blasts a shot so powerful that {} is forced to retreat!".format(self.getEnemyName()))
        
        return self.enemyHealth        
        