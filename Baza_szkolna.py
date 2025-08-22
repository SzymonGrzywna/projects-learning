# Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
#
# Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
#
# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# Polecenie "koniec" - Kończy działanie aplikacji.
#
# Proces tworzenia użytkowników:
#
# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
# Polecenie "koniec" - Wraca do pierwszego menu.
#
# Proces zarządzania użytkownikami:
#
# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
# Polecenie "koniec" - Wraca do pierwszego menu.


# ---==== BAZA DANYCH ==== ---

uczniowie = []      #[
#     Uczen("3f","Szymon","Grzywna"),
#     Uczen("5a","Marcin","Wronek")
# ]
#
nauczyciele = []    #[
#     Nauczyciel(["3f","2a"],"Szymon","Borowiec"),
#     Nauczyciel(["5a","3b"],"Marek","Kanarek"),
# ]
wychowawcy = []    #[
#     Wychowawca("2b", "Dawid", "Palek"),
#     Wychowawca("3c","Monika","Bania")
# ]
# ====== POMOCNICZE ======
def wczytaj_tekst(pytanie):
    return input(pytanie).strip()

def znajdz_ucznia_po_imieniu(imie_nazwisko):
    for u in uczniowie:
        if u["imie_nazwisko"].lower() == imie_nazwisko.lower():
            return u
    return None

def znajdz_nauczyciela_po_imieniu(imie_nazwisko):
    for n in nauczyciele:
        if n["imie_nazwisko"].lower() == imie_nazwisko.lower():
            return n
    return None

def znajdz_wychowawce_po_imieniu(imie_nazwisko):
    for w in wychowawcy:
        if w["imie_nazwisko"].lower() == imie_nazwisko.lower():
            return w
    return None

def znajdz_wychowawce_klasy(nazwa_klasy):
    for w in wychowawcy:
        if w["klasa"].lower() == nazwa_klasy.lower():
            return w
    return None

def uczniowie_klasy(nazwa_klasy):
    wynik = []
    for u in uczniowie:
        if u["klasa"].lower() == nazwa_klasy.lower():
            wynik.append(u)
    return wynik

def nauczyciele_klasy(nazwa_klasy):
    wynik = []
    for n in nauczyciele:
        for k in n["klasy"]:
            if k.lower() == nazwa_klasy.lower():
                wynik.append((n["przedmiot"], n["imie_nazwisko"]))
                break
    return wynik


# ====== TWORZENIE UZYTKOWNIKOW ======
def menu_tworzenia():
    while True:
        print("\nTworzenie uzytkownikow: wpisz jedna z opcji:")
        print("uczen | nauczyciel | wychowawca | koniec")
        wybor = wczytaj_tekst("> ")

        if wybor.lower() == "koniec":
            return

        elif wybor.lower() == "uczen":
            imie_nazwisko = wczytaj_tekst("Podaj imie i nazwisko ucznia: ")
            klasa = wczytaj_tekst('Podaj nazwe klasy (np. "3C"): ')
            if not imie_nazwisko or not klasa:
                print("Blad: imie/nazwisko i klasa sa wymagane.")
                continue
            uczniowie.append({"imie_nazwisko": imie_nazwisko, "klasa": klasa})
            print(f"Dodano ucznia: {imie_nazwisko} do klasy {klasa}.")

        elif wybor.lower() == "nauczyciel":
            imie_nazwisko = wczytaj_tekst("Podaj imie i nazwisko nauczyciela: ")
            przedmiot = wczytaj_tekst("Podaj nazwe przedmiotu: ")
            print("Podawaj kolejne klasy, ktore prowadzi nauczyciel (po jednej w linii).")
            print("Aby zakonczyc, wcisnij Enter na pustej linii.")
            klasy = []
            while True:
                linia = input().strip()
                if linia == "":
                    break
                klasy.append(linia)
            if not imie_nazwisko or not przedmiot:
                print("Blad: imie/nazwisko i przedmiot sa wymagane.")
                continue
            nauczyciele.append({
                "imie_nazwisko": imie_nazwisko,
                "przedmiot": przedmiot,
                "klasy": klasy
            })
            print(f"Dodano nauczyciela: {imie_nazwisko}, przedmiot: {przedmiot}, klasy: {', '.join(klasy) if klasy else '(brak)'}.")

        elif wybor.lower() == "wychowawca":
            imie_nazwisko = wczytaj_tekst("Podaj imie i nazwisko wychowawcy: ")
            klasa = wczytaj_tekst('Podaj nazwe prowadzonej klasy (np. "3C"): ')
            if not imie_nazwisko or not klasa:
                print("Blad: imie/nazwisko i klasa sa wymagane.")
                continue

            istniejacy = znajdz_wychowawce_klasy(klasa)
            if istniejacy:
                istniejacy["imie_nazwisko"] = imie_nazwisko
                print(f"Zmieniono wychowawce klasy {klasa} na: {imie_nazwisko}.")
            else:
                wychowawcy.append({"imie_nazwisko": imie_nazwisko, "klasa": klasa})
                print(f"Dodano wychowawce: {imie_nazwisko} dla klasy {klasa}.")
        else:
            print("Nieznana opcja. Sprobuj ponownie.")


# ====== ZARZADZANIE ======
def menu_zarzadzania():
    while True:
        print("\nZarzadzanie: wpisz jedna z opcji:")
        print("klasa | uczen | nauczyciel | wychowawca | koniec")
        wybor = wczytaj_tekst("> ")

        if wybor.lower() == "koniec":
            return

        elif wybor.lower() == "klasa":
            klasa = wczytaj_tekst('Podaj nazwe klasy (np. "3C"): ')
            lista_uczniow = uczniowie_klasy(klasa)
            wych = znajdz_wychowawce_klasy(klasa)

            print(f"\nKlasa {klasa}:")
            if lista_uczniow:
                print("Uczniowie:")
                for u in lista_uczniow:
                    print("-", u["imie_nazwisko"])
            else:
                print("Brak uczniow w tej klasie.")

            if wych:
                print("Wychowawca:", wych["imie_nazwisko"])
            else:
                print("Brak przypisanego wychowawcy.")

        elif wybor.lower() == "uczen":
            imie_nazwisko = wczytaj_tekst("Podaj imie i nazwisko ucznia: ")
            uczen = znajdz_ucznia_po_imieniu(imie_nazwisko)
            if not uczen:
                print("Nie znaleziono takiego ucznia.")
                continue

            klasa_ucznia = uczen["klasa"]
            lekcje = nauczyciele_klasy(klasa_ucznia)

            print(f"\nUczen: {uczen['imie_nazwisko']} (klasa {klasa_ucznia})")
            if lekcje:
                print("Lekcje i nauczyciele:")
                for przedmiot, nauczyciel in lekcje:
                    print(f"- {przedmiot}: {nauczyciel}")
            else:
                print("Brak przypisanych lekcji dla tej klasy.")

        elif wybor.lower() == "nauczyciel":
            imie_nazwisko = wczytaj_tekst("Podaj imie i nazwisko nauczyciela: ")
            n = znajdz_nauczyciela_po_imieniu(imie_nazwisko)
            if not n:
                print("Nie znaleziono takiego nauczyciela.")
                continue

            print(f"\nNauczyciel: {n['imie_nazwisko']}, przedmiot: {n['przedmiot']}")
            if n["klasy"]:
                print("Prowadzone klasy:")
                for k in n["klasy"]:
                    print("-", k)
            else:
                print("Brak przypisanych klas.")

        elif wybor.lower() == "wychowawca":
            imie_nazwisko = wczytaj_tekst("Podaj imie i nazwisko wychowawcy: ")
            w = znajdz_wychowawce_po_imieniu(imie_nazwisko)
            if not w:
                print("Nie znaleziono takiego wychowawcy.")
                continue

            klasa = w["klasa"]
            lista_uczniow = uczniowie_klasy(klasa)

            print(f"\nWychowawca: {w['imie_nazwisko']} (klasa {klasa})")
            if lista_uczniow:
                print("Uczniowie:")
                for u in lista_uczniow:
                    print("-", u["imie_nazwisko"])
            else:
                print("Brak uczniow w tej klasie.")
        else:
            print("Nieznana opcja. Sprobuj ponownie.")


# ====== START PROGRAMU ======
print("Witaj w systemie bazy szkolnej.")
while True:
    print("\nGlowne menu: wpisz jedna z komend:")
    print("utworz | zarzadzaj | koniec")
    komenda = input("> ").strip()

    if komenda.lower() == "koniec":
        print("Koniec programu. Do zobaczenia!")
        break
    elif komenda.lower() == "utworz":
        menu_tworzenia()
    elif komenda.lower() == "zarzadzaj":
        menu_zarzadzania()
    else:
        print("Nieznana komenda. Sprobuj ponownie.")