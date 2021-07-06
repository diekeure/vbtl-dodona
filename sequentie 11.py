lengte = float(input("Geef de lengte van de muur (in m): "))
hoogte = float(input("Geef de hoogte van de muur (in m): "))
aantal_breedtes = (lengte + 0.519) // 0.52
aantal_rollen = (aantal_breedtes * hoogte + 9.999) // 10
print("Minimumaantal te kopen rollen:", aantal_rollen)








