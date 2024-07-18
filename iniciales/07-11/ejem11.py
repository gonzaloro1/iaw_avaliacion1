# ejem11.py

dato=7
#dato=3.456
#dato="Hola"

if type(dato) is int:
    print("\nEl valor de dato es: %d y es un ENTERO" % dato)
else: 
    print("\nEl valor de dato  NO es un ENTERO")
    
if type(dato) is float:
    print("\nEl valor de dato es: %.2f y es un REAL" % dato)
else: 
    print("\nEl valor de dato  NO es un REAL")

if type(dato) is str:
    print("\nEl valor de dato es: %s y es un STRING\n" % dato)
else: 
    print("\nEl valor de dato  NO es un STRING\n")
