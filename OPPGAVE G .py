#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:01:58 2024

@author: bruker
"""

import matplotlib.pyplot as plt
from datetime import datetime
from Oppgave6d import LagListe as Lagliste
from Oppgave_e import convert_to_datetime as Konventer_til_dato

# Eksempeldata: Tidspunkter og temperaturer (må passe i lengde)
Navn,Stasjon,Tid,Lufttemperatur,Lufttrykk = Lagliste('datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt',5)
print(Tid)

Dato = [Konventer_til_dato(dato, '%d.%m.%Y %H:%M') for dato in Tid]
temperaturer = [float(temp.replace(',', '.')) for temp in Lufttemperatur]

# Kontroller at lengdene matcher
assert len(Dato) == len(temperaturer), "Listene over tidspunkter og temperaturer må ha samme lengde!"

# Funksjon for glidende gjennomsnitt
def glidende_gjennomsnitt(tidspunkter, temperaturer, n):
    gjennomsnitt_tider = []
    gjennomsnitt_temperaturer = []
    
    for i in range(n, len(temperaturer) - n):
        snitt = sum(temperaturer[i-n:i+n+1]) / (2 * n + 1)
        gjennomsnitt_tider.append(tidspunkter[i])
        gjennomsnitt_temperaturer.append(snitt)
    
    return gjennomsnitt_tider, gjennomsnitt_temperaturer

# Kall funksjonen for n = 2 (eller 30 i ditt tilfelle)
n = 2
gj_tider, gj_temperaturer = glidende_gjennomsnitt(Dato, temperaturer, n)

# Plotting
plt.plot(Dato, temperaturer, label='Original temperatur')
plt.plot(gj_tider, gj_temperaturer, color='orange', label=f'Glidende gjennomsnitt (n={n})')

plt.xlabel('Tidspunkt')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur med glidende gjennomsnitt')
plt.legend()
plt.xticks(rotation=45)
plt.show()

    