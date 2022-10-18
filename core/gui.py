#!/usr/bin/env python3
from flet import Container,Page,FilePicker,FilePickerResultEvent,ElevatedButton,Column,Row,Dropdown,TextField,Text,dropdown,icons,colors
from os import path,listdir
class XSCPGUI:
    page = None
    pick_files_dialog = FilePicker()
    selectfilesbutton = ElevatedButton(
        "Selectionner des fichiers",
        icon=icons.UPLOAD_FILE
    )
    selectfoldersbutton = ElevatedButton(
        "Selectionner des dossiers",
        icon=icons.UPLOAD_FILE
    )
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
    sources = {}
    guidircontent = []
    middlecontainer = Container()
    middlecolumn = Column()
    middlelabelcontainer = Container()
    middlelabelrow = Row()
    middlelabel = Text(value='selectionnez les fichiers|repertoires à transferer')
    changedirfield = TextField(value=guipath,label='répertoire actuel')
    changedirbutton = ElevatedButton(text='go')
    sourceslist = Column()
    sourceslistcontainer = Container(bgcolor=colors.TEAL)
    bottomcontainer = Container()
    bottomrow = Row()
    statustext = Text()


    toprow.controls = [destentry,hostentry,userentry,pwdentry,docopybutton]
    topcontainer.content = toprow

    sourceslistcontainer.content = sourceslist

    middlelabelcontainer.content = middlelabel
    middlelabelrow.controls = [middlelabelcontainer,pick_files_dialog,selectfilesbutton,selectfoldersbutton]
    middlecolumn.controls = [middlelabelrow,sourceslistcontainer]
    middlecontainer.content = middlecolumn


    bottomrow.controls = [statustext]
    bottomcontainer.content = bottomrow
    
    containercolumn.controls = [topcontainer,middlecontainer,bottomcontainer]
    container.content = containercolumn

    def update_sources(self,sourcesfiles):
        if sourcesfiles is not None:
            for source in sourcesfiles:
                self.sources[source.name] = {'name':source.name,'path':source.path}
            self.update_sources_view()

    def update_dir_sources(self,sourcesfolders):
        if sourcesfolders is not None:
            print(sourcesfolders)
            for [sourcename,sourcepath] in sourcesfolders:
                print(sourcename)
                self.sources[sourcename] = {'name':sourcename,'path':sourcepath}
            self.update_sources_view()
        
    
    def sources_list(self):
        return [ self.sources[source].path for source in self.sources ]

    def update_sources_view(self):
        self.sourceslist.controls = []
        def do_remove_source(e):
            sourcek = e.control.tooltip
            sources = {}
            for k in self.sources:
                if k is not sourcek:
                    sources[k] = self.sources[k]
            self.sources = sources
            self.update_sources_view()

        for sourcek in self.sources:
            sk = sourcek
            source = self.sources[sourcek]
            sourcelemcontainer  = Container(padding=10)
            sourcelemrow        = Row()
            sourcelemname       = Text(value=f"{source['name']}")
            sourcelempath       = Text(value=f"{source['path']}")
            sourcelemdelete     = ElevatedButton(text="retirer",tooltip=source['name'],bgcolor=colors.RED_200,on_click=lambda x :do_remove_source(x))
            sourcelemrow.controls = [sourcelemname,sourcelempath,sourcelemdelete]
            sourcelemcontainer.content = sourcelemrow
            self.sourceslist.controls.append(sourcelemcontainer)
        self.sourceslistcontainer.update()

    def setguipath(self,guipath):
        self.guipath = guipath

    def pagewidth(self):
        return self.page.window_width if self.page else 0
    
    def pageheight(self):
        return self.page.window_height if self.page else 0
    

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
        self.middlecolumn.width = self.pagewidth()
        self.middlecolumn.height = int(self.pageheight()*80/100)
        self.middlelabelrow.width = int(self.middlecontainer.width)
        self.middlelabelrow.height = int(self.pageheight()*5/100)
        

        self.sourceslistcontainer.width = int(self.middlecontainer.width)
        self.sourceslistcontainer.height = int(self.pageheight()*80/100)
        self.sourceslist.height = int(self.pageheight()*80/100)
        

        self.bottomcontainer.width = self.pagewidth()
        self.bottomcontainer.height = int(self.pageheight()*5/100)
        self.bottomrow.height = int(self.pageheight()*5/100)
        self.page.update()

    def pickfilesresulst(self,e:FilePickerResultEvent):
        if e.path:
            self.update_dir_sources([[e.path.split('/')[-1],e.path]])
        if e.files:
            self.update_sources(e.files)
        self.update_sources_view()


    def init_base_events(self):
        self.pick_files_dialog.on_result=self.pickfilesresulst
        self.selectfilesbutton.on_click=lambda _: self.pick_files_dialog.pick_files(
            allow_multiple=True
        )
        self.selectfoldersbutton.on_click=lambda _: self.pick_files_dialog.get_directory_path()
        
    def _loop(self,page:Page):
        self.page = page   
        self.page.bgcolor = colors.BLUE_GREY_100
        self.init_base_events()
        self.reset_sizes()
        self.page.add(self.container)
        self.page.on_resize = lambda x:self.reset_sizes(self)