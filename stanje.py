from hashmap import HashMap, LinearHashMap
class Stanje(object):

    def __init__(self):
        self._tabla = [[" 01 ", " 02 ", " 03 ", " 04 ", " 05 ", " 06 ", " 07 ", " 08 "],
        [" 09 ", " 10 ", " 11 ", " 12 ", " 13 ", " 14 ", " 15 ", " 16 "],
        [" 17 ", " 18 ", " 19 ", " 20 ", " 21 ", " 22 ", " 23 ", " 24 "]]   
                                                                      
        self._susednaPolja = LinearHashMap()
        self._susednaPolja[1] = [8, 2]
        self._susednaPolja[2] = [1, 3, 10]
        self._susednaPolja[3] = [2, 4]
        self._susednaPolja[4] = [3, 5, 12]
        self._susednaPolja[5] = [4, 6]
        self._susednaPolja[6] = [5, 7, 14]
        self._susednaPolja[7] = [6, 8]
        self._susednaPolja[8] = [7, 1, 16]
        self._susednaPolja[9] = [16, 10]
        self._susednaPolja[10] = [2, 9, 11, 18]
        self._susednaPolja[11] = [10, 12]
        self._susednaPolja[12] = [4, 11, 13, 20]
        self._susednaPolja[13] = [12, 14]
        self._susednaPolja[14] = [6, 13, 15, 22]
        self._susednaPolja[15] = [14, 16]
        self._susednaPolja[16] = [8, 9, 15, 24]
        self._susednaPolja[17] = [24, 18]
        self._susednaPolja[18] = [10, 17, 19]
        self._susednaPolja[19] = [18, 20]
        self._susednaPolja[20] = [12, 19, 21]
        self._susednaPolja[21] = [20, 22]
        self._susednaPolja[22] = [14, 21, 23]
        self._susednaPolja[23] = [22, 24]
        self._susednaPolja[24] = [16, 17, 23]
    
    def getPolje(self, i):
        q = (i-1) // 8
        r = (i-1) % 8
        return self._tabla[q][r]            


    def jePrazno(self, i):
        return self.getPolje(i)[0] == " "

    def jeOkruglo(self, i):
        return self.getPolje(i)[0] == "("               

    def jeUglasto(self, i):     
        return self.getPolje(i)[0] == "["


    def setOkruglo(self, i):
        res = "(" + self.getPolje(i)[1] + self.getPolje(i)[2] + ")"
        q = (i-1) // 8
        r = (i-1) % 8
        self._tabla[q][r] = res

    def setUglasto(self, i):
        res = "[" + self.getPolje(i)[1] + self.getPolje(i)[2] + "]"
        q = (i-1) // 8
        r = (i-1) % 8
        self._tabla[q][r] = res

    def setPrazno(self, i):
        res = " " + self.getPolje(i)[1] + self.getPolje(i)[2] + " "
        q = (i-1) // 8
        r = (i-1) % 8
        self._tabla[q][r] = res

    def suSusedna(self, i, j):
        if j in self._susednaPolja[i]:
            return True
        return False
        # q1 = (i-1) // 8
        # r1 = (i-1) % 8
        # q2 = (j-1) // 8
        # r2 = (j-1) % 8
        # if (q1 == q2) and (abs(r1 - r2) in [1, 7]):            
        #     return True
        # if (r1 == r2) and (r2 in [1, 3, 5, 7]) and (abs(q1 - q2) == 1): 
        #     return True
        # return False

    def jeMogucPotez(self, i, j):                         
        if not self.jePrazno(j):   
            return False
        if self.suSusedna(i, j):
            return True
        return False

    def suTriUNizu(self, i):           #1
        q = (i-1) // 8
        r = (i-1) % 8
        if self.getPolje(i)[0]==" ":
            return False
        if r in [0,2,4]:
            if self.getPolje(i)[0] == self.getPolje(i+1)[0] and self.getPolje(i)[0] == self.getPolje(i+2)[0]:
                return True
        if r in [2, 4, 6]:
            if self.getPolje(i)[0] == self.getPolje(i-1)[0] and self.getPolje(i)[0] == self.getPolje(i-2)[0]:
                return True
        if r==0:
            if self.getPolje(i)[0] == self.getPolje(i+6)[0] and self.getPolje(i)[0] == self.getPolje(i+7)[0]:
                return True
        if r==6:
            if self.getPolje(i)[0] == self.getPolje(i+1)[0] and self.getPolje(i)[0] == self.getPolje(i-6)[0]:
                return True
        if r in [1, 3, 5, 7]:
            if self.getPolje(r+1)[0] == self.getPolje(r+9)[0] and self.getPolje(r+9)[0] == self.getPolje(r+17)[0]:
                return True
            if not(r == 7):
                if self.getPolje(i)[0] == self.getPolje(i+1)[0] and self.getPolje(i)[0] == self.getPolje(i-1)[0]:
                    return True
            if r == 7:
                if self.getPolje(i)[0] == self.getPolje(i-7)[0] and self.getPolje(i)[0] == self.getPolje(i-1)[0]:
                    return True
        return False
    
     
    def brMica(self, c):
        res = 0
        i = 1
        while i<8:
            if i < 7:
                for j in range(3):
                    if self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i + 2 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c:
                        res+=1
            else:
                for j in range(3):
                    if self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i - 6 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c:
                        res+=1
            i+=2
        i = 2
        while i<=8:
            if self.getPolje(i)[0] == self.getPolje(i + 8)[0] and self.getPolje(i)[0] == self.getPolje(i + 16)[0] and self.getPolje(i)[0] == c:
                res+=1
            i+=2
        return res
            
    def razlikaMica(self):                              #2
        return self.brMica("(") - self.brMica("[")

    def brBlokiranih(self, c):                          #3
        res = 0
        for i in range(1, 25):
            if self.jeBlokiran(i) and self.getPolje(i)[0] == c:
                    res += 1
        return res
    
    def razlikaBlokiranih(self):
        return self.brBlokiranih("[") - self.brBlokiranih("(")

    def jeBlokiran(self, i):
        for j in range(1, 25):              
            if self.suSusedna(i, j) and (self.jeMogucPotez(i, j)):
                return False
        return True
    
    def brFigura(self, c):
        res = 0
        for i in range (1, 25):
            if self.getPolje(i)[0] == c:
                res += 1
        return res

    def razlikaFigura(self):                          #4
        return self.brFigura("(") - self.brFigura("[")
    
    def brSkoroMica(self, c):
        res = 0
        i = 1
        while i < 8:
            if i < 7:
                for j in range(3):
                    if (self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c and self.getPolje(i + 2 + 8*j)[0] == " ") or \
                        (self.getPolje(i + 8*j)[0] == self.getPolje(i + 2 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c and self.getPolje(i + 1 + 8*j)[0] == " ") or \
                            (self.getPolje(i + 2 + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i + 8*j)[0] == " "):
                        res+=1
            else:
                for j in range(3):
                    if (self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c and self.getPolje(i - 6 + 8*j)[0] == " ") or \
                        (self.getPolje(i + 8*j)[0] == self.getPolje(i - 6 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c and self.getPolje(i + 1 + 8*j)[0] == " ") or \
                            (self.getPolje(i - 6 + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i + 8*j)[0] == " "):
                        res+=1
            i+=2
        i = 2
        while i<=8:
            if (self.getPolje(i)[0] == self.getPolje(i + 8)[0] and self.getPolje(i)[0] == c and self.getPolje(i + 16)[0] == " ") or \
                (self.getPolje(i)[0] == self.getPolje(i + 16)[0] and self.getPolje(i)[0] == c and self.getPolje(i + 8)[0] == " ") or \
                    (self.getPolje(i + 16)[0] == self.getPolje(i + 8)[0] and self.getPolje(i + 8)[0] == c and self.getPolje(i)[0] == " "):
                res+=1
            i+=2
        return res

    def razlikaSkoroMica(self):                                   #5
        return self.brSkoroMica("(") - self.brSkoroMica("[")

    def brDuplaMica(self, c):                                   #7
        res = 0
        for j in range(3):
            i = 1
            while i < 8:
                if self.getPolje(i + 8*j)[0] == c:
                    if i in [3,5]:
                        if self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i + 2 + 8*j)[0] and \
                            self.getPolje(i + 8*j)[0] == self.getPolje(i - 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i - 2 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c:
                            res+=1
                    elif i == 1:
                        if self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i + 2 + 8*j)[0] and \
                            self.getPolje(i + 8*j)[0] == self.getPolje(i + 6 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i + 7 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c:
                            res+=1
                    elif i == 7: 
                        if self.getPolje(i + 8*j)[0] == self.getPolje(i + 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i - 6 + 8*j)[0] and \
                            self.getPolje(i + 8*j)[0] == self.getPolje(i - 1 + 8*j)[0] and self.getPolje(i + 8*j)[0] == self.getPolje(i - 2 + 8*j)[0] and self.getPolje(i + 8*j)[0] == c:
                            res+=1
                i+=2
        i = 2
        while i < 8:
            if self.getPolje(i)[0] == self.getPolje(i + 8)[0] and self.getPolje(i)[0] == self.getPolje(i + 16)[0] and self.getPolje(i)[0] == c:
                if self.getPolje(i - 1)[0] == self.getPolje(i+1)[0] and self.getPolje(i - 1)[0] == c:
                    res+=1
                elif self.getPolje(i + 7)[0] == self.getPolje(i + 9)[0] and self.getPolje(i + 7)[0] == c:
                    res+=1
                elif self.getPolje(i + 15)[0] == self.getPolje(i + 17)[0] and self.getPolje(i + 15)[0] == c:
                    res+=1
            i+=2
        if self.getPolje(i)[0] == self.getPolje(i + 8)[0] and self.getPolje(i)[0] == self.getPolje(i + 16)[0] and self.getPolje(i)[0] == c:
                if self.getPolje(i - 1)[0] == self.getPolje(i - 7)[0] and self.getPolje(i - 1)[0] == c:
                    res+=1
                elif self.getPolje(i + 7)[0] == self.getPolje(i + 1)[0] and self.getPolje(i + 7)[0] == c:
                    res+=1
                elif self.getPolje(i + 15)[0] == self.getPolje(i + 9)[0] and self.getPolje(i + 15)[0] == c:
                    res+=1
        return res
        
    def razlikaDuplaMica(self):
        return self.brDuplaMica("(") - self.brDuplaMica("[")

    def brSkoroDuplaMica(self, c):
        res = 0
        for j in range(0, 3):
            i = 1
            while i < 8:
                if self.getPolje(i + 8*j)[0] == c:
                    if i not in [1, 7]:
                        if (self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i + 2 + 8*j)[0] == " " and self.getPolje(i - 1 + 8*j)[0] == c and self.getPolje(i - 2 + 8*j)[0] == " ") or \
                            (self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i + 2 + 8*j)[0] == " " and self.getPolje(i - 1 + 8*j)[0] == " " and self.getPolje(i - 2 + 8*j)[0] == c) or \
                                (self.getPolje(i + 1 + 8*j)[0] == " " and self.getPolje(i + 2 + 8*j)[0] == c and self.getPolje(i - 1 + 8*j)[0] == c and self.getPolje(i - 2 + 8*j)[0] == " ") or \
                                    (self.getPolje(i + 1 + 8*j)[0] == " " and self.getPolje(i + 2 + 8*j)[0] == c and self.getPolje(i - 1 + 8*j)[0] ==" " and self.getPolje(i - 2 + 8*j)[0] == c):
                            res+=1
                    elif i==1:
                        if (self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i + 2 + 8*j)[0] == " " and self.getPolje(i + 7 + 8*j)[0] == c and self.getPolje(i + 6 + 8*j)[0] == " ") or \
                            (self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i + 2 + 8*j)[0] == " " and self.getPolje(i + 7 + 8*j)[0] == " " and self.getPolje(i + 6 + 8*j)[0] == c) or \
                                (self.getPolje(i + 1 + 8*j)[0] == " " and self.getPolje(i + 2 + 8*j)[0] == c and self.getPolje(i + 7 + 8*j)[0] == c and self.getPolje(i + 6 + 8*j)[0] == " ") or \
                                    (self.getPolje(i + 1 + 8*j)[0] == " " and self.getPolje(i + 2 + 8*j)[0] == c and self.getPolje(i + 7 + 8*j)[0] ==" " and self.getPolje(i + 6 + 8*j)[0] == c):
                            res+=1
                    else:
                        if (self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i - 6 + 8*j)[0] == " " and self.getPolje(i - 1 + 8*j)[0] == c and self.getPolje(i - 2 + 8*j)[0] == " ") or \
                            (self.getPolje(i + 1 + 8*j)[0] == c and self.getPolje(i - 6 + 8*j)[0] == " " and self.getPolje(i - 1 + 8*j)[0] == " " and self.getPolje(i - 2 + 8*j)[0] == c) or \
                                (self.getPolje(i + 1 + 8*j)[0] == " " and self.getPolje(i - 6 + 8*j)[0] == c and self.getPolje(i - 1 + 8*j)[0] == c and self.getPolje(i - 2 + 8*j)[0] == " ") or \
                                    (self.getPolje(i + 1 + 8*j)[0] == " " and self.getPolje(i - 6 + 8*j)[0] == c and self.getPolje(i - 1 + 8*j)[0] ==" " and self.getPolje(i - 2 + 8*j)[0] == c):
                            res+=1
                i+=2
        return res
    
    def razikaSkoroDuplaMica(self):                                         #6
        return self.brSkoroDuplaMica("(") - self.brSkoroDuplaMica("[")


    def __str__(self):
        s=""
        s+=(self.getPolje(1) + "-----------" + self.getPolje(2) + "-----------" + self.getPolje(3) + "\n")
        s+=(" |              |              |\n")
        s+=(" |   " + self.getPolje(9) + "------" + self.getPolje(10) + "------" + self.getPolje(11) + "  |\n")
        s+=(" |    |         |         |    |\n")
        s+=(" |    |   " + self.getPolje(17) + "-" + self.getPolje(18) + "-" + self.getPolje(19) + "  |    |\n")
        s+=(" |    |    |         |    |    |\n")
        s+=(self.getPolje(8) + "-" + self.getPolje(16) + "-" + self.getPolje(24) + "      " + self.getPolje(20) + "-" + self.getPolje(12) + "-" + self.getPolje(4) + "\n")
        s+=(" |    |    |         |    |    |\n")
        s+=(" |    |   " + self.getPolje(23) + "-" + self.getPolje(22) + "-" + self.getPolje(21) + "  |    |\n")
        s+=(" |    |         |         |    |\n")
        s+=(" |   " + self.getPolje(15) + "------" + self.getPolje(14) + "------" + self.getPolje(13) + "  |\n")
        s+=(" |              |              |\n")
        s+=(self.getPolje(7) + "-----------" + self.getPolje(6) + "-----------" + self.getPolje(5) + "\n")
        return s

if __name__ == "__main__":
    st=Stanje()
    st.setOkruglo(1)
    st.setOkruglo(2)
    st.setOkruglo(5)
    st.setUglasto(6)
    st.setOkruglo(7)
    st.setOkruglo(9)
    st.setOkruglo(11)
    st.setOkruglo(12)
    st.setUglasto(16)
    st.setOkruglo(19)
    st.setOkruglo(20)
    st.setOkruglo(4)
    st.setOkruglo(13)
    st.setOkruglo(3)
    st.setOkruglo(8)
    print(st)
    s = input("")
    for i in range(1,25):
        print(str(st.jeBlokiran(i)) + str(i))
    print(st.brBlokiranih("("))