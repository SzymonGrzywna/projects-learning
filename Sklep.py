# # # Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.
# # #
# # # Program po uruchomieniu wyświetla informację o dostępnych komendach:
# # #
# # # saldo
# # # sprzedaż
# # # zakup
# # # konto
# # # lista
# # # magazyn
# # # przegląd
# # # koniec
# # #
# # # Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:
# # #
# # saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
# # sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
# # zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
# # konto - Program wyświetla stan konta.
# # lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
# # magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
# # przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
# # # koniec - Aplikacja kończy działanie.
# # #
# # # Dodatkowe wymagania:
# # # #
# # # Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
# # # Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
# # # Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
# # # Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.


# ----------------------------------------------------------------------
stan_konta = 0.0
historia = []
magazyn = [{
    "nazwa_produktu": "JAJKA",  "cena_produktu": 1.29, "ilosc_dostepna": 100
},
    {
    "nazwa_produktu": "MLEKO",  "cena_produktu": 3.69, "ilosc_dostepna": 50
},
    {
    "nazwa_produktu": "SZYNKA", "cena_produktu": 4.99, "ilosc_dostepna": 5
},
    {
    "nazwa_produktu": "KURS_PIERWSZA_PRACA_STYCZEN_2026", "cena_produktu": 777, "ilosc_dostepna": 1
    }]

while True:
    print()
    print(30 * "V")
    print("Lista dostepnych komend: ")
    print(30 * "V")
    print("-= SALDO =-")
    print("-= SPRZEDAZ =-")
    print("-= ZAKUP =-")
    print("-= KONTO =-")
    print("-= LISTA =-")
    print("-= MAGAZYN =-")
    print("-= PRZEGLAD =-")
    print("-= KONIEC =-")
    print()

    komenda = input("Wprowadz komende:").upper()
    print(f"Wprowadziles komende :{komenda}")

    # ------------------- KONIEC ----------------
    if komenda == "KONIEC":
        print("\n======== KONCZYMY DZIALANIE PROGRAMU =======")
        break

    # ---------------- SALDO ---------------------
    elif komenda == "SALDO":
        print("\nCo chcesz zrobić ze stanem konta?")
        print("1 – DODAJ (+)")
        print("2 – ODEJMIJ (-)")

        wybor = input("Wybierz 1 lub 2: ")
        if wybor == "1":
            kwota = float(input("Ile chcesz DODAĆ? "))
            stan_konta += kwota
            historia.append(("saldo", kwota))
            print("Dodano (+):", kwota, "zł")

        elif wybor == "2":
            kwota = float(input("Ile chcesz ODJĄĆ? "))
            stan_konta -= kwota
            historia.append(("saldo", -kwota))
            print(f"Odjęto (-): {kwota} zł")
        else:
            print("Niepoprawny wybór – wracam do menu.")

        print("Aktualny stan konta:", stan_konta, "zł")

    # --------------- SPRZEDAZ -------------------
    elif komenda == "SPRZEDAZ":
        wybrany_produkt = input("\n Jaki produkt chcesz wybrać? ").upper()
        ilosc_produktu = int(input("Ile szt? "))
        znaleziono_produkt = False
        for produkt in magazyn:
            if produkt["nazwa_produktu"] == wybrany_produkt:
                if ilosc_produktu > produkt["ilosc_dostepna"]:
                    print("Brak wystarczającej ilości produktu")
                    break
                produkt["ilosc_dostepna"] -= ilosc_produktu
                stan_konta += produkt["cena_produktu"] * ilosc_produktu
                historia.append(("sprzedaz", wybrany_produkt, produkt["cena_produktu"], ilosc_produktu))
                znaleziono_produkt = True
                break
        if not znaleziono_produkt:
            print("Brak produktu w magazynie")

    # ----------------- ---- ZAKUP ----------------
    elif komenda == "ZAKUP":
        wybrany_produkt = input("\nJaki produkt chcesz kupić? ").upper()
        cena = float(input("Podaj cenę za sztukę: "))
        ilosc = int(input("Ile sztuk kupujesz? "))
        koszt = cena * ilosc

        if koszt > stan_konta:
            print("Nie masz tyle środków na koncie")
            continue
        if cena <= 0 or ilosc <= 0:
            print("Cena i ilość muszą być dodatnie")
            continue

        znaleziono = False
        for produkt in magazyn:
            if produkt["nazwa_produktu"] == wybrany_produkt:
                produkt["ilosc_dostepna"] += ilosc
                produkt["cena_produktu"] = cena
                znaleziono = True
                break
        if not znaleziono:
            magazyn.append({
                "nazwa_produktu": wybrany_produkt,
                "cena_produktu": cena,
                "ilosc_dostepna": ilosc
            })

        stan_konta -= koszt
        historia.append(("zakup", wybrany_produkt, cena, ilosc))
        print(f"Zakup udany. Stan konta: {stan_konta} zł")

    # --------------------- KONTO -----------------
    elif komenda == "KONTO":
        print(f" \n Stan konta: {stan_konta} zł")

    # ---------------- LISTA -----------------
    elif komenda == "LISTA":
        print(magazyn)

    # --------------- MAGAZYN --------------------------
    elif komenda == "MAGAZYN":
        wybrany_produkt = input("\n Jaki wybierasz produkt? :").upper()
        znaleziono_produkt = False
        for produkt in magazyn:
            if produkt["nazwa_produktu"] == wybrany_produkt:
                print(produkt)
                znaleziono_produkt = True
                break
        if not znaleziono_produkt:
            print("Brak produktu w magazynie")

    # -------------------- PRZEGLAD -----------------------
    elif komenda == "PRZEGLAD":
        od = input("\n Podaj zakres (od) (ENTER = początek): ")
        do = input("Podaj zakres (do) (ENTER = koniec): ")

        od_i = int(od) if od else 0
        do_i = int(do) if do else len(historia) - 1

        if od_i < 0 or do_i >= len(historia) or od_i > do_i:
            print(f"Zakres poza listą! Masz {len(historia)} zapisanych komend.")
            continue

        print("\n--- HISTORIA ---")
        for historia_f in range(od_i, do_i + 1):
            print(historia_f, historia[historia_f])
        print("---------------------")

