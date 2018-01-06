def cechy_postaci(rasa=0):
    import random
    import Walidatory
    wynik ={}  #definiuje  wynik  ktory zwraca funkcja cechy_postaci  jako  slownik
    wynik["Suma PH"]=0  #  w pierwszej pozycji  słownika wstawiam  nazwe Suma_PH o wartosci 0
    losowo=int(input("Czy cechy sam podasz(0), czy wylosujesz(1)?:  ")) # czy  postać będzie losowana czy recznie  robiona.
    if losowo==0: #poniżej jest generowanie postaci reczne
        if rasa==1:
            refleks = Walidatory.walidacja([1, 0, 1, int(input("Wprowadz wartość refleks (jako aves możesz mieć go nawet 12): "))])
            while refleks >12:
                refleks=int(input("Wprowadz wartość refleks (jako aves możesz mieć go nawet 12): "))
        else:
            refleks=Walidatory.walidacja([1,0,1,int(input("Wprowadz wartość refleks: "))])
        if rasa==2:
            cialo=int(input("Wprowadz wartość ciało (jako amfibia  możesz je mieć nawet 12): "))
        else:
            cialo = int(input("Wprowadz wartość ciało: "))
        psychika=int(input("Wprowadz wartość psychika: "))
        koordynacja=int(input("Wprowadz wartość koordynacja: "))
        zmysly=int(input("Wprowadz wartość zmysły: "))
        if rasa==0:
            mechanika=int(input("Wprowadz wartość mechanika (jako mammes możesz mieć jej nawet 12): "))
        else:
            mechanika = int(input("Wprowadz wartość mechanika: "))
        akcja=int(input("Wprowadz wartość akcja: "))
        sterowanie=int(input("Wprowadz wartość sterowanie: "))

        rcpkzmas= {
        "refleks":refleks,
        "ciało":cialo,
        "psychika":psychika,
        "koordynacja":koordynacja,
        "zmysły":zmysly,
        "mechanika":mechanika,
        "akcja":akcja,
        "sterowanie":sterowanie,
        }
        wynik = {  #  przygotowuje to co zwraca  funkcja cechy_postaci
            "Suma PH":sum(rcpkzmas.values())  # pierwsza  pozycja  slownika wynik jest suma
        }
        wynik.update(rcpkzmas)# do słownika wynik  z 1 pozycją suma_ph dodaje slownik rcpkzmas
    else:  #ponizej jest generowanie postaci randomowe
        while int(wynik["Suma PH"])<50:
            rcpkzmas = {
                "refleks":random.randint(1, 10),
                "ciało":random.randint(1, 10),
                "psychika":random.randint(1, 10),
                "koordynacja":random.randint(1, 10),
                "zmysły":random.randint(1, 10),
                "mechanika":random.randint(1, 10),
                "akcja":random.randint(1, 10),
                "sterowanie":random.randint(1, 10),
            }
            if rasa==0:
                rcpkzmas["mechanika"] = Walidatory.walidacja([rasa, 1, 0,random.randint(1, 12)])
            elif rasa==1:
                rcpkzmas["refleks"] = Walidatory.walidacja([rasa,1, 0,random.randint(1, 12)])
            elif rasa==2:
                rcpkzmas["ciało"] = Walidatory.walidacja([rasa,1, 0,random.randint(1, 12)])
            else:
                rcpkzmas={
                    "refleks":0,
                    "ciało":0,
                    "psychika":0,
                    "koordynacja":0,
                    "zmysły":0,
                    "mechanika":0,
                    "akcja":0,
                    "sterowanie":0,
                }

            wynik={
                "Suma PH":sum(rcpkzmas.values())
                }
            wynik.update(rcpkzmas)
    return wynik



