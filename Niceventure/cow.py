from ursina import *

from inventory import *

class Cow(Button):
    def __init__(self,position = (0,0)):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = load_texture('assets/Cow1.png'),
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 1)

        self.timer = 1
        self.seconds = 0

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                GiveItem("Rohes Rindfleisch", 1)
                destroy(self)

    def update(self):
        self.timer += 1

        if self.timer == 21:
            self.timer = 1
            self.seconds += 1
            if self.seconds == 8:
                self.seconds = 0
        elif self.seconds == 0:
            self.texture = load_texture('assets/Cow1.png')
        elif self.seconds == 2:
            self.position = (0,-1)
        elif self.seconds == 3:
            self.position = (1,-1)
        elif self.seconds == 5:
            self.texture = load_texture('assets/Cow2.png')
        elif self.seconds == 6:
            self.position = (0,-1)
        elif self.seconds == 7:
            self.position = (-1,-1)