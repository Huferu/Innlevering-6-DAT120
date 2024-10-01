def LagListe(filnavn:str, antallLister:int):
    try:
        fil = open(filnavn, "r")
    except FileNotFoundError():
        print("Fant ikke fil")
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


# print(LagListe("datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt",5))
# print("")
# print(LagListe("datafiler/trykk_og_temperaturlogg_rune_time.csv.txt",5))