# Écrivez votre code ici !
"""
Un dévoilement de dictionnaireCrétins fruits avec les clés "pomme", "banane"Et "orange", et les valeurs "rouge", "jaune"Et "orange".
AjoutezLa clé "kiwi"Avec la valeur "vert"au dictionnaire fruits.
Accédez à la valeur correspondant à la clé "banane"et stockez-la dans une variable appelée couleur_banane.
Modifiez la valeur associée à la clé "pomme"Verser "vert".
Supprimez la clé "banane"du dictionnaire fruits.
AffichezLes clés restantes dans le dictionnaire.
"""
fruits={
  "pomme":"rouge","banane":"jaune","orange":"orange"
}
fruits["kiwi"]="vert"
couleur=fruits.get("banane")
fruits["pomme"]="vert"
del fruits["banane"]
print(fruits)
