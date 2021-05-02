class factura:
    def __init__(self,paciente,doctor,PConsulta,POperacion,PInternado,total,fecha):
        self.paciente = paciente
        self.doctor = doctor
        self.PConsulta = PConsulta
        self.POperacion = POperacion
        self.PInternado = PInternado
        self.total = total
        self.fecha = fecha
    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getPaciente(self):
        return self.paciente
    
    def getFecha(self):
        return self.fecha
        
    def getDoctor(self):
        return self.doctor
    
    def getPConsulta(self):
        return self.PConsulta

    def getPOperacion(self):
        return self.POperacion

    def getPInterno(self):
        return self.PInternado
    def getTotal(self):
        return self.total
    def setPaciente(self,paciente):
        self.paciente = paciente
    
    def setDoctor(self,doctor):
        self.doctor = doctor

    def setPConsulta(self,consulta):
        self.PConsulta = consulta

    def setPOperacion(self,operacion):
        self.POperacion = operacion

    def setPInterno(self,interno):
        self.PInternado = interno
    
    