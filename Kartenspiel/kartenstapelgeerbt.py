from stapel import Stapel
from random import randint

class Kartenstapel(Stapel):
    def __init__(self):
        self.liste = ['X-A', 'X-K', 'X-D', 'X-B', 'X-10', 'X-9', 'X-8', 'X-7',
            'P-A', 'P-K', 'P-D', 'P-B', 'P-10', 'P-9', 'P-8', 'P-7',
            'H-A', 'H-K', 'H-D', 'H-B', 'H-10', 'H-9', 'H-8', 'H-7',
            'K-A', 'K-K', 'K-D', 'K-B', 'K-10', 'K-9', 'K-8', 'K-7']
        self.wert = 0 
    def mischen(self):

        """
        Die aktuell im Kartenstapel vorliegenden Karten werden neu angeordnet.
        Hierzu wird eine zufällig gewählte neue Reihenfolge bestimmt.
        """

        neueListe = []
        aktuelleAnzahl = len(self.liste)
        while aktuelleAnzahl > 0:
            i = randint(0, aktuelleAnzahl-1)
            neueListe = neueListe + [self.liste[i]]
            del self.liste[i]
            aktuelleAnzahl = len(self.liste)
        self.liste = neueListe
        
        
    def KartenWert(self, karte):
        #Karo
        if karte[0] == 'K' and karte[-1] == '7':
            self.wert = 1
        if karte[0] == 'K' and karte[-1] == '8':
            self.wert = 2
        if karte[0] == 'K' and karte[-1] == '9':
            self.wert = 3
        if karte[0] == 'K' and karte[-1] == '0':
            self.wert = 4
        if karte[0] == 'K' and karte[-1] == 'B':
            self.wert = 5
        if karte[0] == 'K' and karte[-1] == 'D':
            self.wert = 6
        if karte[0] == 'K' and karte[-1] == 'K':
            self.wert = 7
        if karte[0] == 'K' and karte[-1] == 'A':
            self.wert = 8
        #Herz
        if karte[0] == 'H' and karte[-1] == '7':
            self.wert = 9
        if karte[0] == 'H' and karte[-1] == '8':
            self.wert = 10
        if karte[0] == 'H' and karte[-1] == '9':
            self.wert = 11
        if karte[0] == 'H' and karte[-1] == '0':
            self.wert = 12
        if karte[0] == 'H' and karte[-1] == 'B':
            self.wert = 13
        if karte[0] == 'H' and karte[-1] == 'D':
            self.wert = 14
        if karte[0] == 'H' and karte[-1] == 'K':
            self.wert = 15
        if karte[0] == 'H' and karte[-1] == 'A':
            self.wert = 16
        #Pik
        if karte[0] == 'P' and karte[-1] == '7':
            self.wert = 17
        if karte[0] == 'P' and karte[-1] == '8':
            self.wert = 18
        if karte[0] == 'P' and karte[-1] == '9':
            self.wert = 19
        if karte[0] == 'P' and karte[-1] == '0':
            self.wert = 20
        if karte[0] == 'P' and karte[-1] == 'B':
            self.wert = 21
        if karte[0] == 'P' and karte[-1] == 'D':
            self.wert = 22
        if karte[0] == 'P' and karte[-1] == 'K':
            self.wert = 23
        if karte[0] == 'P' and karte[-1] == 'A':
            self.wert = 24
        #Kreuz
        if karte[0] == 'X' and karte[-1] == '7':
            self.wert = 25
        if karte[0] == 'X' and karte[-1] == '8':
            self.wert = 26
        if karte[0] == 'X' and karte[-1] == '9':
            self.wert = 27
        if karte[0] == 'X' and karte[-1] == '0':
            self.wert = 28
        if karte[0] == 'X' and karte[-1] == 'B':
            self.wert = 29
        if karte[0] == 'X' and karte[-1] == 'D':
            self.wert = 30
        if karte[0] == 'X' and karte[-1] == 'K':
            self.wert = 31
        if karte[0] == 'X' and karte[-1] == 'A':
            self.wert = 32
        return self.wert
    
    