# [pyxel](https://github.com/kitao/pyxel)  
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
# Usage
## Code
### client.py
```python
from pyxel_server import pyxel_server
import pyxel

class App:
    def __init__(self):
        self.client = pyxel_server.client("127.0.0.1", "5000")
        pyxel.init(self.client.width, self.client.height, fps=self.client.fps)
        self.text = "Client text"
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.text = self.client.var("text")

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, round(self.client.height / 2), self.text, 7)

App()
```
### server.py
```python
from pyxel_server import pyxel_server

def update(self):
  self.variables["text"] = str(self.frame_count)
  
variables = {
    "text": "Server Text"
}

pyxel_server.server("127.0.0.1", "5000", 256, 144, 24, update, variables=variables)
```
## What will happen
When you press space in the client, it will get the server's text variable and the text on the screen will change to the server's `frame_count`.  
## What are they doing
### client.py
Imports necessary modules.  
###  - `__init__()`  
Initializes the client with the server `Host` and `Port` by getting necessary information including the width and height of the client.  
Initializes pyxel application with the client's recieved `self.client.width` and `self.client.height`.  
Sets local variable called `text` with some text.  
Runs pyxel application.  
###  - `update()`  
Checks if the space bar is pressed  
If pressed, it will set the local `text` variable to the server's `text` variable  
###  - `draw()`  
Clears screen  
Draws text from local `text` variable  
### server.py
Imports necessary modules.    
Creates a dictionary with needed variables for the server.  
Initializes the server to run on `Host` and `Port`, sets default pyxel `AppWidth`, `AppHeight` and `AppFPS`, server `update()` function to run local `update()`, and server variables with the `variables` dictionary. 
###  - `update()`
Sets server variable `text` to the current `frame_count`.  
# Used software
* [pyxel](https://github.com/kitao/pyxel)  
* [flask](https://flask.palletsprojects.com)  
* [requests](https://docs.python-requests.org)  
