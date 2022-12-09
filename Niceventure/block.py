from ursina import *

class Block(Entity):
    def __init__(self,position = (0,-2,0),color = color.color(120,3,1),texture = 'box'):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = texture,
        color = color,
        scale = 1)
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                GiveItem("Holz", 2)
                destroy(self)