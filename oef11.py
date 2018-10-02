def biggerThan (a, b):
    if a > b:
        return a
    else:
        return b


def biggestOutOfThree(a,b,c):
    biggest = biggerThan(a,biggerThan(b,c))
    print(biggest)
    return

biggestOutOfThree(6,3,4)