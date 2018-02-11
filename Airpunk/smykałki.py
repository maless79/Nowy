import Logi

def smykalki_lista():

    smykalki  = {
        "1":["As  przestworzy", "BONUS", "OPIS"],
        "2":["Geniusz", "BONUS", "OPIS"],
        "3": ["Kasiarz", "BONUS", "OPIS"],
        "4": ["Kontakty", "BONUS", "OPIS"],
        "5": ["Macgyveryzm", "BONUS", "OPIS"],
        "6":["Medyk", "BONUS", "OPIS"],
        "7":["Nerwy  z neotynium", "BONUS", "OPIS"],
        "8":["Paker", "BONUS", "OPIS"],
        "9":["Rewolwerowiec", "BONUS", "OPIS"],
        "10":["Strzelec wyborowy", "BONUS", "OPIS"],
        "11":["Sokole  oko", "BONUS", "OPIS"],
        "12":["Swobodne spadanie", "BONUS", "OPIS"],
        "13":["Sztuki walki", "BONUS", "OPIS"],
        "14":["Zmysł walki", "BONUS", "OPIS"],
        }
    Logi.logowanie_zdarzen(smykalki)
    for nr_smykalki in smykalki:   # genruje ladnie  wyglądającą listę smykałek do obejrzenia na ekranie
        print ("Smykałka  nr  %s: %s" %(nr_smykalki, smykalki[str(nr_smykalki)]) + "\n")
    nr_smykalki=int(input("Wybieram smykałkę  nr: "))  # każe userowi wybrać właściwą smykałkę dla  niego
    print (" \n"+"Wybrałeś smykałkę nr: %i - %s" %(nr_smykalki, smykalki[str(nr_smykalki)]) + "\n") #pokazuje co wybral
    smykalki=smykalki[str(nr_smykalki)]  #  przekazuje na return wybrana smykalke
    Logi.logowanie_zdarzen(smykalki)
    return smykalki