#    |   |
#    |   |
#    |   | 

import random    

def auswahl_spielmodus():
    while True:
        modus = input("Möchtest du gegen einen anderen Spieler (1) oder gegen den Computer (2) spielen? (1/2): ")
        if modus in ["1", "2"]:
            return modus
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

spielmodus = auswahl_spielmodus()

    
class Spieler:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
Spieler1 = Spieler("Gustav", "X")
Spieler2 = Spieler("Herbert", "O")   
 
spielfeld = [[" " for _ in range(3)] for _ in range(3)]
  
def drucke_spielfeld (spielfeld):
    for reihe in spielfeld:
        print("|".join(reihe))
          
drucke_spielfeld(spielfeld)      


def spiel_beenden(spielfeld):
     
    for i in range(3):
         
        if spielfeld[i][0] == spielfeld[i][1] == spielfeld[i][2] != " ":
            return True
       
        if spielfeld[0][i] == spielfeld[1][i] == spielfeld[2][i] != " ":
            return True
    
    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] != " " or spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] != " ":
        return True
    
    if all(spielfeld[i][j] != " " for i in range(3) for j in range(3)):
        return True
    return False

def spieler_zug(Spieler, spielfeld):
    zug_gültig = False
    while not zug_gültig:
        zug = input(f"{Spieler.name}, wähle ein Feld (1-9): ")
        if zug.isdigit():
            zug_nummer = int(zug)
            if 1 <= zug_nummer <= 9:
                x = (zug_nummer - 1) // 3
                y = (zug_nummer - 1) % 3
                if spielfeld[x][y] == " ":
                    spielfeld[x][y] = Spieler.symbol
                    zug_gültig = True
                else:
                    print("Feld ist bereits belegt. Bitte wähle ein anderes Feld.")
            else:
                print("Ungültige Zahl. Bitte wähle eine Zahl zwischen 1 und 9.")
        else:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")    
            
def computer_zug(spielfeld, symbol):
    freie_felder = [(i, j) for i in range(3) for j in range(3) if spielfeld[i][j] == " "]
    if freie_felder:
        x, y = random.choice(freie_felder)
        spielfeld[x][y] = symbol 
        print("Bot Herbert´s Zug")           
                         
aktueller_spieler = Spieler1
while not spiel_beenden(spielfeld):
    drucke_spielfeld(spielfeld)

    if aktueller_spieler == Spieler1 or spielmodus == "1":
        spieler_zug(aktueller_spieler, spielfeld)
    else:
        computer_zug(spielfeld, Spieler2.symbol)

    if spiel_beenden(spielfeld):
        break

    if aktueller_spieler == Spieler1:
        aktueller_spieler = Spieler2
    else:
        aktueller_spieler = Spieler1

        
drucke_spielfeld(spielfeld)
print("Spiel beendet!")
if spiel_beenden(spielfeld):
    print(f"Glückwunsch {aktueller_spieler.name}, du hast gewonnen!")
else:
    print("Unentschieden!")

        




