# ejercicio11.py
# ejemplo de apoyo para hacer este ejercicio
#    ejem011.py
 
#dato=7
#dato=3.456
dato="Hola"

if type(dato) is int:
    print("\nEl valor de dato es: %d y es un ENTERO\n" % dato)
elif type (dato) is float:
    print("\nEl valor de dato es: %.3f y es un REAL\n" % dato)
else: 
    print("\nEl valor de dato es: %s y es un STRING\n" % dato)
    
