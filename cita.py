class cita:
    def __init__(self,paciente,motivo,fecha,hora,estado,tipo,doctor):
        self.paciente = paciente
        self.motivo = motivo
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.tipo = tipo
        self.doctor = doctor
    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getPaciente(self):
        return self.paciente
    
    def getMotivo(self):
        return self.motivo

    def getDoctor(self):
        return self.doctor

    def getFecha(self):
        return self.fecha

    def getHora(self):
        return self.hora

    def getTipo(self):
        return self.tipo
        
    def getEstado(self):
        return self.estado

    def setPaciente(self,paciente):
        self.paciente = paciente
    
    def setMotivo(self,motivo):
        self.motivo = motivo

    def setFecha(self,fecha):
        self.fecha = fecha

    def setHora(self,hora):
        self.hora = hora
    def setEstado (self,estado):
        self.estado = estado
    
    def setDoctor(self,doctor):
        self.doctor = doctor