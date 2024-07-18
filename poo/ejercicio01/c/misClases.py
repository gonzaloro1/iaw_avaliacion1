# (poo\ejercicio01\c)    misClases.py
# Clases
#   Alumno()

class Alumno():

	def __init__(self,nombre="Sin nombre",edad=0):
		self.__nombre=nombre
		self.__edad=edad

	def __str__(self):
		return self.__nombre+" con esta edad "+str(self.__edad)

