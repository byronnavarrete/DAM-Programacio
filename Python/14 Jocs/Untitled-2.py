#!/usr/bin/env python3
import os
import random

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Definició de les propietats amb els preus i lloguers
class Propietat:
    def __init__(self, nom, lloguer_casa, lloguer_hotel, comprar_terreny, comprar_casa, comprar_hotel):
        self.nom = nom
        self.lloguer_casa = lloguer_casa
        self.lloguer_hotel = lloguer_hotel
        self.comprar_terreny = comprar_terreny
        self.comprar_casa = comprar_casa
        self.comprar_hotel = comprar_hotel
        self.propietari = None  # No té propietari al principi

# Definim les propietats segons la taula de preus
propietats = {
    "Lauria": Propietat("Lauria", 10, 15, 50, 200, 250),
    "Rosselló": Propietat("Rosselló", 10, 15, 50, 225, 255),
    "Marina": Propietat("Marina", 15, 15, 50, 250, 260),
    "C. de cent": Propietat("C. de cent", 15, 20, 50, 275, 265),
    "Muntaner": Propietat("Muntaner", 20, 20, 60, 300, 270),
    "Aribau": Propietat("Aribau", 20, 20, 60, 325, 275),
    "Sant Joan": Propietat("Sant Joan", 25, 25, 60, 350, 280),
    "Aragó": Propietat("Aragó", 25, 25, 60, 375, 285),
    "Urquinaona": Propietat("Urquinaona", 30, 25, 70, 400, 290),
    "Fontana": Propietat("Fontana", 30, 30, 70, 425, 300),
    "Les Rambles": Propietat("Les Rambles", 35, 30, 70, 450, 310),
    "Pl. Catalunya": Propietat("Pl. Catalunya", 35, 30, 70, 475, 320),
    "P. Àngel": Propietat("P. Àngel", 40, 35, 80, 500, 330),
    "Via Augusta": Propietat("Via Augusta", 40, 35, 80, 525, 340),
    "Balmes": Propietat("Balmes", 50, 40, 80, 550, 350),
    "Pg. de Gràcia": Propietat("Pg. de Gràcia", 50, 50, 80, 525, 360)
}

# Taulell del Monopoly
def imprimir_taula_monopoly(jugadors):
    taula = [
        ["Parking", "Urquinaona", "Fontana", "Sort", "Rambles", "Pl.Catalunya", "Anr próx"],
        ["Aragó", "", "", "", "", "", "Angel"],
        ["S.Joan", "", "", "", "", "", "Augusta"],
        ["Caixa", "", "", "", "", "", "Caixa"],
        ["Aribau", "", "", "", "", "", "Balmes"],
        ["Muntaner", "", "", "", "", "", "Gracia"],
        ["Presó", "Consell", "Marina", "Sort", "Rosselló", "Lauria", "Sortida"]
    ]

    # Afegir la informació dels jugadors a les caselles buides
    for fila in range(len(taula)):
        for col in range(len(taula[fila])):
            if taula[fila][col] == "":  # Casella buida
                taula[fila][col] = mostrar_info_jugadors(jugadors)

    # Mostra la taula
    for fila in taula:
        print("+--------" * len(fila) + "+")
        for element in fila:
            print(f"|{element:^8}", end="")
        print("|")
    print("+--------" * len(fila) + "+")

# Afegir informació dels jugadors en caselles buides
def mostrar_info_jugadors(jugadors):
    info = ""
    for jugador in jugadors:
        info += f"{jugador.color[0]}{jugador.saldo}€ "  # Mostrem la inicial del color i el saldo
    return info.strip()

# Classe del Banc
class Banco:
    def __init__(self):
        self.dinero = 10000000

    def ajustar_dinero(self):
        if self.dinero < 500000:
            self.dinero += 1000000

# Classe Jugador
class Jugador:
    def __init__(self, nom, color):
        self.nom = nom
        self.color = color
        self.saldo = 2000
        self.posicio = (6, 6)  # Comença a la casella de sortida
        self.carrers = []
        self.presó = False

    def moure(self, valor_dau, recorregut):
        index_posicio = recorregut.index(self.posicio)
        nova_posicio = (index_posicio + valor_dau) % len(recorregut)
        self.posicio = recorregut[nova_posicio]

    def comprar_propietat(self, propietat):
        if self.saldo >= propietat.comprar_terreny:
            propietat.propietari = self
            self.saldo -= propietat.comprar_terreny
            self.carrers.append(propietat.nom)
            print(f"{self.nom} ha comprat {propietat.nom} per {propietat.comprar_terreny}€.")
        else:
            print(f"{self.nom} no té prou diners per comprar {propietat.nom}.")

# Funció per tirar els daus
def tirar_daus():
    dau1 = random.randint(1, 6)
    dau2 = random.randint(1, 6)
    return dau1, dau2

# Funció per triar el color del jugador
def seleccionar_color_jugador(nom):
    colors_disponibles = ["Groc", "Taronja", "Vermell", "Blau", "Negre"]
    color_seleccionat = None
    while color_seleccionat not in colors_disponibles:
        print(f"{nom}, tria un color: {', '.join(colors_disponibles)}")
        color_seleccionat = input("Color: ").capitalize()
        if color_seleccionat not in colors_disponibles:
            print(f"Color no vàlid. Tria entre {', '.join(colors_disponibles)}.")
        else:
            colors_disponibles.remove(color_seleccionat)  # Elimina el color seleccionat de les opcions
    return color_seleccionat

# Funció per configurar els jugadors
def crear_jugadors():
    jugadors = []
    num_jugadors = int(input("Quants jugadors participaran? (2-5): "))
    for i in range(num_jugadors):
        nom_jugador = input(f"Introdueix el nom del Jugador {i + 1}: ")
        color_jugador = seleccionar_color_jugador(nom_jugador)
        jugadors.append(Jugador(nom_jugador, color_jugador))
    return jugadors

# Recorrer el taulell
recorregut = [
    (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0),  # Inferior
    (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0),  # Esquerra
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),  # Superior
    (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)  # Dreta
]

# Funció per comprovar si la posició actual té propietat
def comprovar_propietat(jugador):
    posicio_actual = recorregut[jugador.posicio[0]][jugador.posicio[1]]
    if posicio_actual in propietats:
        propietat = propietats[posicio_actual]
        if propietat.propietari is None:
            jugador.comprar_propietat(propietat)
        else:
            print(f"{jugador.nom ha de pagar lloguer de {propietat.lloguer_casa}€ a {propietat.propietari.nom}.")
            jugador.saldo -= propietat.lloguer_casa
            propietat.propietari.saldo += propietat.lloguer_casa

# Funció principal
def joc():
    banc = Banco()
    jugadors = crear_jugadors()
    
    while True:
        imprimir_taula_monopoly(jugadors)
        
        for jugador in jugadors:
            print(f"\nTorn de {jugador.nom}.")
            dau1, dau2 = tirar_daus()
            print(f"Has tret un {dau1} i un {dau2} (total: {dau1 + dau2})")
            jugador.moure(dau1 + dau2, recorregut)
            comprovar_propietat(jugador)
            
            # Mostra saldo i estat del banc
            print(f"Saldo del banc: {banc.dinero}€")
            for jug in jugadors:
                print(f"{jug.nom}: {jug.saldo}€")

            continuar = input("Vols continuar? (s/n): ")
            if continuar.lower() != "s":
                print("\nFi de la partida!")
                return

if __name__ == "__main__":
    joc()
