class enfermedad:
    def __init__(self,nombre,contador):
        self.nombre = nombre
        self.contador = contador
    
    def getNombre(self):
        return self.nombre

    def getContador(self):
        return self.contador
        
    def setContador(self,contador):
        self.contador = contador
    
    def __gt__(self, enfermedad):
        return self.contador > enfermedad.contador