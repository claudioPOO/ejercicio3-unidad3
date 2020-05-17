from Inscripcion import Inscripcion
import numpy as np
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
        arc=open('Inscripciones.csv','w')
        for m in range(len(self.__arre)):
            f=str(self.__arre[m].getFecha())
            pag=str(self.__arre[m].getPago())
            per=str(self.__arre[m].getPersona())
            t=str(self.__arre[m].getTaller())
            arc.write(f)
            arc.write(pag)
            arc.write(per)
            arc.write(t)
            arc.write('\n')
        arc.close()    
    def mostrar(self):
        for i in range(len(self.__arre)):
            print(self.__arre[i])
    def buscaI(self,dni):
        i=0
        band=0
        while(i<len(self.__arre))and(band==0):
            r=self.__arre[i].compara(dni)
            if(r!=False):
                band=1
            else:
                i=i+1
        if band==1:
            return r
        else:
            return False
    def CancelaPago(self,pos):
        a=self.__arre[pos].actualizaPa()
        return a
