#!/usr/bin/env python3

import os
import platform
import random

nom = ""
cognoms = ""
dni = ""

# Aquesta funció neteja la pantalla, no la modifiquis
def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

clearScreen()

import random
import string

pets = {}

def createCode():
    """
    Genera un codi aleatori de mascota amb el format NNNLLL-A, on:
    
    - Les NNN són tres dígits aleatoris entre 0 i 9.
    - Les LLL són tres lletres majúscules aleatòries de l'alfabet anglès (sense Ñ ni Ç).
    - A és un número entre 1 i 15, que representa l'any de naixement de la mascota.

    Paràmetres:
        No rep cap paràmetre.

    Funcionament:
        Es generen tres números aleatoris, tres lletres majúscules aleatòries, i un número aleatori entre 1 i 15.
        Aquests valors es concatenen per formar el codi en el format NNNLLL-A.

    Retorn:
        Retorna un string que conté el codi generat.

    Exemple:
        createCode()
        '534LTH-11'
    """
    pass

def createName():
    """
    Genera un nom aleatori per a una mascota d'una llista predefinida de noms.

    Paràmetres:
        No rep cap paràmetre.

    Funcionament:
        Selecciona un nom aleatori de la llista de noms següent:
        ["Max", "Bella", "Luna", "Charlie", "Lucy", "Cooper", "Bailey", "Daisy", "Sadie", "Oliver"]

    Retorn:
        Retorna un string que conté el nom aleatori seleccionat.

    Exemple:
        createName()
        'Charlie'
    """
    pass

def createAge():
    """
    Genera una edat aleatòria per a una mascota.

    Paràmetres:
        No rep cap paràmetre.

    Funcionament:
        Retorna un número aleatori entre 1 i 15, que representa l'edat de la mascota.

    Retorn:
        Retorna un enter que conté l'edat generada.

    Exemple:
        createAge()
        7
    """
    pass

def createType():
    """
    Genera un tipus de mascota aleatori d'una llista predefinida.

    Paràmetres:
        No rep cap paràmetre.

    Funcionament:
        Selecciona un tipus de mascota aleatori de la llista següent:
        ["gos", "gat", "conill", "hamster", "ocell"]

    Retorn:
        Retorna un string que conté el tipus de mascota seleccionat.

    Exemple:
        createType()
        'gat'
    """
    pass

def createActivities():
    """
    Genera una llista d'activitats aleatòries per a una mascota.

    Paràmetres:
        No rep cap paràmetre.

    Funcionament:
        Selecciona entre 2 i 5 activitats aleatòries de la llista següent, sense repetir:
        ["Correr", "Saltar", "Nedar", "Caçar", "Jugar a la pilota", "Dormir"]

    Retorn:
        Retorna una llista amb les activitats seleccionades.

    Exemple:
        createActivities()
        ['Correr', 'Jugar a la pilota', 'Dormir']
    """
    pass

def addPets(number):
    """
    Afegeix un nombre determinat de mascotes al diccionari global 'pets'.

    Paràmetres:
        - number: Un enter que indica el nombre de mascotes a afegir.

    Funcionament:
        Genera mascotes aleatòries amb els atributs 'name', 'age', 'type' i 'activities'.
        Assigna un codi únic per a cada mascota mitjançant la funció createCode().
        Afegeix cada mascota al diccionari global 'pets', amb el codi com a clau.

    Retorn:
        Retorna una llista amb els codis de les mascotes afegides.

    Exemple:
        addPets(3)
        (addPets) 3 pets added
        ['534LTH-11', '057MRP-16', '805XAY-58']
    """
    pass

def searchPets(param, value):
    """
    Busca mascotes al diccionari 'pets' que coincideixin amb el valor donat per un paràmetre especificat.

    Paràmetres:
        - param: Un string que indica el paràmetre de cerca (per exemple: 'name', 'age', 'type', 'activities').
        - value: El valor que ha de coincidir amb el paràmetre donat per a realitzar la cerca.

    Funcionament:
        Recorre totes les mascotes al diccionari 'pets' i comprova si el valor del paràmetre especificat coincideix amb el valor donat.
        Si hi ha coincidències, afegeix el codi de la mascota a una llista de resultats.

    Retorn:
        No retorna res explícitament, però imprimeix el nombre de mascotes trobades i els seus codis.

    Exemple:
        searchPets('name', 'Charlie')
        (searchPets) Found 1: ['534LTH-11']
    """
    pass

def modifyPets(code, param, value):
    """
    Modifica una mascota existent al diccionari 'pets' segons el paràmetre i valor donats.

    Paràmetres:
        - code: El codi de la mascota a modificar.
        - param: El paràmetre a modificar (per exemple: 'name', 'age', 'type', 'activities').
        - value: El nou valor per assignar al paràmetre indicat. Per a 'activities', el valor ha de ser una llista separada per comes.

    Funcionament:
        Si la mascota amb el codi donat existeix, es modifica el paràmetre especificat.
        Si es vol modificar 'activities', es converteix el valor en una llista separada per comes.
        Si el codi no existeix, es mostra un missatge d'error.

    Retorn:
        No retorna res explícitament, però imprimeix un missatge indicant si la mascota ha estat modificada o no trobada.

    Exemple:
        modifyPets('534LTH-11', 'name', 'Rocky')
        (modifyPets) Pet 534LTH-11 modified
    """
    pass

def deletePets(codes):
    """
    Elimina mascotes del diccionari 'pets' segons els codis donats.

    Paràmetres:
        - codes: Una llista de codis de mascotes que es volen eliminar.

    Funcionament:
        Recorre els codis donats i elimina la mascota del diccionari si el codi existeix.
        Si s'elimina alguna mascota, s'afegeix el codi a una llista de mascotes eliminades.

    Retorn:
        No retorna res explícitament, però imprimeix una llista de codis de mascotes que han estat eliminades.

    Exemple:
        deletePets(['534LTH-11'])
        (deletePets) Pets deleted: ['534LTH-11']
    """
    pass

def mainRun():
    """
    Mostra un menú d'opcions per gestionar el diccionari de mascotes 'pets'.

    Paràmetres:
        No rep cap paràmetre.

    Funcionament:
        El programa mostra un menú interactiu amb les opcions següents:
        - 1) Llista: Llista totes les mascotes registrades.
        - 2) Afegir: Permet afegir noves mascotes al diccionari 'pets'.
        - 3) Modificar: Modifica les dades d'una mascota existent.
        - 4) Esborrar: Elimina una mascota pel seu codi.
        - 5) Buscar: Cerca mascotes segons un paràmetre i valor especificats.
        - 0) Sortir: Finalitza l'execució del programa.

        Segons l'opció seleccionada, el programa demana informació addicional si cal (nombre de mascotes a afegir, codi de la mascota a modificar o esborrar, etc.).
        Si es selecciona una opció no vàlida, es mostra un missatge d'error.

    Retorn:
        No retorna res explícitament, però gestiona el diccionari global 'pets' i realitza les operacions seleccionades.

    Exemple d'execució:
        Gestió de mascotes:
        1) Llista
        2) Afegir
        3) Modificar
        4) Esborrar
        5) Buscar
        0) Sortir
        Escull una opció [0-5]: 2
        Quantes mascotes vols afegir? 3
        (addPets) 3 pets added
    """
    pass

if __name__ == '__main__':
    mainRun()