def gelijkAan(x,y):
    if x==y:
        print('{0} is gelijk aan {1}'.format(x,y))
        return
    else:
        print ('{0} is niet gelijk aan {1}'.format(x,y))

int1 = int(input('Geef het eerste nummer op: '))
int2 = int (input('Geef het tweede nummer op: '))

gelijkAan(int1, int2)