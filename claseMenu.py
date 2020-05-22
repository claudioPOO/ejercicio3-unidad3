import  os
from clasePersona import Persona
from Inscripcion import Inscripcion
from TallerCapacitacion import TallerC
import datetime
class Menu :
    __switcher = None
    def  __init__ ( self ):
        self.__switcher  = { 1 : self.opcion1 ,
                            2 : self. opcion2 ,
                            3: self. opcion3,
                            4: self .opcion4,
                            5: self. opcion5,
                            6: self.opcion6,
                            0: self. salir
                         }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , MT,MI,MP):
        func = self . __switcher . get ( op , lambda : print ( "Opción no válida" ))
        func ( MT,MI,MP )
    def  salir ( self,MT,MI,MP):
        print ( 'Salir' )
    def  opcion1 (self, MT,MI,MP):
        MT.cargarTalleres()
        MT.mostrar()
    def  opcion2 ( self,MT,MI,MP ):
        n=input('NOMBRE ')
        d=input('Direccion ')
        dn=input('DNI ')
        unaP=Persona(n,d,dn)
        MP.agregaP(unaP)
        os.system('cls')
        t=input('Taller al que desea ingresar ')
        band=0
        while(band==0):
            taller=MT.buscaTaller(t)
            if(isinstance(taller,TallerC)==True):
                print('El taller está disponible')
                band=1
            else:
              print('Taller No disponible,Ingrese otro')
              t=input(' ')
        today = datetime.date.today()
        fecha=str(today)
        unaInscripcion=Inscripcion(fecha,False,unaP,taller)
        MI.agregaInscripcion(unaInscripcion)
        taller.ainscripcion(unaInscripcion)
        print('Inscripcion satisfactoria\n')
        print(unaInscripcion)
        print('\n')
    def opcion3(self,MT,MI,MP):
      dn=input('DNI PARA CONOCER SI ESTA INSCRIPTO ')
      os.system('cls')
      persona=MI.buscapersona(dn,False)
      if(isinstance(persona,TallerC)==True):
          persona.NombreyMonto()
      else:
          if(persona==0):
             print('No esta Inscripto')
    def opcion4(self,MT,MI,MP):
      iden=int(input('Id Taller: '))
      MT.buscainscripcion(iden)
    def opcion5 (self,MT,MI,MP):
        dni=input('DNI PARA REGISTRAR PAGO ')
        persona=MI.buscapersona(dni,True)
        if(isinstance(persona,TallerC)==True):
            print('Pago Cancelado')
        else:
            print('No se encontro persona')
        print('-------inscripciones---')
        MI.mostrar()      
    def opcion6(self,MT,MI,MP):
        MI.creArchivo()
        