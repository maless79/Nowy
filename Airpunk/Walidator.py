import re

def walidacja (do_walidacji=3, rasa=1):

    sprawdzanie=re.match("[5-9]{1}",str(do_walidacji))

    #([1-3]{1}, do_walidacji)
    if sprawdzanie is not None:
        do_walidacji
    else:
        do_walidacji=None
    return do_walidacji


z=walidacja()
print (z)