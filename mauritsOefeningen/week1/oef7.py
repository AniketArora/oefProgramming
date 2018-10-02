#functie zet het aantal dagen, uren en minuten om naar seconden en telt ze bij elkaar op
def naarSeconden (dag, uur, minuten):
    totaal = dag*86400 + uur*3600 + minuten*60
    return totaal


dagen = int(input('Geef het aantal dagen op: '))
uren = int(input('Geef het aantal uren op: '))
minuten = int(input("Geef het aantal minuten op: "))
seconden = int(input("Geef het aantal seconden op: "))

totaal = naarSeconden(dagen,uren,minuten) + seconden

print("Het totale aantal seconden bedraagt: " + str(totaal))