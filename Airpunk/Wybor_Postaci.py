#-*-coding: utf-8-*-
import Logi
import Airpunk_Cechy
import Walidatory
sprawdzacz=0
while(sprawdzacz<=1):
    rasy=["Mammes","Aves","Amfibia"] # lista ras
    rasa_postaci=int(input("Wybierz rasę postaci:\n 0- %s \n 1- %s\n 2- %s \n Wybieram rasę nr: " %(rasy[0],rasy[1],rasy[2])))
    # input z informacją o tym w jaki sposób wybrać rasy,ze zdefiniowanej listy "rasy"
    if Walidatory.walidacja([rasa_postaci,0,0]) is not None:  # regex sprawdzający czy wpisane cyfry to 1,2,3
        try:
            Logi.logowanie_zdarzen("\n Wybrałeś: %s! \n" %rasy[int(rasa_postaci)])
            sprawdzacz=2 # zamknięcie pętli jeśli poprawnie wybrano rasę
        except IndexError:
            Logi.logowanie_zdarzen("Nie wybrałeś liczby z zakresu 1-3.")
    else:
        Logi.logowanie_zdarzen("Wpisałeś niedozwolony znak.")
if rasa_postaci==0:
    Logi.logowanie_zdarzen(Airpunk_Cechy.cechy_postaci(0))
elif rasa_postaci==1:
    print(Airpunk_Cechy.cechy_postaci(1))
elif rasa_postaci==2:
    print(Airpunk_Cechy.cechy_postaci(2))
else:
    Logi.logowanie_zdarzen("Nieoczekiwany błąd rasy. Prawdopodobnie źle wybrano rasę postaci.")
Logi.logowanie_zdarzen("\n EXIT")

