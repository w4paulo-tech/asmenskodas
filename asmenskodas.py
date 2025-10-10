import datetime

def pavienis_kodas(asmens_kodas):
    "Gražina asmens kodą saraše."
    pavienis = []
    for x in asmens_kodas:
        pavienis.append(x)
    return pavienis

def data(sk):
    "Gražina gimimo data str."
    pavienis_kodas(sk)
    pilni_metai = sk[1], sk[2], sk[3], sk[4], sk[5], sk[6]
    return "".join(pilni_metai)

def kontrolinis_skaicius(sk):
    "Gražina ar tinkamas paskutinis asmens kodo skaičius."
    # sk = pavienis_kodas(sk2)
    s1 = int(sk[0]) * 1 + int(sk[1]) * 2 + int(sk[2]) * 3 + int(sk[3]) * 4 + \
        int(sk[4]) * 5 + int(sk[5]) * 6 + int(sk[6]) * 7 + int(sk[7]) * 8 + \
        int(sk[8]) * 9 + int(sk[9]) * 1

    s2 = int(sk[0]) * 3 + int(sk[1]) * 4 + int(sk[2]) * 5 + int(sk[3]) * 6 + \
        int(sk[4]) * 7 + int(sk[5]) * 8 + int(sk[6]) * 9 + int(sk[7]) * 1 + \
        int(sk[8]) * 2 + int(sk[9]) * 3
    
    if s1 % 11 != 10 and s1 % 11 == int(sk[10]):
        return True    
    elif (s1 % 11 == 10 and s2 % 11 != 10) and s2 % 11 == int(sk[10]):
        return True    
    elif (s1 % 11 == 10 and s2 % 11 == 10) and s2 % 11 == int(sk[10]):
        return True    
    else:
        return False
          
def validus(asmens_kodas):
    "Patikrina ar validus asmens kodas."
    if len(asmens_kodas) == 11:
        if int(asmens_kodas[0]) in range(3, 7):
            if datetime.datetime.strptime(data(asmens_kodas), "%y%m%d"):
                if (kontrolinis_skaicius(asmens_kodas)) == True:
                    return print(f"Asmens kodas: {asmens_kodas} validus.")
                else:
                    return print(f"Netinkamas kontrolinis skaičius {asmens_kodas[10]}.")
            return print(f"Netinkama data: {data(asmens_kodas)}")
        return print(f"Netinkamas pirmas skaičius: {asmens_kodas[0]}")
    return print("Netinkamas skaitmenų kiekis.")

def asmens_lytis(lytis):
    "Sugeneruoja pirmą skaičių"
    metai = input("Įveskite gimimo metus (YYYY-MM-DD): ")

    if int(lytis) == 1:
        if (datetime.datetime.strptime(metai, "%Y-%m-%d") >= 
        datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")):
            return 5
        else:
            return 3
    
    if int(lytis) == 0:
        if (datetime.datetime.strptime(metai, "%Y-%m-%d") >= 
            datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")):
            return 6
        else:
            return 4
        
# def gimimo_metai():
#     return metai

def generuoti(metai):

    skaicius = f"{asmens_lytis(input("1 - Vyras, 0 - Moteris\nĮveskite lytį: "))}\
            {datetime.datetime.strptime(metai, "%y%m%d")}\
            {input("Įveskite tris eilės numerio skaičius: ")}"
    return print(skaicius)

    
while True:
    print("1 - asmens kodo tikrinimui, 2 - asmens kodo generavimui, 0 - išeiti.")
    kodas = input("Pasirinkite: ")
    match kodas:
        case '0':
            break
        case '1':
            validus(input("Įveskite asmens kodą: "))
        case '2':
            # metai = input("Įveskite gimimo metus (YYYY-MM-DD")
            generuoti(input("iveskite"))
        case _:
            print("Netinkamas pasirinkimas.")    

        




        
    

    



    