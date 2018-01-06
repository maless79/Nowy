def walidacja(rasa_cecha12_wartosc=[0,0,0,0]):
# parametrami jest lista: 0 - rasa 0,1,2 1- czy sprawdzamy cechę12 2 - czy  sprawdzamy  ceche10 3 -wartość cechy po zwrocie
    import re

    sprawdzanie=re.match("[0-2]{1}",str(rasa_cecha12_wartosc[0])) # sprawdzenie czy rasa jest wybrana poprawnie 0,1,2

    if sprawdzanie is not None:
        zwrot=rasa_cecha12_wartosc[0]  # jeżeli rasa jest ok to zwracamy nr rasy
    else:
        zwrot=None

    if rasa_cecha12_wartosc[1]==1 and zwrot is not None: # jeżeli rasa była okay to można sprawdzać dalej cechę12
        if (rasa_cecha12_wartosc[3]) >=1 and (rasa_cecha12_wartosc[3])<=12:
            zwrot=rasa_cecha12_wartosc[3] # jeżeli cecha się mieści to zwracamy jej wartość
        else:
            zwrot=None #jeżeli cecha się nie mieści to zwracamy None

    if rasa_cecha12_wartosc[2]==1 and zwrot is not None: # jeżeli rasa była okay to można sprawdzać dalej cechę10
        if (rasa_cecha12_wartosc[2]) >=1 and (rasa_cecha12_wartosc[2])<=10:
            zwrot=rasa_cecha12_wartosc[3] # jeżeli cecha się mieści to zwracamy jej wartość
        else:
            zwrot=None #jeżeli cecha się nie mieści to zwracamy None

    return zwrot
