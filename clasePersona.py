class Persona:
    __Nombre=''
    __direccion=''
    __DNI=''
    def __init__(self,nombre,direc,dni):
        self.__Nombre=nombre
        self.__direccion=direc
        self.__DNI=dni
    def getNombre(self):
        return self.__Nombre
    def getD(self):
        return self.__direccion
    def getDNI(self):
        return self.__DNI
    def __str__(self):
        s='Nombre '+self.__Nombre+' Direccion '+self.__direccion+' DNI '+self.__DNI
        return s
    