def converToHumanYears (x):
    dogYears = x
    if dogYears > 2:
        dogYear = 22 + (dogYears - 2) * 5
        return dogYear
    elif dogYears == 1:
        dogYear = 14
        return dogYear
    elif dogYears == 2:
        dogYear = 22
        return dogYear
    else:
        print ('Input is not valid')


dogYears = int(input('Geef de leeftijd van uw hond op: '))

print ('Deze leeftijd komt overeen met {0} mensen jaren'.format(converToHumanYears(dogYears)))


