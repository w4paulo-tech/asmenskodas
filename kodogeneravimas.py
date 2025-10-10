from datetime import datetime

class KodoGeneravimas:
    def __init__(self):
        return
    
    def asmens_lytis(self, lytis):
        "Sugeneruoja pirmą skaičių"

        if int(lytis) == 1:
            if (datetime.strptime(self.metai, "%Y-%m-%d") >= 
            datetime.strptime("2000-01-01", "%Y-%m-%d")):
                return 5
            else:
                return 3
        elif int(lytis) == 2:
            if (datetime.strptime(self.metai, "%Y-%m-%d") >= 
                datetime.strptime("2000-01-01", "%Y-%m-%d")):
                return 6
            else:
                return 4  
        
    def pavienis_kodas(self, pavienis):
        "Gražina skaičius saraše."
        pavienis = []
        for x in self.nepilnas:
            pavienis.append(int(x))
        return pavienis
        
    def kontrolinis_skaicius(self):
        "Gražina paskutini asmens kodo skaičių."
        sk = self.pavienis_kodas(self.nepilnas)
        s1 = sk[0] * 1 + sk[1] * 2 + sk[2] * 3 + sk[3] * 4 + \
            sk[4] * 5 + sk[5] * 6 + sk[6] * 7 + sk[7] * 8 + \
            sk[8] * 9 + sk[9] * 1

        s2 = sk[0] * 3 + sk[1] * 4 + sk[2] * 5 + sk[3] * 6 + \
            sk[4] * 7 + sk[5] * 8 + sk[6] * 9 + sk[7] * 1 + \
            sk[8] * 2 + sk[9] * 3
        
        if s1 % 11 != 10:
            return s1 % 11 
        elif s1 % 11 == 10 and s2 % 11 != 10:
            return s2 % 11 
        else:
            return "0"    
    
    def gimimo_metai(self):
        skaicius2_7 = datetime.strptime(self.metai, "%Y-%m-%d").strftime("%y%m%d")
        return skaicius2_7
      
    def generuoti(self):
        "Sugeneruoja validų asmens kodą."
        while True:
            try:
                skaicius1 = int(input("1 - Vyras, 2 - Moteris\nĮveskite lytį: "))
                if skaicius1 == 1 or 2:
                    self.metai = input("Įveskite gimimo metus (YYYY-MM-DD): ")
                    try:
                        if datetime.strptime(self.metai, "%Y-%m-%d"):
                            skaicius8_10 = input("Įveskite tris eilės numerio skaičius: ")
                            if len(skaicius8_10) != 3:
                                return print("Įvestas netinkamas kiekis skaičių.")
                            else:
                                self.nepilnas = (str(self.asmens_lytis(skaicius1)) + 
                                                str(self.gimimo_metai()) + str(skaicius8_10))
                                return print(f"Jūsų asmens kodas yra: "
                                            f"{self.nepilnas + str(self.kontrolinis_skaicius())}  ")
                    except ValueError:        
                        return print("Blogu formatu įvesta data.")
            except ValueError:
                return print("Neteisingai įvesta lytis.")