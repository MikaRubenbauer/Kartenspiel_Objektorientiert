######################################## Mika Rubenbauer, 16.05.2023, Herr Wagner, INF, Keep or Throw #########################################
#Imports
from kartenstapelgeerbt import Kartenstapel
from stapel import Stapel 

#######################################

#Variablen erstellen
s1 = Kartenstapel()
t = Stapel() #Throw Stapel
k = Stapel() #Keep Stapel
f = 0 #Zähler für Fehler
i = 0 #Zähler für Karten auf Keep Stapel
x = False  #Legt fest ob bestimmte Infos geprintet werden (Unterschied bei einfachem und normalen Modus) 

########################################

#Vergleich Funktion für Wert,
def vergleich(aktuelleKarte):
    #Varaiblen globaliesieren
    global i
    global f
    global x
    #Wert bestimmen
    w1 = s1.KartenWert(aktuelleKarte)
    keepKarte = k.top()
    w2 = s1.KartenWert(keepKarte)
    #Wert vergleichen
    if w1 > w2:
        #In keep Stappel pushen
        k.push(aktuelleKarte)
        print( )
        print('Die Karte' " \033[32m" + aktuelleKarte + "\033[0m"' wurde auf deinen Stapel gelegt')
        if x == True: #Extra für einfach Modus
            print('Deine bisherigen Karten sind: ',k.getStapel())
            print( )
            i = i + 1
            einfachSpiel()
        else:
            print( )
            i = i + 1
            spiel() #zurück zur Ursprungsfunktion
    else:
        #In throw Stapel pushen
        t.push(aktuelleKarte)
        print( )
        print('Die Karte'" \033[91m" + aktuelleKarte + "\033[0m"' wurde auf den Throw Stapel gelegt')
        if x == True: #Extra für einfach Modus
            print('Deine bisher weggeworfenen Karten sind: ',t.getStapel())
            print(" \033[91m" + '!!! vergiss nicht das deine Karte nicht höher sein darf als: ',k.top(),' Wert(',s1.KartenWert(k.top()),')' + "\033[0m")
            print( )
            f = f + 1
            einfachSpiel()
        else:
            print( )
            f = f + 1
            spiel() #zurück zur Ursprungsfunktion
       
  
            
        

##############################################

#Vorbereitung fürs Spiel
s1.mischen()
print('Wilkommen im Spiel Herr Wagner')
print( )
h = str(input('Möchten sie die Spielregeln (j)/(n)'))
if h == 'j':
    #Spielregeln
    print( ) 
    print('Sie bekommem nach jedem Zug eine' " \033[34m" + 'Karte' + "\033[0m")
    print('Sie können diese entweder behalten indem sie k eingeben, dann wird diese Karte auf ihren'" \033[32m" + 'keep Stapel' + "\033[0m" ' gelegt ')
    print('Oder sie legen sie auf ihren'" \033[91m" + 'throw Stapel' + "\033[0m"' mit der Eingabe t')
    print('Das Ziel ist es so viele Karten wie möglich auf ihrem'" \033[32m" + 'keep Stapel' + "\033[0m" ' zu haben')
    print('Jedoch kann eine Karte nur auf ihren'" \033[32m" + 'keep Stapel' + "\033[0m"' gelegt werden, wenn ihr'" \033[35m" 'Wert' + "\033[0m" +' höher ist als der ihrer obersten Karte')
    print('Außerdem können sie gleich den Modus auswählen mit dem sie spielen wollen. Im einfachen Modus stehen ihnen viele extra Informationen zu verfügung')
    print( )
h2 = str(input('Möchten sie die Reihenfolge der Karten sehen (j)/(n)'))
print ( )
if h2 == 'j':
    print(' Sortiert von höchster Wert zu niedrigster: ')
    print(" \033[34m" + 'X-A,', 'X-K,', 'X-D,', 'X-B,', 'X-10,', 'X-9,', 'X-8,', 'X-7,',
            'P-A,', 'P-K,', 'P-D,', 'P-B,', 'P-10,', 'P-9,', 'P-8,', 'P-7,',
            'H-A,', 'H-K,', 'H-D,', 'H-B,', 'H-10,', 'H-9,', 'H-8,' 'H-7,',
            'K-A,', 'K-K,', 'K-D,', 'K-B,', 'K-10,', 'K-9,', 'K-8,', 'K-7' + "\033[0m")
    print( )

print('Viel Spaß und erfolg beim Spiel :)')
print('LOS GEHTS !')
print( )
print( )
print( )
print( )
print( )
print( )

##################################

#Hauptspiel
def spiel():
    global i
    global f
    #Variablen globalisieren
    while not s1.getStapel() == []:
        aktuelleKarte = s1.pop()
        print('Die aktuelle Karte ist:' " \033[34m" + aktuelleKarte + "\033[0m")
        frage = str(input('Auf welchen Stapel soll die Karte : '))
        if frage == 't':
            #Throw Stapel
            t.push(aktuelleKarte)
            print( )
            print('Die Karte'" \033[91m" + aktuelleKarte + "\033[0m"' wurde auf den throw Stapel gelegt')
            print( )
            spiel() #Rekursiver Aufruf der Funktion 
        elif frage == 'k':
            #Alles was mit keep zu tun hat
            if k.getStapel() == []:
                #Die erste Karte die auf den Keep Stapel kommt muss nicht vergliechen werden deshalb wird sie hier auf den keep Stapel gelegt
                k.push(aktuelleKarte)
                print( )
                print('Die Karte'" \033[32m" + aktuelleKarte + "\033[0m"' wurde auf deinen Stapel gelegt')
                print( )
                i = i + 1
                spiel() #Die funktion wird rekusiv wieder aufgerufen um die nächste karte zu ziehen
            else:
                #Ruft vergleich Funktion auf 
                vergleich(aktuelleKarte)
                
############################################

#Extra Spiel funktion für vereinfachte Version   
def einfachSpiel():
    #Varaiblen globalisieren
    global i
    global f
    global x
    x = True #x wird True damit vergleich Funktion extra prints hat 
    while not s1.getStapel() == []:
        aktuelleKarte = s1.pop()
        print('Die aktuelle Karte ist:' " \033[34m" + aktuelleKarte + "\033[0m")
        print('Der Wert der aktuellen Karte ist: '" \033[35m" + str(s1.KartenWert(aktuelleKarte)) + "\033[0m")
        frage = str(input('Auf welchen Stapel soll die Karte' " \033[32m" + '(k)' + "\033[0m"' /'" \033[91m" + '(t)' + "\033[0m" ': ' ))
        if frage == 't':
            #throw Stapel
            t.push(aktuelleKarte)
            print( )
            print('Die Karte'" \033[91m" + aktuelleKarte + "\033[0m"' wurde auf den throw Stapel gelegt')
            print('Deine bisher weggeworfenen Karten sind: ',t.getStapel()) #Ausgabe vom throw Stapel
            print( )
            einfachSpiel() #Rekursiver Aufruf der Funktion
        elif frage == 'k':
            #Alles mit keep 
            if k.getStapel() == []:
                #Für den ersten keep Befehl
                k.push(aktuelleKarte)
                print( )
                print('Die Karte'" \033[32m" + aktuelleKarte + "\033[0m"' wurde auf deinen Stapel gelegt') 
                print('Deine bisherigen  Karten sind: ',k.getStapel()) #Ausgabe vom keep Stapel damit man seine KArten sieht
                print( )
                i = i + 1
                einfachSpiel() #Rekursiver Aufruf der Funktion
            else:
                #Ruft vergleich Funktion auf 
                vergleich(aktuelleKarte)    
        
########################################

#Wählt modus aus
print( )
modus = str(input('Welchen Modus möchtest du spielen, den normalen (n) oder den einfachen (e): '))
if modus == 'n':
    print( )
    print( ) 
    spiel() #normale Version
elif modus == 'e':
    print( )
    print( )
    einfachSpiel() #einfache Version 


    




#######################################

#Zusammenfassung der Ergebnisse
print('Das Spiel ist zuende')
print('Du hast: '" \033[32m" + str(i) + "\033[0m"' Karten behalten')
print('Deshalb sieht dein keep Stapel folgendermaßen aus: ',k.getStapel())
print('Du hast aber auch: '" \033[91m" + str(f) + "\033[0m"' Fehler gemacht')
if f > 5: 
    print('Das geht besser') #Wenn mehr als 5 Fehler gemacht wurden
    print( )
else:
    print('gut gemacht')
    print( )
neu = str(input('Möchtest du eine neue runde spielen (j)/(n)?')) #Für neue Runde
print( )
if neu == 'n':
    print('Ok schade wir sehen und bestimmt bald wieder')
elif neu == 'j':
    print('Toll! welche Version ?')
    modus = str(input('Den normalen (n) oder den vereinfachten (e): '))
    print( )
    if modus == 'n':
        for l in range(200):
            print( )
        #Ressete alle Variablen und mischt neu
        s1 = Kartenstapel()
        s1.mischen()
        k = Stapel()
        t = Stapel()
        i = 0
        f = 0
        x = False 
        spiel()
    elif modus == 'e':
        for l in range(200):
            print( )
        #Ressete alle Variablen und mischt neu
        s1 = Kartenstapel()
        s1.mischen()
        k = Stapel()
        t = Stapel()
        i = 0
        f = 0
        einfachSpiel()
        
        







