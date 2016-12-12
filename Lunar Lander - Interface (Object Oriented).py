''' interfaces.py
A module containing two interfaces for the lunar lander game.
The graphic lander interface allows the game to be played graphically, while the text lander
interface allows the game to be played by text only through the terminal.
'''

import sys
try: 
    import graphics 
except ImportError:
    sys.stderr.write("Couldn't import graphics.py module.\n") 
    sys.stderr.write("This is fine for Part I of the assignment.\n")
    sys.stderr.write("For Part II you should make sure that graphics.py" +
                                " is in the correct directory.\n")

class TextLanderInterface:
    '''Text-based interface for lander game. Use this one for testing'''

    def showInfo(self, lander):
        '''Display lander's status to user'''
        altitude = lander.getAltitude()
        velocity = lander.getVelocity()
        fuel = lander.getFuel()
        print("Altitude is", altitude, "meters.\nVelocity is", velocity, ".\nFuel left is", fuel)

    def getThrust(self):
        '''Get thrust amount from user. Returns thrust amount as an int.'''
        thrustAmountString = input("Thrust amount? ")
        if thrustAmountString == "":
            return 0
        return int(thrustAmountString)

    def showCrash(self):
        '''Display to user that we crashed'''
        print("Crash! Oh noes!")

    def showLanding(self):
        '''Display to user that we landed safely'''
        print("Hooray, the Eagle has landed!")

    def close(self):
        '''Close the interface'''
        print("Goodbye")

class GraphicLanderInterface:
    '''GraphicLanderInterface class is a graphical interface 
        for your lunar lander game. Used in part 2 of the assignment.'''

    def __init__(self):
        '''Constructor that initializes the graphics window
        and shapes that we will use for drawing things'''

        # initialize window
        self.win = graphics.GraphWin("Lunar Lander Game", 320, 500)
        # transform coordinates
        self.win.setCoords(0, -10, 300, 600)
        
        self.background = graphics.Image(graphics.Point(500, 550), "largeSpace.gif")
        self.background.draw(self.win)
        
        self.surfacePolygon = self.createSurface()
        self.surfacePolygon.draw(self.win)

        self.landerPolygon = None
        
        self.text = None   #used to store displayed information about the lander
        self.descriptors = None

    def showInfo(self, lander):
        '''This method gets the lander's info and displays them to the user. 
        Then a lander is drawn in the graphics window.'''
        self.text = graphics.Text(graphics.Point(80, 520), "")
        alt = lander.getAltitude()
        vel = lander.getVelocity()
        fuel = lander.getFuel()
        infoString = str(alt) + "                  " + str(vel) + "              " + str(fuel)
        self.text.setText(infoString)   #putting the lander's values into self.text
        self.text.setTextColor("white")
        self.text.setStyle("bold")
        self.text.draw(self.win)
        self.descriptors = graphics.Text(graphics.Point(85, 540), "Altitude       Velocity       Fuel")
        self.descriptors.setTextColor("white")
        self.descriptors.setStyle("bold")
        self.descriptors.draw(self.win)
        
        # if lander polygon is drawn, undraw it
        if self.landerPolygon:
            self.landerPolygon.undraw()
        self.landerPolygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, alt),
                graphics.Point(self.win.width/2 - 3, alt + 10),
                graphics.Point(self.win.width/2 + 3, alt + 10),
                graphics.Point(self.win.width/2 + 10, alt))
        self.landerPolygon.setFill("gray")
        self.landerPolygon.draw(self.win)

    def getThrust(self):
        '''This method waits for a user's mouse click then returns
        an integer as the thrust amount. User has the option of using 0-3 units of thrust'''
        thrust1Button = graphics.Rectangle(graphics.Point(10, 410), graphics.Point(60, 450))
        thrust1Button.setFill("red")   #makes each button easier to differentiate
        thrust1Button.draw(self.win)
        thrust1Text = graphics.Text(graphics.Point(35, 400), "1 Thrust")
        thrust1Text.setTextColor("white")
        thrust1Text.setStyle('bold')
        thrust1Text.draw(self.win)
        
        thrust2Button = graphics.Rectangle(graphics.Point(70, 410), graphics.Point(120, 450))
        thrust2Button.setFill("blue")
        thrust2Button.draw(self.win)
        thrust2Text = graphics.Text(graphics.Point(95, 400), "2 Thrust")
        thrust2Text.setTextColor("white")
        thrust2Text.setStyle('bold')
        thrust2Text.draw(self.win)
        
        thrust3Button = graphics.Rectangle(graphics.Point(10, 350), graphics.Point(60, 390))
        thrust3Button.setFill("yellow")
        thrust3Button.draw(self.win)
        thrust3Text = graphics.Text(graphics.Point(35, 340), "3 Thrust")
        thrust3Text.setTextColor("white")
        thrust3Text.setStyle('bold')
        thrust3Text.draw(self.win)
        
        noThrustButton = graphics.Rectangle(graphics.Point(70, 350), graphics.Point(120, 390))
        noThrustButton.setFill("black")
        noThrustButton.draw(self.win)
        noThrustText = graphics.Text(graphics.Point(95, 340), "No thrust")
        noThrustText.setTextColor("white")
        noThrustText.setStyle('bold')
        noThrustText.draw(self.win)     
        
        validClick = False
        while validClick == False:
            clickLocation = self.win.getMouse()
            clickX = clickLocation.getX()
            clickY = clickLocation.getY()
            if clickX >= 10 and clickX <= 60:  #checking which button the click's
                                               #coordinate matches
                if clickY >= 410 and clickY <= 450:
                    thrust1Text.undraw()
                    thrust2Text.undraw()
                    thrust3Text.undraw()
                    noThrustText.undraw()
                    self.text.undraw()
                    self.descriptors.undraw()
                    validClick = True  #a valid click is given, so the turn proceeds
                    return 1
                elif clickY >= 350 and clickY <= 390:
                    thrust1Text.undraw()
                    thrust2Text.undraw()
                    thrust3Text.undraw()
                    noThrustText.undraw()
                    self.text.undraw()
                    self.descriptors.undraw()
                    validClick = True 
                    return 3
            elif clickX >= 70 and clickX <= 120:
                if clickY >= 410 and clickY <= 450:
                    thrust1Text.undraw()
                    thrust2Text.undraw()
                    thrust3Text.undraw()
                    noThrustText.undraw()
                    self.text.undraw()
                    self.descriptors.undraw()
                    validClick = True
                    return 2
                elif clickY >= 350 and clickY <= 390:
                    thrust1Text.undraw()
                    thrust2Text.undraw()
                    thrust3Text.undraw()
                    noThrustText.undraw()
                    self.text.undraw()
                    self.descriptors.undraw()
                    validClick = True 
                    return 0


    def showCrash(self, lander):
        '''Crash message... displays an image of a crashed lunar lander and displays
        a graphical text to the user saying that the lander has crashed. Gives the user
        a score based on his / her performance.'''
        self.landerPolygon.undraw()
        self.landerPolygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 13, 0),
                graphics.Point(self.win.width/2 - 6, 10),
                graphics.Point(self.win.width/2 - 3, 10),
                graphics.Point(self.win.width/2 - 3, 0))
        self.landerPolygon = graphics.Image(graphics.Point(100, 150), "explosion.gif")
        self.landerPolygon.draw(self.win)
        #displays an image of an explosion to show the crash of the lander
        crash = graphics.Text(graphics.Point(150, 460), "Crash! Oh noes!")
        crash.setStyle("bold")
        crash.setSize(30)
        crash.setFace("helvetica")
        crash.setTextColor("white")
        crash.draw(self.win)
        fuel = lander.getFuel()
        velocity = lander.getVelocity()
        scoreCalc = int(fuel + (100 / (-1 * velocity)))   
        #self-derived formula for calculating a player's score. The higher the velocity,
        #the lower the score will be, (vel *-1 as vel will be negative upon reaching the surface).
        #Likewise, the more fuel left, the higher the score will be.
        scoreString = "Your overall score is: " + str(scoreCalc)
        score = graphics.Text(graphics.Point(150, 430), scoreString)
        score.setFill("red")
        score.draw(self.win)
        self.win.getMouse()
        if self.win.getMouse():
            self.win.close()

    def showLanding(self, lander):
        '''Landing message... displays a celebratory graphical text to inform the user that
        the lander has safely landed. Gives the user a score based on his / her performance.'''
        self.landerPolygon.undraw()
        self.landerPolygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, 0),
                graphics.Point(self.win.width/2 - 3, 10),
                graphics.Point(self.win.width/2 + 3, 10),
                graphics.Point(self.win.width/2 + 10, 0))
        self.landerPolygon.setFill("gray")
        self.landerPolygon.draw(self.win)
        safe = graphics.Text(graphics.Point(150, 330), "Hooray,\n the Eagle has landed!")
        safe.setStyle('bold')
        safe.setTextColor('red')
        safe.setSize(30)
        safe.setFace('helvetica')
        fuel = lander.getFuel()
        velocity = lander.getVelocity()
        scoreCalc = int(fuel + (100 / (-1 * velocity)) + 20)   #bonus 20 points for
                                                               #successful landing
        scoreString = "Your overall score is: " + str(scoreCalc)
        score = graphics.Text(graphics.Point(150, 190), scoreString)
        score.setFill("red")
        score.draw(self.win)
        safe.draw(self.win)
        self.win.getMouse()
        if self.win.getMouse():  #waits for user mouse click before continuing
            self.win.close()

    def close(self):
        self.win.close()

    def createSurface(self):
        '''Draws the surface of the moon'''
        circ = graphics.Circle(graphics.Point(160, -795), 800)  #draws a curved moon
                                                                #surface to look more realistic
        circ.setFill("gray")
        return circ