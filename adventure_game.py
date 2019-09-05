# Maureen Landgraf
from random import random
from random import randrange
from enemy_class import Enemy
from player_class import Player
from graphics import *

def introText():
    print("The Ghostbusters have hired you as the fifth Ghostbuster,")
    print("but before they could show you the ropes, they were kidnapped")
    print("by Gozer the Gozerian! You must navigate the streets of New York")
    print("towards the Empire State Building where they're being held captive, ")
    print("catching ghosts with your trusty proton pack and ghost traps along the way.")
    print("But be careful! You only have a limited amount of energy in your proton pack!")
    print("Defeat any ghostly enemies in your way and save the Ghostbusters before Gozer destroys")
    print("the city and then the world!\n")
    
def inputName():
    name = input("Enter player's name: ")
    return name

#randomly initializes an enemy object to one of four enemies
def getEnemy():
    r = random()
    if r < 0.25:
        enemy = Enemy( "Gozer", 100 )
    elif r >= 0.25 and r < 0.5:
        enemy = Enemy( "Zuul", 50 )
    elif r >= 0.5 and r < 0.75:
        enemy = Enemy( "Stay-Puft Marshmallow Man", 80 )
    else:
        enemy = Enemy( "Slimer", 30 )
    return enemy

#creates 10 blocks for the player to move forward through
def stepForward( player ):
    stepsLeft = 10
    while stepsLeft > 0 and player.getProtonEnergy() > 0:
        takeStep = input( "Drive forward (y/n)? ")
        if takeStep == "y":
            stepsLeft = randomAction( player, stepsLeft )
            stepsLeft = stepsLeft - 1
        elif takeStep == "n":
            if random() > 0.5 and player.ghostsCollected > 0:
                player.ghostsCollected = player.ghostsCollected - 1
                print("You dawdled and one of your ghosts has escaped!")
                print("You now only have {} ghosts!".format(player.ghostsCollected))
            else:
                print("Keep moving forward, New York is depending on you!")
        else:
            print("Please enter y or n.")
        if stepsLeft > 0 and player.getProtonEnergy() > 0:
            print("The Empire State Building is now {} blocks ahead of you.".format( stepsLeft ))
    return stepsLeft

# function randomly selects an enemy, an amount of ghosts to capture, an amount of energy to lose, or amount of energy to gain
def randomAction( player, stepsLeft ):
    r = random()
    if r < 0.4:
        #create an enemy object - enemy will randomly be selected from the getEnemy() function
        print("A ghostly enemy approaches!")
        enemy = getEnemy()
        enemy.getEnemyInfo(enemy.getEnemyName())
        stepsLeft = fight( enemy, player, stepsLeft )
    elif r >= 0.4 and r < 0.5:
        player.loseEnergy()
    elif r >= 0.5 and r < 0.75:
        player.getGhosts()
    else:
        player.getExtraEnergy()
    return stepsLeft
 
# when fight function is randomly selected, a random enemy appears and deducts player's health until enemy or player is down to 0 
def fight( enemy, player, stepsLeft ):
    shouldYouAttack = input("Do you want to attack {}(y/n)? If not, you will have to move back 1 block: ".format(enemy.getEnemyName()))
    while shouldYouAttack == 'y' and enemy.getEnemyHealth() > 0 and player.getProtonEnergy() > 0:
        if enemy.getEnemyHealth() > 0 and player.getProtonEnergy() > 0:
            enemy.playerAttacksEnemy()
        if enemy.getEnemyHealth() > 0 and player.getProtonEnergy() > 0:
            player.enemyAttacksPlayer()
        if enemy.getEnemyHealth() <= 0:
            print("{} was defeated soundly! Onwards!".format(enemy.getEnemyName()))
            break
        if player.getProtonEnergy() <= 0:
            print("Oh no! Your proton pack is out of energy! You have nothing left to fight the ghosts with!")
            break
        shouldYouAttack = input("Attack again? (y/n): ")
    if shouldYouAttack == "n":
        stepsLeft = stepsLeft + 1
        print("You retreated to the previous block.")
    return stepsLeft

def winnerGraphic():
    win = GraphWin("Ghostbusters Adventure", 500, 500)
    win.setBackground('black')
    
    head = Circle(Point(250, 250), 100)
    head.setFill("white")
    head.draw(win)
    
    eye1 = Circle(Point(220, 220), 20)
    eye1.setOutline("black")
    eye1.draw(win)
    
    pupil1 = Circle(Point(220, 230), 10)
    pupil1.setOutline("black")
    pupil1.setFill("black")
    pupil1.draw(win)
    
    eye2 = Circle(Point(280, 220), 20)
    eye2.setOutline("black")
    eye2.draw(win)
    
    pupil2 = Circle(Point(280, 230), 10)
    pupil2.setFill("black")
    pupil2.draw(win)
    
    eyebrow1 = Line(Point( 200, 200), Point( 230, 190))
    eyebrow1.draw(win)
    
    eyebrow2 = Line(Point( 280, 190), Point( 310, 200))
    eyebrow2.draw(win)
    
    mouth = Polygon(Point( 200, 280), Point(300, 280), Point( 280, 320), Point( 220, 320))
    mouth.setFill("black")
    mouth.draw(win)
    
    tongue = Polygon(Point( 220, 320), Point( 240, 310), Point( 260, 310), Point( 270, 320))
    tongue.setFill("pink")
    tongue.draw(win)
    
    hat = Polygon(Point(160, 180), Point(115, 150), Point(180, 90), Point(300, 100), Point(285, 125))
    hat.setFill("white")
    hat.draw(win)
    
    hatStripe = Polygon(Point( 160, 180), Point(285, 125), Point( 290, 160), Point(160 , 210))
    hatStripe.setFill("navy")
    hatStripe.draw(win)
    
    pom = Circle(Point(180, 90), 10)
    pom.setFill("navy")
    pom.draw(win)
    
    tassle = Polygon(Point(110, 165), Point(100, 150), Point(175, 90), Point(165, 120))
    tassle.setFill('red')
    tassle.draw(win)
    
    text = Text( Point(220, 173), "STAY PUFT")
    text.setFill("white")
    text.setSize(9)
    text.draw(win)
    
    textWin = Text( Point( 250, 400), "YOU WIN!")
    textWin.setFill("white")
    textWin.setSize(30)
    textWin.setFace("courier")
    textWin.draw(win)
    
    win.getMouse()
    win.close()
    
def main():
    #display introductory text describing the game
    introText()
    
    #create a player object with parameters for the player's name (to be entered by player) and
    player = Player( inputName() )
    
    print("You hop into the Ecto-1 and see the Empire State Building 10 blocks ahead of you.")
    stepsLeft = stepForward( player )
    currentEnergy = player.getProtonEnergy()
    
    if currentEnergy > 0 and stepsLeft == 0:
        print("\nCongratulations! You have reached the Empire State Building and rescued the Ghostbusters!")
        print("FINAL STATS FOR {}: ".format(player.getPlayerName()))
        print("     Ghosts Caught: {}".format(player.getGhostsCollected()))
        print("     Proton Energy: {}".format(player.getProtonEnergy()))
        winnerGraphic()
        
    if currentEnergy <= 0:
        currentEnergy = 0
        print("\nGAME OVER")
        print("You and the rest of New York City have succumbed to this paranormal war. The world is doomed.")
        print("FINAL STATS FOR {}: ".format(player.getPlayerName()))
        print("     Ghosts Caught: {}".format(player.getGhostsCollected()))
        print("     Proton Energy: {}".format(currentEnergy))

main()