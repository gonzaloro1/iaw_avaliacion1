# (poo\ejercicio01\d)    misClases.py
# Clases
#   Alumno()

class Alumno():

	def __init__(self,nombre="Sin nombre",edad=0):
		self.__nombre=nombre
		self.__edad=edad
	@property
	def nombre(self):
		print("Mostrando atributo")
		return self.__nombre

	@nombre.setter
	def nombre(self,nombre):
		print("Adjudicando atributo")
		self.__nombre=nombre	

	@property
	def edad(self):
		return self.__edad

	@edad.setter
	def edad(self,edad):
		self.__edad=edad

	def __str__(self):
		return self.__nombre+"  "+str(self.__edad)

