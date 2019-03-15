from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay

WINDOWWIDTH=1280
WINDOWHEIGHT=720 

class CarSprite():
    def __init__(self):
        self.carSprite_image = pyglet.image.load('car_sprite_resized10percent.png')
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, 0,0)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
    def draw(self):
        self.carSprite.draw()
    def updateX(self,value):
        value += self.carSprite.x
        self.carSprite.update(x=value)
    def updateY(self,value):
        value += self.carSprite.y
        self.carSprite.update(y=value)
    

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        glClearColor(1,1.0,1.0,1)
        self.fps_display = FPSDisplay(self)
        self.car = CarSprite()
        print(self.car.x)

    def on_key_press(self, symbol,modifiers):
        if symbol == key.UP:
            print('accelerate')
            self.car.updateX(20)
        elif symbol == key.DOWN:
            print('reverse')
            self.car.updateX(-20)
        elif symbol == key.LEFT:
            print('turn left')
            self.car.updateY(20)
            self.car.y +=20
        elif symbol == key.RIGHT:
            print('turn right')
            self.car.updateY(-20)
        elif symbol == key.ESCAPE:
            pyglet.app.exit()
        else:
            print('key code '+str(symbol))

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            print('release accelerate')
        elif symbol == key.DOWN:
            print('release reverse')
        elif symbol == key.LEFT:
            print('release turn left')
        elif symbol == key.RIGHT:
            print('release turn right')
        else:
            print('release key code '+str(symbol))

    def on_draw(self):
        self.clear()
        self.car.draw()
        self.fps_display.draw()

    def update(self, dt):
        pass   

if __name__ == "__main__":
    window = MyWindow(WINDOWWIDTH,WINDOWHEIGHT, "DRIFT AI", resizable=True, vsync =True)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()