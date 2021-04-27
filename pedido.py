from medicamento import medicamento

class pedido:
    def __init__(self,comprador,medicamentos,Id,seguir):
        self.comprador = comprador
        self.medicamentos = medicamentos
        self.Id = Id
        self.seguir = seguir
        
    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getComprador(self):
        return self.comprador
    
    def getMedicamentos(self):
        return self.medicamentos
    
    def getId(self):
        return self.Id

    def getSeguir(self):
        return self.seguir

    

    def setId(self,Id):
        self.Id = Id
    
    def setComprador(self,comprador):
        self.comprador = comprador

    def setMedicamentos(self,medicamentos):
        self.medicamentos = medicamentos

    def setSeguir(self,seguir):
        self.seguir= seguir
    
    