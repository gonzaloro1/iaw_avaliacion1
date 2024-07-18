# (poo\ejercicio01\a)    ejercicio01.py

import os
from misClases import Alumno

os.system("cls")

alumno=Alumno()
print()
print(alumno)
#print("alumno: "+str(alumno) + " -> "+ str(id(alumno)))
#print(id(alumno))

alumno=Alumno("Juan",33)
print()
print(alumno)
#print("alumno: "+str(alumno) + " -> "+ str(id(alumno)))
#print(id(alumno))


alumno.nombre="Ana"
alumno.edad=18
print()
print(alumno)
#print("alumno: "+str(alumno) + " -> "+ str(id(alumno)))
#print(id(alumno))

print()