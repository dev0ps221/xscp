#!/usr/bin/env python3
from os import system
from getpass import getpass
class XSCPFUNCS:
    def get_keydata_from(self,src,key,ifnot):
        return src[key] if key in src else ifnot

    def build_sources_string(self,sources):
        sourcestr = ""
        for source in sources:
            sourcestr = f"{sourcestr} \'{source}\'"
        return sourcestr

    def docopy(self,data={}):
        sources = self.get_keydata_from(data,'sources',[])
        dest = self.get_keydata_from(data,'dest',None)
        host = self.get_keydata_from(data,'host',None)
        user = self.get_keydata_from(data,'user',None)
        pwd = self.get_keydata_from(data,'pwd',None)
        if len(sources) and dest and host and user and pwd:
            actionstr = f"sshpass -p '{pwd}' scp -rv {self.build_sources_string(sources)} {user}@{host}:{dest}" 
            print(actionstr)

funcs = XSCPFUNCS()



data = {}
data['sources'] = []
data['sources'].append('/home/dev0ps221/xscpsrc/x.ovpn')
data['sources'].append('/home/dev0ps221/Downloads/AUD-20220820-WA0104.mp3')
data['host']='127.0.0.1'
data['dest']='/home/dev0ps221/justcopy'
data['user']=input('username>')
data['pwd']=getpass('password>')
funcs.docopy(data)