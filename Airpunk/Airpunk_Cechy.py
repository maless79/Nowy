def cechy_postaci(rasa=0):
    import random
    import Walidatory

    rcpkzmas = {
        "refleks":random.randint(1, 10),
        "cialo":random.randint(1, 10),
        "psychika":random.randint(1, 10),
        "koordynacja":random.randint(1, 10),
        "zmysly":random.randint(1, 10),
        "mechanika":random.randint(1, 10),
        "akcja":random.randint(1, 10),
        "sterowanie":random.randint(1, 10),
    }

    if rasa==0:
        rcpkzmas["mechanika"] =Walidatory.walidacja([rasa, 1, random.randint(1, 12)])
    elif rasa==1:
        rcpkzmas["refleks"] = Walidatory.walidacja([rasa,1, random.randint(1, 12)])
    elif rasa==2:
        rcpkzmas["cialo"] = Walidatory.walidacja([rasa,1, random.randint(1, 12)])
    else:
        rcpkzmas={
            "refleks":0,
            "cialo":0,
            "psychika":0,
            "koordynacja":0,
            "zmysly":0,
            "mechanika":0,
            "akcja":0,
            "sterowanie":0,
        }
    return rcpkzmas



