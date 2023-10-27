'''
Zadanie 1 (4 pkt)
Wykorzystując dekoratory, napisz cache dla funkcji tetranacci z poprzedniego zadania.
Ten dekorator powinien zapobiegać przed ponownym obliczaniem tych samych wartości.
'''

def cache(func):
    cached = {}

    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]

    return wrapper

class Tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.counter = 0
        self.values = [0, 0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.steps:
            self.counter += 1
            if self.counter <= 4:
                return self.values[self.counter-1]
            else:
                next_value = sum(self.values)
                self.values = self.values[1:] + [next_value]
                return next_value
        else:
            raise StopIteration

    @cache
    def tetranacci(self, n):
        if n < 1:
            return 0
        elif n <= 4:
            return self.values[n - 1]
        else:
            return self.tetranacci(n - 1) + self.tetranacci(n - 2) + self.tetranacci(n - 3) + self.tetranacci(n - 4)


steps = 10
tet = Tetranacci(steps)
for i in range(1, steps + 1):
    print(tet.tetranacci(i))

'''
Zadanie 2 (4 pkt)
Zaimplementuj własny generator o nazwie repeat, zwracający obiekt podany przez użytkownika dokładnie N razy.
Jeśli wartość parametru N nie została określona, generator powinien zwracać wartości w nieskończoność.

PRZYKŁAD
repeat(10, 3) → 10 10 10
repeat(10, 5) → 10 10 10 10 10
repeat(5) → 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5…
repeat(5, None) → 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5…
'''

def repeat(value, n=None):
    if n is None:
        while True:
            yield value
    else:
        for _ in range(n):
            yield value

for val in repeat(10, 3):
    print(val)

for val in repeat(10, 5):
    print(val)

# for val in repeat(5):
#     print(val)
#
# for val in repeat(5, None):
#     print(val)

'''
Zadanie 3 (1 pkt)
W kodzie z zajęć w klasie Pojazd utwórz atrybut, który niezależnie od utworzonego obiektu będzie miał taką samą wartość.
każdy obiekt ma mieć kolor biały
'''
class Pojazd:
    def __init__(self, predkosc_max, przebieg, nazwa_modelu):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg
        self.nazwa_modelu = nazwa_modelu
        self.kolor = "biały"

pojazd1 = Pojazd(240, 50, "tesla")
pojazd2 = Pojazd(180, 17, "mercedes")
print(pojazd1.kolor)
print(pojazd2.kolor)

'''
Zadanie 4 (2 pkt)
Wykorzystaj klasy Autobus i Pojazd.
Zdefiniuj metodę opłata, k†óra będzie miała wartość domyślną liczba_miejsc * 100
Jeżeli Pojazd jest instancją Autobusu, opłata ma zostać powiększona o 10% wartości opłaty początkowej.
Np. jeżeli autobus domyślnie ma 50 miejsc to opłata całkowita wyniesie 5500
'''

class Pojazd:
    def __init__(self, predkosc_max, przebieg, liczba_miejsc):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg
        self.liczba_miejsc = liczba_miejsc

    def opłata(self):
        return self.liczba_miejsc * 100

class Autobus(Pojazd):
    def __init__(self, predkosc_max, przebieg, nazwa_modelu, liczba_miejsc):
        super().__init__(predkosc_max, przebieg, liczba_miejsc)
        self.nazwa_modelu = nazwa_modelu

    def opłata(self):
        opłata_początkowa = super().opłata()
        return opłata_początkowa * 1.1

pojazd = Pojazd(240, 50, 50)
autobus = Autobus(180, 17, "Mercedes", 50)

print(pojazd.opłata())
print(autobus.opłata())

'''
Zadanie 5 (4 pkt)
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c.
Klasa powinna zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze.
Główną metodą powinna być rozwiaz(), która zwraca miejsca zerowe podanej funkcji.
Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0,
a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub zerze rozwiązań.
'''

import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"Funkcja kwadratowa: {self.a}x^2 + {self.b}x + {self.c}")

    def oblicz_wartosc(self, x):
        return self.a * x**2 + self.b * x + self.c

    def rozwiaz(self):
        delta = self.b**2 - 4*self.a*self.c

        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Nieskończenie wiele rozwiązań"
                else:
                    return "Brak rozwiązań"
            else:
                x = -self.c / self.b
                return f"Jedno rozwiązanie: x = {x}"
        else:
            if delta > 0:
                x1 = (-self.b - math.sqrt(delta)) / (2*self.a)
                x2 = (-self.b + math.sqrt(delta)) / (2*self.a)
                return f"Dwa rozwiązania: x1 = {x1}, x2 = {x2}"
            elif delta == 0:
                x = -self.b / (2 * self.a)
                return f"Jedno rozwiązanie: x = {x}"
            else:
                return "Brak rozwiązań"

def main():
    f1 = FunkcjaKwadratowa(2, 3, 1)
    f1.wypisz()
    print(f"Wartość dla x=0: {f1.oblicz_wartosc(0)}")
    print(f"Wartość dla x=1: {f1.oblicz_wartosc(1)}")

    print(FunkcjaKwadratowa(0, 0, 0).rozwiaz())
    print(FunkcjaKwadratowa(0, 0, 1).rozwiaz())
    print(FunkcjaKwadratowa(0, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, -5, 6).rozwiaz())
    print(FunkcjaKwadratowa(1, 4, 4).rozwiaz())

if __name__ == "__main__":
    main()
