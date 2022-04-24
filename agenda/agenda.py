'''
script en python que implemente una agenda de contactos haciendo uso de un diccionario. Para el diccionario las llaves sera los nombres y 
como valor estara una tupla que contenga el numero de telefono y el contacto electronico. La agenda se guardara en un archivo JSON del 
cual se podran recuperar los contactos y en el cual se podran agregar los nuevos contactos.Se mantendra un menu con las siguientes opciones:

1) Agregar contacto
2) Mostrar contactos
3) buscar un contacto
4) eliminar contacto
0) salir
'''

import json
from contacto import *
import pathlib
import os

class Agenda:

    SALIR = 0 
    AGREGAR = 1
    MOSTRAR = 2
    BUSCAR = 3
    ELIMINAR = 4

    def __init__(self):
        self._contactos = []
        self.recuperarContactos('contactos.json')


    #destructor de clase
    def __del__(self):
        self.almacenarContactos('contactos.json')


    @property
    def contactos(self):
        return self._contactos
    
    @contactos.setter
    def contactos(self, valor):
        self._contactos = valor

    @contactos.deleter
    def contactos(self):
        del self._contactos


    def recuperarContactos(self, nombreArchivo):
        if pathlib.Path(nombreArchivo).exists(): #se fija si existe esa base de datos
            with open(nombreArchivo, 'r') as archivo:
                datos = json.load(archivo)  #carga el archivo de esa ruta en la variable datos
            for cont in datos['contactos']:
                self.contactos.append(desdeJSON(cont))


    def almacenarContactos(self, nombreArchivo):
        with open(nombreArchivo,'w') as archivo:
            json.dump({'contactos':self.contactos}, archivo, cls=ContactoEncoder, indent=4 )#tercer parametro indica como tiene que escribir el formato. Cuarto parametro sirve para mostrar de forma organizada la estructura json


    def agregarContacto(self):
        os.system('cls')
        print('Agregar contacto')
        nombre = input('Nombre: ')
        numero = input('Numero: ')
        email = input('Email: ')
        self.contactos.append(Contacto(nombre,numero,email))

    
    def mostrarContactos(self):
        os.system('cls')
        print('Mis contactos')
        if (len(self.contactos) == 0):
            print('No hay contactos agendados!')
        else:
            for cont in self.contactos:
                print(f'{cont}')
                print('-'*50)

    '''
    def desdeJSON2(nombreArchivo):
        lista = []
        with open(nombreArchivo, 'r') as archivo:
                datos = json.load(archivo)  #carga el archivo de esa ruta en la variable datos
                for cont in datos['contactos']:
                    lista.append(cont)

        return lista
    '''


    def buscarContacto(self):
        os.system('cls')
        print('Mis contactos')
        nombre = input('Ingrese nombre a buscar: ')
        if (len(self.contactos) == 0):
            print('No hay contactos agendados!')
        else:
            pos = 1
            for i in self.contactos:
                if(i["nombre"] == nombre):
                    print(f'{i["nombre"]}, en la posicion {pos}')
                    pos += 1
                else: 
                    pos += 1


    '''

    def buscarContacto(self, nombreArchivo):
        os.system('cls')
        print('Buscar contacto')
        with open(nombreArchivo) as arch:
            json.load(arch)
            if(len(self.contactos) == 0):
                print('No se ingresaron contactos!')
            else:
                nombre = input('Nombre: ')
                coincidencias = 0
                for con, datos in arch:
                    if(con == nombre):
                        print(f'Nombre: {con}')
                        print(f'Telefono: {datos[0]}')
                        print(f'Email: {datos[1]}')
                        coincidencias += 1
                        print('-'*50)
                if (coincidencias == 0):
                    print('No se encontro el contacto')
                else:
                    print(f'Se encontraron {coincidencias} contactos!')



     
    def eliminarContacto(agenda, nombreArchivo):
        os.system('cls')
        print('Eliminar contacto')
        contacto = input('Ingrese el nombre del contacto a eliminar: ')

        with open(nombreArchivo,'+r') as archivo:
            for i , k in agenda.items():
                if(i == contacto):
                    print(f'{i} , {k}')


    '''


    def menu(self):
        total = 0
        continuar = True
        while continuar:
            os.system('cls')
            print(f''' Mi agenda
{Agenda.AGREGAR}) Agregar contacto
{Agenda.MOSTRAR}) Mostar contacto
{Agenda.BUSCAR}) Buscar contacto
{Agenda.ELIMINAR}) Eliminar contacto
{Agenda.SALIR}) Salir
            ''')
            opc = int(input('Seleccione la opcion: '))
            try:
                opc = int(opc)
            except:
                opc = -1
            if opc == Agenda.AGREGAR:
                self.agregarContacto()
                total += 1
            elif opc == Agenda.MOSTRAR:
                self.mostrarContactos()
            elif opc == Agenda.BUSCAR:
                self.buscarContacto()
            elif opc == Agenda.SALIR:
                continuar = False
            else:
                os.system('cls')
                print('Opcion no valida!')
            input('Presiona enter para continuar...')
        print('Adios!')

        '''
            elif opc == Agenda.ELIMINAR:
                self.eliminarContacto()'''