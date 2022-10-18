#!/usr/bin/env python3
from flet import app
from core.gui import XSCPGUI


gui = XSCPGUI()
app(target=gui._loop)
