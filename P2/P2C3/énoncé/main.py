# Ecrivez votre code ici
#Définition de la fonction pour calculer le salaire mensuel
def salaire_mensuel(salaire) :
    salaire=salaire/12
    return salaire

#Définition de la fonction pour calculer le salaire hebdomadaire
def salaire_hebdomadaire(salaire) :
    salaire_hebdomadaire=salaire/4
    return salaire_hebdomadaire

#Définition de la fonction pour calculer le salaire horaire
def salaire_horaire(salaire_hebdomadaire,heures_de_travaille) :
    salaire_horaire=salaire_hebdomadaire/heures_de_travaille
    return salaire_horaire
#demander l'utilisateur de saiasir un montant 
_salaire=input("entrez votre salaire annuelle : ")
#je convertis la saisis en entier pour pouvoir effectuer les calculs
_salaire=int(_salaire)
_horaire=input("entrez le nombre d'heures travailler par semaine : ")
_horaire=int(_horaire)
#j'appelle les fonctions et stock les retour dans des variables pour les afficher plu tard
salaireMensuel=salaire_mensuel(_salaire)
salaireHebdo=salaire_hebdomadaire(salaireMensuel)
salaireHoraire=salaire_horaire(salaireHebdo,_horaire)
#la consigne était d'afficher le salaire horaire uniquement. J'ai afficher par la même occasion le salaire mensuelle et hebdomaire pour vérifier si les calculs ont bien passé normalement 
print(f"votre salaire est de {salaireMensuel} par mois, {salaireHebdo} hebdomadaire et {salaireHoraire} par heure")
