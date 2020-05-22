from Inscripcion import Inscripcion
import numpy as np
from clasePersona import Persona
class ManejaIns:
    __arre=None
    __cantidad=0
    __dimension=5
    def __init__(self,cantidad=5):
        self.__arre=np.empty(cantidad,dtype=Inscripcion)
    def agregaInscripcion(self,Inscripcion):
        if(self.__cantidad==self.__dimension):
            self.__dimension=self.__dimension+5
            self.__arre.resize(self.__dimension)
            self.__arre[self.__cantidad]=Inscripcion
            self.__cantidad+=1
        else:
            self.__arre[self.__cantidad]=Inscripcion
            self.__cantidad+=1
    def creArchivo(self):
        arc=open('Inscripciones.csv','a')
        i=0
        while(i<self.__cantidad):
            f=self.__arre[i].getFecha()
            pag=self.__arre[i].getPago()
            per=self.__arre[i].getPersona()
            t=self.__arre[i].GuardaTaller()
            arc.write(f)
            arc.write(';')
            arc.write(pag)
            arc.write(';')
            arc.write(per)
            arc.write(';')
            arc.write(t)
            arc.write('\n')
            i=i+1
        arc.close()    
    def mostrar(self):
        for i in range(len(self.__arre)):
            print(self.__arre[i])
    def buscapersona(self,dni,pago):
        i=0
        band=0
        while(band==0):
            if(i<self.__cantidad):  
              if(self.__arre[i].comparaPersona(dni)==1):
                   taller=self.__arre[i].getTaller()
                   if(pago==True):
                     self.__arre[i].CancelaPago()
                   band=1
              else:
                    i=i+1
            else:
                band=2

        if(band==1):
            return taller
        else:
            if(band==2):    
              print('Persona no encontrada')              
    
