# Ecrivez votre code ici !
nombres=input("saissez une liste de nombre séparé par une virgule : ")
liste=nombres.split(",")
somme=0
element =0
sup=()
i=()
#j'affiche liste pour voir quelle type de donnée contient liste
print (liste)
"""
première possibilité pour convertir les donnée de liste en entier:
for i in range(len(liste)):
  liste[i]=int(liste[i])
print(liste)
"""
#Une autre possibilité de convertir liste en entier et les stocké dans une liste liste_entier
liste_entier = [ int(i) for i in liste]
print(liste_entier)
#calculer et afficher la somme ainsi que la moyenne des éléments contenu dans liste_entier
for element in liste_entier:
    somme=somme+element
    moyenne=somme/len(liste_entier)
print(f"la somme des élément est : {somme} et la moyenne est : {moyenne}")
c =0

"""
Compter le nombre de nombres d'élément dans liste_entier supérieur à la moyenne 
for int_element in liste_entier:
    if int_element > moyenne:
        c+=1
        sup=int_element
        print(sup)
print(f"le nombre de nomres supérieur à la moyenne est {c}")
"""
#Une autre façon de compter le nombre de nombre d'élément supérieur à la moyenne et les afficher
list_sup=[]
for int_element in liste_entier:
    if int_element > moyenne:
        list_sup.append(int_element)
print(list_sup)
print(len(list_sup))
