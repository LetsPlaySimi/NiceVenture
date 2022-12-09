from ursina import *

class Item(Entity):
    def __init__(self,position = (0,0),texture = ''):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 0.5)
