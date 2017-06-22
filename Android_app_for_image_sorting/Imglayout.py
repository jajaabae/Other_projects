from kivy.uix.floatlayout import FloatLayout
#from kivy.graphics import Color, Rectangle
from kivy.graphics import Rectangle


from gm.get_background_color import get_background_color

class Imglayout(FloatLayout):

    def __init__(self,**args):
        super(Imglayout,self).__init__(**args)

        with self.canvas.before:
            get_background_color() #Color(1,1,1,1) #Color(0,0,0,0)
            self.rect=Rectangle(size=self.size,pos=self.pos)

        self.bind(size=self.updates,pos=self.updates)
    def updates(self,instance,value):
        self.rect.size=instance.size
        self.rect.pos=instance.pos
