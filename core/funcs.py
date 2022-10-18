#!/usr/bin/env python3

class XSCPFUNCS:
    def get_keydata_from(self,src,key,ifnot):
        return src[key] if key in src else ifnot
    def docopy(self,data={}):
        sources = self.get_keydata_from(data,'sources',[])
        dest = self.get_keydata_from(data,'dest',None)
        host = self.get_keydata_from(data,'host',None)
        user = self.get_keydata_from(data,'user',None)
        pwd = self.get_keydata_from(data,'pwd',None)
        if len(sources) and dest and host and usr and pwd:
            actionstr = 