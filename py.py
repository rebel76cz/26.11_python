class Student:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = []
        self.predmet = None

    def pridat_hodnoceni(self, hodnoceni):
        self.hodnoceni.append(hodnoceni)

    def nastavit_predmet(self, predmet):
        self.predmet = predmet

    def zobraz_informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Příjmení: {self.prijmeni}")
        print(f"Předmět: {self.predmet}")
        print("Hodnocení:", self.hodnoceni)


class Ucitel:
    def __init__(self, jmeno, predmet):
        self.jmeno = jmeno
        self.predmet = predmet

    def pridat_hodnoceni(self, student, hodnoceni):
        student.pridat_hodnoceni(hodnoceni)

print("Info o studentovi:")
martin = Student("Martin", "Hruška")
martin.nastavit_predmet("Matematika")

ucitel = Ucitel("Pan Učitel", "Matematika")
ucitel.pridat_hodnoceni(martin, 90)

martin.zobraz_informace()
