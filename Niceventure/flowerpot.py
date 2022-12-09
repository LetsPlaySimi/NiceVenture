from ursina import *

from inventory import *

class FlowerPot(Button):
    def __init__(self,position,texture):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 1)

        self.timer = 0
        self.textureCount = 0
        self.textCount = -1
        self.txt = ""
        self.destroytxt = 1
        self.kompliment = ["Du siehst heute aber gut aus!","Ich mag dich!","Du strahlst wie eine Sonne!"]

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self.txt)

                self.textCount += 1

                if self.textCount == 3:
                    self.textCount = 0

                self.txt = Text(text=self.kompliment[self.textCount],position = (-0.5,0))

    def update(self):
        self.timer += 1

        if self.timer == 20:
            self.timer  = 0
            self.textureCount += 1
            if self.textureCount == 5:
                self.textureCount = 1
            self.texture = load_texture('assets/FlowerPot/FlowerPot' + str(self.textureCount) + '.png')
            self.destroytxt += 1
            if self.destroytxt == 10:
                destroy(self.txt)
                self.destroytxt = 1