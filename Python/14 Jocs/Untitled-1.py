#!/usr/bin/env python3
import os
import random

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
propietats
def imprimir_taula_monopoly(jugador_posicions):
    taula = [
        ["Parking", "Urquinaona", "Fontana", "Sort", "Rambles", "Pl.Catalunya", "Anr próx"],
        ["Aragó", "", "", "", "", "", "Angel"],
        ["S.Joan", "", "", "", "", "", "Augusta"],
        ["Caixa", "", "", "", "", "", "Caixa"],
        ["Aribau", "", "", "", "", "", "Balmes"],
        ["Muntaner", "", "", "", "", "", "Gracia"],
        ["Presó", "Consell", "Marina", "Sort", "Roselló", "Lauria", "Sortida"]
    ]
    
    # Afegim la posició dels jugadors a la taula
    for jugador, pos in jugador_posicions.items():
        fila, columna = pos
        if taula[fila][columna]:
            taula[fila][columna] += " " + jugador[0]  # Afegim la inicial del nom del jugador
        else:
            taula[fila][columna] = jugador[0]
    
    for fila in taula:
        print("+--------" * len(fila) + "+")
        for element in fila:
            print(f"|{element:^8}", end="")
        print("|")
    print("+--------" * len(taula[0]) + "+")

class Banco:
    def __init__(self):
        self.dinero = 10000000

    def ajustar_dinero(self):
        if self.dinero < 500000:
            self.dinero += 1000000

class Jugador:
    def __init__(self, nom, color):
        self.nom = nom
        self.color = color
        self.saldo = 2000
        self.posicio = (6, 6)  # Comença a la casella "Sortida"
        self.carrers = []
        self.presó = False
        self.turns_presó = 0

    def moure(self, valor_dau, recorregut):
        index_posicio = recorregut.index(self.posicio)
        nova_posicio = (index_posicio + valor_dau) % len(recorregut)
        self.posicio = recorregut[nova_posicio]

jugadors = [
    Jugador("Groc", "G"),
    Jugador("Taronja", "T"),
    Jugador("Vermell", "V"),
    Jugador("Blau", "B")
]

def tirar_daus():
    dau1 = random.randint(1, 6)
    dau2 = random.randint(1, 6)
    return dau1, dau2

# Definim el recorregut en ordre per les caselles del taulell
recorregut = [
    (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0),  # Inferior
    (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0),  # Esquerra
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),  # Superior
    (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)  # Dreta
]

propietats = {
    (4, 0): Propietat("Aribau", 325, 20),
    (4, 6): Propietat("Balmes", 550, 50),
    # Altres propietats...
}

# Bucle principal del joc
banc = Banco()
jugador_posicions = {jug.nom: jug.posicio for jug in jugadors}
random.shuffle(jugadors)

while True:
    for jugador in jugadors:
        clearScreen()
        imprimir_taula_monopoly(jugador_posicions)
        
        print(f"\nTorn de {jugador.nom}!")
        input("Prem Enter per tirar els daus...")
        dau1, dau2 = tirar_daus()
        valor_daus = dau1 + dau2
        print(f"{jugador.nom} ha tret {dau1} i {dau2}. Es mou {valor_daus} espais.")
        
        # Mou el jugador
        jugador.moure(valor_daus, recorregut)
        jugador_posicions[jugador.nom] = jugador.posicio
        
        # Comprovar propietat
        comprovar_propietat(jugador)
        
        # Ajustar diners del banc si cal
        banc.ajustar_dinero()

        # Mostrar saldo
        print(f"Saldo de {jugador.nom}: {jugador.saldo}€")
        print(f"Saldo del banc: {banc.dinero}€")
        
        # Continuar jugant?
        continuar = input("Vols continuar? (s/n): ")
        if continuar.lower() != "s":
            print("\nFi de la partida!")
            break
    if continuar.lower() != "s":
        break
if __name__ == "__main__":
    mainRun()