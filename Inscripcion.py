
class Inscripcion:
    __fecha=0
    __pago=''
    __persona=None
    __tcap=None
    def __init__(self,fecha,pago,persona,tcap):
        self.__fecha=fecha
        self.__pago=pago
        self.__persona=persona
        self.__tcap=tcap
    def __str__(self):
        s='Fecha {} \n'.format(self.__fecha)+'Pago {} \n'.format(self.__pago)+'Persona\n{} \n'.format(self.__persona)
        return s
    def comparaPersona(self,dni):
        if(dni==self.__persona.getDNI()):
            return 1
        else:
            if(dni!=self.__persona.getDNI()):
                return 0
    def actualizaPa(self):
        self.__pago=True
    def getTaller(self):
        return self.__tcap
    def getFecha(self):
        s='Fecha De Inscripcion: {} '.format(self.__fecha)
        return s
    def getPago(self):
        s='Pago? {} '.format(self.__pago)
        return s
    def getPersona(self):
        s='Nombre {} '.format(self.__persona.getNombre())+'Dni {} '.format(self.__persona.getDNI())+'Direccion {} '.format(self.__persona.getD())
        return s
    def CancelaPago(self):
        self.__pago=True
        self.__tcap.Cancelamonto()
    def GuardaTaller(self):
        s='Taller {} '.format(self.__tcap.getNombreT())
        return s