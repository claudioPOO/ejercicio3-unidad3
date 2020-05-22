from TallerCapacitacion import TallerC
import csv
import numpy as np
class ManejaTaller:
    __arre=None
    __cantidad=0
    def __init__(self,cantidad=1):
        self.__arre=np.empty(cantidad,dtype=TallerC)
    def cargarTalleres(self):
        tall=open('Talleres.csv')
        reader=csv.reader(tall,delimiter=';')
        for fila in reader:
            if(len(fila)==1):
                cant=int(fila[0])
                self.__arre.resize(cant)
            else:
                unTaller=TallerC(fila[0],fila[1],fila[2],fila[3])
                self.__arre[self.__cantidad]=unTaller
                self.__cantidad=self.__cantidad+1
                   
        
        tall.close()
    def mostrar(self):
        for i in range(len(self.__arre)):
            print(self.__arre[i])
    def buscaTaller(self,nombre):
        i=0
        band=0
        while(i<len(self.__arre))and(band==0):
            if(nombre==self.__arre[i].getNombreT()):
                if(self.__arre[i].getVacantes()!=0):
                    self.__arre[i].setVacantes()    
                    band=1
                else:
                    print('No Hay Vacantes')
                    band=2
            else:
                i=i+1
        if(band==1):
            return self.__arre[i]
        else:
            return False             
  

    def muestra(self,i):
        s='Taller {}'.format(self.__arre[i].getNombreT())+' Monto Adeudado {}'.format(self.__arre[i].getM())
        print(s)
    def buscainscripcion(self,iden):
        i=0
        band=0
        while(i<len(self.__arre))and (band==0):
            if(self.__arre[i].getIDT()==iden):
                self.__arre[i].mostrarinscriptos()
                band=1
            else:
                i=i+1
              