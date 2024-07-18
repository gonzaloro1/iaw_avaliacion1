# (poo\ejercicio01\b)    misClases.py
# Clases
#   Alumno()

class Alumno():

	def __init__(self,nombre="Sin nombre",edad=0):
		self._nombre=nombre
		self._edad=edad

	def __str__(self):
		return self._nombre+"  "+str(self._edad)

