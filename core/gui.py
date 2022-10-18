#!/usr/bin/env python3
from flet import Container,Page,FilePicker,FilePickerResultEvent,ElevatedButton,Column,Row,Dropdown,TextField,Text,dropdown,colors
from os import path,listdir
class XSCPGUI:
    page = None
    pick_files_dialog = FilePicker(on_result=self.pickfilesresulst)
    guipath = path.expanduser("~")
    topcontainer = Container(bgcolor=colors.CYAN,padding=10)
    container = Container()
    containercolumn = Column()
    toprow = Row()
    hostentry = TextField(label='hote')
    pwdentry = TextField(label='mot de passe',password=True)
    userentry = TextField(label='nom d\'utilisateur')
    destentry = TextField(label='repertoire cible')
    docopybutton = ElevatedButton(text='transferer')
    sources = []
    guidircontent = []
    middlecontainer = Container()
    middlerow = Row()
    middlelabelcontainer = Container()
    middlelabelrow = Row()
    middlelabel = Text(value='selectionnez les fichiers|repertoires à transferer')
    changedirfield = TextField(value=guipath,label='répertoire actuel')
    changedirbutton = ElevatedButton(text='go')
    foldercontentbox = Column()
    foldercontentboxcontainer = Container()
    foldercontentcontainer = Container()
    foldercontent = Column(scroll='always')
    sourceslist = Column()
    sourceslistcontainer = Container(bgcolor=colors.TEAL)
    bottomcontainer = Container()
    bottomrow = Row()
    statustext = Text()


    toprow.controls = [destentry,hostentry,userentry,pwdentry,docopybutton]
    topcontainer.content = toprow


    foldercontentcontainer.content = foldercontent
    middlelabelcontainer.content = middlelabel
    middlelabelrow.controls = [middlelabelcontainer,changedirfield,changedirbutton]
    foldercontentbox.controls = [middlelabelrow,foldercontentcontainer]
    foldercontentboxcontainer.content = foldercontentbox

    sourceslistcontainer.content = sourceslist

    middlerow.controls = [foldercontentboxcontainer,sourceslistcontainer]
    middlecontainer.content = middlerow


    bottomrow.controls = [statustext]
    bottomcontainer.content = bottomrow
    
    containercolumn.controls = [topcontainer,middlecontainer,bottomcontainer]
    container.content = containercolumn

    def setguipath(self,guipath):
        self.guipath = guipath

    def pagewidth(self):
        return self.page.window_width if self.page else 0
    
    def pageheight(self):
        return self.page.window_height if self.page else 0
    
    def showdircontent(self):
        self.guidircontent = listdir(self.guipath)
        self.update_dircontent_view()

    def update_dircontent_view(self):
        self.foldercontent.controls = []
        for elem in self.guidircontent:
            elemcontrolcontainer = Container()
            elemcontrol = Row()
            elemcontrolname = Text(value=elem)
            elemcontrol.controls = [elemcontrolname]
            elemcontrolcontainer.content = elemcontrol
            self.foldercontent.controls.append(elemcontrolcontainer)
        self.foldercontent.update()

    def reset_sizes(self,ev=None):
        self.topcontainer.width = self.pagewidth()
        self.toprow.width = self.pagewidth()
        self.toprow.height = int(self.pageheight()*5/100)
        self.hostentry.width = int(self.pagewidth()/5) - 15
        self.pwdentry.width = int(self.pagewidth()/5) - 15
        self.userentry.width = int(self.pagewidth()/5) - 15
        self.destentry.width = int(self.pagewidth()/5) - 5
        self.docopybutton.width = int(self.pagewidth()/5) - 25
        self.topcontainer.height = int(self.pageheight()*10/100)

        self.middlecontainer.width = self.pagewidth()
        self.middlecontainer.height = int(self.pageheight()*90/100)
        self.middlerow.width = self.pagewidth()
        self.middlerow.height = int(self.pageheight()*80/100)
        self.middlelabelrow.width = int(self.middlecontainer.width*77.6/100)
        self.middlelabelrow.height = int(self.pageheight()*5/100)
        

        self.sourceslistcontainer.width = int(self.middlecontainer.width*20/100)
        self.sourceslistcontainer.height = int(self.pageheight()*80/100)
        self.sourceslist.height = int(self.pageheight()*80/100)
        
        self.foldercontentboxcontainer.width = int(self.middlecontainer.width*77.6/100)
        self.foldercontentboxcontainer.height = int(self.pageheight()*80/100)
        self.foldercontentbox.width = int(self.middlecontainer.width*77.6/100)
        self.foldercontentbox.height = int(self.pageheight()*80/100)
        
        self.foldercontentcontainer.width = int(self.pagewidth()*80/100)
        self.foldercontentcontainer.height = int(self.pageheight()*80/100)
        

        self.foldercontent.width = int(self.middlecontainer.width*77.6/100)
        self.foldercontent.height = int(self.pageheight()*70/100) 
        


        self.bottomcontainer.width = self.pagewidth()
        self.bottomcontainer.height = int(self.pageheight()*5/100)
        self.bottomrow.height = int(self.pageheight()*5/100)
        self.page.update()

    def pickfilesresulst(self,e:FilePickerResultEvent):



    def init_base_events(self):
        def on_changedir_field(ev):
            self.setguipath(self.changedirfield.value)
        def on_do_changedir(ev):
            self.showdircontent()
        self.changedirfield.on_change = on_changedir_field
        self.changedirbutton.on_click = on_do_changedir

    def _loop(self,page:Page):
        self.page = page   
        self.page.bgcolor = colors.BLUE_GREY_100
        self.reset_sizes()
        self.init_base_events()
        self.page.add(self.container)
        self.page.on_resize = lambda x:self.reset_sizes(self)
        self.showdircontent()