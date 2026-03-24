# Ecrivez votre code ici !
A=input("saisir un nombre entier:")
B=input("saisir un nombre entir:")
résultat=int
#vérification de si les nombres saisis sont numériques avec isnumeric()

if not A.isnumeric() or not B.isnumeric():
  print("Erreur: les nombres doivent être numérique")
  raise sytemeExit("fin diu programmes")

#convertir les nombres en entier

int(A)
int(B)

#Créer une variable oppération pour poser l'opération souhaité

opération=input("quelle opération souhaitez vous effectuer ['+', '-', '*' ou '/']:")

#Vérifier l'oppération

match opération :
  case "+":
     résultat=A+B
  case "-":
     résultat=A-B
  case "*":
     résultat=A*B
  case "/":
     résultat=A/B  
  case _:
     raise systemeExit("fin du programme")

print(f"le résultat est {résultat}.")
