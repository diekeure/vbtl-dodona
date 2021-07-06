import math
rz1 = float(input("Geef de lengte van de eerste rechthoekszijde: "))
rz2 = float(input("Geef de lengte van de tweede rechthoekszijde: "))
schuine = math.sqrt(rz1 ** 2 + rz2 ** 2)
omtrek = round(rz1 + rz2 + schuine, 2)
oppervlakte = round(rz1 * rz2 / 2, 2)
print("Omtrek rechthoekige driehoek:", omtrek)
print("Oppervlakte rechthoekige driehoek:", oppervlakte)







