#!/usr/bin/python
# -*- coding: utf-8 -*-
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Hola Mundo!")

        self.button = Gtk.Button(label="Hazme click")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hola Mundo!")

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

main()
