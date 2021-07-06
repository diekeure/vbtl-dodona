gewicht = int(input("Hoeveel gram weegt het pakje? "))
afstand = int(input("Hoeveel kilometer moet het pakje afleggen? "))
begonnen_gewicht = (gewicht + 19) // 20
begonnen_afstand = (afstand + 9) // 10
prijs = 2 + begonnen_gewicht * 0.4 + begonnen_afstand * 0.3
print("Prijs voor het versturen van het pakje:", prijs, "euro")

