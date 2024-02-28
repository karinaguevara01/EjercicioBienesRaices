class Cuarto:
    '''numero ventanas
       medida ventanas'''
       
    def __init__(self, numVentanas, medidaVentanas):
        self.numVentanas=numVentanas
        self.__medidaVentanas= medidaVentanas
        
    def getNumVentanas(self):
        return self.numVentanas

    def setNumVentanas(self, numVentanas):
        self.numVentanas = numVentanas

    def getMedidaVentanas(self, medidaVentanas):
        return self.__medidaVentanas

    def setMedidaVentanas(self, medidaVentanas):
        self.__medidaVentanas = medidaVentanas

class Sala:
    '''chimenea
       descripcion'''
       
    def __init__(self, chimenea, descripcion ):
        self.__chimenea=chimenea
        self.__descripcion=descripcion
      
    def getChimenea(self):
        return self.__chimenea

    def getDescripcion(self, descripcion):
        return self.__descripcion
    
    def setChimenea(self, chimenea):
        self.__chimenea = chimenea

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
 
class Lavatrastos:
    '''depositos
       agua caliente'''
       
    def __init__(self, depositos, aguaCaliente) :
        self.__depositos=depositos
        self.__aguaCalienTe= aguaCaliente
     
    def getDepositos(self):
        return self.__depositos

    def getAguaCaliente(self):
        return self.__aguaCaliente
    
    def setDepositos(self, depositos):
        self.__depositos = depositos

    def setAguaCaliente(self, aguaCaliente):
        self.__aguaCaliente = aguaCaliente

class Patio:
    '''area social
       medidas
       descripcion'''
       
    def __init__(self, areaSocial, medidas, descripcion) :
        self.__areaSocial=areaSocial
        self.__medidas=medidas
        self.__descripcion= descripcion

    def getAreaSocial(self):
        return self.__areaSocial
    
    def getMedidas(self):
        return self.__medidas
    
    def getDescripcion(self):
        return self.__descripcion

    def setAreaSocial(self, areaSocial):
        self.__areaSocial = areaSocial

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setMedidas(self, medidas):
        self.__medidas=medidas

class Estado:
    '''Nombre
       fecha'''
       
    def __init__(self, nombre, fecha):
        self.__nombre=nombre
        self.__fecha=fecha

    def getFecha(self):
        return self.__fecha
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setFecha(self, fecha):
        self.__fecha = fecha
