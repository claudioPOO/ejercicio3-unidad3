
import os
from ManejaTaller import ManejaTaller
from Manejainsc import ManejaIns
from Manejap import ManejaPersona
from claseMenu import Menu

if __name__ == '__main__':
   
   MT=ManejaTaller()
   MI=ManejaIns()
   MP=ManejaPersona()
   menu = Menu()
   salir = False
   while not salir:
        print("\n------------Menu------------\n1. cargar archivo talleres\n2. Inscribir una persona\n3. buscar inscripto por Dni\n4. Taller para conocer inscriptos\n5.Registrar pago\n6.Guardar archivo\n0. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op,MT,MI,MP)
        salir = op == 0