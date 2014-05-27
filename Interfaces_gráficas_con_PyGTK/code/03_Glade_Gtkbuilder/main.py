#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import os

os.system("clear")

class Handler:
	def __init__(self):
		self.__valor = True

	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)

	def onButtonPressed(self, button):
		print("Hello World!")
		
	def onButtonClick(self, button):
		if self.__valor:
			self.__btnLabel = button.get_label()
			button.set_label("Contenido nuevo")
			self.__valor = False
		else:
			self.__btnLabel = button.get_label()
			button.set_label("button2")
			self.__valor = True
		print self.__btnLabel
	valor = True
	btnLabel = ""

builder = Gtk.Builder()
builder.add_from_file("builder_example.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
