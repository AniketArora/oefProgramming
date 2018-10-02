def printWelkom (naam, groep = "1NMCT"):
    print ('Welkom {0} van groep {1}'.format(naam, groep))
    return


naam = input('Geef uw naam op: ')

printWelkom(naam)

naam = "Frank"
groep = '1NMCT2'

printWelkom(naam, groep)