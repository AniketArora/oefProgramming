# Commentarieer je oefeningen
voornaam = "Kobe"
mail = "kobejanssens@outlook.com"
print("Janssens \nKobe \nkobe.janssens@outlook.com")
print("Janssens \tKobe \tkobe.janssens@outlook.com")
print("\n")
print("Achternaam: Janssens")

#gebruik van variabelen
print("Voornaam: " + voornaam)

#concatenatie of placeholders
print("E-mail: {}".format(mail))
print(f"E-mail: {mail}")
print("Voornaam: {0}\t E-mail:  {1}".format(voornaam,mail))

#data opvragen
#postcode = input("Postcode: ")
#print(postcode)

#datatype
print(type(voornaam))
print(type(1))
print(type(1.2))

getal1 = input("Getal1: ")
getal2 = input("Getal2: ")

print(getal1 + getal2)


#oef3
naam = input("Naam: ")
voornaam = input("Voornaam: ")
leeftijd = input("Leeftijd: ")

print("Welkom {0} {1}! Jij bent vandaag {2} jaar".format(naam,voornaam,leeftijd))

#oef4
dec1 = 1
dec2 = 20

print(hex(20))


#oef6
hoogte = float(input("hoogte"))
basis = float(input("basis"))
print(hoogte * basis / 2)