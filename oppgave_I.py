import matplotlib.pyplot as plt
from datetime import datetime as datetime
from Oppgave6d import LagListe as LagListe
from Oppgave_e import convert_to_datetime as konverter_til_tid

filNavn1 = "datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
filNavn2 = "datafiler/trykk_og_temperaturlogg_rune_time.csv.txt"

# Hent data fra filene
dato_og_tid_streng, tid_siden_start, trykk_barometer_streng, trykk_absolutt_streng, temperatur_streng = LagListe(filNavn2, 5)
navn, stasjon, stasjon_tid_streng, lufttemperatur_streng, lufttrykk_streng = LagListe(filNavn1, 5)

# Konverter data til riktig format
temperatur = [float(temp.replace(',', '.')) for temp in temperatur_streng]
lufttemperatur = [float(temp.replace(',', '.')) for temp in lufttemperatur_streng]
trykk_absolutt = [float(trykk.replace(',', '.')) for trykk in trykk_absolutt_streng]
lufttrykk = [float(trykk.replace(',', '.')) for trykk in lufttrykk_streng]
trykk_barometer = []
for trykk in trykk_barometer_streng:
    trykk = trykk.replace(',','.')
    try:
        trykk_barometer.append(float(trykk))
    except Exception as e:
        trykk_barometer.append(0)

dato_og_tid = [konverter_til_tid(dato, "%m.%d.%Y %H:%M") for dato in dato_og_tid_streng]
stasjon_tid = [konverter_til_tid(dato, "%d.%m.%Y %H:%M") for dato in stasjon_tid_streng]

# Plot temperatur
plt.subplot(2, 1, 1)
plt.plot(dato_og_tid, temperatur, label='Temperatur (fil 2)')
plt.plot(stasjon_tid, lufttemperatur, label='Lufttemperatur (fil 1)')

plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur fra begge filer')
plt.legend()

# Plot trykk
plt.subplot(2, 1, 2)
plt.plot(dato_og_tid, trykk_absolutt, label='Absolutt trykk (fil 2)')
plt.plot(stasjon_tid, lufttrykk, label='Lufttrykk (fil 1)')
plt.plot(dato_og_tid, trykk_barometer, label='Barometrisk trykk (fil 2)')
plt.xlabel('Tid')
plt.ylabel('Trykk (hPa)')
plt.title('Atmosfærisk trykk fra begge filer')
plt.legend()

plt.tight_layout()
plt.show()
