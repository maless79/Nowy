import Logi

def smykalki_lista():

    smykalki  = {
        "1":["As  przestworzy", "+3 sterowanie, +3  samoloty", "Postać ma wyjątkową smykałkę do latania samolotami i innymi statkami powietrznymi. Instynktownie wyczuwa odległość, wiatry oraz ich kierunek i siłę, wysokość, na której się znajduje jak i świetnie panuje nad maszyną. Postać z taką smykałką otrzymuje  modyfikator +3 do sterowania oraz +3 do umiejętności samoloty (nawet, jeśli postać nie posiada tej umiejętności). \n"],
        "2":["Geniusz", "+6  mechanika", "Postać jest wybitnie inteligentna. Potrafi z niezwykłą wnikliwością analizować fakty i skutecznie budować związki przyczynowo skutkowe. Zazwyczaj też potrafi szybko i trzeźwo ocenić sytuację, nawet w warunkach dużego napięcia. Postać otrzymuje na stałe modyfikator +6 do testów opartych na Mechanice."],
        "3":["Kasiarz", "+6 otwieranie,  15 automatycznie zdaje", "Od najmłodszych lat postać rozumiała i umiała otwierać wszelkie zamki, stacyjki, blokady. Przy pomocy swojego kompletu różnorodnych wytrychów, uniwersalnych kluczy i kabli jest wstanie otworzyć niemal każdy zamek, uruchomić każdy silnik, oraz bez huku otworzyć każdy sejf. Postać zdaje automatycznie testy na poziomie 15 i niższym otwierania  oraz dostaje modyfikator +6 do testów umiejętności Otwieranie."],
        "4":["Kontakty", "+6 kontakty", "Postać posiada wrodzony talent do poznawania i zjednywania sobie ludzi, co zaowocowało wieloma bardzo intratnymi znajomościami. Postać zawsze ma, do kogo się zgłosić w kłopocie, znajdzie osobę, która chętnie kupi lub sprzeda nietypowy towar, albo zorganizuje potrzebne osoby do wyprawy, czy napadu. Postać posiada modyfikator do  umiejętności kontakty na poziomie +6 (nawet, jeśli postać nie posiada tej umiejętności)."],
        "5":["Macgyveryzm", "Macgyveryzm", "Postać ma wrodzony ponadprzeciętny talent do budowy i naprawy urządzeń mechanicznych. Potrafi w nieszablonowy sposób łączyć elementy i tworzyć maszyny i urządzenia, które nie są jeszcze znane nauce. Za każdym razem, gdy postać usiłuje stworzyć, coś, co MG uznaje za przekraczające wiedzę i znajomość świata, deklaruje użycie  umiejętność MacGyveryzm. Po udanym teście na poziomie zadanym przez MG urządzenie  zostaje zbudowane i działa. Postać często sama nie umie wyjaśnić jak dane urządzenie działa, po prostu intuicyjnie buduje jakąś rzecz. Dla każdej rzeczy, każdego wynalazku zbudowanego  w oparciu o Macgyveryzm postać musi wykonać test osobno, nawet, jeżeli wcześniej już coś takiego konstruowała. Tylko postać posiadająca smykałkę Macgyveryzm może posiadać umiejętność Macgyveryzm."],
        "6":["Medyk", "+6  medycyna", "Postać od dziecka instynktownie umiała opatrywać rany, nastawiać złamanekończyny, a nawet szybko nauczyła się odbierać porody, zwierząt i ludzi. Z łatwością też wyszukiwała zioła, czy nawet odkrywała ich nowe zastosowanie. Wszystkie te doświadczenia spowodowały, iż nawet bez ukończonych studiów lekarskich jest wstanie pomóc rannym i potrzebującym, co często czyni z niej szczególnie cenny nabytek w zespole. Postać otrzymuje modyfikator do umiejętności medycyna na poziomie +6 (nawet, jeśli postać nie posiada tej umiejętności)."],
        "7":["Nerwy  z neotynium", "+6 odpornośc na stres", "Postać urodziła się z jakimś brakiem lub nadmiarem połączeń nerwowych, co objawia się niemal całkowitą niewrażliwością postaci na stres, odpornością na najkoszmarniejsze sceny czy zwykłym brakiem strachu niemal przed czymkolwiek. Postać otrzymuje modyfikator +6 do testów odporności na stres, nawet, jeśli nie posiada tej umiejętności."],
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
    while (int(nr_smykalki)>=14):
        try:
            nr_smykalki=int(input("Wybieram smykałkę  nr: "))  # każe userowi wybrać właściwą smykałkę dla  niego
            Logi.logowanie_zdarzen("Wybrano smykalke nr %s" %nr_smykalki)
            opis_smykalki = smykalki[str(nr_smykalki)]
            print (" \n"+"Wybrałeś smykałkę nr: %i - %s" %(nr_smykalki, opis_smykalki[0]) + "\n") #pokazuje co wybral
        except  (KeyError,  ValueError):
            nr_smykalki=int(nr_smykalki)
            Logi.logowanie_zdarzen(print("Mozesz wybrac liczbe z zakresu od 1 do 14!"))
    smykalki=smykalki[str(nr_smykalki)]  #  przekazuje na return wybrana smykalke
    Logi.logowanie_zdarzen(smykalki)
    return smykalki