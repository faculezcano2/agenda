'''
main.py

script que permite el registro y consultas de contactos de una agenda.
Los contacots seran modelados dentro de una clase y podran ser almacenados en un archivo con formato JSON y recuperados desde el mismo.
La agenda sera modelada dentro de una clase que podra administrar los objetos de tibo contacto.
'''

from agenda import Agenda

def main():
    ag = Agenda()
    ag.menu()


if __name__ == '__main__':
    main()