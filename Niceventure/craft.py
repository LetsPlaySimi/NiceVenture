from ursina import *

from inventory import *

class Craft(Button):
    def __init__(self,key = held_keys,position = (0,0),req = ["TestItem","TestItem"], reqCount = [1,1], result = "TestItemResult", resultCount = 1):
        super().__init__(
        parent = scene,
        position = position,
        model = 'quad',
        origin_y = 0.5,
        texture = load_texture('assets/Holzschwert.png'),
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 1)

        self.req = req
        self.reqCount = reqCount
        self.result = result
        self.resultCount = resultCount

    def input(self,key = held_keys):
        error = False
        if self.hovered:
            if key == 'left mouse down':
                for i in range(0,len(self.req)):
                    if not CheckItems(self.req[i],self.reqCount[i]):
                        error = True
                if not error:
                    for i in range(0,len(self.req)):
                        RemoveItems(self.req[i],self.reqCount[i])
                    GiveItem(self.result,self.resultCount)
                    destroy(self)