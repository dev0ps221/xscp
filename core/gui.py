#!/usr/bin/env python3
from flet import Container,Page,ElevatedButton,Column,Row,Dropdown,TextField,Text,dropdown,colors

class XSCPGUI:
    page = None
    topcontainer = Container()
    container = Container()
    containercolumn = Column()
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
    foldercontentbox = Column()
    foldercontentboxcontainer = Container()
    foldercontentcontainer = Container()
    foldercontent = Column()
    bottomcontainer = Container()
    bottomrow = Row()
    statustext = Text()


    toprow.controls = [destentry,hostentry,userentry,pwdentry,docopybutton]
    topcontainer.content = toprow


    foldercontentcontainer.content = foldercontent
    middlelabelcontainer.content = middlelabel
    middlecolumn.controls = [middlelabelcontainer,foldercontentcontainer]
    middlecontainer.content = middlecolumn

    bottomrow.controls = [statustext]
    bottomcontainer.content = bottomrow
    
    containercolumn.controls = [topcontainer,middlecontainer,bottomcontainer]
    container.content = containercolumn

    def pagewidth(self):
        return self.page.window_width if self.page else 0
    
    def pageheight(self):
        return self.page.window_width if self.page else 0
    


    def reset_sizes(self):
        self.topcontainer.width = self.pagewidth()
        self.toprow.width = self.pagewidth()
        self.hostentry.width = int(self.pagewidth()/5) - 10
        self.pwdentry.width = int(self.pagewidth()/5) - 10
        self.userentry.width = int(self.pagewidth()/5) - 10
        self.destentry.width = int(self.pagewidth()/5) - 10
        self.docopybutton.width = int(self.pagewidth()/5) - 10
        self.topcontainer.height = int(self.pageheight()*20/100)
        self.middlecontainer.width = self.pagewidth()
        self.middlecontainer.height = int(self.pageheight()*70/100)
        self.bottomcontainer.width = self.pagewidth()
        self.bottomcontainer.height = int(self.pageheight()*10/100)


    def _loop(self,page:Page):
        self.page = page   
        self.reset_sizes()
        self.page.add(self.container)