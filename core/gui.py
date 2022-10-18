#!/usr/bin/env python3
from flet import Container,ElevatedButton,Column,Row,DropDown,TextField,Text,dropdown,colors

class XSCPGUI:
    page = None
    topcontainer = Container()
    toprow = Row()
    hostentry = TextField(label='hote')
    pwdentry = TextField(label='mot de passe',password=True)
    userentry = TextField(label='nom d\'utilisateur')
    destentry = TextField(label='repertoire cible')
    docopybutton = ElevatedButton(text='transferer')
    sources = []
    middlecontainer = Container()
    middlecolumn = Column()
    middlelabelcontainer = Container()
    middlelabel = Text(value='selectionnez les fichiers|repertoires à transferer')
    foldercontentcontainer = Container()
    foldercontent = Column()
    bottomcontainer = Container()
    bottomrow = Row()
    staustext = Text()


    topcontainer.content = toprow
    toprow.controls = [destentry,hostentry,userentry,pwdentry]


    foldercontentcontainer.content = foldercontent
    middlelabelcontainer.content = middlelabel
    middlecolumn.controls = [middlelabelcontainer,foldercontentcontainer]
    middlecontainer.content = middlecolumn
    


    def pagewidth(self):
        return self.page.window_width if self.page else 0
    
    def pageheight(self):
        return self.page.window_width if self.page else 0
    


    def reset_sizes(self):
        self.topcontainer.width = self.pagewidth()
        self.topcontainer.height = int(self.pageheight()*20/100)
        self.middlecontainer.width = self.pagewidth()
        self.middlecontainer.height = int(self.pageheight()*70/100)
        self.bottomcontainer.width = self.pagewidth()
        self.bottomcontainer.height = int(self.pageheight()*10/100)

    def __loop(self,Page:page):
        self.page = page   
        self.reset_sizes()