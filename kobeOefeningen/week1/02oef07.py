#oef7
dagen = int(input("Aantal dagen: "))
uren = int(input("Aantal uren: "))
minuten = int(input("Aantal minuten: "))
seconden = int(input("Aantal seconden: "))
totaalSeconden = minuten * 60 + seconden + uren *60*60 + dagen * 24*60*60
print("Het totaal aantal seconden is" + totaalSeconden)