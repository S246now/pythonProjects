###############################################################
# El Ahorcado - A Simple Exercise 1
# using random
###############################################################
from random import choice

def seleccion_palabra():
    lista_palabras = ["tomate","audifonos","mascotas","calendario"]
    palabra_seleccionada = choice(lista_palabras)
    return palabra_seleccionada

def muestra_guiones(palabra):
    n_letras = len(list(palabra))
    lista_guiones = ["_ "] * n_letras
    return lista_guiones
 
def validar_letra(letra,palabra):
    if letra in palabra:
        return True
    else:
        return False

def cambiar_a_letra(letra, lista_guiones):
    tuples = list(enumerate(palabra))
    for par in tuples:
        if par[1] == letra:
            lista_guiones[par[0]] = par[1]
    print(lista_guiones)

def verifica_lista(lista_guiones):
    if '_ ' in lista_guiones:
        return True
    else:
        return False
    
    
print("\n********************")
print("Bienvenida/o!\n** Tienes 6 vidas  para completar la palabra **")
vidas = 6
palabra = seleccion_palabra()
lista_guiones = muestra_guiones(palabra)
print("La palabra es ", lista_guiones)

while vidas > 0:
    print(f"Tienes {vidas} vidas restantes")
    letra = input("\nEscoge una letra: ")
    presente = validar_letra(letra,palabra)
    if presente:
        cambiar_a_letra(letra, lista_guiones)
    else:
        vidas -= 1
        print(f"no hay '{letra}' en la palabra seleccionada")

    if verifica_lista(lista_guiones) == False:
            print("Felicidades! Has ganado")
            print("********************\n")
            break
else:
    print("Has perdido :C")
    print("********************\n")

# EXTRA
# podría mostrar las letras ya ingresadas
# y controlar el re ingreso de las letras con un mensajito