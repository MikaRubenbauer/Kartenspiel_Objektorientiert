#-----------------------------------------------------------
# Stapel
#-----------------------------------------------------------

class Stapel(object):

    """
    Es können Daten beliebigen Typs auf den Stapel gelegt werden.
    Alle Stapelelemente werden in einer Liste verwaltet.
    Dabei werden die Elemente folgendermaßen angeordnet:
    [... <- unten ... oben -> ...}
    """

    __slots__ = ('liste')
    
    def __init__(self, pListe = []):
        
        """ 
        Der Konstruktor erzeugt einen leeren Stapel, wenn man keine
        Ausgangsbelegung vorgibt. Es kann aber auch eine
        Ausgangsbelegung als Liste übergeben werden.
        Beispiele:
        >>> s = Stapel()
        >>> s.liste
        []
        >>> s = Stapel(['a', 'b', 'c'])
        >>> s.liste
        ['a', 'b', 'c']
        """
        
        self.liste = pListe

    def isEmpty(self):
        
        """
        Die Methode überprüft, ob der Stapel Elemente enthält
        und liefert als Ergebnis einen Wahrheitswert zurück.
        Beispiel:
        >>> s = Stapel()
        >>> s.isEmpty()
        True
        >>> s = Stapel(['a', 'b', 'c'])
        >>> s.isEmpty()
        False
        """
        
        if self.liste == []:
            return True
        else:
            return False

    def push(self, element):
        
        """
        Mit der Methode push wird ein übergebenes Element
        oben auf den Stapel gelegt.
        Beispiel:
        >>> s = Stapel(['a', 'b'])
        >>> s.push('c')
        >>> s.liste
        ['a', 'b', 'c']
        """
        
        self.liste = self.liste + [element]

    def pop(self):
        
        """
        Mit der Methode pop wird das oberste Element des
        Stapels entfernt und als Ergebnis zurückgeliefert,
        sofern der Stapel Elemente hat.
        Beispiel:
        >>> s = Stapel()
        >>> s.pop()
        >>> s.liste
        []
        >>> s = Stapel(['a', 'b', 'c'])
        >>> s.pop()
        'c'
        >>> s.liste
        ['a', 'b']
        """
        
        if not self.isEmpty():
            oberstesElement = self.liste[len(self.liste)-1]
            self.liste = self.liste[:len(self.liste)-1]
            return oberstesElement
        else:
            return None

    def top(self):
        
        """
        Die Methode top liefert das oberste Element des
        Stapels (falls ein solches existiert), entfernt
        es aber nicht aus dem Stapel.
        Beispiel:
        >>> s = Stapel(['a', 'b', 'c'])
        >>> s.top()
        'c'
        >>> s = Stapel()
        >>> s.top()
        """
        
        if not self.isEmpty():
            return self.liste[len(self.liste)-1]      

    def setStapel(self, pListe):
        
        """
        Mit der Methode setStapel kann man eine (als Liste)
        übergebene Ausgangsbelegung erzeugen.
        Beisiel:
        >>> s = Stapel()
        >>> s.setStapel(['a', 'b', 'c'])
        >>> s.liste
        ['a', 'b', 'c']
        """
        
        self.liste = pListe

    def getStapel(self):

        """
        Die Methode getStapel liefert die aktuellen Elemente
        des Stapels in Listenform zurück.
        Beispiel:
        >>> s = Stapel()
        >>> s.setStapel(['a', 'b', 'c'])
        >>> s.getStapel()
        ['a', 'b', 'c']
        """
        
        return self.liste

# Modultest

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=False)
