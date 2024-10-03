def LagListe(filnavn:str, antallLister:int = 1):
    try:
        fil = open(filnavn, "r")
    except FileNotFoundError():
        print("Fant ikke fil")
        return[]
    except Exception as e:
        print(e)
        return
    lister = [[] for i in range(antallLister)]
    linjer = fil.readlines()
    for linje in linjer[1:-1]:
        kolonne = linje.strip().split(";")
        for i in range(min(antallLister, len(kolonne))):
            lister[i].append(kolonne[i])
    return lister

if(__name__ == '__main__'):
    import matplotlib.pyplot as plt
    from datetime import datetime
    filNavn1 = "datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
    filNavn2 = "datafiler/trykk_og_temperaturlogg_rune_time.csv.txt"
    Navn,Stasjon,Tid,Lufttemperatur,Lufttrykk = LagListe(filNavn1, 5)
    Dato_og_tid,Tid_siden_start,Trykk_barometer,Trykk_absolutt, Temperatur = LagListe(filNavn2, 5)

    NyTid = [datetime.strptime(dato, "%d.%m.%Y %H:%M") for dato in Tid]
    
    print(NyTid)
    print(Lufttemperatur)
    plt.plot(NyTid, Lufttemperatur, label = "Temperatur")
    plt.plot(NyTid, Lufttrykk, label = "Trykk")
    plt.xlabel = ('Tid')
    plt.ylabel = ('Verdi')
    plt.title('Temperatur og trykk fra første fil')
    plt.legend()
    plt.show()