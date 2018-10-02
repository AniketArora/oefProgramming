def geefCelsius (temp):
    tempInCelsius = (temp - 32)*5/9
    return tempInCelsius


def geefFahrenheit (temp):
    tempInFahrenheit = (temp*9/5) + 32
    return tempInFahrenheit


unit = input('Welke eenheid gebruikt u? [C:celsius, F:fahrenheit]')

if unit.lower() == 'c':
    temp = int(input('Geef uw temperatuur op in celsius: '))
    print('De overeenkomstige temperatuur in Fahrenheit is: {0}'.format(geefFahrenheit(temp)))

if unit.lower() == 'f':
    temp = int(input('Geef uw temperatuur op in Fahrenheit: '))
    print('De overeenkomstige temperatuur in celsius is: {0}'.format(geefCelsius(temp)))


