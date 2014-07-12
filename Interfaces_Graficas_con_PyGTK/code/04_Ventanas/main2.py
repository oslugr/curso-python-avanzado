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
	builder=None
	def __init__(self):
		# Iniciamos el GtkBuilder para tirar del fichero de glade
		self.builder = Gtk.Builder()
		self.builder.add_from_file("ventanas2.glade")
		self.handlers = {
			"onDeleteWindow": self.onDeleteWindow,
			"on_btn_clicked": self.on_btn_clicked,
			"onCloseAboutDialog": self.onCloseAboutDialog}
		
		# Conectamos las señales e iniciamos la aplicación
		self.builder.connect_signals(self.handlers)
		self.window = self.builder.get_object("window")
		self.btn = self.builder.get_object("btn")
		self.txt = self.builder.get_object("entry")
		self.about = self.builder.get_object("aboutdialog")

		dato = 1
		self.txt.set_text(str(dato))

		self.window.show_all()
		self.window.resize(300,300)		

	def onDeleteWindow(self, *args):
		print "Taluego noruego"
		Gtk.main_quit(*args)

	def on_btn_clicked(self, window):
		print "Aparece querido Acerca de"
		print "Introduce un dato"
		
		self.about.show()

	def onCloseAboutDialog(self,window,data=None):
		print "Digan adiós a nuestro Acerca de"
		self.about.hide()


def main():
	window = Handler()
	Gtk.main()
	return 0

if __name__ == '__main__':
	main()
