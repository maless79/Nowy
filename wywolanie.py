import os

file = open("C:/L20171109.log") # Otwieram plik
tekst=file.read() # wczytuje plik do zmiennej
file.close() # zamykam połączenie z plikiem - od teraz operuję tylko  na zmiennej
print("Wczytany plik zawiera %d znaków." % len(tekst))
numerator,line_amount, occurings=1,0,0 # deklaruję zmienne do liczenia linii, wystąpień i lini z wystąpieniami
print("Wprowadź szukane słowo:")
input= str(input()) # pobieram od operatora słowo z konsoli
print("Wprowadziłeś słowo: %s" %input) # potwierdszam co wpisał operator
for line in (tekst.split("\n")): # dziele plik na linie, względem końca linii, w zależności od edytora proste dzielenie na linie tego co widze moze być niepoprawne
    occurings=occurings+line.count(input) # zliczam pojawiaenia sie szukanego wyrazu w linii
    if occurings>0: # jeżelie choć raz się wyraz pojawi
        line_amount+=1 # zliczam taką linię
    numerator+=1 # podnosze nr lini, niezaleznie od znalezionych wyrazow
print("Słowo %s pojawiło się w tekście %d razy w %d liniach."  % (input, occurings, line_amount))