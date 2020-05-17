
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
    def compara (self,dni):
        if(dni==self.__persona.getDNI()):
            return self.__tcap.getNombreT()
        else:
            return False
    def actualizaPa(self):
        self.__pago=True
    def mostrarT(self):
        return 'Taller\n{}'.format(self.__tcap)
    def getFecha(self):
        return self.__fecha
    def getPago(self):
        return self.__pago
    def getPersona(self):
        s='{}'.format(self.__persona.getNombre())+' {}'.format(self.__persona.getDNI())+' {}'.format(self.__persona.getD())
        return s
    def getTaller(self):
        s='{}'.format(self.__tcap.getIDT())+'{}'.format(self.__tcap.getNombreT())
        return s
