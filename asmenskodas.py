from kodotikrinimas import KodoTikrinimas
from kodogeneravimas import KodoGeneravimas


if __name__ == '__main__':
    asmenskodas = KodoTikrinimas()
    kodogeneravimas = KodoGeneravimas()
    while True:
        print("1 - asmens kodo tikrinimui, 2 - asmens kodo generavimui, 0 - išeiti.")
        kodas = input("Pasirinkite: ")
        match kodas:
            case '0':
                break
            case '1':
                asmenskodas.validus(input("Įveskite asmens kodą: "))
            case '2':
                kodogeneravimas.generuoti()
            case _:
                print("Netinkamas pasirinkimas.")    
