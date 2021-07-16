import pyxel
from datetime import datetime
from pyxel_server import client
from threading import Thread

class App:
    def __init__(self):
        self.address = input("Server Address: ")
        self.port = input("Server Port: ")
        self.clientPort = input("Client Port: ")
        self.username = input("Choose Username: ")
        self.Updating = False
        self.Requesting = False
        self.x = 0
        self.y = 0
        self.addX = 0
        self.addY = 0
        self.client = client.run(self.address, self.port, False, "127.0.0.1", self.clientPort)
        self.client.connect(self.username)
        self.client.appinfo()
        request = self.client.request.post("/check/" + self.username, json={"key": self.client.key})
        self.connection = str(request["status"]) + " Last Checked: " + str(datetime.now().strftime("%H:%M:%S"))
        pyxel.init(self.client.width, self.client.height, caption=self.username, fps=self.client.fps, quit_key=pyxel.KEY_F2)
        pyxel.run(self.update, self.draw)

    def sync(self):
        self.Requesting = True
        self.client.getLocalVar("x", Value=self.x)
        self.client.getLocalVar("y", Value=self.y)
        self.Requesting = False

    def input(self):
        if self.client.btnp(pyxel.KEY_UP):
            self.addY = -1.25
        if self.client.btnp(pyxel.KEY_DOWN):
            self.addY = 1.25
        if (self.client.btnr(pyxel.KEY_UP) and not pyxel.btn(pyxel.KEY_DOWN)) or (self.client.btnr(pyxel.KEY_DOWN) and not pyxel.btn(pyxel.KEY_UP)):
            self.addY = 0
        if self.client.btnp(pyxel.KEY_LEFT):
            self.addX = -1.25
        if self.client.btnp(pyxel.KEY_RIGHT):
            self.addX = 1.25
        if (self.client.btnr(pyxel.KEY_LEFT) and not pyxel.btn(pyxel.KEY_RIGHT)) or (self.client.btnr(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT)):
            self.addX = 0

    def update(self):
        self.Updating = True
        if pyxel.btnr(pyxel.KEY_ESCAPE):
            self.client.disconnect()
            pyxel.quit()

        if pyxel.frame_count % round(pyxel.DEFAULT_FPS / 2) == 0 and not self.Requesting:
            Thread(target=self.sync()).start()

        self.input()

        self.x += self.addX
        self.y += self.addY
        for objname in self.client.objects.keys():
            self.client.predict(self.client.objects[objname])
        if self.client.btnr(pyxel.KEY_SPACE):
                if not self.status == "Unscynced":
                    request = self.client.post("/deinit/" + self.username, json={"key": self.client.key}).json()
                    self.connection = str(request["status"]) + " Last Checked: " + str(datetime.now().strftime("%H:%M:%S"))

        if self.client.btnr(pyxel.KEY_R):
                request = self.client.post("/check/" + self.username, json={"key": self.client.key})
                self.connection = str(request["status"]) + " Last Checked: " + str(datetime.now().strftime("%H:%M:%S"))
        self.Updating = False


    def draw(self):
        if not self.Updating:
            pyxel.cls(0)
            pyxel.text(0, 0, "Key: " + str(self.client.key), 5)
            pyxel.text(0, 10, "Connected: " + str(self.connection), 5)
            self.client.renderAll()
App()
