
#Datei einfügen
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "General_ledger_sample.csv")

#Datei einlesen
df = pd.read_csv(file_path, sep=",")

#Duplikate finden
duplikate = df[df.duplicated(keep=False)]
print("\n-Duplikat gefunden")
if duplikate.empty:
    print("Keine Duplikate gefunden.")
else:
    print(duplikate)

#Anomalien finden
anomalien = df[df["amount"] > 10000]
if anomalien.empty:
  print("\n-Keine Anomalie gefunden")
else:
  print("\n-Anomalie gefunden")
  print(anomalien)


#Summe aller Beträge
Ergebnis = df["amount"]. sum()
gruppierte_summe =df.groupby("user_id")["amount"].sum()
print(gruppierte_summe)


#Nach Datum sortieren
df["posting_date"] = pd.to_datetime(df["posting_date"], format='%Y-%m-%d')
Wochenendtransaktion = df[df["posting_date"].dt.day_of_week >= 5]
if Wochenendtransaktion.empty:
    print("\n-Keine Transaktion am Wochenende")
else:
    print("\n-Transaktion am Wochenende")
    print(Wochenendtransaktion)



#Benfords Law und Vergleichswerte für Benford's Law
import pandas as pd
erste_ziffern = df["amount"].astype(str).str[0]
benford_verteilung = (
    erste_ziffern.value_counts(normalize=True).sort_index() * 100
).reindex([str(i) for i in range(1, 10)], fill_value=0.0).round(2)
benford_soll = pd.Series({
    '1': 30.1,
    '2': 17.6,
    '3': 12.5,
    '4': 9.7,
    '5': 7.9,
    '6': 6.7,
    '7': 5.8,
    '8': 5.1,
    '9': 4.6
})
vergleichs_tabelle = pd.DataFrame({
    "Ist-Wert": benford_verteilung,
    "Soll-Wert": benford_soll
})

print("\nBENFORD'S LAW VERGLEICH")
print(vergleichs_tabelle)