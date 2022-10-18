#!/usr/bin/env python3

class XSCPFUNCS:
    def docopy(self,data={}):
        sources = data['sources'] if 'sources' in data else []
        dest = data['dest'] if 'dest' in data else None