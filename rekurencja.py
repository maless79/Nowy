def rekurencja_def (Parametr1, Parametr2=0):
    iterator=1
    while iterator<Parametr1:
        Parametr1=Parametr1*(Parametr1-1)
        wynik=Parametr1
        iterator+=1
        print (wynik)
        print (iterator, " ", Parametr1)
        input ("dawaj kolejna runde")
    return wynik