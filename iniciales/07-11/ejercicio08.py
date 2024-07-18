# ejercicio08.py
# ejemplo de apoyo para hacer este ejercicio
#    ejem08.py
 
print ("\nLos números a, b, c serán distintos")
a=int(input("\nDame a: "))
b=int(input("Dame b: "))
c=int(input("Dame c: "))
if a>b:
    if a>c:
        print ("\na es el MAYOR")
    else:
        print ("\nc es el MAYOR")
else:
    if b>c:
        print ("\nb es el MAYOR")
    else:
        print ("\nc es el MAYOR")
print ("\nFIN del programa\n")

