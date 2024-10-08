# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:01:17 2024

@author: michael sivertsen
"""

import matplotlib.pyplot as plt
from datetime import datetime as datetime
from Oppgave6d import LagListe as LagListe
from Oppgave_e import convert_to_datetime as konverter_til_tid

filNavn1 = "datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
filNavn2 = "datafiler/trykk_og_temperaturlogg_rune_time.csv.txt"

dato_og_tid_streng, tid_siden_start, trykk_barometer, trykk_absolutt, temperatur_streng = LagListe(filNavn2, 5)
navn, stasjon, stasjon_tid_streng, lufttemperatur_streng, lufttrykk_streng = LagListe(filNavn1, 5)

temperatur = [float(temp.replace(',', '.')) for temp in temperatur_streng]
lufttemperatur = [float(temp.replace(',', '.')) for temp in lufttemperatur_streng]

dato_og_tid = [konverter_til_tid(dato, "%m %d %Y %H:%M") for dato in dato_og_tid_streng]
stasjon_tid = [konverter_til_tid(dato, "%d.%m.%Y %H:%M")  for dato in stasjon_tid_streng]

plt.plot(dato_og_tid,temperatur)
plt.plot(stasjon_tid,lufttemperatur)
plt.xlabel = ('Tid')
plt.ylabel = ('Verdi')
plt.title('Temperatur og trykk fra første fil')
plt.legend()
plt.show()
