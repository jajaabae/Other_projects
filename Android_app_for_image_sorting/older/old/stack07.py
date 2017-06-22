#qpy:kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import os


class Imglayout(FloatLayout):

    def __init__(self,**args):
        super(Imglayout,self).__init__(**args)

        with self.canvas.before:
            Color(0,0,0,0)
            self.rect=Rectangle(size=self.size,pos=self.pos)

        self.bind(size=self.updates,pos=self.updates)
    def updates(self,instance,value):
        self.rect.size=instance.size
        self.rect.pos=instance.pos

		
class fileNameContainer():
	count = 0
	#images=['Ill1.jpg', 'BlueFractal.jpg']
	images=[]
	
	def __init__(self):
		picExtentions = ['.bmp', '.jpg', 'JPG'] #, '.png'
		#
		#fileNameContainer.images=['Ill1.jpg', 'BlueFractal.jpg']
		imgs = []
		#print os.listdir(os.getcwd())
		for item in os.listdir(os.getcwd()):
			for pe in picExtentions:
				if pe in item:
					#print item
					imgs += [item]
		#print 'imgs', imgs
		fileNameContainer.images=imgs
		
	
	def increment(self):
		if fileNameContainer.count == len(fileNameContainer.images)-1:
			fileNameContainer.count = 0
		else:
			fileNameContainer.count += 1
	
	def getFileName(self):
		ret = self.images[self.count]
		self.increment()
		return ret


class MainTApp(App):
	#im=Image(source='title.png')
	fnc = fileNameContainer()
	im=Image(source=fnc.getFileName())
    
	def build(self):
		root = BoxLayout(orientation='vertical')
		c = Imglayout()
		root.add_widget(c)

		self.im.keep_ratio= False
		self.im.allow_stretch = True        
		cat=Button(text="Categories",size_hint=(1,.07))
		cat.bind(on_press=self.callback)        
		c.add_widget(self.im)
		root.add_widget(cat);
		return root

	def callback(self, value):
		fnc2 = fileNameContainer()
		self.im.source = fnc2.getFileName()

		
		
if __name__ == '__main__':
    MainTApp().run()



	
	
	
	
	