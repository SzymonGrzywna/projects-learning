print("Generator kartka urodzinowa ")
imie = input("Podaj Imię Solenizanta ")


nazwisko = input("Podaj Nazwisko ")

rok = input("Podaj Rok Urodzenia ")

data =  2025  - int(rok)

print(f"Twój Znajomy {imie} ma {data}")



tekst = input("Spersonalizowana Wiadomość ")

nadawca = input("Podaj Imię Nadawcy ")


szablon = ("""
 .....::::: {} {} :::::.....

Wszystkiego najlepszego z okazji ..::{}::.. urodzin!

{}

Pozdrawiam!
{}
""")

print(szablon.format(imie, nazwisko, data, tekst, nadawca))