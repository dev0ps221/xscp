#!/usr/bin/env python3
from flet import Container,Column,Row,DropDown,TextField,Text,dropdown,colors

class XSCPGUI:
    page = None
    topcontainer = Container()
    toprow = Row()
    hostentry = TextField(label='hote')
    pwdentry = TextField(label='mot de passe',password=True)
    userentry = TextField(label='nom d\'utilisateur')
    destentry = TextField(label='repertoire cible')
    sources = []
    middlecontainer = Container()
    middlelabel = Text(value='selectionnez les fichiers|repertoires à transferer')
    bottomcontainer = Container()


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