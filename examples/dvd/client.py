import pyxel
import pyxel_server
from threading import Thread

class App:
    def __init__(self):
        #Configure host & port
        self.client = pyxel_server.client(Host="127.0.0.1", Port="5000")
        #Same as pyxel.init() but will sync to server's client defaults
        pyxel.init(width=self.client.width, height=self.client.height, fps=self.client.fps, caption="NO DISC")
        #Get json from route
        request = self.client.get(Route="/dvdinfo")
        #Set variables with the json
        self.x = request["x"]
        self.y = request["y"]
        self.addX = request["addX"]
        self.addY = request["addY"]
        self.color = request["color"]
        #Minus width & border with dvd-width & dvd-height so the DVD logo is always visible
        self.width = pyxel.width - request["dvd-width"]
        self.height = pyxel.height - request["dvd-height"]
        #Variable to make sure pyxel won't draw until update is finished
        self.finishUpdate = False
        #Loads DVD asset
        pyxel.load("assets/dvd.pyxres")
        #Runs application
        pyxel.run(self.update, self.draw)

    def sync(self):
        #Gets server data and synchronizes with client data
        request = self.client.get(Route="/dvdinfo")
        self.x = request["x"]
        self.y = request["y"]
        self.addX = request["addX"]
        self.addY = request["addY"]
        self.color = request["color"]

    def update(self):
        #Disables draw function
        self.finishUpdate = False
        #If 0.5 second is passed
        if pyxel.frame_count % round(pyxel.DEFAULT_FPS / 2) == 0:
            #This may take time so it is ran in a seperate thread
            Thread(target = self.sync).start()
        else:
            #Else do local DVD bouncing logic
            #The reason why is so the output is as smooth as possible
            #And every second it will resynchronize with the server to make it as accurate
            #If touching border
            if self.x == self.width or self.y == self.height or self.y == 0 or self.x == 0:
                #Set direction opposite to the border
                if self.x == self.width:
                    self.addX = -1
                if self.y == self.height:
                    self.addY = -1
                if self.y == 0:
                    self.addY = 1
                if self.x == 0:
                    self.addX = 1  
                if self.color == 15:
                    self.color = 3
                else:
                    self.color += 1
            #Add addX & addY to x & y
            self.y += self.addY
            self.x += self.addX
        #Enables draw function
        self.finishUpdate = True

    def draw(self):
        #Makes sure pyxel won't draw until update is finished
        if self.finishUpdate:
            #Clear screen
            pyxel.cls(0)
            #Reset dvd image color
            pyxel.pal()
            #Color dvd image with current color
            pyxel.pal(7, round(self.color))
            #Place image on screen
            pyxel.blt(self.x, self.y, 0, 0, 0, 24, 14)
#Runs App.__init__()
App()
