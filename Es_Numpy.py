""" Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media, minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.

Compiti:
Crea una dataset di dati da almeno 24 posizioni
Calcola la temperatura media 
Trova la temperatura massima e minima.
Determina la temperatura più probabile per le prossime 4 posizioni rispetto a un aumento costante 
di 0,2 gradi al giorno ogni settimana. """

import numpy as np

#dataset randomico contenente 24 temperature registrate
def genera_temperature():
    array_temp = np.random.randint(0, 50, size = 24)
    print(array_temp)
    return array_temp

def media(array_temp):
    media = np.mean(array_temp)
    print(f"La media delle temperature è: {media:.2f} °C")

def max_min(array_temp):
    max = np.max(array_temp)
    min = np.min(array_temp)
    print (f"La temperatura massima è {max:.2f} °C e quella minima è {min:.2f} °C")

#Determinare la temperatura più probabile per le prossime 4 posizioni
def previsione(array_temp):

    #Aumento di 0.2 gradi al giorno ogni settimana
    aumento_giornaliero = 0.2 / 7

    #Calcolo delle prossime 4 temperature
    prossime_temperature = array_temp[-1] + aumento_giornaliero * np.arange(1, 5)
    print(f"Prossime 4 temperature previste: {prossime_temperature}")




#test
array_temp = genera_temperature()
media(array_temp)
max_min(array_temp)
previsione(array_temp)