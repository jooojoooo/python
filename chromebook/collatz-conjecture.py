import turtle


def collatz_c(x):
    zahlenfolge = [x]
    while x > 1:
        if x % 2 == 0: x = x // 2
        else: x = x * 3 + 1
        zahlenfolge.append(x)
    return zahlenfolge

def vergleich(zahl):
    ergebnisliste = collatz_c(zahl)
    schritt_liste[zahl] = len(ergebnisliste)
    return ergebnisliste

schritt_liste = {}
mode = input("Eine [Z]ahl oder alle Zahlen bis [n]")
if mode.lower() == "z":
  while True:
    try:
      zahl = int(input("Bitte gib eine Zahl ein\n"))
      ergebnisliste = vergleich(zahl)
      print("Zahlenfolge: " + str(ergebnisliste))
    except ValueError:
      break

elif mode.lower() == "n":    
  for i in range(int(input("Bis zu welcher Zahl? "))):
    vergleich(i)
    
print(schritt_liste)
print("calculating Diagramm")

s = turtle.Screen()
s.setworldcoordinates(0, 0, len(schritt_liste),200)
pen = turtle.Turtle()

for key, value in schritt_liste.items():
  pen.pendown()
  pen.goto((key,value))