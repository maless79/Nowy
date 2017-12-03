def cechy_postaci(rcpkzmas):
    import random

    rcpkzmas={
        "refleks":random.randint(1,10),
        "cialo":random.randint(1,10),
        "psychika":random.randint(1,10),
        "koordynacja":random.randint(1,10),
        "zmysly":random.randint(1,10),
        "akcja":random.randint(1,10),
        "sterowanie":random.randint(1,10),
    }
    return rcpkzmas

rcpkzmas={}
print(cechy_postaci(rcpkzmas))

