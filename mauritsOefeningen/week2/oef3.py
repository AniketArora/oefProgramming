import datetime

def olderThanEighteen (userYear, userMonth, userDay):

    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day

    if year == userYear + 18:
        if userMonth == month:
            if userDay <= day:
                print ('Ok, u mag alcohol drinken.')
                return
            else:
                print ('U mag nog niet drinken. \nKom later nog eens terug')
        elif userMonth < month:
            print ('Ok, u mag alcohol drinken.')
            return
        else:
            print ('U mag nog niet drinken. \nKom later nog eens terug')
    elif year < userYear + 18:
        print ('Ok, u mag alcohol drinken.')
        return
    else:
        print ('U mag nog niet drinken. \nKom later nog eens terug')


birthyear = int(input('Geef uw geboorte jaar op: '))
birthmonth = int(input('Geef uw geboortemaand op als integer: '))
birthday = int(input('Geef uw geboortedag op: '))

olderThanEighteen(birthyear, birthmonth, birthday)