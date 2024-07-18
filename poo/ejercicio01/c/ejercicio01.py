# (poo\ejercicio01\c)    ejercicio01.py

import os
from misClases import Alumno

os.system("cls")

alumno=Alumno()
print(alumno)

alumno=Alumno("Juan",33)
print(alumno)

alumno._Alumno__nombre="Ana"
alumno._Alumno__edad=18
print(alumno)
