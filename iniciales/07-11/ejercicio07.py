# ejercicio07.py
# ejemplos de apoyo para hacer este ejercicio
#    ejem07a.py
#    ejem07b.py
#    ejem07c.py
#    ejem07d.py
 
a=int(input("\nDame a: "))
b=int(input("Dame b: "))
if a==b:
    print("\na es IGUAL que b")
    print("Valor de a: "+str(a)+" y valor de b: "+str(b))
    a=a+5
    print ("Incrementamos en 5 el valor de a")
    print("Nuevo valor de a: "+str(a)+"\n")
else:
    print("\na es DISTINTO de b")
    print("Valor de a: "+str(a)+" y valor de b: "+str(b))
    a=a-3
    print ("Decrementamos en 3 el valor de a")
    print("Nuevo valor de a: "+str(a)+"\n")
print ("FIN del programa\n")

