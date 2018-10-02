import math

def geslaagd (score):
    score = int(round(score))
    if score >= 10:
        print('U bent geslaagd.')
    else:
        print ('Helaas, volgende keer beter.')


score = float(input('Geef uw score op.'))

geslaagd(score)