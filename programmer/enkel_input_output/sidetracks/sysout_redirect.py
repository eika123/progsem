import sys

print('Skriver en melding til out.log')
saveout = sys.stdout
fsock = open('out.log', 'w')
sys.stdout = fsock

print('Denne meldingen blir logget med funksjonen print() i stedet for å bli skrevet til kommandolinjen')
sys.stdout = saveout
fsock.close()
print('Ferdig. Sjekk out.log')
