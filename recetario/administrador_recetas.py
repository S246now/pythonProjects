###############################################################
# Recetario - A Simple Exercise 2
# using directories
###############################################################
from pathlib import Path
import shutil

#region CLASSES
class Recetario:
    """ 
    Manejo de operaciones relacionadas con recetas y categorías
    """
    def __init__(self, ruta_base):
        self.ruta_base = Path(ruta_base)

    def buscar_archivos(self):
        """ 
        Devuelve lista de rutas de archivos .txt encontrados
        """
        return list(self.ruta_base.glob('**/*.txt'))
    
    def contar_recetas(self):
        """
        Cuenta el número de recetas en una ruta específica
        """
        return sum(1 for _ in Path(self.ruta_base).glob('**/*.txt'))
    
    def mostrar_recetas(self, lista_archivos):
        """ 
        Mostrar recetas en la lista de buscar_archivos()
        """
        for cont, archivo in enumerate(lista_archivos, start=1):
            print(f'{cont}) {Path(archivo).stem}')

    def obtener_categorias(self, lista_archivos):
        """ 
        Devuelve un dic de las categorías(folders)
        """
        lista_categorias = {Path(archivo).parent.stem for archivo in lista_archivos}  
        dic_categorias = {}   
        for cont, categoria in enumerate(lista_categorias, start=1):
                dic_categorias[cont] = categoria
        return dic_categorias
    
    def mostrar_categorias(self, dic_categorias):
        """ 
        Mostrar categorias en la lista
        """
        for cont, categoria in dic_categorias.items():
            print(f'{cont}) {categoria}')

    def crear_receta(self, categoria):
        """ 
        Añadir nuevo archivo .txt en una carpeta(categoría) específica
        """
        nombre = input("Cómo se llama la nueva receta?: ")
        archivo = Path(self.ruta_base / categoria / f'{nombre}.txt')
        if archivo.exists:
            print(f"La receta {nombre} ya existe")
        else:
            with archivo.open('w') as abierto:
                contenido = input("Ingresa el contenido de la receta: ")
                abierto.write(contenido)
            print(f"La receta {nombre} se ha creado con éxito!")

    def crear_categoria(self):
        """ 
        Crear nueva carpeta
        """
        nombre = input("Nombre de la nueva categoría: ")
        carpeta = Path(self.ruta_base / nombre)
        if carpeta.exists():
            print(f"La categoría {nombre} ya existe")
        else:
            carpeta.mkdir()
            print(f"Se ha creado la categoría {nombre}!")
        self.crear_receta(nombre)

    def eliminar_receta(self, archivo):
        """ 
        Eliminar un archivo .txt
        """
        nombre = Path(self.ruta_base / archivo)
        if nombre.exists():  # Comprobar si existe
            nombre.unlink()
            print(f"El archivo '{archivo.stem}' eliminado correctamente!")
        else:
            print(f"El archivo '{archivo}' no existe.")

    def eliminar_categoria(self, categoria):
        """ 
        Eliminar una carpeta y su contenido
        """
        nombre = Path(self.ruta_base / categoria)
        if nombre.exists():
            try:
                shutil.rmtree(nombre)
                print("La Categoría ha sido eliminada correctamente!")
            except Exception:
                print("Ha ocurrido un error al intentar eliminarlo")
        else:
            print(f"No se pudo eliminar la categoría {categoria}")

class Menu:
    """ 
    Manejo de operaciones relacionadas con el menú del programa.
    """
    def __init__(self, opciones):
        self.opciones = opciones

    def mostrar_menu(self):
        print("\n*** Menú ***")
        for clave, valor in self.opciones.items():
            print(f"[{clave}] {valor}")
        print("************")

class Validacion:
    def __init__(self, mensaje, minimo=None, maximo=None):
        self.mensaje = mensaje
        self.minimo = minimo
        self.maximo = maximo

    def pedir_numero(self):
        while True:
            try:
                numero = int(input(self.mensaje))
                if (self.minimo is not None and numero < self.minimo) or (self.maximo is not None and numero > self.maximo):
                    print(f"Por favor, introduce un número entre {self.minimo} y {self.maximo}.")
                else:
                    return numero
            except ValueError:
                print("Entrada no válida. Debes ingresar un número.")
#endregion

#region MAIN
def main():
    """ 
    Programa principal 
    """
    recetario = Recetario(Path.cwd() / 'Recetas')
    
    # ------- MENU -------
    MENU_OPTIONS = {
            1: "Leer receta",
            2: "Crear receta",
            3: "Crear categoría",
            4: "Eliminar receta",
            5: "Eliminar categoría",
            6: "Finalizar"
        }
    
    # ------- PROGRAM -------
    print("\n********************")
    print("** Bienvenida/o a tu Administrador de Recetas! **")
    ruta_actual = Path.cwd() / 'Recetas'
    print("Las recetas se encuentran en la ruta: ", ruta_actual)
    print(f"\nTienes {recetario.contar_recetas()} recetas: ")
    lista_archivos = recetario.buscar_archivos()
    recetario.mostrar_recetas(lista_archivos)

    opcion = 1
    while opcion in MENU_OPTIONS:
        menu = Menu(MENU_OPTIONS)
        menu.mostrar_menu()
        valida = Validacion("Elige una opción: ",1,len(MENU_OPTIONS))
        opcion = valida.pedir_numero()

        # ------- LEER RECETA -------
        if opcion == 1:
            print("\n**** [1] Leer Receta ****")
            dic_categorias = recetario.obtener_categorias(lista_archivos)
            recetario.mostrar_categorias(dic_categorias)
            valida_categoria = Validacion("\nElige una categoría: ",1,len(lista_archivos))
            numero_categoria = valida_categoria.pedir_numero()

            archivos_categoria = Recetario(ruta_actual / dic_categorias[numero_categoria])
            lista_archivos_categoria = archivos_categoria.buscar_archivos()
            recetario.mostrar_recetas(lista_archivos_categoria)
            valida_receta = Validacion("\n¿Qué receta deseas leer?: ",1,len(lista_archivos))
            numero_receta = valida_receta.pedir_numero()
            
            archivo = Path(lista_archivos_categoria[numero_receta-1])
            with archivo.open('r') as abierto:
                print(abierto.read())
        
        # ------- CREAR RECETA -------
        elif opcion == 2:
            print("\n**** [2] Crear Receta ****")
            dic_categorias = recetario.obtener_categorias(lista_archivos)
            recetario.mostrar_categorias(dic_categorias)
            valida_categoria = Validacion("\nElige una categoría: ",1,len(lista_archivos))
            numero_categoria = valida_categoria.pedir_numero()

            archivos_categoria = Recetario(ruta_actual / dic_categorias[numero_categoria])
            lista_archivos_categoria = archivos_categoria.buscar_archivos()
            recetario.mostrar_recetas(lista_archivos_categoria)

            recetario.crear_receta(dic_categorias[numero_categoria])

        # ------- CREAR CATEGORÍA -------
        elif opcion == 3:
            print("\n**** [3] Crear Categoría ****")
            dic_categorias = recetario.obtener_categorias(lista_archivos)
            recetario.mostrar_categorias(dic_categorias)
            recetario.crear_categoria()

        # ------- ELIMINAR RECETA -------
        elif opcion == 4:
            print("\n**** [4] Eliminar Receta ****")
            dic_categorias = recetario.obtener_categorias(lista_archivos)
            recetario.mostrar_categorias(dic_categorias)
            valida_categoria = Validacion("\nElige una categoría: ",1,len(lista_archivos))
            numero_categoria = valida_categoria.pedir_numero()

            archivos_categoria = Recetario(ruta_actual / dic_categorias[numero_categoria])
            lista_archivos_categoria = archivos_categoria.buscar_archivos()
            recetario.mostrar_recetas(lista_archivos_categoria)
            valida_receta = Validacion("\n¿Qué receta deseas eliminar?: ",1,len(lista_archivos))
            numero_receta = valida_receta.pedir_numero()

            recetario.eliminar_receta(lista_archivos_categoria[numero_receta-1])

        # ------- ELIMINAR CATEGORÍA -------
        elif opcion == 5:
            print("\n**** [5] Eliminar Categoría ****")
            dic_categorias = recetario.obtener_categorias(lista_archivos)
            recetario.mostrar_categorias(dic_categorias)
            valida_categoria = Validacion("\n¿Qué categoría deseas eliminar?: ",1,len(lista_archivos))
            numero_categoria = valida_categoria.pedir_numero()

            recetario.eliminar_categoria(dic_categorias[numero_categoria])

        # ------- FINALIZAR -------
        else:
            print("\n**** Finalizando ****")
            break
        print("********************")
    else:
        print("Opción no válida.")
    
if __name__ == "__main__":
    main()
#endregion
