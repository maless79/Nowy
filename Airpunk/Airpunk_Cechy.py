def cechy_postaci(rasa=0):
    import random
    import Walidatory
    wynik ={}
    wynik["Suma PH"]=0
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
            rcpkzmas["mechanika"] =Walidatory.walidacja([rasa, 1, random.randint(1, 12)])
        elif rasa==1:
            rcpkzmas["refleks"] = Walidatory.walidacja([rasa,1, random.randint(1, 12)])
        elif rasa==2:
            rcpkzmas["ciało"] = Walidatory.walidacja([rasa,1, random.randint(1, 12)])
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
        i = int(wynik["Suma PH"])
    return wynik



