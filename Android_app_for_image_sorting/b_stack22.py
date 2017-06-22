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


class HandleTaggingContainer():
    def __init__(self, fileName):
        self.fileName = fileName+'.txt'
        self.refreshTagsFromFile()
        
    def refreshTagsFromFile(self):
        tags = self.getTagsFromFile()
        self.tags = tags
        return tags
    
    def getTagsFromFile(self):
        p = os.path.realpath(__file__).replace('\\', '/').split('/')
        p = '/'.join(p[0:-1])
        os.chdir(p)
        
        #makeTagFile if needed
        fip = p+'/'+self.fileName
        self.initFileIfNone(fip)
        
        f = open( self.fileName, 'r')
        lines = f.readlines()
        f.close()
        tags = []
        
        for l in lines:
            tags+= [l.replace('\n', '')]
        return tags
        
    def initFileIfNone(self, fip):
        if not os.path.exists( fip ):
            f = open(self.fileName, 'w')
            #tmp action:
            '''
            f.write("""Art
something
Experience""")
            '''
            f.close()
    
    def saveTagsToFile(self, tmpTagList ):
        p = os.path.realpath(__file__).replace('\\', '/').split('/')
        p = '/'.join(p[0:-1])
        os.chdir(p)
        
        f = open(self.fileName, 'w')
        for t in tmpTagList :
            f.write(t+'\n')
        f.close()
        
    def toggleTag(self, currentTag):
        tmpTagList = self.refreshTagsFromFile()
#        tmpTagList = self.getTagList(fileName)
        if currentTag in tmpTagList:
            tmpTagList.remove(currentTag)
        else:
            tmpTagList+=[currentTag]
        self.saveTagsToFile(tmpTagList)
        


        
        
        
class TagContainerClass():
    allTagLists={}
    
    def updateTagList(self, currentTag, fileName):
        htc = HandleTaggingContainer(fileName)
        htc.toggleTag( currentTag )
    
    def getTagList(self, fileName):
        htc = HandleTaggingContainer(fileName)
        return htc.refreshTagsFromFile()
    
    def saveTagList(self, tmpTagList, fileName):
        #self.allTagLists[fileName]=tmpTagList
        pass

        

class MainTApp(App):
    global fnc
    fnc = fileNameContainer()
    im=Image(source=fnc.getCurrentFileName())
    
    addedTags = []
    tagPreText = "Tags: "
    tagText = '--'
    currentTag = '-'

    tagContainer = TagContainerClass()
           

            
    btnList = get_btnList() #btnList = ['B', 'C', 'D']
    for b in btnList:
        string = """
global %s%s
def %s%s(self, value):
    self.currentTag= '%s'
    self.actOnCurrentTag(None)
        """
        string = string % (b, b, 'tagFun_', b, b)
        exec(string)
    
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
        
        # Title display "button"
        texta = fnc.getCurrentFileName()
        texta = texta.split('.')[0]
        self.titleButton =Button(text=texta,size_hint=( 1 ,.05), background_color=(0,0,0,0.2))
        #self.act_cat=Button(text="action")
        self.titleButton.bind(on_press=self.updateTitlebutton)
        tmp.add_widget( self.titleButton );
        
        
        # Tags display "button"
        self.tagsButton =Button(text=self.tagText,size_hint=( 1 ,.05), background_color=(0,0,0,0.2))
        self.tagsButton.bind(on_press=self.updateTagDisp)
        tmp.add_widget( self.tagsButton );
        
        
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
            cat=Button(text=b, size_hint=(None, 0.1), background_color=(0, 0, 0, 0.1))
            #cat.bind(on_press=self.tagButtonClick)
            string = "cat.bind(on_press=self.%s%s)"
            string = string % ('tagFun_', b)
            exec(string)
            tmp.add_widget(cat);
            
            
        self.updateTagDisp(None)
        
        root.add_widget(tmp)
        
        return root

    def next(self, value):
        #fnc = fileNameContainer()
        self.im.source = fnc.getNextFileName()
        text = fnc.getCurrentFileName()
        text = text.split('.')[0]
        self.titleButton.text = text
        self.updateTagDisp(None)
        
    def previous(self, value):
        #fnc = fileNameContainer()
        self.im.source = fnc.getPrevFileName()
        text = fnc.getCurrentFileName()
        text = text.split('.')[0]
        self.titleButton.text = text
        self.updateTagDisp(None)
        
    def tagButtonClick(self, value):
        print value.text
        #fnc = fileNameContainer()
        print fnc.getCurrentFileName()
        #self.textBox.text = fnc2.getCurrentFileName()
        #value.text= fnc2.getCurrentFileName()
        self.updateTagDisp(None)

    def tagButtonClick_act(self, value):
        print value.text
        fnc = fileNameContainer()
        print fnc.getCurrentFileName()
        #self.textBox.text = fnc2.getCurrentFileName()
        #self.act_cat.text = fnc2.getCurrentFileName()
        text = fnc.getCurrentFileName()
        text = text.split('.')[0]
        self.act_cat.text = text
        
    def updateTitlebutton(self, value):
        text = fnc.getCurrentFileName()
        text = text.split('.')[0]
        self.titleButton.text = text
        
    def updateTagDisp( self, value ):
        fileName = fnc.getCurrentFileName()
        addedTagsFromContainer = self.tagContainer.getTagList(fileName)
        text = self.tagPreText
        if len( addedTagsFromContainer ) > 0:    
            for t in addedTagsFromContainer:
                text += t+', '
        self.tagText = text
        self.tagsButton.text = self.tagText
    
    def actOnCurrentTag(self, value):
        #self.addedTags+=[self.currentTag]
        fileName = fnc.getCurrentFileName()
        cTag = self.currentTag
        self.addedTags = self.tagContainer.updateTagList( cTag , fileName )
        self.updateTagDisp(None)
        

        
if __name__ == '__main__':
    MainTApp().run()



    
    
    
    
    
