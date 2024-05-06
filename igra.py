from stanje import Stanje
import time
import os

class Igra(object):

    __slots__ = ['_trenutnoStanje', '_odigranPotez', '_porekloPoteza', '_brojFigura']

    def __init__(self):
        self._trenutnoStanje = Stanje()
        self._odigranPotez = 0
        self._porekloPoteza = 0
        self._brojFigura = 0

    def getBrojFigura(self):
        return self._brojFigura

    def staviFiguru(self):
        b = self.getBrojFigura()
        b+=1
        self._brojFigura = b

    def setBrojFigura(self, i):
        self._brojFigura = i

    def jeKrajPrveFaze(self):
        return self.getBrojFigura() == 18

    def jeKrajDrugeFaze(self):
        if self._trenutnoStanje.brFigura("[") == 2:
            return True, "("
        elif self._trenutnoStanje.brFigura("(") == 2:
            return True, "["
        if self._trenutnoStanje.brBlokiranih("[") == self._trenutnoStanje.brFigura("["):
            return True, "("
        elif self._trenutnoStanje.brBlokiranih("(") == self._trenutnoStanje.brFigura("("):
            return True, "["
        return False, " "

    def getOdigranPotez(self):
        return self._odigranPotez
    
    def setOdigranPotez(self, i):
        self._odigranPotez = i

    def getPorekloPoteza(self):
        return self._porekloPoteza
    
    def setPorekloPoteza(self, i):
        self._porekloPoteza = i

    def prikaziTablu(self):
        print(self._trenutnoStanje)

    def jeBrisljivo(self, i):
        if not self._trenutnoStanje.suTriUNizu(i):
            return True
        brisljivo = True
        for j in range(1, 25):
            if self._trenutnoStanje.getPolje(i)[0] == self._trenutnoStanje.getPolje(j)[0] and not self._trenutnoStanje.suTriUNizu(j):
                brisljivo = False
        return brisljivo
        
    def brisi(self, i):
        self._trenutnoStanje.setPrazno(i)

    def pocniIgru(self):
        os.system('cls')
        self.prikaziTablu()
        p = int(input("Hajde da igramo Mice! Odaberite polje brojem od 1 do 24. \n"))
        self._trenutnoStanje.setUglasto(p)
        self.staviFiguru()
        self.setOdigranPotez(p)

    def heuristika1(self):
        res = 26 * self._trenutnoStanje.razlikaMica() + self._trenutnoStanje.razlikaBlokiranih() +  9 * self._trenutnoStanje.razlikaFigura() + 10 * self._trenutnoStanje.razlikaSkoroMica() + 7 * self._trenutnoStanje.razikaSkoroDuplaMica()
        return res
    
    def heuristika2(self):
        kraj = 0
        rezultat, pobednik = self.jeKrajDrugeFaze()
        if rezultat:
            if pobednik == "(":
                kraj = 1086
            elif pobednik == "[":
                kraj = -1086
        res = kraj + 43 * self._trenutnoStanje.razlikaMica() + 10 * self._trenutnoStanje.razlikaBlokiranih() +  11 * self._trenutnoStanje.razlikaFigura() + 8 * self._trenutnoStanje.razlikaDuplaMica()
        return res
    
    def max1(self, dubina, alfa, beta):

        maxv = -9999999
        pi = None
        if self.jeKrajPrveFaze() or dubina == 0:
            return self.heuristika1(), self.getOdigranPotez(), 0
        
        for x in range(1, 25):
            if self._trenutnoStanje.jePrazno(x):
                pomocna1 = self.getBrojFigura()
                pomocna2 = self.getOdigranPotez()
                self._trenutnoStanje.setOkruglo(x)
                self.staviFiguru()
                self.setOdigranPotez(x)
                if self._trenutnoStanje.suTriUNizu(self.getOdigranPotez()):
                    pi = x
                    maxbris = -9999999
                    for y in range(1, 25):
                        if self._trenutnoStanje.jeUglasto(y) and self.jeBrisljivo(y):
                            self.brisi(y)
                            if (self.heuristika1() + 18) > maxbris:
                                obr = y
                                maxbris = self.heuristika1() + 18
                            self._trenutnoStanje.setUglasto(y)
                    self._trenutnoStanje.setPrazno(x)
                    self.setBrojFigura(pomocna1)
                    self.setOdigranPotez(pomocna2)
                    return maxbris, pi, obr

                (m, n, o) = self.min1(dubina - 1, alfa, beta)
                if m > maxv:
                    maxv = m
                    pi = x
                self._trenutnoStanje.setPrazno(x)
                self.setBrojFigura(pomocna1)
                self.setOdigranPotez(pomocna2)
            
            if maxv >= beta:
                return maxv, pi, 0
                
            if maxv > alfa:
                alfa = maxv
        
        return maxv, pi, 0
    
    def min1(self, dubina, alfa, beta):

        minv = 9999999
        qi = None
        if self.jeKrajPrveFaze() or dubina == 0:
            return self.heuristika1(), self.getOdigranPotez(), 0

        for x in range(1,25):
            if self._trenutnoStanje.jePrazno(x):
                pomocna1 = self.getBrojFigura()
                pomocna2 = self.getOdigranPotez()
                self._trenutnoStanje.setOkruglo(x)
                self.staviFiguru()
                self.setOdigranPotez(x)
                if self._trenutnoStanje.suTriUNizu(self.getOdigranPotez()):
                    qi = x
                    minbris = 9999999
                    for y in range(1, 25):
                        if self._trenutnoStanje.jeOkruglo(y) and self.jeBrisljivo(y):
                            self.brisi(y)
                            if (self.heuristika1() - 18) < minbris:
                                obr = y
                                minbris = self.heuristika1() - 18
                            self._trenutnoStanje.setOkruglo(y)
                    self._trenutnoStanje.setPrazno(x)
                    self.setBrojFigura(pomocna1)
                    self.setOdigranPotez(pomocna2)
                    return minbris, qi, obr
                
                (m, n, o) = self.max1(dubina - 1, alfa, beta)
                if m < minv:
                    minv = m
                    qi = x
                self._trenutnoStanje.setPrazno(x)
                self.setBrojFigura(pomocna1)
                self.setOdigranPotez(pomocna2)
            
            if minv <= alfa:
                return minv, qi, 0
                
            if minv < beta:
                alfa = minv

        return minv, qi, 0

    def max2(self, dubina, alfa, beta):

        maxv = -9999999
        pizvor = None
        pdestinacija = None
        if dubina == 0:
            return self.heuristika2(), [self.getOdigranPotez(), self.getPorekloPoteza()] , 0
        
        rezultat, pobednik = self.jeKrajDrugeFaze()
        if rezultat:
            return self.heuristika2(), [self.getOdigranPotez(), self.getPorekloPoteza()] , 0
        
        for x in range(1, 25):
            if self._trenutnoStanje.jeOkruglo(x):
                for y in self._trenutnoStanje._susednaPolja[x]:                    
                    if self._trenutnoStanje.jeMogucPotez(x, y):  
                        pomocna1 = self.getOdigranPotez()
                        pomocna2 = self.getPorekloPoteza()
                        self._trenutnoStanje.setPrazno(x)
                        self._trenutnoStanje.setOkruglo(y)
                        self.setPorekloPoteza(x)
                        self.setOdigranPotez(y)
                        if self._trenutnoStanje.suTriUNizu(self.getOdigranPotez()):
                            pizvor = x
                            pdestinacija = y
                            maxbris = -9999999
                            for z in range(1, 25):
                                if self._trenutnoStanje.jeUglasto(z) and self.jeBrisljivo(z):
                                    self.brisi(z)
                                    if (self.heuristika2() + 14) > maxbris:
                                        obr = z
                                        maxbris = (self.heuristika2() + 14)
                                    self._trenutnoStanje.setUglasto(z)
                            self._trenutnoStanje.setOkruglo(x)
                            self._trenutnoStanje.setPrazno(y)
                            self.setOdigranPotez(pomocna1)
                            self.setPorekloPoteza(pomocna2)
                            return maxbris, [x, y], obr
                        (m, n, o) = self.min2(dubina - 1, alfa, beta)
                        if m > maxv:
                            maxv = m
                            pizvor = x
                            pdestinacija = y
                        self._trenutnoStanje.setOkruglo(x)
                        self._trenutnoStanje.setPrazno(y)
                        self.setOdigranPotez(pomocna1)
                        self.setPorekloPoteza(pomocna2)
            
                    if maxv >= beta:
                        return maxv, [pizvor, pdestinacija], 0
                    
                    if maxv > alfa:
                        alfa = maxv
            
        return maxv, [pizvor, pdestinacija], 0
    
    def min2(self, dubina, alfa, beta):

        minv = 9999999
        qizvor = None
        qdestinacija = None
        if dubina == 0:
            return self.heuristika1(), [self.getOdigranPotez(), self.getPorekloPoteza()], 0

        rezultat, pobednik = self.jeKrajDrugeFaze()
        if rezultat:
            return self.heuristika2(), [self.getOdigranPotez(), self.getPorekloPoteza()] , 0
        
        for x in range(1, 25):
            if self._trenutnoStanje.jeUglasto(x):
                for y in self._trenutnoStanje._susednaPolja[x]:                    
                    if self._trenutnoStanje.jeMogucPotez(x, y):                        
                        pomocna1 = self.getOdigranPotez()
                        pomocna2 = self.getPorekloPoteza()
                        self._trenutnoStanje.setPrazno(x)
                        self._trenutnoStanje.setOkruglo(y)
                        self.setPorekloPoteza(x)
                        self.setOdigranPotez(y)
                        if self._trenutnoStanje.suTriUNizu(self.getOdigranPotez()):
                            qizvor = x
                            qdestinacija = y
                            minbris = 9999999
                            for z in range(1, 25):
                                if self._trenutnoStanje.jeOkruglo(z) and self.jeBrisljivo(z):
                                    self.brisi(z)
                                    if (self.heuristika2() - 14) < minbris:
                                        obr = z
                                        minbris = (self.heuristika2() - 14)
                                    self._trenutnoStanje.setOkruglo(z)
                            self._trenutnoStanje.setUglasto(x)
                            self._trenutnoStanje.setPrazno(y)
                            self.setOdigranPotez(pomocna1)
                            self.setPorekloPoteza(pomocna2)
                            return minbris, [x, y], obr
                        (m, n, o) = self.min2(dubina - 1, alfa, beta)
                        if m > minv:
                            minv = m
                            qizvor = x
                            qdestinacija = y
                        self._trenutnoStanje.setUglasto(x)
                        self._trenutnoStanje.setPrazno(y)
                        self.setOdigranPotez(pomocna1)
                        self.setPorekloPoteza(pomocna2)
                    
                    if minv <= alfa:
                        return minv, [qizvor, qdestinacija], 0
                        
                    if minv < beta:
                        alfa = minv
        
        return minv, [qizvor, qdestinacija], 0
        
    
    def igraj(self):
        self.pocniIgru()
        while not self.jeKrajPrveFaze():
            os.system("cls")
            self.prikaziTablu()
            if self._trenutnoStanje.getPolje(self.getOdigranPotez())[0] == "(":
                potezi = ""
                for i in range(1, 25):
                    if self._trenutnoStanje.jePrazno(i):
                        potezi += str(i)
                        potezi += " "
                print("Moguci potezi: " + potezi)
                qi = input("Unesite polje. ")
                qi = int(qi)
                while not self._trenutnoStanje.jePrazno(qi):
                    qi = int(input("Polje je zauzeto, probajte ponovo.\n"))
                self._trenutnoStanje.setUglasto(qi)
                self.staviFiguru()
                self.setOdigranPotez(qi)
                
                rezultat = self._trenutnoStanje.suTriUNizu(self.getOdigranPotez())
                if rezultat:
                    os.system("cls")
                    self.prikaziTablu()
                    qi = input("Unesite polje na kojoj je protivnicka figura koju zelite da obrisete.\n")
                    qi = int(qi)
                    while (not self._trenutnoStanje.jeOkruglo(qi)) or (not self.jeBrisljivo(qi)):
                        qi = int(input("Na polju nije protivnicka figura, ili jeste ali u mici, probajte ponovo.\n"))
                    self.brisi(qi)
                    

            elif self._trenutnoStanje.getPolje(self.getOdigranPotez())[0] == "[":
                start = time.time()
                (m, pi, obr) = self.max1(3, -9999999, 9999999)
                end = time.time()
                s=input("Vreme evaluacije: {}s".format(round(end - start, 7))+" [ENTER] ")
                self._trenutnoStanje.setOkruglo(pi)
                self.staviFiguru()
                os.system("cls")
                self.prikaziTablu()
                s=input("Protivnik je stavio figuru na polje " + str(pi) + ". [ENTER] ")
                self.setOdigranPotez(pi)
                if obr > 0:
                    s=input("Protivnik je obrisao figuru sa polja " + str(obr) + ". [ENTER] ")
                    self.brisi(obr)

        os.system('cls')
        self.prikaziTablu()
        print("Vreme je za drugu fazu! [ENTER] ")
        s=input("")
        rezultat, pobednik = self.jeKrajDrugeFaze()
        while not rezultat:
            os.system("cls")
            self.prikaziTablu()
            if self._trenutnoStanje.getPolje(self.getOdigranPotez())[0] == "(":
                potezi = ""
                for i in range(1, 25):
                    if self._trenutnoStanje.jeUglasto(i):
                        for j in self._trenutnoStanje._susednaPolja[i]:
                            if self._trenutnoStanje.jePrazno(j):
                                potezi += str(i) + " na " + str(j) +", "
                print("Moguci potezi: " + potezi[:-2])
                i = int(input("Odaberite polje sa kog zelite da premestite figuru\n"))
                while (not(self._trenutnoStanje.getPolje(i)[0] == "[")) or self._trenutnoStanje.jeBlokiran(i):
                    i=int(input("Polje je blokirano ili nije vasa figura, probajte ponovo.\n"))
                
                j = int(input("Unesite polje na koje hocete da pomerite figuricu.\n"))    
                while not(self._trenutnoStanje.jeMogucPotez(i,j)):
                    j=int(input("Nemoguc potez, probajte ponovo.\n"))
                self._trenutnoStanje.setPrazno(i)
                self._trenutnoStanje.setUglasto(j)
                self.setOdigranPotez(j)
                self.setPorekloPoteza(i)
                
                rezultat = self._trenutnoStanje.suTriUNizu(self.getOdigranPotez())
                if rezultat:
                    os.system("cls")
                    self.prikaziTablu()
                    qi = input("Unesite polje na kojoj je protivnicka figura koju zelite da obrisete.\n")
                    qi = int(qi)
                    while (not self._trenutnoStanje.jeOkruglo(qi)) or (not self.jeBrisljivo(qi)):
                        qi = int(input("Na polju nije protivnicka figura ili jeste ali u mici, probajte ponovo.\n"))
                    self.brisi(qi)
                    

            elif self._trenutnoStanje.getPolje(self.getOdigranPotez())[0] == "[":
                start = time.time()
                (m, pi, obr) = self.max2(4, -9999999, 9999999)
                end = time.time()
                s=input("Vreme evaluacije: {}s".format(round(end - start, 7))+" [ENTER] ")
                self._trenutnoStanje.setOkruglo(pi[1])
                self._trenutnoStanje.setPrazno(pi[0])
                os.system("cls")
                self.prikaziTablu()
                s=input("Protivnik je sa " + str(pi[0]) + " stavio figuru na polje " + ". [ENTER] ")
                self.setOdigranPotez(pi[1])
                self.setPorekloPoteza(pi[0])
                if obr > 0:
                    s=input("Protivnik je obrisao figuru sa polja " + str(obr) + ". [ENTER] ")
                    self.brisi(obr)
            rezultat, pobednik = self.jeKrajDrugeFaze()
        if pobednik == "[":
            print("Gotova igra! Cestitam, pobedili ste! \n")
        else:
            print("Gotova igra! Protivnik je pobedio. \n")

if __name__ == "__main__":
    ig = Igra()
    ig.igraj()

