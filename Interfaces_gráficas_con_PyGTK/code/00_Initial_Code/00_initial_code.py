#!/usr/bin/python
# -*- coding: utf-8 -*-
from gi.repository import Gtk

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()