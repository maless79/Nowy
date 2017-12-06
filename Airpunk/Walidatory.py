import re

def walidacja (do_walidacji=0, rasa=0):

    sprawdzanie=re.match("[1-3]{1}",str(do_walidacji))

    #([1-3]{1}, do_walidacji)
    if sprawdzanie is not None:
        do_walidacji
    else:
        do_walidacji=None
    return do_walidacji


z=walidacja()
print (z)