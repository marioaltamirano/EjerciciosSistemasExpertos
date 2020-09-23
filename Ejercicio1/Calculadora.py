
#MARIO AGUSTIN ALTAMIRANO LANDAVERDE
import math
def menu():
    print ("""
    Elija una opcion : \n
    opcion 1 = suma \n
    opcion 2 = resta \n
    opcion 3 = multiplicacion \n 
    opcion 4 = division \n  
    opcion 5 = potencia \n  
    opcion 6 = raiz cuadrada \n  
    """
    )
    opcion= int(input("Elige una opcion"))
    return opcion
    
class Numeros:
    def suma(self,x,y):
        print(x+y)
    def resta(self,x,y):
        print(x-y)
    def multi(self,x,y):
        print(x*y)
    def div(self,x,y):
        print(x/y)
    def potencia(self,x,y):
        print(x**y)
    def raiz(self,x):
        print(math.sqrt(x))

operacion=Numeros()

opcion=menu()
if (opcion==1):
    valor1 = int(input("escribe un numero "))
    valor2 = int(input("escribe segundo numero "))
    operacion.suma(valor1,valor2)
if (opcion==2):
    valor1 = int(input("escribe un numero "))
    valor2 = int(input("escribe segundo numero "))
    operacion.resta(valor1,valor2)
if (opcion==3):
    valor1 = int(input("escribe un numero "))
    valor2 = int(input("escribe segundo numero "))
    operacion.multi(valor1,valor2)
if (opcion==4):
    valor1 = int(input("escribe un numero "))
    valor2 = int(input("escribe segundo numero "))
    operacion.div(valor1,valor2)
if (opcion==5):
    valor1 = int(input("escribe la base "))
    valor2 = int(input("escribe el exponente "))
    operacion.potencia(valor1,valor2)
if (opcion==6):
    valor1 = int(input("escribe el numero "))
    operacion.raiz(valor1)