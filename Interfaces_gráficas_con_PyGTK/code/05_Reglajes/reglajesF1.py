#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       reglagesF1.py
#       
#       Copyright 20144 Oficina de Software Libre <osl@ugr.es>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sqlite3

from electre import Electre
from gi.repository import Gtk

class Electre_GUI:
	def onButtonPressed(self,button):
		priority = []
		deseado = []
		decisional = []
		
		for i in range(10,19):
			combobox = self.builder.get_object("combobox%s" % i)
			tree_iter = combobox.get_active_iter()
			if tree_iter != None:
				model = combobox.get_model()
				value = model[tree_iter][0]
				priority.append(value)
				
		for i in range(1,10):
			combobox = self.builder.get_object("combobox%s" % i)
			tree_iter = combobox.get_active_iter()
			if tree_iter != None:
				model = combobox.get_model()
				value = model[tree_iter][0]
				deseado.append(value)
				
		db = "speed_circuits.db"
		connection=sqlite3.connect(db)
		cursor=connection.cursor()
		cursor.execute("select AleronD, AleronT, Peso, Suspension, Cambios, \
		                Suelo, Revoluciones, Frenos, Camber from results \
		                where ID_circuit = '%s'" % self.get_id_circuito())
		row = cursor.fetchall()
		for r in row:
			decisional.append(r)
			
		cursor.close()
		
		ele = Electre(len(row),9)
		sol = ele.resolver(decisional,priority,deseado)
		
		datos ={'d1': str(row[sol][0]),
				 'd2': str(row[sol][1]),
				 'd3': str(row[sol][2]),
				 'd4': str(row[sol][3]),
				 'd5': str(row[sol][4]),
				 'd6': str(row[sol][5]),
				 'd7': str(row[sol][6]),
				 'd8': str(row[sol][7]),
				 'd9': str(row[sol][8]),}
		
		self.populate_entry_optimo(datos)
		
    
	def onCircuitActivate(self, menuitem):
		self.circuito = menuitem.get_label()
		image = self.builder.get_object("image1")
		image.set_from_file(self.get_image(self.circuito))
				
		entry1 = self.builder.get_object("entry1")
		entry2 = self.builder.get_object("entry2")
		entry3 = self.builder.get_object("entry3")
		entry4 = self.builder.get_object("entry4")
		entry5 = self.builder.get_object("entry5")
		entry6 = self.builder.get_object("entry6")
		entry7 = self.builder.get_object("entry7")
		entry8 = self.builder.get_object("entry8")
		entry9 = self.builder.get_object("entry9")
		entry10 = self.builder.get_object("entry10")
				
		datos = self.get_datos(self.circuito)
		
		entry1.set_text(datos['d1'])
		entry2.set_text(datos['d2'])
		entry3.set_text(datos['d3'])
		entry4.set_text(datos['d4'])
		entry5.set_text(datos['d5'])
		entry6.set_text(datos['d6'])
		entry7.set_text(datos['d7'])
		entry8.set_text(datos['d8'])
		entry9.set_text(datos['d9'])
		entry10.set_text(datos['d10'])
		
		datos ={'d1': str("000"),
				 'd2': str("000"),
				 'd3': str("000"),
				 'd4': str("000"),
				 'd5': str("000"),
				 'd6': str("000"),
				 'd7': str("000"),
				 'd8': str("000"),
				 'd9': str("000"),}
		
		self.populate_entry_optimo(datos)
		
		button1 = self.builder.get_object("button1")
		button1.set_sensitive(True)
		
		return True
		
	def onAboutDialog(self, *args):
		self.about = self.builder.get_object("aboutdialog1")
		self.about.show_all()
		
	def onCloseAbout(self, *args):
		self.about = self.builder.get_object("aboutdialog1")
		self.about.hide()
		
	
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("rF1.glade")
		self.handlers = {"onDeleteWindow": Gtk.main_quit,
						"onButtonPressed": self.onButtonPressed,
						"onCircuitActivate": self.onCircuitActivate,
						"onAboutDialog": self.onAboutDialog,
						"onCloseAbout": self.onCloseAbout,}
        
		self.builder.connect_signals(self.handlers)
		self.init_combobox()
		button1 = self.builder.get_object("button1")
		button1.set_sensitive(False)
		self.window = self.builder.get_object("reglajes")
		self.window.show_all()
		
	def init_combobox(self):
		renderer_text = Gtk.CellRendererText()
		
		for i in range(1,19):
			combobox = self.builder.get_object("combobox%s" % i)
			combobox.pack_start(renderer_text, True)
			combobox.add_attribute(renderer_text, "text", 0)
		
		return True


	def populate_entry_optimo(self,datos):
		entry11 = self.builder.get_object("entry11")
		entry12 = self.builder.get_object("entry12")
		entry13 = self.builder.get_object("entry13")
		entry14 = self.builder.get_object("entry14")
		entry15 = self.builder.get_object("entry15")
		entry16 = self.builder.get_object("entry16")
		entry17 = self.builder.get_object("entry17")
		entry18 = self.builder.get_object("entry18")
		entry19 = self.builder.get_object("entry19")

		entry11.set_text(datos['d1'])
		entry12.set_text(datos['d2'])
		entry13.set_text(datos['d3'])
		entry14.set_text(datos['d4'])
		entry15.set_text(datos['d5'])
		entry16.set_text(datos['d6'])
		entry17.set_text(datos['d7'])
		entry18.set_text(datos['d8'])
		entry19.set_text(datos['d9'])

	def get_image(self, circuito):
		images ={'Albert Park': 'resources/albert_park.jpg',
				 'Sepang': "resources/sepang.jpg",
				 'Shangai': 'resources/shangai.jpg',
				 'Bahrain': 'resources/bahrein.jpg',
				 'Montmelo': 'resources/catalunya.jpg',
				 'Monte Carlo': 'resources/monacocir.jpg',
				 'Estambul Park': 'resources/estambul.jpg',
				 'Silverstone': 'resources/silverstone.jpg',
				 'Hockenheim': 'resources/alemania_circuito.jpg',
				 'Hungaroring': 'resources/hungria.jpg',
				 'Valencia': 'resources/valencia.jpg',
				 'Spa': 'resources/spa.jpg',
				 'Monza': 'resources/monza.jpg',
				 'Marina Bay': 'resources/singapur.jpg',
				 'Suzuka': 'resources/japon.jpg',
				 'Interlagos': 'resources/brasil.jpg',
				 'Abu Dhabi': 'resources/abu.jpg',
				 'Portada': 'resources/portada.jpg',}
		
		if images.has_key(circuito):
			return images[circuito]
		else:
			return images['Portada']
		
	def get_datos(self, circuito):
		db = "speed_circuits.db"
		connection=sqlite3.connect(db)
		cursor=connection.cursor()
		cursor.execute("select * from circuits where Nombre = '%s'" % circuito)
		row = cursor.fetchall()
		cursor.close()
		
		datos ={'d1': str(row[0][1]) + ' Km',
				 'd2': str(row[0][2]) + ' Vueltas',
				 'd3': str(row[0][3]) + ' Seg',
				 'd4': str(row[0][4]) + ' m',
				 'd5': str(row[0][5]) + ' Km/h',
				 'd6': str(row[0][11]) + '/' + str(row[0][6]) ,
				 'd7': row[0][7],
				 'd8': row[0][8],
				 'd9': row[0][9],
				 'd10': str(row[0][10]),}
				
		return datos

	def get_id_circuito(self):
		id_circuito = {'Albert Park': 1,
						'Sepang': 2,
						'Shangai': 3,
						'Bahrain': 4,
						'Montmelo': 5,
						'Monte Carlo': 6,
						'Estambul Park': 7,
						'Silverstone': 8,
						'Hockenheim': 9,
						'Hungaroring': 10,
						'Valencia': 11,
						'Spa': 12,
						'Monza': 13,
						'Marina Bay': 14,
						'Suzuka': 15,
						'Interlagos': 16,
						'Abu Dhabi': 17,}
		
		return id_circuito[self.circuito]

def main():
	window = Electre_GUI()
	Gtk.main()

	return 0

if __name__ == '__main__':
	main()

