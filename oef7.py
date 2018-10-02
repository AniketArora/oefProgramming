def toLowerCase(string):
    string = string.lower()
    return string


def equal(string1, string2):
    string1 = toLowerCase(string1)
    string2 = toLowerCase(string2)

    if string1 == string2:
        print ('The strings are equal.')
        return
    else:
        print ('The strings are not equal.')


string1 = 'hallo'
string2 = 'Hallo'

equal(string1, string2)

string3 = 'poop'
string4 = 'morepoop'

equal(string3, string4)