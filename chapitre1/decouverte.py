#opérateurs arithmétiques 
print("7 + 2 = ", 7 + 2)
print("7 - 2 = ", 7 - 2)
print("7 * 2 = ", 7 * 2)
print("7 / 2 = ", 7 / 2)
print("7 % 2 = ", 7 % 2)

# priorité des opérateurs
print("7 + 2 * 3 = ", 7 + 2 * 3)
print("(7 + 2) * 3 = ", (7 + 2) * 3)

# comparaison : résultat booléen
print("7 > 2 = ", 7 > 2)
print("7 < 2 = ", 7 < 2)
print("7 == 2 = ", 7 == 2)
print("7 != 2 = ", 7 != 2)

#arrondi et conversion de type
print("Arrondi de 45.987899899 : ", round(45.987899899, 2))
print("Conversion en entier de 45.987899899 : ", int(45.987899899))
print("Conversion en flottant de 45 : ", float(45))

#aberations de type : flottant
print( "0.1 + 0.2 = ", round(0.1 + 0.2, 1))

#conditions et logiques booléennes
# == opérateurs d'égalité
print("5 == 5 : ", 5 == 5) #True
print("5 == 6 : ", 5 == 6) #False
print("melvin == melvin : ", "melvin" == "melvin") #True
print("melvin == Melvin : ", "melvin" == "Melvin") #False -> sensible à la casse

#comparaisons chainées
note = 15
print("10 < note < 20 : ", 10 < note < 20) #True

#différencier = et ==
noteparfaite = note == 20
print("noteparfaite : ", noteparfaite) #False

#conditions and, or, not
moyenne = 11.5
nombreabsences = 4
a_rendu_son_projet = True

#and : vrai seulement si les deux conditions sont vraies
admis_sans_reserve = moyenne >= 10 and nombreabsences <= 3
print("admis_sans_reserve : ", admis_sans_reserve) #False

#or : vrai si au moins une des deux conditiosn est vraie
envoi_alerte = moyenne < 8 or nombreabsences > 3
print("envoi_alerte : ", envoi_alerte)

#not : inverse la valeur booléenne
print("Projet manquant : ", not a_rendu_son_projet)

#parenthèses rendent les combinaisons plus lisibles
peut_passer_jury = (moyenne >= 10 or a_rendu_son_projet) and not nombreabsences > 10
print("peut_passer_jury : ", peut_passer_jury) #True

#If / elif / else
note = float(input("Quelle est la note ? ").replace(",", "."))
if note >= 10 :
    print("Bravo vous avez la moyenne")
    print("Continue comme ça")

elif note >= 8:
    print("Vous êtes proche de la moyenne")
    print("Il faut un petit effort supplémentaire")

else: 
    print("Vous n'avez pas la moyenne")
    print("Il faut travailler davantage")
    
print("Fin du programme")

#indentation correspond à 4 espaces

#conditions imbriquées
#v1
if note >= 14 :
    print("Imbrication : bon résultat")
else :
    if note >= 10 :
        print("Imbrication: résultat correct")
    else :
        print("Imbrication: résultat insuffisant")

#v2 mm logique avec elif

if note >= 14:
    print("Avec Elif : bon résultat")
elif note >= 10:
    print("Avec Elif : résultat correct")
else :
    print("Avec Elif : résultat insuffisant")
    
#break : permet de sortir immédiatement d'une boucle
#continue : permet de passer immédiatement à l'itération suivante d'une boucle

# print("Nombres impairs de 1 à 9")
# for iteration in range(1, 10):
#     if iteration % 2 == 0 : 
#         continue #nombrepair on passe à l'itération suivante
#     print(iteration, end=" ")
# print()

# print("Recherche du premier multiple de 7 à partir de 50")
# for nombre in range(50, 100): 
#     if nombre % 7 == 0:
#         print("Trouvé : ", nombre)
#         break
# print("Fin de la recherche")

# while True: 
#     responseUser = input("Tapez sur la touche h pour quitter : ")
#     if responseUser.lower() == "h":
#         break
#     print("Fin de la boucle infinie")
    
#Les boucles imbriquées
#en-tête
# print("   ", end=" ")
# for colonne in range(1, 6):
#     print(f" {colonne:>4}", end=" ")
# print()
# print("-" * 24)

# for ligne in range(1, 6):
#     print(f"{ligne:>2} | ", end="")
#     for colonne in range(1, 6): 
#         print(f" {ligne * colonne:>4} ", end="")
#     print()
        
#Les fonctions
def calculer_age(annee_de_naissance):
    return 2026 - annee_de_naissance
age = calculer_age(1984)
print(f"Vous avez {age} ans.")