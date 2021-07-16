# [Pyxel](https://github.com/kitao/pyxel)  
# [Reference](https://floppidisk.github.io/pyxel_server/reference)  
# [Contributing](https://floppidisk.github.io/pyxel_server/contribute)  
# Install
```
pip install pyxel-server
```  
or
```
https://pypi.org/project/pyxel-server/
```
# Example
## Code
### client.py
```python
import pyxel
from pyxel_server import client

class App:
    def __init__(self):
        self.address = input("Server Address: ")
        self.port = input("Server Port: ")
        self.clientPort = input("Client Port: ")
        self.username = input("Choose Username: ")
        self.Updating = False
        self.points = 0
        # Connects to server and runs pyxel app
        self.client = client.run(self.address, self.port, False, "127.0.0.1", self.clientPort)
        self.client.connect(self.username)
        self.client.appinfo()
        pyxel.init(self.client.width, self.client.height, caption=self.username, fps=self.client.fps, quit_key=pyxel.KEY_F2)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.Updating = True
        # Custom Quit Key, Force quit is F2
        if pyxel.btnr(pyxel.KEY_ESCAPE):
            self.client.disconnect()
            pyxel.quit()
        # Checks if button is pressed and sends to server
        self.client.btnp(pyxel.KEY_SPACE)
        # Every half second it will get the user's points
        if pyxel.frame_count % round(pyxel.DEFAULT_FPS / 2) == 0:
            self.points = self.client.getLocalVar("points")
        self.Updating = False
    def draw(self):
        if not self.Updating:
            # Clear screen
            pyxel.cls(0)
            # Draw score
            pyxel.text(0, 0, str(self.points), 10)
            # Render all objects
            self.client.renderAll()
App()
```
### server.py
```python
from pyxel_server import pyxelobj, server
import pyxel
import random

def update(self):
    # If the dot is not activated
    if not self.variables.activated:
        # Create a new one and send it
        self.variables.x = random.randrange(0, 256)
        self.variables.y = random.randrange(0, 144)
        obj = pyxelobj.obj(pyxelobj.new("dot", self.variables.x, self.variables.y, 0, 0, [[7]]))
        self.variables.activated = True
        self.sendObj(obj)
    # Loops through every single user
    for Username, User in self.Users.__getallusers__().items():
        # If user pressed space
        if User.input.get(str(pyxel.KEY_SPACE)) and self.variables.visible:
            # Add 1 point to user
            User.variables.points += 1
            # Set the dot to be not activated
            self.variables.pressed = False
            User.input[str(pyxel.KEY_SPACE)] = False
            
LocalVariables = {
    "points": 0
}
GlobalVariables = {
    "pressed": False,
    "x": random.randrange(0, 256),
    "y": random.randrange(0, 144)
}
server.run("127.0.0.1", "5000", 256, 144, 12, update,LocalVariables=LocalVariables, GlobalVariables=GlobalVariables)
```
## What will happen
This is a game of who pressed space first when the dot apears.
## [More](https://github.com/FloppiDisk/pyxel_server/tree/main/examples)
# Used software
* [python3](https://python.org)
* [pyxel](https://github.com/kitao/pyxel)  
* [flask](https://flask.palletsprojects.com)  
* [requests](https://docs.python-requests.org)  
