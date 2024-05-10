from datetime import datetime

# Adatok
adatok = [
    {"nev": "Szendrei Csongor", "szak": "Mérnökinfo", "neptun kód": "CM5RVO"},

]

# Fájlba írás
with open("adatok.txt", "w") as file:
    for adat in adatok:
        file.write(f"Név: {adat['nev']}, Szak: {adat['szak']}, Neptun kód: {adat['neptun']}\n")

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    def listaz(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")

# Szálloda, szobák és foglalások inicializálása
szalloda = Szalloda("Példa Szálloda")
szalloda.uj_szoba(EgyagyasSzoba("101"))
szalloda.uj_szoba(KetagyasSzoba("201"))
szalloda.uj_szoba(EgyagyasSzoba("102"))

foglalasok_kezelo = FoglalasKezelo(szalloda)
foglalasok_kezelo.foglalas("101", datetime(2024, 5, 15))
foglalasok_kezelo.foglalas("201", datetime(2024, 5, 20))
foglalasok_kezelo.foglalas("101", datetime(2024, 5, 25))
foglalasok_kezelo.foglalas("102", datetime(2024, 5, 25))
foglalasok_kezelo.foglalas("201", datetime(2024, 5, 30))

# Felhasználói interfész és adatvalidáció
print("Üdvözöljük a Példa Szálloda foglalási rendszerében!")

while True:
    print("\nVálasszon egy műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Művelet kiválasztása: ")

    if valasztas == "1":
        szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
        datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            if datum < datetime.now():
                print("Hibás dátum! Kérjük adjon meg egy jövőbeli dátumot.")
            else:
                ar = foglalasok_kezelo.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"Sikeres foglalás! Ár: {ar} Ft")
                else:
                    print("Nem sikerült foglalni, ilyen szoba nem létezik.")
        except ValueError:
            print("Hibás dátumformátum!")

    elif valasztas == "2":
        print("Jelenlegi foglalások:")
        foglalasok_kezelo.listaz()
        foglalas_index = input("Adja meg a lemondani kívánt foglalás sorszámát: ")
        try:
            foglalas_index = int(foglalas_index)
            if 0 < foglalas_index <= len(foglalasok_kezelo.foglalasok):
                if foglalasok_kezelo.lemondas(foglalasok_kezelo.foglalasok[foglalas_index - 1]):
                    print("A foglalás sikeresen törölve.")
                else:
                    print("Nem sikerült törölni a foglalást.")
            else:
                print("Hibás sorszám!")
        except ValueError:
            print("Hibás sorszám!")

    elif valasztas == "3":
        print("Foglalások:")
        foglalasok_kezelo.listaz()

    elif valasztas == "4":
        print("Kilépés...")
        break

    else:
        print("Hibás választás!")

