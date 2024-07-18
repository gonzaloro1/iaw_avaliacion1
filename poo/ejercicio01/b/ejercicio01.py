# (poo\ejercicio01\b)    ejercicio01.py

import os
from misClases import Alumno

os.system("clear")

alumno=Alumno()
print(alumno)

alumno=Alumno("Juan",33)
print(alumno)

alumno._nombre="Ana"
alumno._edad=18
print(alumno)
