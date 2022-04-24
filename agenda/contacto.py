'''
contacto.py

mdodelo sencillo de un contacto
atributos:
    nombre:  --nombre del contacto a agendar
    numero:  --numero del contacto a agregar
    email:   --email del contacto a agregrar
'''

import json

class Contacto:
    def __init__(self, nombre='', numero='', email=''):
        self._nombre = nombre
        self._numero = numero
        self._email = email
    


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @nombre.deleter
    def nombre(self):
        del self._nombre



    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor
    
    @numero.deleter
    def numero(self):
        del self._numero

    

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor
    
    @email.deleter
    def email(self):
        del self._email

    

    def __str__(self):
        ESPACIOS = 8 
        return f'''{"nombre: " : <{ESPACIOS}}{self.nombre}
{"numero: " : <{ESPACIOS}}{self.numero}
{"email: " : <{ESPACIOS}}{self.email}'''


#serializacion de la informacion: convertir la info de formato python a formato JSON
class ContactoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contacto): #se fija si el objeto es de tipoo Contacto 
            return {'nombre':obj.nombre, 'numero':obj.numero, 'email':obj.email } #lo pone del formato que debe ser
        return json.JSONEncoder.default(self, obj) #sino devuelve lo que se escribio


#convertir a partir del formato JSON a un Contacto
def desdeJSON(diccionario):
    return Contacto(diccionario['nombre'], diccionario['numero'], diccionario['email'])
