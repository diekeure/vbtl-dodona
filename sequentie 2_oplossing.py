toets1 = int(input("Hoeveel is de score op de eerste toets? ")) 
toets2 = int(input("Hoeveel is de score op de tweede toets? "))
toets3 = int(input("Hoeveel is de score op de derde toets? "))
totaal = toets1 + toets2 + toets3
gemiddelde = round(totaal / 3, 2)
percentage = round(totaal / 60 * 100, 2)
print("Totaalscore =", totaal)
print("Gemiddelde score =", gemiddelde)
print("Percentage =", percentage, "%")











