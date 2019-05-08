
import os
import numpy as np
pathClientes = './data/clientes.csv'
pathLibros = './data/libros.csv'
pathLibros = './data/prestamos.csv'
pathHistorial = './data/historial.csv'
arreglo_clientes=open(pathClientes,'r')

def ingresarCliente():
    print('INGRESE LOS DATOS DEL CLIENTE')
    cedula = input('CEDULA: ')
    nombre = input('NOMBRE: ')
    anio = input('AÑO DE NACIMIENTO: ')

def editarCliente():
    print('EDITAR CLIENTE')
    cedula = input('Ingrese la cedula del cliente a editar')
    consultarCliente(cedula)

def consultarCliente(cedula):
    for item in arreglo_clientes.readlines():
        if(item.split(',')[0]==cedula):
            print(item)
switchCliente = {
    '1':ingresarCliente,
    '2':editarCliente
}
def opcionCliente(op):
    func = switchCliente.get(op,'nothing')
    return func()
def registrarCliente():
    print('REGISTRAR CLIENTE')
    print('1.-Ingresar.')
    print('2.-Editar.')
    print('3.-Eliminar.')
    op=input('Elija una opcion... ')
    os.system('cls')
    opcionCliente(op)

def registrarLibro():
    print('REGISTRAR LIBRO')
    print('1.-Ingresar.')
    print('2.-Editar.')
    print('3.-Eliminar.')
    input('Elija una opcion')
    os.system('cls')
def prestarLibro():
    print('PRESTAR LIBRO')
def devolverLibro():
    print('DEVOLVER LIBRO')
switch = {
        '1':registrarCliente,
        '2':registrarLibro,
        '3':prestarLibro,
        '4':devolverLibro
    }
def elegirOpcion(op):
    func=switch.get(op,"nothing")
    return func()    
def menuPrincipal():
    print('1.-Registrar cliente.')
    print('2.-Registrar libro.')
    print('3.-Prestar Libro.')
    print('4.-Devolver Libro.')
    opcion = input('Elija una opcion... ')
    os.system('cls')
    elegirOpcion(opcion)


menuPrincipal()
    
