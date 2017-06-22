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
    im=Image(source=fnc.getCurrentFileName())
    #global act_cat
    #self.act_cat=Button(text="action")
    global fncg
    fncg = fileNameContainer()
    
    def build(self):
        #root = BoxLayout(orientation='vertical')
        root = FloatLayout()
        #root = FloatLayout(invert_y = 1)

        c = Imglayout()
        root.add_widget(c)
        
        self.im.keep_ratio= True
        self.im.allow_stretch = True
        c.add_widget(self.im)
        
        
        tmp = StackLayout()
        #tmp = StackLayout(pos_hint={'x':0, 'y':-0.8})
        
        texta = fncg.getCurrentFileName()
        texta = texta.split('.')[0]
        self.titleButton =Button(text=texta,size_hint=( 1 ,.05), background_color=(0,0,0,0.2))
        #self.act_cat=Button(text="action")
        self.titleButton.bind(on_press=self.updateTitlebutton)
        tmp.add_widget( self.titleButton );
        
        
        
        widthOfMainButtons=1.0/3
        
        cat=Button(text="Prev",size_hint=( widthOfMainButtons ,.1), background_color=(0,0,0,0.2))
        cat.bind(on_press=self.previous)
        tmp.add_widget(cat);
        
        cat=Button(text="Next",size_hint=( widthOfMainButtons ,.1), background_color=(0,0,0,0.2))
        cat.bind(on_press=self.next)
        tmp.add_widget(cat);
        
        self.act_cat =Button(text="action",size_hint=( widthOfMainButtons ,.1), background_color=(0,0,0,0.2))
        #self.act_cat=Button(text="action")
        self.act_cat.bind(on_press=self.tagButtonClick_act)
        tmp.add_widget( self.act_cat );
        
        

        btnList = get_btnList() #btnList = ['B', 'C', 'D']
        for b in btnList:
            cat=Button(text=b, size_hint=(None, 0.05), background_color=(0, 0, 0, 0.1))
            cat.bind(on_press=self.tagButtonClick)
            tmp.add_widget(cat);
        
        
        root.add_widget(tmp)
        
        
        return root

    def next(self, value):
        fnc2 = fileNameContainer()
        self.im.source = fnc2.getNextFileName()
        text = fnc2.getCurrentFileName()
        text = text.split('.')[0]
        self.titleButton.text = text
        
    def previous(self, value):
        fnc2 = fileNameContainer()
        self.im.source = fnc2.getPrevFileName()
        text = fnc2.getCurrentFileName()
        text = text.split('.')[0]
        self.titleButton.text = text
        
    def tagButtonClick(instance, value):
        print value.text
        fnc2 = fileNameContainer()
        print fnc2.getCurrentFileName()
        #self.textBox.text = fnc2.getCurrentFileName()
        #value.text= fnc2.getCurrentFileName()

    def tagButtonClick_act(self, value):
        print value.text
        fnc2 = fileNameContainer()
        print fnc2.getCurrentFileName()
        #self.textBox.text = fnc2.getCurrentFileName()
        #self.act_cat.text = fnc2.getCurrentFileName()

        text = fnc2.getCurrentFileName()
        text = text.split('.')[0]
        self.act_cat.text = text
    def updateTitlebutton(self, value):
        text = fnc2.getCurrentFileName()
        text = text.split('.')[0]
        self.titleButton.text = text
        
        
if __name__ == '__main__':
    MainTApp().run()



    
    
    
    
    
