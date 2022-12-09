from ursina import *

from inventory import *

class Tree(Button):
    def __init__(self,position = (0,0)):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = load_texture('assets/tree.png'),
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 1)
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                GiveItem("Holz", 2)
                destroy(self)