#-*-coding: utf-8-*-
import re

sprawdzacz=0
while(sprawdzacz<=1):
    rasy=["Mammes","Aves","Amfibia"] # lista ras
    rasa_postaci=input("Wybierz rasę postaci:\n 1- %s \n 2- %s\n 3- %s \n Wybieram rasę nr: " %(rasy[0],rasy[1],rasy[2]))
    # input z informacją o tym w jaki sposób wybrać rasy
    if re.match("[1-3]{1}",rasa_postaci) is not None: # regex sprawdzający czy wpisane cyfry to 1,2,3
        try:
            print("Wybrałeś %s" %rasy[int(rasa_postaci)-1])
            sprawdzacz=2 # zamknięcie pętli jeśli poprawnie wybrano rasę
        except IndexError:
            print("Nie wybrałeś liczby z zakresu 1-3.")
    else:
        print("Wpisałeś niedozwolony znak.")


print("EXIT")

