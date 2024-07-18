# (poo\ejercicio01\d)    ejercicio01.py

import os
from misClases import Alumno

os.system("cls")

alumno=Alumno()
print(alumno)
print(alumno.nombre)

alumno=Alumno("Juan",33)
print(alumno)

alumno.nombre="Ana"
alumno.edad=18
print(alumno)
