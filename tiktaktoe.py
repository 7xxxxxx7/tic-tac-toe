import pygame
import sys
import random

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und Titel
breite, hoehe = 300, 300
fenster = pygame.display.set_mode((breite, hoehe))
pygame.display.set_caption('Tic-Tac-Toe')

# Farben
HINTERGRUND = (255, 255, 255)
LINIEN_FARBE = (0, 0, 0)

# Klasse für die Spieler
class Spieler:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

# Spieler erstellen
Spieler1 = Spieler("Gustav", "X")
Spieler2 = Spieler("Herbert", "O")

# Spielfeld
spielfeld = [[" " for _ in range(3)] for _ in range(3)]

# Funktion zum Zeichnen des Spielfelds
def zeichne_spielfeld():
    # Fensterhintergrund
    fenster.fill(HINTERGRUND)

    # Zeichnen der Tic-Tac-Toe-Linien
    for x in range(1, 3):
        pygame.draw.line(fenster, LINIEN_FARBE, (x * 100, 0), (x * 100, hoehe), 5)
        pygame.draw.line(fenster, LINIEN_FARBE, (0, x * 100), (breite, x * 100), 5)

    # Zeichnen der X und O Symbole
    for zeile in range(3):
        for spalte in range(3):
            zeichen = spielfeld[zeile][spalte]
            if zeichen == "X":
                pygame.draw.line(fenster, LINIEN_FARBE, (spalte * 100 + 20, zeile * 100 + 20), (spalte * 100 + 80, zeile * 100 + 80), 5)
                pygame.draw.line(fenster, LINIEN_FARBE, (spalte * 100 + 80, zeile * 100 + 20), (spalte * 100 + 20, zeile * 100 + 80), 5)
            elif zeichen == "O":
                pygame.draw.circle(fenster, LINIEN_FARBE, (spalte * 100 + 50, zeile * 100 + 50), 40, 5)

# Funktionen für Spiellogik
def spiel_beenden(spielfeld):
    # Überprüfen, ob ein Spieler in einer Zeile gewonnen hat
    for zeile in spielfeld:
        if zeile[0] == zeile[1] == zeile[2] != " ":
            return True

    # Überprüfen, ob ein Spieler in einer Spalte gewonnen hat
    for spalte in range(3):
        if spielfeld[0][spalte] == spielfeld[1][spalte] == spielfeld[2][spalte] != " ":
            return True

    # Überprüfen, ob ein Spieler in einer Diagonale gewonnen hat
    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] != " ":
        return True
    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] != " ":
        return True

    # Überprüfen, ob alle Felder gefüllt sind (Unentschieden)
    for zeile in spielfeld:
        for zelle in zeile:
            if zelle == " ":
                return False  # Spiel ist noch nicht beendet

    # Wenn alle Felder gefüllt sind und niemand gewonnen hat, ist das Spiel unentschieden
    return True

def ermitteln_gewinner(spielfeld):
    # Überprüfen auf Gewinner in Zeilen, Spalten und Diagonalen
    for i in range(3):
        if spielfeld[i][0] == spielfeld[i][1] == spielfeld[i][2] != " ":
            return spielfeld[i][0]
        if spielfeld[0][i] == spielfeld[1][i] == spielfeld[2][i] != " ":
            return spielfeld[0][i]

    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] != " ":
        return spielfeld[0][0]
    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] != " ":
        return spielfeld[0][2]

    # Überprüfen auf Unentschieden
    if all(spielfeld[i][j] != " " for i in range(3) for j in range(3)):
        return "Unentschieden"

    return None


def spieler_zug(spielfeld, x, y, symbol):
    if spielfeld[x][y] == " ":
        spielfeld[x][y] = symbol
        return True
    return False

def computer_zug(spielfeld, symbol):
    freie_felder = [(i, j) for i in range(3) for j in range(3) if spielfeld[i][j] == " "]
    if freie_felder:
        x, y = random.choice(freie_felder)
        spielfeld[x][y] = symbol 
        print("Bot Herbert´s Zug")  
        
def zeichne_buttons():
    neues_spiel_button = pygame.Rect(breite // 2 - 80, hoehe // 2 - 60, 160, 40)
    beenden_button = pygame.Rect(breite // 2 - 80, hoehe // 2 + 20, 160, 40)

    pygame.draw.rect(fenster, (0, 128, 0), neues_spiel_button)
    pygame.draw.rect(fenster, (128, 0, 0), beenden_button)

    font = pygame.font.Font(None, 36)
    neues_spiel_text = font.render('Neues Spiel', True, (255, 255, 255))
    beenden_text = font.render('Beenden', True, (255, 255, 255))

    fenster.blit(neues_spiel_text, (breite // 2 - 70, hoehe // 2 - 55))
    fenster.blit(beenden_text, (breite // 2 - 50, hoehe // 2 + 25))

    return neues_spiel_button, beenden_button

def pruefe_button_klicks(neues_spiel_button, beenden_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if neues_spiel_button.collidepoint(x, y):
                return 'new_game'
            elif beenden_button.collidepoint(x, y):
                return 'quit'
    return None
        

# Auswahl des Spielmodus
def auswahl_spielmodus():
    while True:
        modus = input("Möchtest du gegen einen anderen Spieler (1) oder gegen den Computer (2) spielen? (1/2): ")
        if modus in ["1", "2"]:
            return modus
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

spielmodus = auswahl_spielmodus()

# Hauptspiel-Schleife
aktueller_spieler = Spieler1
laeuft = True
while laeuft:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            laeuft = False

        if event.type == pygame.MOUSEBUTTONDOWN and not spiel_beenden(spielfeld):
            mouseX = event.pos[0]  # X-Koordinate des Mausklicks
            mouseY = event.pos[1]  # Y-Koordinate des Mausklicks

            geklickte_zeile = int(mouseY // 100)
            geklickte_spalte = int(mouseX // 100)

            if spieler_zug(spielfeld, geklickte_zeile, geklickte_spalte, aktueller_spieler.symbol):
                if spiel_beenden(spielfeld):
                    laeuft = False
                else:
                    aktueller_spieler = Spieler2 if aktueller_spieler == Spieler1 else Spieler1
                    if spielmodus == "2":
                        computer_zug(spielfeld, Spieler2.symbol)
                        if spiel_beenden(spielfeld):
                            laeuft = False
                        aktueller_spieler = Spieler1

    zeichne_spielfeld()
    pygame.display.update()

    gewinner = ermitteln_gewinner(spielfeld)
    if gewinner:
        endnachricht = f"Glückwunsch, Spieler {gewinner}, hat gewonnen!" if gewinner != "Unentschieden" else "Das Spiel endet unentschieden!"
        print(endnachricht)  # Konsole
        # Hier könnten Sie eine Pause einfügen, bevor das Spiel endet
        pygame.time.wait(2000)
        laeuft = False
        
    if gewinner:
        neues_spiel_button, beenden_button = zeichne_buttons()
        pygame.display.update()
        
        aktion = None
        while aktion is None:
            aktion = pruefe_button_klicks(neues_spiel_button, beenden_button)

        if aktion == 'quit':
            laeuft = False
        elif aktion == 'new_game':
            spielfeld = [[" " for _ in range(3)] for _ in range(3)]
            aktueller_spieler = Spieler1
            continue
        
pygame.quit()
sys.exit()
