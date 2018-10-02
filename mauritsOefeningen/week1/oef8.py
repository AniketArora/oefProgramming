def convertSeconds (y):
    day = y/86400
    remainder = y%86400

    uren = remainder / 3600
    remainder = remainder % 3600

    minuten = remainder / 60
    seconden = remainder % 60

    return '{0}:{1}:{2}:{3}'.format(int(day), int(uren), int(minuten), int(seconden) )

seconden = int(input('Geef het aantal seconden op.'))
print (convertSeconds(seconden))