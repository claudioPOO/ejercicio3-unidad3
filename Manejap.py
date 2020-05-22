from clasePersona import Persona

class ManejaPersona:
        __Personas=[]
        def __init__(self):
            self.__Personas=[]
        def agregaP(self,unaPersona):
            self.__Personas.append(unaPersona)
        def buscaPer(self,dni):
            i=0
            band=False
            while(i<len(self.__Personas))and(band==False):
                if(self.__Personas[i].getDNI()==dni):
                    band=True
                else:
                    i=i+1
            if(band==True):
                return self.__Personas[i]
            else:
                return 0