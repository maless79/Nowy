def cechy_postaci(rcpkzmas, kontrola=0):
    import random
    if kontrola==0:
        rcpkzmas={
            "refleks":random.randint(1,10),
            "cialo":random.randint(1,10),
            "psychika":random.randint(1,10),
            "koordynacja":random.randint(1,10),
            "zmysly":random.randint(1,10),
            "akcja":random.randint(1,10),
            "sterowanie":random.randint(1,10),
        }
    else:
        rcpkzmas={
            "refleks":1,
            "cialo":1,
            "psychika": 1,
            "koordynacja":1,
            "zmysly":1,
            "akcja":1,
            "sterowanie":1,
        }
    return rcpkzmas



