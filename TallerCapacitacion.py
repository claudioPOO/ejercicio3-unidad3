from Inscripcion import Inscripcion
class TallerC:
    __idT=0
    __nombreT=''
    __vacantes=0
    __montoinscripcion=0
    __Inscripciones=[]
    def __init__(self,idt,nombre,vacantes,montoinscripcion):
        self.__idT=int(idt)
        self.__nombreT=nombre
        self.__vacantes=int(vacantes)
        self.__montoinscripcion=int(montoinscripcion)
        self.__Inscripciones=[]
    def getIDT(self):
        return self.__idT
    def getNombreT(self):
        return self.__nombreT
    def __str__(self):
        s='ID {} '.format(self.__idT)+'Nombre: {} '.format(self.__nombreT)+'Vacantes: {} '.format(self.__vacantes)+'Monto Inscripcion: {}'.format(self.__montoinscripcion)
        return s
    def getVacantes(self):
        return self.__vacantes
    def setVacantes(self):
        self.__vacantes=self.__vacantes-1
    def ainscripcion(self,inscripcion):
        self.__Inscripciones.append(inscripcion)
    def getM(self):
        return self.__montoinscripcion
    def mostrarinscriptos(self):
        for i in range(len(self.__Inscripciones)):
            print(self.__Inscripciones[i].getPersona())    
    def NombreyMonto(self):
        print('Taller: {}'.format(self.__nombreT))
        print('Monto Adeudado: {}'.format(self.__montoinscripcion))
    def Cancelamonto(self):
        self.__montoinscripcion=0        