#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

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
