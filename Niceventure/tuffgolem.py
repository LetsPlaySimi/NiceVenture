from ursina import *

from inventory import *

class TuffGolem(Button):
    def __init__(self,position = (0,0)):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = load_texture('assets/TuffGolem1.png'),
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 1)

        self.timer = 1
        self.seconds = -2

    def update(self):
        self.timer += 0.5

        if self.timer == 21:
            self.timer = 1
            self.seconds += 1
            if self.seconds == 10:
                self.seconds = -2
        elif self.seconds == -2:
            self.texture = load_texture('assets/TuffGolem2.png')
        elif self.seconds == 2:
            self.position = (-5,-1)
        elif self.seconds == 3:
            self.position = (-4,-1)
        elif self.seconds == 7:
            self.texture = load_texture('assets/TuffGolem1.png')
        elif self.seconds == 8:
            self.position = (-5,-1)
        elif self.seconds == 9:
            self.position = (-6,-1)