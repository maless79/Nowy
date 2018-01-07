wynik={}
rcpkzmas= {
    "refleks":0,
    "ciało":0,
    "psychika":0,
    "koordynacja":0,
    "zmysły":0,
    "mechanika":0,
    "akcja":0,
    "sterowanie":0,
}


for cecha,wartosc in rcpkzmas.items():
    wartosc=input("Wprowadz wartosc %s: " %cecha)

wynik.update(rcpkzmas)
print  (wynik)



def cechy_postaci(rasa=0):
    import random
    import Walidatory
    import Logi
    wynik ={}  #definiuje  wynik  ktory zwraca funkcja cechy_postaci  jako  slownik
    wynik["Suma PH"]=0  #  w pierwszej pozycji  słownika wstawiam  nazwe Suma_PH o wartosci 0
    losowo=int(input("Czy cechy sam podasz(0), czy wylosujesz(1)?:  ")) # czy  postać będzie losowana czy recznie  robiona.
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
                      wartosc = int(input("Wprowadz wartosc %s: " % cecha))

        if rasa==1:
            refleks = Walidatory.walidacja([1, 0, 1, int(input("Wprowadz wartość refleks (jako aves możesz mieć go nawet 12): "))])
            while refleks >12:
                Logi.logowanie_zdarzen("Wybrałeś liczbę spoza dozwolonego zakresu!")
                refleks=Walidatory.walidacja([1, 0, 1, int(input("Wprowadz wartość refleks (jako aves możesz mieć go nawet 12): "))])
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

        wynik = {  #  przygotowuje to co zwraca  funkcja cechy_postaci
            "Suma PH":sum(rcpkzmas.values())  # pierwsza  pozycja  slownika wynik jest suma
        }
        wynik.update(rcpkzmas)# do słownika wynik  z 1 pozycją suma_ph dodaje slownik rcpkzmas