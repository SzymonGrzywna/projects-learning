
print("_-" * 30)
print("-=PROGRAM DO WYSYLANIA=-")
print("MAX WAGA ELEMENTU 10KG , 1 PACZKA MAX 20KG")
print("_-" * 30)
liczba_elementów = int(input("\nPodaj liczbę elementów do wysłania:"))





if liczba_elementów <= 0:
    print("Brak elementów do wysłania.")
else:
    masa_bieżącej_paczki = 0
    liczba_paczek = 0
    łączna_masa = 0
    wysłane_elementy = 0
    najgorszy_luz = -1
    numer_najgorszej_paczki = 0

    for i in range(1, liczba_elementów + 1):
        masa_elementu = int(input(f"Podaj masę elementu #{i} (1‑10 kg):"))


        if masa_elementu < 1 or masa_elementu > 10:
            print("Niepoprawna masa – kończę pakowanie.")
            break


        if masa_bieżącej_paczki + masa_elementu > 20:
            liczba_paczek += 1
            luz_paczki = 20 - masa_bieżącej_paczki
            if luz_paczki > najgorszy_luz:
                najgorszy_luz = luz_paczki
                numer_najgorszej_paczki = liczba_paczek
            masa_bieżącej_paczki = 0


        masa_bieżącej_paczki += masa_elementu
        łączna_masa += masa_elementu
        wysłane_elementy += 1


    if masa_bieżącej_paczki > 0:
        liczba_paczek += 1
        luz_paczki = 20 - masa_bieżącej_paczki
        if luz_paczki > najgorszy_luz:
            najgorszy_luz = luz_paczki
            numer_najgorszej_paczki = liczba_paczek

    suma_pustych = liczba_paczek * 20 - łączna_masa


    print("\n--- PODSUMOWANIE ---")
    print(f"Wysłane paczki: {liczba_paczek}")
    print(f"Wysłane elementy:{wysłane_elementy} z {liczba_elementów}")
    print(f"Łączna wysłana masa: {łączna_masa} kg")
    print(f"Suma „pustych” kilogramów:{suma_pustych}")
    print(f"Największy luz miała paczka #{numer_najgorszej_paczki} "
          f"({najgorszy_luz} kg wolnego).")