# Pyxel Server
A simple to use API for integration between your [Pyxel](https://github.com/kitao/pyxel) games with servers.  
![preview](https://github.com/FloppiDisk/pyxel_server/raw/main/preview.gif?raw=true)
# Note
Documentation is not finished yet, please do `pip install pyxel-server==0.0.2` instead if you depend on the documentation.  
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
# Contributing
## Issues and Suggestions
Submit the issue or suggestion using the issue tracker, make sure it has not been repeated.  
### Issues
It should include the os, error, python modules used, python version and other relevant information.  
### Suggestions
It should include sample usages, mock-ups and other relevant information.  
## Patches, Feature implementations, and Optimizations
Please submit it in a pull request, issues should be listed if it is a fix.  
  Note: All pull requests submitted are licensed under the [MIT License](https://github.com/FloppiDisk/pyxel_server/blob/main/LICENSE)  
# Reference
Note: `pyxel_server`'s intended features are not fully implemented yet.
## server
### System
* `run(Host, Port, AppWidth, AppHeight, AppFPS, UpdateScript, [WebScript], [InitScript], [Variables])`  
Initializes the server and runs it.  
`Host`: The ip or domain of the server. e.g. `Host="127.0.0.1"`  
`Port`: The port to be opened in the `Host`. e.g. `Port="5000"`  
`AppWidth`: The width of the client's window when connected. e.g. `AppWidth=256`  
`AppHeight`: The height of the client's window when connected. e.g. `AppHeight=144`  
`AppFPS`: The FPS of the client's window when connected. e.g. `AppFPS=24`  
`UpdateScript`: The function to run every 1/`AppFPS`. e.g. `UpdateScript=update`  
  Note: The function must have the parameter `self`.  
`WebScript`: The custom flask events and routes. e.g. `WebScript=web`  
  Note: The function must have the parameter `self` & `app`.  
`InitScript`: The custom initialization function that will be called when `server()` is called. e.g. `InitScript=init`  
  Note: The function must have the parameter `self`.  
`Variables`: A dictionary of variables needed. e.g. `Variables={"Name": "Value"}`  
### Connection
* `sendObj(obj)`  
Converts obj to a json format and sends to all of the clients connected.  
`obj`: The `pyxelobj.obj` e.g. `obj=pyxelobj.obj()`  
### Data  
* `variables`  
A class of all of the global variables.  
  Note: The class will not be created if no global variables are specified in `self.run()`  
e.g.  
`variables.Name = "Value"`  
### Users  
* `Users.__getuser__(user)`  
Returns the User's class.  
`user`: The name of the user e.g. `user="Name"`  
* `Users.__getallusers__()`  
Returns all of the Users in a dictionary in a format like this: `{"Name": <Class>, "Name": <Class>, ...}`  
### User
* `User.variables`
A class of all of the user's variables.  
* `User.key`
The user's key.  
* `User.input`  
A dictionary of all of the keys pressed in a format like this: `{"Button Number": Bool, "Button Number": Bool, ...}`  
  Note: In the client, you must use `btnp(button)` for `User.input` to update.  
## client
### Connection
* `run(Host, Port)`  
Initializes the client with necessary information.  
`Host`: The ip or domain of the server. e.g. `Host="127.0.0.1"`  
`Port`: The port to be opened in the `Host`. e.g. `Port="5000"`  
  Note: You must run this command before anything that needs to use the `client`.  
* `connect(Username)`  
Connects the client to the necessary information.  
`User`: The username e.g. `User="Name"`  
  Note: You must run this command after `run` before using anything from the `client`.  
* `request.post(Route, json)`  
Posts data to a specified route and returns json back.  
`Route`: The path to post e.g. `Route="/var"`  
`json`: The json to post to the `Route` e.g. `json={"Name": "Value"}`  
### Data
* `getGlobalvar(Variable, [Value])`  
Returns & optionaly changes a global variable from the server.  
`Variable`: The variable name e.g. `Variable="Name"`  
`Value`: The value of variable e.g. `Value="Value"`  
  Note: The variable will be changed before it returns.  
* `getLocalvar(Variable, [Value])`  
Returns & optionaly changes a local variable only accessible to the client from the server.  
`Variable`: The variable name e.g. `Variable="Name"`  
`Value`: The value of variable e.g. `Value="Value"`  
  Note: The variable will be changed before it returns.  
### Input
* `btnp(button)`  
Checks for a button press [(see pyxel documentation)](https://github.com/kitao/pyxel#input) then sends result to the server and returns result  
`button`: The button to press e.g. `button=pyxel.KEY_SPACE`  
* `btnr(button)`  
Checks for a button release [(see pyxel documentation)](https://github.com/kitao/pyxel#input) then sends result to the server and returns result  
`button`: The button to press e.g. `button=pyxel.KEY_SPACE`  
### Objects  
* `renderAll()`  
Renders all of the objects in `client.objects`  
* `addObject(obj)`  
Adds an object to `client.objects`  
`obj`: The `pyxelobj.obj` e.g. `obj=pyxelobj.obj()`  
* `addObject(objname)`  
Removes an object from `client.objects`  
* `predict(obj)`  
Predicts an object's next location by adding `obj.addX` to `obj.x` and `obj.addY` to `obj.y`  
`obj`: The `pyxelobj.obj` e.g. `obj=pyxelobj.obj(json)`  
Removes an object from `client.objects`  
`objname`: The name of the object to remove e.g. `objname="Name"`  
# Used software
* [python3](https://python.org)
* [pyxel](https://github.com/kitao/pyxel)  
* [flask](https://flask.palletsprojects.com)  
* [requests](https://docs.python-requests.org)  
