from pyxel_server import pyxelobj, server
import pyxel
from flask import request
from json import load as json_load
from json import loads as json_loads

def web(self, app):
    @app.route("/check/<user>", methods=["POST"])
    def ping(user: str):
        # saves all post data into variable
        incoming = json_loads(request.data)
        # if user exists
        if hasattr(self.Users, user):
            Client = getattr(self.Users, user)
            # if key matches server saved key
            if Client.key == incoming.get("key"):
                # return success
                self.webhost.send({
                    "status": True
                }, incoming.get("return-address"))
            else:
                #if not, return error
                self.webhost.send({
                    "status": "KEY_INVALID"
                }, incoming.get("return-address"))
        else:
            #if does not exist, return error
            self.webhost.send({
                "status": "USER_INVALID"
            }, incoming.get("return-address"))
        return '', 204

def init(self):
    with open("user.pyxelobj") as UserTemplate:
        self.UserTemplate = json_load(UserTemplate)

def update(self):
    for Username, User in self.Users.__getallusers__().items():
        if not User.input.get(str(pyxel.KEY_UP)) and not User.input.get(str(pyxel.KEY_DOWN)):
            User.variables.addY = 0
        else:
            if User.input.get(str(pyxel.KEY_UP)):
                User.variables.addY = -1
            if User.input.get(str(pyxel.KEY_DOWN)):
                User.variables.addY = 1
        if not User.input.get(str(pyxel.KEY_LEFT)) and not User.input.get(str(pyxel.KEY_RIGHT)):
            User.variables.addX = 0
        else:
            if User.input.get(str(pyxel.KEY_LEFT)):
                User.variables.addX = -1
            if User.input.get(str(pyxel.KEY_RIGHT)):
                User.variables.addX = 1
        User.variables.x += User.variables.addX
        User.variables.y += User.variables.addY
        if self.frame_count % round(self.AppFPS / 2) == 0:
            UserObject = pyxelobj.obj(self.UserTemplate)
            UserObject.name = Username
            UserObject.x = User.variables.x
            UserObject.y = User.variables.y
            UserObject.addX = User.variables.addX
            UserObject.addY = User.variables.addY
            self.sendObj(UserObject)

LocalVariables = {
    "x": 0,
    "y": 0,
    "addX": 0,
    "addY": 0
}

GlobalVariables = {
    "players": {}
}

server.run("127.0.0.1", "5000", 256, 144, 12, update, WebScript=web, InitScript=init ,LocalVariables=LocalVariables)
