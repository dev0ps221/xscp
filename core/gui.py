#!/usr/bin/env python3
from core.funcs import XSCPFUNCS
from flet import Container,Page,FilePicker,FilePickerResultEvent,ElevatedButton,Column,Row,Dropdown,TextField,Text,dropdown,icons,colors
from os import path,listdir
class XSCPGUI:
    funcs = XSCPFUNCS()
    page = None
    pick_files_dialog = FilePicker()
    selectfilesbutton = ElevatedButton(
        "fichiers",
        icon=icons.UPLOAD_FILE
    )
    selectfoldersbutton = ElevatedButton(
        "dossiers",
        icon=icons.UPLOAD_FILE
    )
    guipath = path.expanduser("~")
    topcontainer = Container(bgcolor=colors.CYAN,padding=5)
    container = Container()
    containercolumn = Column()
    toprow = Row()
    hostentry = TextField(label='hote',text_size=12)
    pwdentry = TextField(label='mot de passe',password=True,text_size=12)
    userentry = TextField(label='nom d\'utilisateur',text_size=12)
    destentry = TextField(label='repertoire cible',text_size=12)
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
    bottomcontainer = Container(padding=5)
    bottomcolumn = Column(scroll='adaptive')
    statustext = Text()


    toprow.controls = [destentry,hostentry,userentry,pwdentry,docopybutton]
    topcontainer.content = toprow

    sourceslistcontainer.content = sourceslist

    middlelabelcontainer.content = middlelabel
    middlelabelrow.controls = [middlelabelcontainer,pick_files_dialog,selectfilesbutton,selectfoldersbutton]
    middlecolumn.controls = [middlelabelrow,sourceslistcontainer]
    middlecontainer.content = middlecolumn


    bottomcolumn.controls = [statustext]
    bottomcontainer.content = bottomcolumn
    
    containercolumn.controls = [topcontainer,middlecontainer,bottomcontainer]
    container.content = containercolumn

    def init_transfert(self,ev):
        data = self.check_transfert_data()
        if data:
            copyresults = self.funcs.docopy(data)
            self.statustext.value = ('\n'.join(copyresults)+"\naction terminée")
            self.statustext.update()
        else:
            print('no enough data to start the copy')


    def update_sources(self,sourcesfiles):
        if sourcesfiles is not None:
            for source in sourcesfiles:
                self.sources[source.name] = {'name':source.name,'path':source.path}
            self.update_sources_view()

    def update_dir_sources(self,sourcesfolders):
        if sourcesfolders is not None:
            for [sourcename,sourcepath] in sourcesfolders:
                self.sources[sourcename] = {'name':sourcename,'path':sourcepath}
            self.update_sources_view()
        
    
    def sources_list(self):
        ret = []
        for source in self.sources:
            if self.sources[source]['path']:
                ret.append(self.sources[source]['path'])
        return ret 

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
    
    def check_transfert_data(self):
        host = self.hostentry.value
        user = self.userentry.value
        pwd = self.pwdentry.value
        dest = self.destentry.value
        sources = self.sources_list()
        if host and user and pwd and dest and len(sources):
            return {
                'host':host,
                'user':user,
                'pwd':pwd,
                'dest':dest,
                'sources':sources,
            }
        else : return None
        

    def reset_sizes(self,ev=None):
        self.set_sizes()

    def set_sizes(self):
        self.topcontainer.width = self.pagewidth()
        self.toprow.width = self.pagewidth()
        self.toprow.height = int(self.pageheight()*15/100)
        self.hostentry.width = int(self.pagewidth()/5) - 15
        self.pwdentry.width = int(self.pagewidth()/5) - 15
        self.userentry.width = int(self.pagewidth()/5) - 15
        self.destentry.width = int(self.pagewidth()/5) - 5
        self.docopybutton.width = int(self.pagewidth()/5) - 25
        self.topcontainer.height = int(self.pageheight()*15/100)


        self.middlecontainer.width = self.pagewidth()
        self.middlecontainer.height = int(self.pageheight()*70/100)
        self.middlecolumn.width = self.pagewidth()
        self.middlecolumn.height = int(self.pageheight()*70/100)
        self.middlelabelrow.width = int(self.middlecontainer.width)
        self.middlelabelrow.height = int(self.pageheight()*5/100)
        

        self.sourceslistcontainer.width = int(self.middlecontainer.width)
        self.sourceslistcontainer.height = int(self.pageheight()*70/100)
        self.sourceslist.height = int(self.pageheight()*70/100)
        

        self.bottomcontainer.width = self.pagewidth()
        self.bottomcontainer.height = int(self.pageheight()*10/100)
        self.bottomcolumn.height = int(self.pageheight()*10/100)
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
        self.docopybutton.on_click = self.init_transfert
        
    def _loop(self,page:Page):
        self.page = page  
        self.page.minimized = True
        self.page.window_min_width = 800
        self.page.window_min_height = 600
        self.page.window_max_width = 800
        self.page.window_max_height = 600  
        self.page.bgcolor = colors.BLUE_GREY_100
        self.page.bgcolor=colors.CYAN_200
        self.init_base_events()
        self.reset_sizes()
        self.page.on_resize = lambda x:self.reset_sizes(self)
        self.page.title = "XSCP V0.1 - By dev0ps221"
        self.page.add(self.container)
        self.page.update()