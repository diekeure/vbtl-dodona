bedrag = int(input("Geef een geheel bedrag in euro: "))
b50 = bedrag // 50
rest = bedrag % 50
b20 = rest // 20
rest = rest % 20
b10 = rest // 10
rest = rest % 10
b05 = rest // 5
rest = rest % 5
b02 = rest // 2
b01 = rest % 2
print("Aantal briefjes van 50:", b50)
print("Aantal briefjes van 20:", b20)
print("Aantal briefjes van 10:", b10)
print("Aantal briefjes van 5:", b05)
print("Aantal stukken van 2 euro:", b02)
print("Aantal stukken van 1 euro:", b01)




