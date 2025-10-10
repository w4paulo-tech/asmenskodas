from datetime import datetime

class KodoTikrinimas:
    def __init__(self):
        self.pavienis = []        

    def pavienis_kodas(self, asmens_kodas):
        "Gražina asmens kodą saraše."
        self.asmens_kodas = asmens_kodas
        for x in asmens_kodas:
            self.pavienis.append(int(x))
        return self.pavienis

    def data(self, sk):
        "Gražina gimimo data str."
        self.pavienis_kodas(sk)
        return sk[1:7]

    def kontrolinis_skaicius(self):
        "Gražina ar tinkamas paskutinis asmens kodo skaičius."
        sk = self.pavienis
        s1 = int(sk[0] * 1 + sk[1] * 2 + sk[2] * 3 + sk[3] * 4 + \
            sk[4] * 5 + sk[5] * 6 + sk[6] * 7 + sk[7] * 8 + \
            sk[8] * 9 + sk[9] * 1)

        s2 = int(sk[0] * 3 + sk[1] * 4 + sk[2] * 5 + sk[3] * 6 + \
            sk[4] * 7 + sk[5] * 8 + sk[6] * 9 + sk[7] * 1 + \
            sk[8] * 2 + sk[9] * 3)
        
        if s1 % 11 != 10 and s1 % 11 == sk[10]:
            return True    
        elif (s1 % 11 == 10 and s2 % 11 != 10) and s2 % 11 == sk[10]:
            return True    
        elif (s1 % 11 == 10 and s2 % 11 == 10) and s2 % 11 == sk[10]:
            return True    
        else:
            return False
          
    def validus(self, asmens_kodas):
        "Patikrina ar validus asmens kodas."
        if len(asmens_kodas) == 11:
            if int(asmens_kodas[0]) in range(3, 7):
                try:
                    if datetime.strptime(self.data(asmens_kodas), "%y%m%d"):
                        if (self.kontrolinis_skaicius()) == True:
                            return print(f"Asmens kodas: {asmens_kodas} validus.")
                        else:
                            return print(f"Netinkamas kontrolinis skaičius {asmens_kodas[10]}.")
                except ValueError:   
                    return print(f"Netinkama data: {self.data(asmens_kodas)}")
            return print(f"Netinkamas pirmas skaičius: {asmens_kodas[0]}")
        return print("Netinkamas skaitmenų kiekis.")    