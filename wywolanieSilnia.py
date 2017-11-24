from nowy import silnia
import wypelnianieListy
import random
import Postacie
import rekurencja
i=0
while i<10:
    #z = random.randint(1, 10)
    z = random.randint(5, 25)
    if z%2!=0:
        print(z)
        break
    i+=1

#a=rekurencja.rekurencja_def(5)

wielkosc_listy2 = input("wprowadz wielkosc silni: ")
wydruk=silnia(int(wielkosc_listy2))
wielkosc_listy = input("wprowadz wielkosc listy: ")
wydruk2 = wypelnianieListy.wypelnij_liste(int(wielkosc_listy))
print(wydruk)
print(wydruk2)

z = Postacie.Postacie()
print (str(z))
