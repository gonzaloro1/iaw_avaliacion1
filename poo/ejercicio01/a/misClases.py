# (poo\ejercicio01\a)    misClases.py
# Clases
#   Alumno()

class Alumno():

	def __init__(self,nombre="Sin nombre",edad=0):
		self.nombre=nombre
		self.edad=edad

	def __str__(self):
		return self.nombre+"  "+str(self.edad)

