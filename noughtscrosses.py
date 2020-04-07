import pygame
pygame.init()

#creates a window with a white background
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Noughts and Crosses")
bg = pygame.image.load("whitebg.png")


#all of the variables
global checkIt

global mousex
global mousey

global noughtsPlay
global crossPlay

global noughtsWin
global crossesWin
global draw

checkIt = False

noughtsPlay = False
crossPlay = False

noughtsWin = False
crossesWin = False
draw = False

#all of the lists 
crossesList = []
noughtsList = []


#the class of box
class box():
    #initialisation
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.clicked = False
        self.noughtsDraw = False
        self.crossesDraw = False
    

    #draws the box and if it's been clicked, the nought/cross
    def drawSelf(self): 
        pygame.draw.rect(win, (211,211,211), (self.x,self.y,100,100), 3)
        pygame.draw.rect(win, (255,255,255), (self.x,self.y,100,100), 0)
        if self.noughtsDraw == True:
            pygame.draw.circle(win, (169,169,169), (self.x + 50, self.y + 50), 40, 3)

        if self.crossesDraw == True:
            pygame.draw.line(win, (169,169,169), (self.x + 15 ,self.y + 15), (self.x + 85,self.y + 85),4)
            pygame.draw.line(win, (169,169,169), (self.x + 85 ,self.y + 15), (self.x + 15,self.y + 85),4)
            

    #checks if it has been clicked, by whom, and if it's a valid click
    def checkSelf(self):
        global checkIt
        global mousex
        global mousey
        global noughtsPlay
        
        
        if checkIt == True and mousex >= self.x and mousex <= self.x + 100 and mousey >= self.y and mousey <= self.y + 100 and self.clicked == False and noughtsPlay == True:
            self.noughtsDraw = True
            noughtsPlay = False
            self.clicked = True
            crossesPlay = True
            noughtsList.append(self.number)
            

        if checkIt == True and mousex >= self.x and mousex <= self.x + 100 and mousey >= self.y and mousey <= self.y + 100 and self.clicked == False and noughtsPlay == False:
            self.crossesDraw = True
            crossesPlay = False
            self.clicked = True
            noughtsPlay = True
            crossesList.append(self.number)



#a function to check who's turn it is and display their symbol accordingly
def checkPlayer():
    font = pygame.font.SysFont("couriernew", 30)
    if noughtsPlay == True and crossPlay == False and crossesWin == False and draw == False and noughtsWin == False:
        text = font.render("O's turn", 1, (0,0,0))
        win.blit(text, (430, 120))
    if noughtsPlay == False and crossesWin == False and draw == False and noughtsWin == False:
        text1 = font.render("X's turn", 1, (0,0,0))
        win.blit(text1, (430, 120))
            

#a function to check if noughts has won            
def checkNoughts():
    global noughtsList
    global noughtsWin
    for i in noughtsList:
        a1 = noughtsList.count('1')
        a2 = noughtsList.count('2')
        a3 = noughtsList.count('3')
        a4 = noughtsList.count('4')
        a5 = noughtsList.count('5')
        a6 = noughtsList.count('6')
        a7 = noughtsList.count('7')
        a8 = noughtsList.count('8')
        a9 = noughtsList.count('9')
        if a1 == 1 and a2 == 1 and a3 == 1:
            noughtsWin = True
            
        if a4 == 1 and a5 == 1 and a6 == 1:
            noughtsWin = True

        if a7 == 1 and a8 == 1 and a9 == 1:
            noughtsWin = True

        if a1 == 1 and a4 == 1 and a7 == 1:
            noughtsWin = True

        if a2 == 1 and a5 == 1 and a8 == 1:
            noughtsWin = True

        if a3 == 1 and a6 == 1 and a9 == 1:
            noughtsWin = True

        if a1 == 1 and a5 == 1 and a9 == 1:
            noughtsWin = True

        if a3 == 1 and a5 == 1 and a7 == 1:
            noughtsWin = True

        else:
            pass

#a function to check if crosses has won
def checkCrosses():
    global crossesList
    global crossesWin
    for i in crossesList:
        b1 = crossesList.count('1')
        b2 = crossesList.count('2')
        b3 = crossesList.count('3')
        b4 = crossesList.count('4')
        b5 = crossesList.count('5')
        b6 = crossesList.count('6')
        b7 = crossesList.count('7')
        b8 = crossesList.count('8')
        b9 = crossesList.count('9')
        if b1 == 1 and b2 == 1 and b3 == 1:
            crossesWin = True
            
        if b4 == 1 and b5 == 1 and b6 == 1:
            crossesWin = True

        if b7 == 1 and b8 == 1 and b9 == 1:
            crossesWin = True

        if b1 == 1 and b4 == 1 and b7 == 1:
            crossesWin = True

        if b2 == 1 and b5 == 1 and b8 == 1:
            crossesWin = True

        if b3 == 1 and b6 == 1 and b9 == 1:
            crossesWin = True

        if b1 == 1 and b5 == 1 and b9 == 1:
            crossesWin = True

        if b3 == 1 and b5 == 1 and b7 == 1:
            crossesWin = True

#a function to check if anyone has won or if there has been a draw and display the text accordingly
def checkWinner():
    font = pygame.font.SysFont("couriernew", 30)
    global draw
    global crossesWin
    global noughtsWin
    
    if crossesWin == True:
        text = font.render("Crosses Wins!!", 1, (0,0,0))
        win.blit(text, (375, 120))
    
        
        
        
    if noughtsWin == True:
        text = font.render("Noughts Wins!!", 1, (0,0,0))
        win.blit(text, (375, 120))
        
        
    
    else:
        if one.clicked == True and two.clicked == True and three.clicked == True and four.clicked == True and five.clicked == True and six.clicked == True and seven.clicked == True and eight.clicked == True and nine.clicked == True:
            text = font.render("Draw!!", 1, (0,0,0))
            win.blit(text, (450, 120))
            draw = True


            
        
#creates all the box objects
one = box('1',345,200)
two = box('2',450,200)
three = box('3',555,200)
four = box('4',345,305)
five = box('5',450,305)
six = box('6',555,305)
seven = box('7',345,410)
eight = box('8',450,410)
nine = box('9',555,410)


#draws the game window
def gameWindow():
    win.blit(bg, (0,0))
    font = pygame.font.SysFont("couriernew", 30)
    text = font.render("Katie's Noughts And Crosses Game", 1, (169,169,169))
    win.blit(text, (210, 40))
    
    one.drawSelf()
    one.checkSelf()

    two.drawSelf()
    two.checkSelf()

    three.drawSelf()
    three.checkSelf()

    four.drawSelf()
    four.checkSelf()

    five.drawSelf()
    five.checkSelf()

    six.drawSelf()
    six.checkSelf()

    seven.drawSelf()
    seven.checkSelf()

    eight.drawSelf()
    eight.checkSelf()

    nine.drawSelf()
    nine.checkSelf()
    
    checkNoughts()
    checkCrosses()
    checkWinner()
    checkPlayer()
    
    
#declares the first player - noughts    
noughtsPlay = True    

#main loop
run = True

while run:

    pygame.time.delay(100)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            

        #checks if the mouse has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN: 
            position = pygame.mouse.get_pos()
            mousex = position[0]
            mousey = position[1]
            checkIt = True
            
    #updates the display
    gameWindow()
    pygame.display.update()

    if draw == True or noughtsWin == True or crossesWin == True:
        gameWindow()
        pygame.display.update()
        run = False



while run ==  False:
    gameWindow()
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()





    
    
    
    
