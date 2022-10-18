#!/usr/bin/env python3
from os import popen
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
            actionstr = f"sshpass -p '{pwd}' scp -rv  -o \"StrictHostKeyChecking no\" {self.build_sources_string(sources)} {user}@{host}:{dest}" 
            try:
                return popen(actionstr).readlines()
            except Exception as e:
                print("")
funcs = XSCPFUNCS()


