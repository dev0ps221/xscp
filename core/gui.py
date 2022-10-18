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
    middlerow = Row()
    middlelabelcontainer = Container()
    middlelabel = Text(value='selectionnez les fichiers|repertoires à transferer')
    foldercontentbox = Column()
    foldercontentboxcontainer = Container(scroll='adaptive')
    foldercontentcontainer = Container()
    foldercontent = Column()
    sourceslist = Column()
    sourceslistcontainer = Container(bgcolor=colors.TEAL)
    bottomcontainer = Container()
    bottomrow = Row()
    statustext = Text()


    toprow.controls = [destentry,hostentry,userentry,pwdentry,docopybutton]
    topcontainer.content = toprow


    foldercontentcontainer.content = foldercontent
    middlelabelcontainer.content = middlelabel
    foldercontentbox.controls = [middlelabelcontainer,foldercontentcontainer]
    foldercontentboxcontainer.content = foldercontentbox

    sourceslistcontainer.content = sourceslist

    middlerow.controls = [foldercontentboxcontainer,sourceslistcontainer]
    middlecontainer.content = middlerow


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
        self.hostentry.width = int(self.pagewidth()/5) - 15
        self.pwdentry.width = int(self.pagewidth()/5) - 15
        self.userentry.width = int(self.pagewidth()/5) - 15
        self.destentry.width = int(self.pagewidth()/5) - 5
        self.docopybutton.width = int(self.pagewidth()/5) - 25
        self.topcontainer.height = int(self.pageheight()*10/100)
        self.middlecontainer.width = self.pagewidth()
        self.middlecontainer.height = int(self.pageheight()*70/100)
        self.sourceslistcontainer.height = self.middlecontainer.height-5
        self.sourceslist.height = self.middlecontainer.height-5
        self.foldercontentcontainer.height = self.middlecontainer.height-5
        self.foldercontentboxcontainer.width = int(self.middlecontainer.width*80/100)
        self.sourceslistcontainer.width = int(self.middlecontainer.width*30/100)
        self.bottomcontainer.width = self.pagewidth()
        self.bottomcontainer.height = int(self.pageheight()*10/100)


    def _loop(self,page:Page):
        self.page = page   
        self.reset_sizes()
        self.page.add(self.container)