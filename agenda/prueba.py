persona = [ {
    "nombre": "facundo",
    "numero": "2222323",
    "email": "faculezcano2@gmail.com"
},
{
    "nombre": "leandro",
    "numero": "2222323",
    "email": "faculezcano2@gmail.com"
},
{
    "nombre": "jaimito",
    "numero": "2222323",
    "email": "faculezcano2@gmail.com"
},
{
    "nombre": "facundo",
    "numero": "2222323",
    "email": "faculezcano2@gmail.com"
}
]


def averiguarNombre():
    print(len(persona))
    nombreABuscar = input('nombre a buscar: ')
    pos = 1
    for i in persona:
        if(i["nombre"] == nombreABuscar):
            print(f'{i["nombre"]}, en la posicion {pos}')
            pos += 1
        else: 
            pos += 1
        #print(persona[f'{i}']["nombre"])



def main():
    averiguarNombre()

if __name__ == '__main__':
    main()