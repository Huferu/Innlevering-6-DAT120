#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:01:58 2024

@author: bruker
"""

import matplotlib.pyplot as plt
from datetime import datetime

# Eksempeldata: Tidspunkter og temperaturer (må passe i lengde)
tidspunkter = [datetime(2021, 6, 11, i) for i in range(24)]
temperaturer = [16, 15.8, 16.3, 16, 15.5, 16.1, 15.9, 16.4, 17, 16.2, 15.8, 16, 15.6, 16.1, 15.9, 16.3, 16, 15.8, 16.4, 16, 15.8, 16.2, 16.1, 16]

# Kontroller at lengdene matcher
assert len(tidspunkter) == len(temperaturer), "Listene over tidspunkter og temperaturer må ha samme lengde!"

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
gj_tider, gj_temperaturer = glidende_gjennomsnitt(tidspunkter, temperaturer, n)

# Plotting
plt.plot(tidspunkter, temperaturer, label='Original temperatur')
plt.plot(gj_tider, gj_temperaturer, color='orange', label=f'Glidende gjennomsnitt (n={n})')

plt.xlabel('Tidspunkt')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur med glidende gjennomsnitt')
plt.legend()
plt.xticks(rotation=45)
plt.show()

    