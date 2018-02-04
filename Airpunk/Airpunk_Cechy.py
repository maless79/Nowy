def cechy_postaci(rasa=0):
    import random
    import Walidatory
    import Logi
    wynik ={}  #definiuje  wynik  ktory zwraca funkcja cechy_postaci  jako  slownik
    wynik["Suma PH"]=0  #  w pierwszej pozycji  słownika wstawiam  nazwe Suma_PH o wartosci 0
    losowo=int(input("Czy cechy sam podasz(0), czy wylosujesz(1)?:  ")) # czy  postać będzie losowana czy recznie  robiona.
    print  ("\n"*20)
    if losowo==0: #poniżej jest generowanie postaci reczne
        rcpkzmas = {
            "refleks": 0,
            "ciało": 0,
            "psychika": 0,
            "koordynacja": 0,
            "zmysły": 0,
            "mechanika": 0,
            "akcja": 0,
            "sterowanie": 0,
        }
        for cecha, wartosc in rcpkzmas.items():
            wartosc = Walidatory.walidacja([rasa,0,1,int(input("Wprowadz wartosc %s: " % cecha))])
            Logi.logowanie_zdarzen(wartosc)
            while wartosc==None:
                if  rasa==0 and cecha=="mechanika":
                    wartosc = Walidatory.walidacja([rasa, 1, 0, int(input("Zweryfikuj wprowadzona wartosc %s: " % cecha))])
                elif  rasa==1 and cecha=="refleks":
                    wartosc = Walidatory.walidacja([rasa, 1, 0, int(input("Zweryfikuj wprowadzona wartosc %s: " % cecha))])
                elif  rasa==2 and cecha=="ciało":
                    wartosc = Walidatory.walidacja([rasa, 1, 0, int(input("Zweryfikuj wprowadzona wartosc %s: " % cecha))])
                else:
                    wartosc = Walidatory.walidacja([rasa, 0, 1, int(input("Wprowadz wartosc %s: " % cecha))])
            rcpkzmas[cecha]=wartosc
#  DOPISAC ZABEZPIECZENIE PRZED BLEDEM  WALIDACJI

        wynik = {  #  przygotowuje to co zwraca  funkcja cechy_postaci
            "Suma PH":sum(rcpkzmas.values())  # pierwsza  pozycja  slownika wynik jest suma
        }
        wynik.update(rcpkzmas)# do słownika wynik  z 1 pozycją suma_ph dodaje slownik rcpkzmas
        print ("\n"*5)
        print(wynik)
        Logi.logowanie_zdarzen(wynik)
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
        Logi.logowanie_zdarzen(wynik)
        print (wynik)
    return wynik



