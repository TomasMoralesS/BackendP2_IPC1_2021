class receta:
    def __init__(self,paciente,doctor,fecha,padecimiento,descripcion):
        self.paciente= paciente
        self.doctor = doctor
        self.fecha = fecha
        self.padecimiento = padecimiento
        self.descripcion = descripcion
        
    def getPadecimiento(self):
        return self.padecimiento
    
    def getPaciente(self):
        return self.paciente
    
    def getDoc(self):
        return self.doctor
    
    def getDescripcion(self):
        return self.descripcion
    