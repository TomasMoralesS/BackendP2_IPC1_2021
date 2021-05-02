#importando el modulo llamado Flask
from flask import Flask, jsonify , request
from flask_cors import CORS
from admin import admin
from doctor import doctor
from enfermera import enfermera
from paciente import paciente
from medicamento import medicamento
from pedido import pedido
from cita import cita
from factura import factura
from receta import receta
from enfermedad import enfermedad
from datetime import timedelta
import json
#Flask -> Nos sirve para crear la aplicacion servidor
#jsonify -> Nos sirve para mostrar la salida JSON mas ordenada
#request -> Nos sirve para obtener el body de la peticion HTTP

pacientes = []
admins = []
doctors = []
enfermeras = []
medicamentos = []
citas = []
recetas =[]
enfermedades = []
#Los pedidos son los medicamentos que el paciente quiere comprar pero que aun no estan confirmados
#es decir puede cancelar algun medicamento del pedido asi que el estado de compra no es definido
pedidos = []

#Las Compras son los pedidos que fueron confirmados es decir lo que ya se confirmo por comprar.

Compras = []
facturas = []
app = Flask(__name__)
CORS(app)
Id = 1
IdComprador = 1
IdProducto = 1
date = "1999,10,14"
date1 = "2000, 12, 18"
date2 = "1999, 4, 5"
admins.append(admin('Abner','Cardona',date,"M","admin","1234","",0,True))
admins.append(admin('Tomas Alexander','Morales Saquic',date,"M","201900364","MI CUI","42771650",0,True))
'''
Top 5 medicamentos más vendidos
• Top 3 doctores con más citas atendidas
• Enfermedades más comunes (se especificará en módulo de doctores)
'''
'''
medicamentos.append(medicamento("Medicina1",12,"Medicina y ya compa",40,4,12,0,1))
medicamentos.append(medicamento("Medicina2",12,"Medicina y ya compa",30,4,12,0,2))
medicamentos.append(medicamento("Medicina3",12,"Medicina y ya compa",20,4,12,0,3))
medicamentos.append(medicamento("Medicina4",12,"Medicina y ya compa",10,4,12,0,4))
medicamentos.append(medicamento("Medicina5",12,"Medicina y ya compa",50,4,12,0,5))

enfermedades.append(enfermedad("gripe",1))
enfermedades.append(enfermedad("Tos",2))
enfermedades.append(enfermedad("Dolor Estomacal",3))

pacientes.append(paciente('Pancha','Lopez',date1,"F","uno","contra","",3,False))
enfermeras.append(enfermera("NuevaEnfermera1","Apellido1",date2,'F',"PruebaEnfermera1","1234","",2,True))
enfermeras.append(enfermera("NuevaEnfermera2","Apellido1",date2,'F',"PruebaEnfermera2","1234","",2,True))
doctors.append(doctor("TOMAS","MORALES",date1,'M',"PruebaDoctor1","1234","especialidadDePrueba1","",1,True,1))
doctors.append(doctor("MARIANA","GONZALES",date1,'F',"PruebaDoctor2","1234","especialidadDePrueba2","12341234",1,True,2))
doctors.append(doctor("Adelayda","SAQUIC",date1,'F',"PruebaDoctor3","1234","especialidadDePrueba3 Y AGREGUEMOS MAS POR MAMONES XD","12341234",1,True,3))


pacientes.append(paciente('Pancha','Lopez',date1,"F","uno","contra","",3))
doctors.append(doctor("Diego","Morales",date2,"M","Dieguin","diegomorales","Cirugia","12345678",1))
enfermeras.append(enfermera("Adelayda","Morales",date,"F","Marisita","shrek","",2))
'''

@app.route('/cargaMasiva', methods=['POST'])
def agregar():
    
    global pacientes,admins,doctors,enfermeras,Id,citas

    if request.json['tipo'] == 3:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        fecha = request.json['fecha']
        sexo = request.json['sexo']
        Username = request.json['Username']
        contra = request.json['contra']
        tel = request.json['tel']
        tipo = request.json['tipo']
        pacientes.append(paciente(nombre, apellido, fecha, sexo, Username, contra, tel,tipo,True))
        return jsonify({'Mensaje':'Registro/Paciente exitosamente, se le redigira a la pagina de inicio de sesion'+
        ' para que pueda acceder a la plataforma','verdadero':True})

    if request.json['tipo'] == 1:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        fecha = request.json['fecha']
        sexo = request.json['sexo']
        Username = request.json['Username']
        contra = request.json['contra']
        tel = request.json['tel']
        tipo = request.json['tipo']
        especialidad = request.json['especialidad']
        doctors.append(doctor(nombre, apellido, fecha, sexo, Username, contra, especialidad,tel,tipo,True,0))

    if request.json['tipo'] == 2:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        fecha = request.json['fecha']
        sexo = request.json['sexo']
        Username = request.json['Username']
        contra = request.json['contra']
        tel = request.json['tel']
        tipo = request.json['tipo']
        enfermeras.append(enfermera(nombre, apellido, fecha, sexo, Username, contra,tel,tipo,True))

    if request.json['tipo'] == 4:
        nombre = request.json['nombre']
        precio = request.json['precio']
        descripcion = request.json['descripcion']
        cantidad = request.json['cantidad']
        tipo = request.json['tipo']
        identificador = Id
        Id = Id +1
        medicamentos.append(medicamento(nombre,precio,descripcion,cantidad,tipo,identificador,0,0))
        
    if request.json['tipo'] == 5:
        Npaciente= request.json['Npaciente']
        motivo = request.json['motivo']
        fecha = request.json['fecha']
        hora = request.json['hora']
        estado = request.json['estado']
        tipo = 5
        doctorPaciente = request.json['doctor']
        for i in range(len(citas)):
            if citas[i].getPaciente() == Npaciente:
                if citas[i].getEstado() == 3:
                    del citas[i]
        citas.append(cita(Npaciente,motivo,fecha,hora,estado,tipo,doctorPaciente))
        return jsonify({'Mensaje':'Su cita fue registrada, puede visualiar el estado de su cita en el apartado de :"Estado de cita"',})

        

    
    
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Registro/Paciente exitosamente, se le redigira a la pagina de inicio de sesion'+
    ' para que pueda acceder a la plataforma',})

@app.route('/Users', methods=['GET'])
def getUsername():
    # Tenemos nuestra lista en el entorno global, por eso hacemos referencia a ella con la palabra global
    global pacientes,admins,doctors,enfermeras,citas
    # Creamos un arreglo de Python para almacenar la informacion
    Datos = []
    # Hacemos un recorrido de nuestro arreglo
    for admin in admins:
        # Por cada objeto en nuestro arreglo, escribimos un objeto JSON, es decir clave-valor
        objeto = {
            'Username': admin.getUsername(),
            'contrasenia': admin.getContra(),
            'tipo':admin.getTipo()
        }
        # Agregamos el dato encontrado a la lista creada anteriormente.
        Datos.append(objeto)
    
    for doctor in doctors:
        objeto = {
            'Username': doctor.getUsername(),
            'contrasenia': doctor.getContra(),
            'tipo':doctor.getTipo()
        }
        Datos.append(objeto)
    
    for enfermera in enfermeras:
        objeto = {
            'Username': enfermera.getUsername(),
            'contrasenia': enfermera.getContra(),
            'tipo':enfermera.getTipo()
        }
        Datos.append(objeto)
    
    for paciente in pacientes:
        objeto = {
            'Username': paciente.getUsername(),
            'contrasenia': paciente.getContra(),
            'tipo': paciente.getTipo()
        }
        Datos.append(objeto)

    for paciente in citas:
        objeto = {
            'Username': paciente.getPaciente(),
            'fecha': paciente.getFecha(),
            'motivo':paciente.getMotivo(),
            'hora': paciente.getHora(),
            'tipo':paciente.getTipo(),
            'estado':paciente.getEstado(),
            'doctor':paciente.getDoctor()
        }
        Datos.append(objeto)

    # Le mandamos la informacion como respuesta, para este punto recorrio el arreglo y creo objetos JSON.    
    return(jsonify(Datos))

@app.route('/Personas/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre): 
    
    # Referencia al arreglo global
    global admins,doctors,enfermeras,pacientes,medicamentos
    # Recorrido del arreglo
    for admin in medicamentos:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if str(admin.getId()) == str(nombre):
            # Crear el objeto
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            objeto = {
            'nombre': admin.getNombre(),
            'precio':admin.getPrecio(),
            'cantidad':admin.getCantidad(),
            'descripcion':admin.getDescripcion(),
            'tipo':admin.getTipo(),
            'Id':admin.getId()
            
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))
    
    for admin in admins:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if admin.getUsername() == nombre:
            # Crear el objeto
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            objeto = {
            'nombre': admin.getNombre(),
            'apellido': admin.getApellido(),
            'fecha':admin.getFecha(),
            'sexo' :admin.getSexo(),
            'Username':admin.getUsername(),
            'contra':admin.getContra(),
            'tel':admin.getTel(),
            'tipo':admin.getTipo(),
            'seteo':admin.getSeteo()
            
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))
    for doctor in doctors:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if doctor.getUsername() == nombre:
            # Crear el objeto
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            objeto = {
            'nombre': doctor.getNombre(),
            'apellido': doctor.getApellido(),
            'fecha':doctor.getFecha(),
            'sexo' :doctor.getSexo(),
            'Username':doctor.getUsername(),
            'contra':doctor.getContra(),
            'especialidad':doctor.getEspecialidad(),
            'tel':doctor.getTel(),
            'tipo':doctor.getTipo(),
            'seteo':doctor.getSeteo()
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))

    for enfermera in enfermeras:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if enfermera.getUsername() == nombre:
            # Crear el objeto
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            objeto = {
            'nombre': enfermera.getNombre(),
            'apellido': enfermera.getApellido(),
            'fecha':enfermera.getFecha(),
            'sexo' :enfermera.getSexo(),
            'Username':enfermera.getUsername(),
            'contra':enfermera.getContra(),
            'tel':enfermera.getTel(),
            'tipo':enfermera.getTipo(),
            'seteo':enfermera.getSeteo()
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))

    for paciente in pacientes:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if paciente.getUsername() == nombre:
            # Crear el objeto
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            objeto = {
            'nombre': paciente.getNombre(),
            'apellido': paciente.getApellido(),
            'fecha':paciente.getFecha(),
            'sexo' :paciente.getSexo(),
            'Username':paciente.getUsername(),
            'contra':paciente.getContra(),
            'tel':paciente.getTel(),
            'tipo':paciente.getTipo(),
            'seteo':paciente.getSeteo()
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))
    # Si llega a este punto, quiere decir que nunca entro al for, entonces creamos un objeto        
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))

@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    # Hacemos referencia a nuestro usuario global
    global admins,doctors,enfermeras,pacientes,medicamentos
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(admins)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == admins[i].getUsername():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            admins[i].setNombre(request.json['nombre'])
            admins[i].setApellido(request.json['apellido'])
            admins[i].setFecha(request.json['fecha'])
            admins[i].setSexo(request.json['sexo'])
            admins[i].setUsername(request.json['Username'])
            admins[i].setContra(request.json['contra'])
            admins[i].setTel(request.json['tel'])
            admins[i].setTipo(request.json['tipo'])
            admins[i].setSeteo(request.json['seteo'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizaron los datos exitosamente','var':'verdadero'})
    
    

    for i in range(len(doctors)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == doctors[i].getUsername():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            doctors[i].setNombre(request.json['nombre'])
            doctors[i].setApellido(request.json['apellido'])
            doctors[i].setFecha(request.json['fecha'])
            doctors[i].setSexo(request.json['sexo'])
            doctors[i].setUsername(request.json['Username'])
            doctors[i].setContra(request.json['contra'])
            doctors[i].setEspecialidad(request.json['especialidad'])
            doctors[i].setTel(request.json['tel'])
            doctors[i].setTipo(request.json['tipo'])
            doctors[i].setSeteo(request.json['seteo'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizaron los datos exitosamente','var':'verdadero'})
    # Si llega a este punto, quiere decir que salio del for
    

    for i in range(len(enfermeras)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == enfermeras[i].getUsername():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            enfermeras[i].setNombre(request.json['nombre'])
            enfermeras[i].setApellido(request.json['apellido'])
            enfermeras[i].setFecha(request.json['fecha'])
            enfermeras[i].setSexo(request.json['sexo'])
            enfermeras[i].setUsername(request.json['Username'])
            enfermeras[i].setContra(request.json['contra'])
            enfermeras[i].setTel(request.json['tel'])
            enfermeras[i].setTipo(int(request.json['tipo']))
            enfermeras[i].setSeteo(request.json['seteo'])
            print(request.json['seteo'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizaron los datos exitosamente','var':'verdadero'})
    # Si llega a este punto, quiere decir que salio del for
    

    for i in range(len(pacientes)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == pacientes[i].getUsername():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            pacientes[i].setNombre(request.json['nombre'])
            pacientes[i].setApellido(request.json['apellido'])
            pacientes[i].setFecha(request.json['fecha'])
            pacientes[i].setSexo(request.json['sexo'])
            pacientes[i].setUsername(request.json['Username'])
            pacientes[i].setContra(request.json['contra'])
            pacientes[i].setTel(request.json['tel'])
            pacientes[i].setTipo(request.json['tipo'])
            pacientes[i].setSeteo(request.json['seteo'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizaron los datos exitosamente','var':'verdadero'})
    # Si llega a este punto, quiere decir que salio del for
    
    for i in range(len(medicamentos)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if str(medicamentos[i].getId()) == str(nombre):
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            #nombre,apellido,fecha,sexo,Username,contra,tel,tipo
            medicamentos[i].setNombre(request.json['nombre'])
            medicamentos[i].setCantidad(request.json['cantidad'])
            medicamentos[i].setPrecio(request.json['precio'])
            medicamentos[i].setDescripcion(request.json['descripcion'])
            
            
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizaron los datos exitosamente','var':'verdadero'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar','var':'falso'})

@app.route('/Personas', methods=['GET'])
def getPersonas():
    global admins,doctors,enfermeras,pacientes
    Datos = []
    for admin in admins:
        objeto = {
            'Contrasenia': admin.getContra(),
            'Username':admin.getUsername(),
            'tipo':admin.getTipo()
        }
        Datos.append(objeto)
    
    for admin in doctors:
        objeto = {
            'Contrasenia': admin.getContra(),
            'Username':admin.getUsername(),
            'tipo':admin.getTipo()
        }
        Datos.append(objeto)

    for admin in enfermeras:
        objeto = {
            'Contrasenia': admin.getContra(),
            'Username':admin.getUsername(),
            'tipo':admin.getTipo()
        }
        Datos.append(objeto)

    for admin in pacientes:
        objeto = {
            
            'Contrasenia': admin.getContra(),
            'Username':admin.getUsername(),
            'tipo':admin.getTipo()
        }
        Datos.append(objeto)

    return(jsonify(Datos))

@app.route('/Pacientes', methods=['GET'])
def getPacientes():
    global pacientes
    Datos = []
    
    for admin in pacientes:
        #,nombre,apellido,fecha,sexo,Username,contra,tel,tipo
        #contador,element.nombre,element.apellido,element.Username,element.sexo,element.contra]
        objeto = {
            'nombre':admin.getNombre(),
            'apellido':admin.getApellido(),
            'fecha':admin.getFecha(),
            'sexo':admin.getSexo(),
            'Username':admin.getUsername(),
            'contra': admin.getContra(),
            'tel':admin.getTel(),
            'tipo':admin.getTipo(),
            'seteo':admin.getSeteo()
        }
        Datos.append(objeto)

    return(jsonify(Datos))

@app.route('/Enfermeras', methods=['GET'])
def getEnfermeras():
    global enfermeras
    Datos = []
    
    for admin in enfermeras:
        #,nombre,apellido,fecha,sexo,Username,contra,tel,tipo
        objeto = {
            'nombre':admin.getNombre(),
            'apellido':admin.getApellido(),
            'fecha':admin.getFecha(),
            'sexo':admin.getSexo(),
            'Username':admin.getUsername(),
            'Contrasenia': admin.getContra(),
            'tel':admin.getTel(),
            'tipo':admin.getTipo(),
            'seteo':admin.getSeteo()
        }
        Datos.append(objeto)

    return(jsonify(Datos))

@app.route('/Doctores', methods=['GET'])
def getDoctores():
    global doctors
    Datos = []
    
    for admin in doctors:
        #,nombre,apellido,fecha,sexo,Username,contra,tel,tipo
        objeto = {
            'nombre':admin.getNombre(),
            'apellido':admin.getApellido(),
            'fecha':admin.getFecha(),
            'sexo':admin.getSexo(),
            'Username':admin.getUsername(),
            'Contrasenia': admin.getContra(),
            'especialidad':admin.getEspecialidad(),
            'tel':admin.getTel(),
            'tipo':admin.getTipo(),
            'citas':admin.getCitas()
        }
        Datos.append(objeto)

    return(jsonify(Datos))

@app.route('/Medicamentos', methods=['GET'])
def getMedicamentos():
    global medicamentos
    Datos = []
    
    for admin in medicamentos:
        #nombre,precio,descripcion,cantidad,tipo  
        
        objeto = {
            'nombre':admin.getNombre(),
            'precio':admin.getPrecio(),
            'descripcion':admin.getDescripcion(),
            'cantidad':admin.getCantidad(),
            'tipo':admin.getTipo(),
            'Id':admin.getId()
        }
        Datos.append(objeto)

    return(jsonify(Datos))

@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    # Referencia al arreglo global
    global admins,doctors,enfermeras,pacientes,medicamentos
    
    for i in range(len(admins)):
        # Validamos si es el nombre que queremos
        if nombre == admins[i].getUsername():
            # Usamos del para eliminar el objeto
            del admins[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})

    for i in range(len(doctors)):
        if nombre == doctors[i].getUsername():
            del doctors[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    
    for i in range(len(enfermeras)):
        if nombre == enfermeras[i].getUsername():
            del enfermeras[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})

    for i in range(len(pacientes)):
        if nombre == pacientes[i].getUsername():
            del pacientes[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})

    for i in range(len(medicamentos)):
        if str(medicamentos[i].getId()) == str(nombre):
            del medicamentos[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
            
    # Si llega a este punto, quiere decir que salio del for        
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Consumir/<string:nombre>',methods=['GET'])
def descontar(nombre):
    #nombre va a contener al usuario que compra y el id del medicamento entonces usaremos un split
    arreglo = nombre.split(',')
    nuevo = True
    user = arreglo[0]
    Idmedi = arreglo[1]
    listaMedicamentos = []
    #print("el usuario y el id son "+user+" -- "+Idmedi)
    global medicamentos,pacientes,pedidos,IdComprador,IdProducto

    for i in range(len(pacientes)):
        if str(pacientes[i].getUsername()) == str(user):
            #print("parada cero xd")
            for j in range(len(medicamentos)):
                if str(medicamentos[j].getId()) == str(Idmedi) :
                    #print("Se encontro al medicamento con id "+str(Idmedi))
                    if int(medicamentos[j].getCantidad())>0:
                        #print(str(len(pedidos)) +" tamanio actual")
                        if len(pedidos)>0:
                            for K in range(len(pedidos)):
                                #print("primera parada xd")
                                if len(pedidos)>0:
                                    if str(pedidos[K].getComprador()) == str(user) and pedidos[K].getSeguir() == True:
                                        #print("aca entramos UNO")
                                        nuevo = False
                                        Amedicamento = medicamento(medicamentos[j].getNombre(),medicamentos[j].getPrecio(),medicamentos[j].getDescripcion(),1,medicamentos[j].getTipo(),medicamentos[j].getId(),IdProducto,0)
                                        temp = pedidos[K].getMedicamentos()
                                        IdProducto = int(IdProducto+1)
                                        temp.append(Amedicamento)
                                        pedidos[K].setMedicamentos(temp) 
                                        medicamentos[j].setCantidad(int(medicamentos[j].getCantidad()) - 1 )
                                        aux =int(medicamentos[j].getVendido())+1
                                        medicamentos[j].setVendido(aux)

                                        #print("aca salimos UNO")
                                        #print("ahora quedan "+str(medicamentos[j].getCantidad()))
                                        return jsonify({'Mensaje':'true'})

                                    

                            if nuevo:
                                Amedicamento = medicamento(medicamentos[j].getNombre(),medicamentos[j].getPrecio(),medicamentos[j].getDescripcion(),1,medicamentos[j].getTipo(),medicamentos[j].getId(),IdProducto,0)
                                IdProducto = int(IdProducto+1)
                                listaMedicamentos.append(Amedicamento)
                                pedidos.append(pedido(user,listaMedicamentos,IdComprador,True))
                                IdComprador = int(IdComprador+1)
                                medicamentos[j].setCantidad (int(medicamentos[j].getCantidad()) - 1 )
                                aux =int(medicamentos[j].getVendido())+1
                                medicamentos[j].setVendido(aux)
                                #print("aca salimos DOS")
                                #print("ahora quedan "+str(medicamentos[j].getCantidad()))
                                return jsonify({'Mensaje':'true'})
                                    
                                    
                        else:
                            #print("aca vamos campeon")
                            Amedicamento = medicamento(medicamentos[j].getNombre(),medicamentos[j].getPrecio(),medicamentos[j].getDescripcion(),1,medicamentos[j].getTipo(),medicamentos[j].getId(),IdProducto,0)
                            IdProducto = int(IdProducto+1)
                            listaMedicamentos.append(Amedicamento)
                            pedidos.append(pedido(user,listaMedicamentos,IdComprador,True))
                            IdComprador = int(IdComprador+1)
                            medicamentos[j].setCantidad (int(medicamentos[j].getCantidad()) - 1 )
                            aux =int(medicamentos[j].getVendido())+1
                            medicamentos[j].setVendido(aux)
                            #print("ahora quedan "+str(medicamentos[j].getCantidad()))
                            return jsonify({'Mensaje':'true'})

                    else:
                        return jsonify({'Mensaje':'0'})

@app.route('/Compras/<string:nombre>',methods=['GET'])
def comprasM(nombre):
    global  pedidos
    complete = False
    Datos = []
    for admin in pedidos:
        #print("vamos a ir comprarando : "+str(admin.getComprador()) +" con el nombre "+str(nombre)+"el estado de la compra es ")
        imprimir = admin.getSeguir()
        if str(admin.getComprador()) == nombre and imprimir == True:
            Lmedicinas = admin.getMedicamentos()
            for i  in range(len(Lmedicinas)):
                complete = True
                objeto = {
                'Comprador': admin.getComprador(),
                'nombre':Lmedicinas[i].getNombre(),
                'precio':Lmedicinas[i].getPrecio(),
                'cantidad':Lmedicinas[i].getCantidad(),
                'IdProducto':Lmedicinas[i].getIdProducto(),
                'IdCompra':admin.getId()
                }
                Datos.append(objeto)
                

    if complete == False:
        objeto = {
        'Mensaje':"No se pudo carnal"
        }
        return(jsonify(Datos))
    else:
        return(jsonify(Datos))

@app.route('/Compras/<string:nombre>', methods=['DELETE'])
def EliminarCompra(nombre):
    # Referencia al arreglo global
    Ref = nombre.split(',')
    Comprador = Ref[0]
    Nlista = Ref[1]
    Nproducto = Ref[2]

    global pedidos,medicamentos
    
    for i in range(len(pedidos)):
        # Validamos si es el nombre que queremos
        if Comprador == pedidos[i].getComprador():
            if str(Nlista) == str(pedidos[i].getId()):
                lista = pedidos[i].getMedicamentos()
                for j in range(len(lista)):
                    if str(lista[j].getIdProducto()) == Nproducto:
                        for k in range(len(medicamentos)):
                            if lista[j].getId() == medicamentos[k].getId():
                                medicamentos[k].setCantidad(int(medicamentos[k].getCantidad())+1)
                                aux =int(medicamentos[k].getVendido())-1
                                medicamentos[j].setVendido(aux)
                                del lista[j]
                                pedidos[i].setMedicamentos(lista)
                                return jsonify({'Mensaje':'0'})
                        
@app.route('/Comprar/<string:datos>',methods=['GET'])
def RealizarCompra(datos):
    #los datos que necesito son el nombre del comprador y su lista
    arr = datos.split(',')
    nombre = arr[0]
    Idlista = arr[1]
    succes = False
    global pedidos,Compras
    for i in range(len(pedidos)):
        if str(pedidos[i].getComprador()) == str(nombre):
            if int(pedidos[i].getId()) == int(Idlista):
                print("encontro el producto")
                vigencia = pedidos[i].getSeguir()
                print("aca")
                if vigencia:
                    succes = True
                    Compras.append(pedidos[i])
                    pedidos[i].setSeguir(False)

    if succes:
        return jsonify({'Mensaje':'0'})               

    if not succes:
        return jsonify({'Mensaje':'1'})
            
@app.route('/Citas', methods=['GET'])
def getCitas():
    global citas
    Datos = []
    ListaDoc = []
    for doc in doctors:
        objeto0 = {
            'nombre':doc.getNombre(),
            'user':doc.getUsername()
        }
        ListaDoc.append(objeto0)

    for admin in citas:
        #paciente,motivo,fecha,hora,estado,tipo,doctor
        
        objeto = {
            'paciente':admin.getPaciente(),
            'motivo':admin.getMotivo(),
            'fecha':admin.getFecha(),
            'hora':admin.getHora(),
            'estado':admin.getEstado(),
            'doctor':admin.getDoctor()
        }
        Datos.append(objeto)

    return(jsonify({'Citas':Datos,'Docs':ListaDoc}))

@app.route('/ConsumirCitas/<string:data>', methods=['GET'])
def ConsumirCita(data):
    #necesito el nombre del paciente si su estado es aceptado entonces tambien el nombre del doctor y el estado 
    arr = data.split(',')
    paciente = arr[0]
    estado = arr[1]
    doc = arr[2]
    #si le manda 0 entonces es que quiere que cambie a aceptado si el estao es 2 entonces fue rechazado
    global citas,doctors
    if int(estado) == 0:
        for pendientes in citas:
            if str(pendientes.getPaciente()) == str(paciente):
                if 0 == int(pendientes.getEstado()):
                    pendientes.setEstado(1)
                    for docs in doctors:
                        if docs.getUsername() == doc:
                            doc = str(doc)+","+str(docs.getNombre())+","+str(docs.getApellido())
                            #le mandare el user, el nombre y el apellido.
                            pendientes.setDoctor(doc)
                            return jsonify({'Mensaje':'0'})      

    if int(estado) == 2:
        for pendientes in citas:
            if str(pendientes.getPaciente()) == str(paciente):
                if 0 == int(pendientes.getEstado()):
                    pendientes.setEstado(3)
                    pendientes.setDoctor("No se pudo agendar la cita")
                    return jsonify({'Mensaje':'1'})    

    return jsonify({'Mensaje':'2'})      

@app.route('/Facturacion', methods=['POST'])
def facturar():
    global facturas,doctors
    paciente = request.json['paciente']
    doc = request.json['doctor']
    PConsulta = request.json['PConsulta']
    POperacion = request.json['POperacion']
    PInternado = request.json['PInternado']
    total = request.json['Total']
    fecha = request.json['fecha']
    facturas.append(factura(paciente,doc,PConsulta,POperacion,PInternado,total,fecha))
    return jsonify({'Mensaje':'0'})
            
@app.route('/Facturas', methods=['GET'])
def getFact():
    global facturas
    Datos = []
    
    for doc in facturas:
        objeto0 = {
            'fecha':doc.getFecha(),
            'paciente' : doc.getPaciente(),
            'doctor' : doc.getDoctor(),
            'Consulta' : doc.getPConsulta(),
            'Operacion' : doc.getPOperacion(),
            'Internacion' : doc.getPInterno(),
            'Total' : doc.getTotal()
        }
        Datos.append(objeto0)

    return(jsonify({'Citas':Datos}))

@app.route('/recetas', methods=['POST'])
def agregarReceta():
    global recetas,enfermedades
    #self,paciente,doctor,fecha,padecimiento,descripcion,contador
    aux = request.json['padecimiento']
    padecimiento = aux.lower()
    padecimiento = padecimiento.replace(" ", "")
    paciente = request.json['paciente']
    doctor = request.json['doctor']
    descripcion = request.json['descripcion']
    fecha = request.json['fecha']

    if len(enfermedades)>0:
        cont = True
        for pivote in enfermedades:
            if str(pivote.getNombre()) == str(padecimiento):
                cont = False
                pivote.setContador(int(pivote.getContador() + 1))
                recetas.append(receta(paciente,doctor,fecha,padecimiento,descripcion))
                return jsonify({'Mensaje':'0'})
        if cont:
            recetas.append(receta(paciente,doctor,fecha,padecimiento,descripcion))
            enfermedades.append(enfermedad(padecimiento,1))
            return jsonify({'Mensaje':'0'})
            
    else:
        recetas.append(receta(paciente,doctor,fecha,padecimiento,descripcion))
        enfermedades.append(enfermedad(padecimiento,1))
        return jsonify({'Mensaje':'0'})

@app.route('/CompletarCita/<string:nombre>', methods=['PUT'])
def ActualizarCita(nombre):
    global citas,pacientes,doctors
    for cita in citas:
        if str(cita.getPaciente()) == str(nombre):
            if(int(cita.getEstado()) == 1):
                aux = request.json['estado']
                cita.setEstado(int (aux))
                for aux in doctors:
                    data = cita.getDoctor().split(',')
                    if str(aux.getUsername()) == str(data[0]):
                        pivote = int(aux.getCitas()) +1
                        aux.setCitas(pivote)
                        return jsonify({'Mensaje':'0'})

@app.route('/Reportes/<int:data>', methods=['GET'])
def Dreportes(data):    
    global medicamentos,doctors,enfermedades
    Datos = []
    if data == 1:
        if len(medicamentos)>=5:
            Ordenado = sorted(medicamentos, reverse=True)
            #,nombre,precio,descripcion,cantidad,tipo,Id,IdProducto,vendido
            for i in range(0,5):
                objeto = {
                'nombre':Ordenado[i].getNombre(),
                'precio':Ordenado[i].getPrecio(),
                'descripcion':Ordenado[i].getDescripcion(),
                'cantidad':Ordenado[i].getCantidad(),
                'vendido':Ordenado[i].getVendido()
                }
                Datos.append(objeto)
            return(jsonify({'Lista':Datos}))
        else:
            return(jsonify({'Lista':'0'}))

    if data == 2:
        if len(doctors)>=3:
            Ordenado = sorted(doctors, reverse=True)
            for i in range (0,3):
                #nombre,apellido,especialidad,usuario,citas
                objeto = {
                    'nombre' : Ordenado[i].getNombre(),
                    'apellido' : Ordenado[i].getApellido(),
                    'usuario' : Ordenado[i].getUsername(),
                    'citas' : Ordenado[i].getCitas(),
                    'especialidad' : Ordenado[i].getEspecialidad() 
                }
                Datos.append(objeto)
            return(jsonify({'Lista':Datos}))
        else:
            return(jsonify({'Lista':'0'}))

    if data == 3:
        if len(enfermedades)>=3:
            Ordenado = sorted(enfermedades, reverse=True)
            #enfermedad,contador
            for i in range (0,3):
                objeto = {
                    'enfermedad' : Ordenado[i].getNombre(),
                    'contador' : Ordenado[i].getContador()
                }
                Datos.append(objeto)
            return(jsonify({'Lista':Datos}))
        else:
            return(jsonify({'Lista':'0'}))

if __name__ == '__main__':
    app.run(debug = True, port = 3000)

