from ursina import *

from inventory import *

class Player(Button):
    def __init__(self,position,texture):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 0.9)

        self.timer = 0
        self.textureCount = 0
        self.textCount = -1

    def input(self,key):
        if key == 'left mouse down':
            #self.timer = 60
            print()

    def update(self):
        #if(self.atktimer > 0):
        #    self.texture = load_texture('assets/FlowerPot/FlowerPot1.png')
        #    self.atktimer -= 1
        #else:
        #    self.texture = load_texture('assets/FlowerPot/FlowerPot2.png')
        
        self.timer += 1

        if self.timer == 10:
            self.timer  = 0
            self.textureCount += 1
            if self.textureCount == 5:
                self.textureCount = 1
            self.texture = load_texture('assets/Player/Idle/Idle' + str(self.textureCount) + '.png')