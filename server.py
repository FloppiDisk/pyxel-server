import pyxserver

def init(self):
#Custom initialization script
    self.variables["width"] = self.AppWidth - self.variables["dvd-width"]
    self.variables["height"] = self.AppHeight - self.variables["dvd-height"]

def web(self, app):
#Custom flask routes
    @app.route("/dvdinfo")
    def dvdInfo():
    #Returns needed variables
        return {
            "x": self.variables["x"],
            "y": self.variables["y"],
            "addX": self.variables["addX"],
            "addY": self.variables["addY"],
            "color": self.variables["color"],
            "dvd-width": self.variables["dvd-width"],
            "dvd-height": self.variables["dvd-height"]
        }

def update(self):
#DVD bouncing logic
    #If touching border
    if self.variables["x"] == self.variables["width"] or self.variables["y"] == self.variables["height"] or self.variables["y"] == 0 or self.variables["x"] == 0:
        #Set direction opposite to the border
        if self.variables["x"] == self.variables["width"]:
            self.variables['addX'] = -1
        if self.variables["y"] == self.variables["height"]:
            self.variables["addY"] = -1
        if self.variables["x"] == 0:
            self.variables["addX"] = 1  
        if self.variables["y"] == 0:
            self.variables["addY"] = 1
        if self.variables["color"] == 15:
            self.variables["color"] = 3
        else:
            self.variables["color"] += 1
    #Add addX & addY to x & y
    self.variables["y"] += self.variables["addY"]
    self.variables["x"] += self.variables["addX"]


#All of the variables needed for the server
variables = {
    "x": 0,
    "y": 0,
    "addX": 0,
    "addY": 0,
    "color": 3,
    "dvd-width": 24,
    "dvd-height": 14
}

pyxserver.server(Host="127.0.0.1", Port="5000", AppWidth=256, AppHeight=144, AppFPS=24, UpdateScript=update, WebScript=web, InitScript=init, variables=variables)