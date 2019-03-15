from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
class Triangle:
    def __init__(self): 
        self.vertices = pyglet.graphics.vertex_list(3,  ('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.0,0.5,0.0]),('c3B',[100,200,200, 200,101,100, 100,250,100]))

class Quad:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0,1,2,2,3,0],
        ('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]),
        ('c3f',[1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,1.0,1.0]))

class Quad3:
    def __init__(self):
        self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.color = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,1.0,1.0]
        self.indeces = [0, 1, 2, 0, 2, 3]
    def render(self):
        self.vertices = pyglet.graphics.draw_indexed(4,GL_TRIANGLES,self.indeces, ('v3f', self.vertex), ('c3f',self.color))

# class Sprite:
#     def __init__(self):
#         self.sprite_image = pyglet.image.load('car_sprite.jpg')
#         self.sprite= pyglet.sprite.Sprite(self.sprite_image, x=20,y=20)
#     def draw(self):
#         self.sprite.draw()
class Quad2:
    def __init__(self):
        self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.color = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,1.0,1.0]
        self.indeces = [0,1,2,2,3,0]
        self.vertices = pyglet.graphics.vertex_list_indexed(4,self.indeces, ('v3f', self.vertex), ('c3f',self.color))
class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        #self.set_minimum_size(400,300)
        glClearColor(1,1.0,1.0,1)
        self.fps_display = FPSDisplay(self)
        self.image = pyglet.image.load('car_sprite.jpg')
        #self.sprite = pyglet.sprite.Sprite(self.image, -self.width/5, -self.height/5)
        self.sprite = pyglet.sprite.Sprite(self.image, 0, 0)
        self.sprite.scale = .1
    def on_key_press(self, symbol,modifiers):
        if symbol == key.UP:
            print('accelerate')
            self.sprite.x +=20
        elif symbol == key.DOWN:
            print('reverse')
            self.sprite.x -=20
        elif symbol == key.LEFT:
            print('turn left')
            self.sprite.y +=20
        elif symbol == key.RIGHT:
            print('turn right')
            self.sprite.y -=20
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
        self.sprite.draw()
        self.fps_display.draw()


    # def on_resize(self, width, height):
    #     glViewport(0,0,width,height)
    
    def update(self, dt):
        #self.sprite.x +=1
        #print('update')
        pass   

if __name__ == "__main__":
    window = MyWindow(1280,720, "My Pyglet Window", resizable=True, vsync =True)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()