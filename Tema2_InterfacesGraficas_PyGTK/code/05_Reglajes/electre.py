#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       electre.py
#       
#       Copyright 20144 Oficina de Software Libre <osl@ugr.es>
#       
#       ReglajesF1 is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       ReglajesF1 is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with ReglajesF1; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from math import sqrt

class Electre:
	def __init__ (self,alternativas, atributos):
		self.alternativas = alternativas
		self.atributos = atributos
		self.pesos = [0] * atributos
		self.optimo = [0] * atributos
		self.decisional = [] #[[0] * atributos] * alternativas
		self.normalizada = [[0] * atributos] * alternativas
		self.ponderada = [[0] * atributos] * alternativas
		self.concordada = [[0] * atributos] * alternativas
		self.discordada = [[0] * atributos] * alternativas
		self.dominancia = [[0] * atributos] * alternativas
		
		
	def establecerPesos(self, prioridad):
		total = 0.0
		for i in range(0, self.atributos):
			total += prioridad[i]
		for i in range(0, self.atributos):
			self.pesos[i] = prioridad[i]
		
	def establecerOptimo(self, optimo):
		for i in range(0, self.atributos):
			self.optimo[i] = optimo[i]
					
	def establecerDecisional(self, decisional):
		for d in decisional:
			self.decisional.append(d)

	def establecerNormalizada(self):
		for j in range(0, self.atributos):
			suma = 0
			for i in range(0, self.alternativas):
				cuadrado = self.decisional[i][j] * self.decisional[i][j]
				suma = suma + cuadrado
			
			suma = sqrt(suma)
			for i in range(0, self.alternativas):
				self.normalizada[i][j] = (self.decisional[i][j] / suma)
	
	def establecerPonderada(self):
		for i in range(0, self.alternativas):
			for j in range(0, self.atributos):
				self.ponderada[i][j] = self.normalizada[i][j] * self.pesos[j]
				
	def establecerConcordada(self):
		for i in range(0, self.alternativas):
			self.concordada[i][self.atributos - 1] = self.ponderada[i][self.atributos-1]
		
		media = 0
		contador = 0
		
		for i in range(0, self.alternativas):
			for k in range(i+1, self.alternativas):
				contador = contador + 1
				suma = 0
				for j in range(0, self.atributos):
					if (((self.normalizada[i][j] >= self.ponderada[k][j]) and (self.optimo[j] == 1)) or ((self.ponderada[i][j] <= self.ponderada[k][j]) and (self.optimo[j]==0))):
						suma = suma + self.pesos[j]
				self.concordada[i][k] = suma
				self.concordada[k][i] = 1 - suma
				media = media + suma
		
		media = media / contador
		
		for i in range(0, self.alternativas):
			for k in range(0, self.alternativas):
				if self.concordada[i][k] >= media :
					self.concordada[i][k] = 1
				else:
					self.concordada[i][k] = 0
				if i == k:
					self.concordada[i][k] = 0
	
	def establecerDiscordada(self):
		for i in range(0, self.alternativas):
			self.discordada[i][self.atributos - 1] = self.concordada[i][self.atributos-1]
		
		media = 0
		
		for i in range(0, self.alternativas):
			for k in range(0, self.alternativas):
				maximo = 0
				maximo_globlal = 0
				if i != k:
					for j in range(0, self.atributos):
						maximo_actual = self.concordada[i][j] - self.concordada[k][j]
						if maximo_actual < 0:
							maximo_actual =  maximo_actual * (-1.0)
						if maximo_actual > maximo_global:
							maximo_globlal = maximo_actual
						if (((self.concordada[i][j] < self.concordada[k][j]) and (self.optimo[j] == 1)) or ((self.ponderada[i][j] > self.ponderada[k][j]) and (self.optimo[j] == 0))):
							maximo_actual = self.concordada[i][j] - self.concordada[k][j]
						if maximo_actual < 0:
							maximo_actual = maximo_actual * (-1.0)
						if maximo_actual > maximo:
							maximo = maximo_actual
				
				self.discordada[i][k] = maximo / maximo_global
				media = media + self.discordada[i][k]	
		
		media = media / ((self.alternativas * self.alternativas) - this.alternativas)
		
		for i in range(0, self.alternativas):
			for k in range(0, self.alternativas):
				if i != k:
					if self.discordada[i][k] <= media:
						self.discordada[i][k] = 1
					else:
						self.discordada[i][k] = 0
				else:
					self.discordada[i][k] = 0
	
	def establecerDominada(self):
		for i in range(0, self.alternativas):
			for j in range(0, self.atributos):
				self.dominancia[i][j] = 0
		
		for i in range(0, self.alternativas):
			self.dominancia[i][self.alternativas - 1] = self.concordada[i][self.alternativas - 1]
		
		for i in range(0, self.alternativas):
			for j in range(0, self.alternativas):
				if self.concordada[i][j] == self.discordada[i][j]:
					self.dominancia[i][j] = self.concordada[i][j]
	
	def resolver(self, decisional, prioridad, optimo):
		self.establecerPesos(prioridad)
		self.establecerOptimo(optimo)
		self.establecerDecisional(decisional)
		self.establecerNormalizada()
		self.establecerPonderada()
		self.establecerConcordada()
		self.establecerConcordada()
		self.establecerDominada()
		
		print "DECISIONAL"
		self.mostrar(self.decisional)
		print "NORMALIZADA"
		self.mostrar(self.normalizada)
		print "PONDERADA"
		self.mostrar(self.ponderada)
		print "CONCORDADA"
		self.mostrar(self.concordada)
		print "DISCORDADA"
		self.mostrar(self.discordada)
		print "DOMINANCIA"
		self.mostrar(self.dominancia)
		
		mejor = False
		reglaje = 0
		j=0
		for i in range(0, self.alternativas):
			mejor = True
			while (j<self.atributos and mejor):
				if self.dominancia[i][j] == 1.0:
					mejor = False
				else:
					reglaje = i
				j = j+1
		return reglaje
		
	def mostrar(self, matriz):
		for i in range(0, self.alternativas):
			for j in range(0, self.atributos):
				print matriz[i][j],
			print			
