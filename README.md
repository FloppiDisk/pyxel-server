# pyxserver
A simple to use API for integration between pyxel games and servers.  
![Preview](https://github.com/FloppiDisk/pyxserver/blob/main/preview.gif?raw=true)


# Reference
Note: Reference is not finished yet.
## Server
* `server(Host, Port, AppWidth, AppHeight, AppFPS, UpdateScript, \[WebScript\], \[InitScript]\, \[Variables\])`  
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
## Client
* `client(Host, Port)`
`Host`: The ip or domain of the server. e.g. `Host="127.0.0.1"`  
`Port`: The port to be opened in the `Host`. e.g. `Port="5000"`  
## Client
