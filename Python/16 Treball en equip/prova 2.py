#!/usr/bin/env python3
import os
import platform
import random

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Jugador:
    def jugador (self, nom, color):
        self.nom = nom
        self.color = color
        self.diners = 2000  
        self.posicio = 0 
        self.propietats = []  
        self.presoner = False  
        self.cartes_preso = 0  

    def moure(self, espais):
        self.posicio = (self.posicio + espais) % 40  # Suposant que hi ha 40 caselles al tauler
        print(f"{self.nom} s'ha mogut a la posició {self.posicio}")

class Banco:
    def init(self):
        self.dinero = 10000000

    def ajustar_dinero(self):
        if self.dinero < 500000:
            self.dinero += 1000000


def monopoly():
        # Definim els carrers i les caselles especials
    carrers = [
        "Lauria", "Rosselló", "Marina", "Consell de cent",
        "Muntaner", "Aribau", "Sant Joan", "Aragó",
        "Urquinaona", "Fontana", "Les Rambles", "Plaça Catalunya",
        "Portal de l'Àngel", "Via Augusta", "Balmes", "Passeig de Gràcia"
    ]

    # Caselles especials amb les seves funcions específiques
    caselles_especials = {
        "Sortida": "passar_sortida",  # El jugador guanya 200€
        "Presó": "caure_a_preso",  # Funcionalitat especial
        "Anr pró": "anar_a_preso",  # Envia a la presó
        "Parking": "sense_efecte",  # No afecta el jugador
        "Sort": "tirar_sort",  # Casella que activa una carta de sort
        "Caixa": "tirar_caixa"  # Casella que activa una carta de caixa
    }
    taula = [
            ["Parking", "Urquinaona", "Fontana", "Sort", "Rambles", "Pl.Catalunya", "Anr próx"],
            ["Aragó","", "Angel"],
            ["S.Joan","", "Augusta"],
            ["Caixa","" , "Caixa"],
            ["Aribau", "", "Balmes"],
            ["Muntaner", "", "Gracia"],
            ["Presó", "Consell", "Marina", "Sort", "Roselló", "Lauria", "Sortida"]
        ]

    jugadors = [
                Jugador("Groc", "G"),
                Jugador("Taronja", "T"),
                Jugador("Vermell", "V"),
                Jugador("Blau", "B")
        ]
    random.shuffle(jugadors)
    jugador = jugadors, Jugador
    jugadors = jugador, Jugador
    def imprimir_taula_monopoly():
                
        for fila in taula:
            print("+--------" * len(fila) + "+")
            for element in fila:
                print(f"|{element:^8}", end="")
            print("|")
        print("+--------" * len(taula[0]) + "+")

    def tirar_daus():
        dau1 = random.randint(1, 6)
        dau2 = random.randint(1, 6)
        return dau1, dau2

    def jugar_torn(jugador, tauler):
        dau1, dau2 = tirar_daus()
        print(f"{jugador.nom} ha tret {dau1} i {dau2}")
        espais = dau1 + dau2
        jugador.moure(espais)
        casella = tauler.obtenir_casella(jugador.posicio)
        
        if casella.tipus == "carrer":
            if casella.propietari is None:
                print(f"{jugador.nom} pot comprar {casella.nom} per {casella.preu}€")
                # Afegir la lògica per comprar
            else:
                print(f"{jugador.nom} ha de pagar lloguer a {casella.propietari.nom}")
                # Afegir la lògica de pagar lloguer
        elif casella.tipus == "especial":
            # Caselles especials com presó o sortida
            if casella.nom == "Presó":
                jugador.presoner = True
                print(f"{jugador.nom} ha caigut a la presó!")

    def tirar_sort(jugador):
        cartes_sort =  [
            ("Sortir de la presó"),  # Carta que permet sortir de la presó
            ("Anar a la presó"),  # Va directament a la presó
            ("Anar a la sortida"),  # Va a la sortida i cobra 200€
            ("Anar tres espais enrere"),  # Retrocedeix 3 caselles
            ("Fer reparacions"),  # Paga 25€ per cada propietat, 100€ per cada hotel
            ("Escollit alcalde"),  # Cada jugador paga 50€
        ]
        carta = random.choice(cartes_sort)
        
        if carta == "Sortir de la presó":
            jugador['cartes_preso'] += 1
            print(f"{jugador['color']} ha tret una carta de Sortir de la Presó.")
        elif carta == "Anar a la presó":
            anar_a_preso(jugador)
        elif carta == "Anar a la sortida":
            jugador['posicio'] = 0  # Casella de sortida
            passar_sortida(jugador)
        elif carta == "Anar tres espais enrere":
            jugador['posicio'] -= 3
            print(f"{jugador['color']} ha retrocedit tres espais fins a la posició {jugador['posicio']}.")
        elif carta == "Fer reparacions":
            pagament = 25 * len(jugador['propietats']) + 100 * jugador.get('hotels', 0)
            jugador['diners'] -= pagament
            print(f"{jugador['color']} paga {pagament}€ en reparacions.")
        elif carta == "Escollit alcalde":
            # Cada jugador paga 50€ al jugador actual
            print(f"{jugador['color']} ha estat escollit alcalde! Tots els jugadors li paguen 50€.")


    # Inicialitzem els jugadors amb 2000€
    jugadors = [{"color": color, "lletra": lletra, "diners": 2000, "posicio": 0} 
                for color, lletra in colors_jugadors.items()]


    # Mostrem l'ordre dels jugadors a la casella de Sortida
    def imprimir_sortida(jugadors):
        ordre_tirada = "".join([jugador["lletra"] for jugador in jugadors])
        print("+--------+")
        print(f"|{ordre_tirada:^8}| Significa que primer tira el {jugadors[0]['color']},")
        print("|Sortida | després els altres, segons l'ordre de les lletres")
        print("+--------+")

    def tirar_caixa(jugador):
        cartes_caixa = [
            "Sortir de la presó", 
            "Anar a la presó", 
            "Error de la banca, guanyes 150€", 
            "Despeses mèdiques, pagues 50€", 
            "Despeses escolars, pagues 50€", 
            "Reparacions al carrer, pagues 40€", 
            "Concurs de bellesa, guanyes 10€"
        ]
        carta = random.choice(cartes_caixa)
        
        if carta == "Sortir de la presó":
            jugador['cartes_preso'] += 1
            print(f"{jugador['color']} ha tret una carta de Sortir de la Presó.")
        elif carta == "Anar a la presó":
            anar_a_preso(jugador)
        elif carta == "Error de la banca, guanyes 150€":
            jugador['diners'] += 150
            print(f"{jugador['color']} guanya 150€ gràcies a un error de la banca!")
        elif carta == "Despeses mèdiques, pagues 50€":
            jugador['diners'] -= 50
            print(f"{jugador['color']} paga 50€ en despeses mèdiques.")
        elif carta == "Despeses escolars, pagues 50€":
            jugador['diners'] -= 50
            print(f"{jugador['color']} paga 50€ en despeses escolars.")
        elif carta == "Reparacions al carrer, pagues 40€":
            jugador['diners'] -= 40
            print(f"{jugador['color']} paga 40€ en reparacions al carrer.")
        elif carta == "Concurs de bellesa, guanyes 10€":
            jugador['diners'] += 10
            print(f"{jugador['color']} guanya 10€ en un concurs de bellesa!")


    def gestionar_casella(jugador, casella):
        if casella in caselles_especials:
            funcio_especial = caselles_especials[casella]
            globals()[funcio_especial](jugador)  # Crida la funció corresponent
        else:
            print(f"{jugador['color']} ha caigut a {casella}, que és un carrer.")



    def imprimir_informacio_jugadors(jugadors, banca):
        # Mostrem la informació de la banca
        print("+--------+--------+ Banca:")
        print(f"|Pl.Cat  |Anr pró | Diners: {banca['diners']}")
        print("|        |        |")
        print("+--------+--------+")

        # Per a cada jugador, imprimim la seva informació
        for jugador in jugadors:
            print(f"         | {jugador['propietat_principal']:<8} | Carrers: {', '.join(jugador['propietats'])}")
            print(f"         |        | Diners: {jugador['diners']}")
            if jugador['especial']:
                print(f"         +--------+ Especial: {jugador['especial']}")
            else:
                print(f"         +--------+ Especial: (res)")
            print()

    # Simulem el moviment d'alguns jugadors i mostrem les fitxes en una casella específica
    def imprimir_fitxes_a_casella(casella, fitxes):
        fitxes_en_ordre = "".join(fitxes)
        print("+--------+")
        print(f"|{fitxes_en_ordre:^8}| Significa que a la casella {casella},")
        print(f"|{casella:^8}| hi ha les fitxes {', '.join(fitxes)} en aquest ordre.")
        print("+--------+")

        def iniciar_partida():
            jugadors = inicialitzar_jugadors()
            tauler = inicialitzar_tauler()
            banca = Banco()
            
        torn_actual = 0
        while not fi_del_joc():
            jugador_actual = jugadors[torn_actual]
            
            imprimir_taula_monopoly()
            imprimir_informacio_jugadors(jugadors, banca)
            
            dau1, dau2 = tirar_daus()
            nou_posicio = moure_jugador(jugador_actual, dau1 + dau2)
            gestionar_casella(jugador_actual, nou_posicio, tauler)
            
            accio = obtenir_accio_jugador()
            executar_accio(jugador_actual, accio, tauler, banca)
            
            if accio == 'trucs':
                gestionar_trucs(jugador_actual, jugadors, tauler, banca)
            
            torn_actual = (torn_actual + 1) % len(jugadors)
    
    mostrar_guanyador(jugadors)

    def passar_sortida(jugador):
        jugador['diners'] += 200
        print(f"{jugador['color']} ha passat per la Sortida i guanya 200€. Total diners: {jugador['diners']}")

    def caure_a_preso(jugador):
        jugador['presoner'] = True
        jugador['torns_preso'] = 0  # Nombre de torns que ha estat a la presó
        print(f"{jugador['color']} ha caigut a la Presó!")

    def anar_a_preso(jugador):
        jugador['posicio'] = 10  # Suposant que la casella de la presó és la 10
        caure_a_preso(jugador)

    def sense_efecte(jugador):
        print(f"{jugador['color']} ha caigut a Parking, no passa res.")

monopoly(Jugador)


