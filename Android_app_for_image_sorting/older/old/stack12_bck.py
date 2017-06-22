#qpy:kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import os

import gm.remove_pyc
from Imglayout import Imglayout
from fileNameContainer import fileNameContainer
from gm.get_btnList import get_btnList

from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class MainTApp(App):
    fnc = fileNameContainer()
    im=Image(source=fnc.getFileName())
    
    def build(self):
        #root = BoxLayout(orientation='vertical')
        root = FloatLayout()
        #root = FloatLayout(invert_y = 1)

        c = Imglayout()
        root.add_widget(c)
        
        self.im.keep_ratio= True
        self.im.allow_stretch = True
        c.add_widget(self.im)
        
        """
        cat=Button(text="A",size_hint=(0,.07))#, pos_hint=(1,1)
        cat.bind(on_press=self.tagButtonClick)
        root.add_widget(cat);

        btnList = get_btnList() #btnList = ['B', 'C', 'D']
        for b in btnList:
            cat=Button(text=b,size_hint=(0,.07))
            cat.bind(on_press=self.tagButtonClick)
            root.add_widget(cat);
        
        cat=Button(text="Next",size_hint=(1,.07))
        cat.bind(on_press=self.callback)
        root.add_widget(cat);
        #"""

        #"""
        #tmp = StackLayout()
        #tmp = StackLayout(pos_hint={'x':0, 'y':-.5})
        #tmp = StackLayout(pos_hint={'bottom': 0.5})
        #tmp = StackLayout(pos_hint={'top': 0.1})
        #tmp = StackLayout(pos_hint={'bottom': 0.5})
        #tmp = StackLayout(pos=(1,1))
        #tmp = StackLayout(anchor_y='bottom')
        #tmp = StackLayout(pos=(root.x, -root.height/2))
        
        tmp = StackLayout()
        #tmp = StackLayout(pos_hint={'x':0, 'y':-0.8})
        
        
        cat=Button(text="Next",size_hint=(1,.05), background_color=(0,0,0,0.2))
        cat.bind(on_press=self.callback)
        tmp.add_widget(cat);

        btnList = get_btnList() #btnList = ['B', 'C', 'D']
        for b in btnList:
            #cat=Button(text=b,size_hint=(0,.07))
            #cat=Button(text=b,size_hint=(0,0.05))
            #cat=Button(text=b, size_hint_x=None, width=100)
            cat=Button(text=b, size_hint=(None, 0.05), background_color=(0, 0, 0, 0.1))
            cat.bind(on_press=self.tagButtonClick)
            tmp.add_widget(cat);
        
        
        root.add_widget(tmp)
        #"""


        
        return root

    def callback(self, value):
        fnc2 = fileNameContainer()
        self.im.source = fnc2.getFileName()
        
    def tagButtonClick(instance, value):
        print value.text

        
        
if __name__ == '__main__':
    MainTApp().run()



    
    
    
    
    
