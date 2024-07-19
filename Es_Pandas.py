""" Scenario: Una catena di ristoranti vuole analizzare le vendite giornaliere in diverse filiali.
Obiettivo: Utilizzare pandas per calcolare le vendite medie giornaliere per ogni filiale.
Dati: Il dataset contiene colonne "Data", "Filiale" e "Vendite".

Compiti:
Genera i dati da un file CSV.
Utilizza groupby() per raggruppare i dati per "Data" e "Filiale".
Calcola la media delle vendite giornaliere per filiale
Calcola quale filiale ha venduto di più
Salva tutti i valori e i risultati su un nuovo file(ES: csv). """
import pandas as pd


def carica_dati(file_path):
    df = pd.read_csv(file_path)
    print(df)
    return df

def raggruppa_dati(df):
    grouped_df = df.groupby(['Data', 'Filiale']).agg({'Vendite': 'sum'}).reset_index()
    print("Dati raggruppati per 'Data' e 'Filiale':")
    print(grouped_df)
    return grouped_df

def calcola_media_vendite(df):
    media_vendite = df.groupby('Filiale')['Vendite'].mean().reset_index()
    media_vendite.columns = ['Filiale', 'Media_Vendite_Giornaliere']
    print("Media delle vendite giornaliere per filiale:")
    print(media_vendite)
    return media_vendite

def filiale_con_vendite_massime(df):
    totale_vendite_filiale = df.groupby('Filiale')['Vendite'].sum().reset_index()
    filiale_massima = totale_vendite_filiale.loc[totale_vendite_filiale['Vendite'].idxmax()]
    print("Filiale con vendite totali massime:")
    print(filiale_massima)
    return filiale_massima

def salva_dati(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"I risultati sono stati salvati nel file: {risultato_path}")



#test
file_path = 'Test 19 luglio/vendite_filiali.csv'  
df = carica_dati(file_path)

grouped_df = raggruppa_dati(df)

media_vendite = calcola_media_vendite(grouped_df)

filiale_massima = filiale_con_vendite_massime(grouped_df)

risultato_path = 'risultati_vendite_filiali.csv'
salva_dati(media_vendite, risultato_path)

