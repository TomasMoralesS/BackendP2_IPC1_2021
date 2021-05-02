#PARA NO PERDER LA REFERENCIA A JAVA USAMOS CLASES
class doctor:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    
    def __init__(self,nombre,apellido,fecha,sexo,Username,contra,especialidad,tel,tipo,seteo,citas):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.sexo = sexo
        self.Username = Username
        self.contra = contra
        self.tel = tel
        self.tipo = tipo
        self.especialidad = especialidad
        self.seteo =seteo
        self.citas = citas
    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getSeteo(self):
        return self.seteo
    def setSeteo(self,seteo):
        self.seteo = seteo
    def getCitas(self):
        return self.citas
    def setCitas(self,citas):
        self.citas = citas
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getFecha(self):
        return self.fecha

    def getSexo(self):
        return self.sexo

    def getUsername(self):
        return self.Username
    
    def getContra(self):
        return self.contra
    
    def getTel(self):
        return self.tel

    def getTipo(self):
        return self.tipo

    def getEspecialidad(self):
        return self.especialidad


    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setFecha(self,fecha):
        self.fecha = fecha
    
    def setSexo(self,sexo):
        self.sexo = sexo
    
    def setUsername(self , Username):
        self.Username = Username
    
    def setContra(self, contra):
        self.contra = contra
    
    def setTel(self , tel):
        self.tel = tel
    
    def setEspecialidad(self , especialidad):
        self.especialidad = especialidad

    def setTipo(self,tipo):
        self.tipo = tipo

    def __gt__(self, doctor):
        return self.citas > doctor.citas