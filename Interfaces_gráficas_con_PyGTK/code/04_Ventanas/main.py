#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import os
os.system("clear")

class Handler:
	builder=None
	def __init__(self):
		# Iniciamos el GtkBuilder para tirar del fichero de glade
		self.builder = Gtk.Builder()
		self.builder.add_from_file("ventanas.glade")
		self.handlers = {
			"onDeleteWindow": self.onDeleteWindow,
			"on_btn_clicked": self.on_btn_clicked,
			"onCloseAboutDialog": self.onCloseAboutDialog}
		
		# Conectamos las señales e iniciamos la aplicación
		self.builder.connect_signals(self.handlers)
		self.window = self.builder.get_object("window")
		self.about = self.builder.get_object("aboutdialog")
		self.window.show_all()
		self.window.resize(300,300)		

	def onDeleteWindow(self, *args):
		print "Taluego noruego"
		Gtk.main_quit(*args)

	def on_btn_clicked(self, window):
		print "Aparece querido Acerca de"
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
