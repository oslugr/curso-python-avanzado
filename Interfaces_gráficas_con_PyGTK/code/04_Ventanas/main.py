#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import os
os.system("clear")

class Handler:
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)

	def on_btn_clicked(self, window):
		window.show_all();




builder = Gtk.Builder()
builder.add_from_file("ventanas.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

about = builder.get_object("aboutdialog")
about.show_all()

Gtk.main()
