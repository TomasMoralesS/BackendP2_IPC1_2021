class medicamento:
    def __init__(self,nombre,precio,descripcion,cantidad,tipo,Id,IdProducto,vendido):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.tipo = tipo
        self.Id = Id
        self.IdProducto = IdProducto
        self.vendido = vendido

    def getIdProducto(self):
        return self.IdProducto

    def setIdProducto(self,id):
        self.IdProducto = id
    def getNombre(self):
        return self.nombre
    
    def getVendido(self):
        return self.vendido
    def setVendido(self,vendido):
        self.vendido = vendido
    def getPrecio(self):
        return self.precio
    
    def getDescripcion(self):
        return self.descripcion

    def getCantidad(self):
        return self.cantidad

    def getTipo(self):
        return self.tipo
    def getId(self):
        return self.Id

    def setId(self,Id):
        self.Id = Id
    
    def setNombre(self,nombre):
        self.nombre = nombre

    def setPrecio(self,precio):
        self.precio = precio

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    
    def setCantidad(self,cantidad):
        self.cantidad = cantidad

    def setTipo(self,tipo):
        self.tipo = tipo

    def __gt__(self, medicamento):
        return self.vendido > medicamento.vendido    