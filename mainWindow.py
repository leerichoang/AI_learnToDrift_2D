from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay

WINDOWWIDTH=1280
WINDOWHEIGHT=720 

class CarSprite():
    def __init__(self):
        self.carSprite_image = pyglet.image.load('car_sprite_resized10percent.png')
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, 500,500)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
        self.theta = self.carSprite.rotation
    def draw(self):
        self.carSprite.draw()
    
    def getX(self):
        self.x = self.carSprite.x
        return self.x
    def getY(self):
        self.y = self.carSprite.y
        return self.y
    def getTheta(self):
        self.theta = self.carSprite.rotation
        return self.theta

    def updateX(self,value):
        value += self.getX()
        self.carSprite.update(x=value)
    def updateY(self,value):
        value += self.getY()
        self.carSprite.update(y=value)
    def updateTheta(self,degree):  
        degree += self.getTheta()
        self.carSprite.update(rotation=degree)


    

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        glClearColor(1,1.0,1.0,1)
        self.fps_display = FPSDisplay(self)
        self.car = CarSprite()
        print(self.car.theta)
        self.key_handler = key.KeyStateHandler()

    # def on_key_press(self, symbol,modifiers):
    #     if symbol == key.MOTION_UP:
    #         print('accelerate')
    #         self.car.updateX(20)
    #     elif symbol == key.MOTION_DOWN:
    #         print('reverse')
    #         self.car.updateX(-20)
    #     elif symbol == key.MOTION_LEFT:
    #         print('turn left')
    #         #self.car.updateY(20)
    #         self.car.updateTheta(-2)
    #     elif symbol == key.MOTION_RIGHT:
    #         print('turn right')
    #         #self.car.updateY(-20)
    #         self.car.updateTheta(2)
    #     elif symbol == key.ESCAPE:
    #         pyglet.app.exit()
    #     else:
    #         print('key code '+str(symbol))

    # def on_key_release(self, symbol, modifiers):
    #     if symbol == key.UP:
    #         print('release accelerate')
    #     elif symbol == key.DOWN:
    #         print('release reverse')
    #     elif symbol == key.LEFT:
    #         print('release turn left')
    #     elif symbol == key.RIGHT:
    #         print('release turn right')
    #     else:
    #         print('release key code '+str(symbol))

    def on_draw(self):
        self.clear()
        self.car.draw()
        self.fps_display.draw()


    def update(self, dt):
        if self.key_handler[key.LEFT]:
            print('turn left')
            #self.car.updateY(20)
            self.car.updateTheta(-2)
        if self.key_handler[key.RIGHT]:
            print('turn right')
            #self.car.updateY(-20)
            self.car.updateTheta(2)

if __name__ == "__main__":
    window = MyWindow(WINDOWWIDTH,WINDOWHEIGHT, "DRIFT AI", resizable=True, vsync =True)
    window.push_handlers(window.key_handler)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()