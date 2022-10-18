#!/usr/bin/env python3
from flet import Container,Column,Row,DropDown,TextEntry,Text,dropdown,colors


class XSCPGUI:
    page = None
    topcontainer = Container()
    middlecontainer = Container()
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