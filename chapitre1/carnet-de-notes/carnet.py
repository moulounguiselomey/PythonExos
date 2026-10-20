# nom_etudiant = "Timothée"
# note_1 = 11.5
# note_2 = 8
# note_3 = 13

# print("Etudiant : ",nom_etudiant)
# print("NOTES : ", note_1, note_2, note_3)

# #calculs :
# nombre_de_notes = 3
# somme_des_notes = note_1 + note_2 + note_3
# moyenne = somme_des_notes / nombre_de_notes
# print("Moyenne : ", moyenne)

# #Comparaison : le résultat sera un booléen (True ou False)
# est_admis = moyenne >= 10

# #affichage des résultats :
# print("Etudiant : ", nom_etudiant)
# print("Somme des notes : ", somme_des_notes)
# print("Moyenne : ", moyenne)
# print("Admis : ", est_admis)

# #vérification du typage
# print("Type de l'étudiant : ", type(nom_etudiant))
# print("Type de la somme des notes : ", type(somme_des_notes))
# print("Type de la moyenne : ", type(moyenne))
# print("Type de l'admission : ", type(est_admis))

# print("=====CARNET DE NOTES=====")
# nom_etudiant = input("Nom de l'étudiant : ")
# note_1 = float(input("Note 1 : (sur 20)")).replace(",", ".")
# note_2 = float(input("Note 2 : (sur 20)")).replace(",", ".")
# note_3 = float(input("Note 3 : (sur 20)")).replace(",", ".")

# nombre_de_notes = 3
# moyenne= (note_1 + note_2 + note_3) / nombre_de_notes

# print("Etudiant : ", nom_etudiant)
# print(f"Notes : {note_1:.2f}, {note_2:.2f}, {note_3:.2f}")
# print(f"Moyenne : {moyenne:.2f}")
# #:.2f permet d'arrondir à 2 décimales

# #validité des notes : une note est valide si elle est comprise entre 0 et 20
# notes_valides = (0 <= note_1 <= 20) and (0 <= note_2 <= 20) and (0 <= note_3 <= 20)

# if not notes_valides : 
#     print("Erreur : Une ou plusieurs notes ne sont oas valides, doivent être comprises entre 0 et 20")
    
# else: 
#     moyenne = (note_1 + note_2 + note_3) / 3
#     print(f"Etudiant: {nom_etudiant}")
#     print(f"Notes : {note_1: .2f}, {note_2: .2f}, {note_3: .2f}")
#     print(f"Moyenne: {moyenne: .2f}")
    
#Boucle infinie
#compteur = 1
#somme = 0
#while computer <= 3: 
#    somme += compteur

#print("somme : ",somme")

for répète son bloc pour chaque élément d'une sèquence 
range() : génère une sèquence de nombres, ex : range (5) génère les nombres de 0 à 4
range(fin): range (0) => -1
range(debut, fin) : range(3, 9) les chiffres de 3 à 8
range(debut, fin, pas) : range(2, 10, 2) => 2, 4, 6, 8

for i in range(5): 
    print("Tour numéro : ", i, end=" ")
print()

for note in range(0, 21, 5):
    print("Note : ", note, end=" ")
print()

from os import replace


print("----BOUCLES----")
nom_etudiant = input("nom de l'étudiant : ")

note_1 = float(input("Note 1 (sur 20)").replace(",", "."))
note_2 = float(input("Note 2 (sur 20)").replace(",", "."))
note_3 = float(input("Note 3 (sur 20)").replace(",", "."))

#Accumulateurs
sommes_des_notes = 0.0
nombre_de_notes = 0
note_minimale = 0
note_maximale = 20.0

choix = ""
while choix != "0" :
    print()
    print("1 : ajouter une note")
    print("2 : ajouter plusieurs notes au menu")
    print("3 : afficher le bulletin")
    print("0 : quitter")
    choix = input("Votre choix : ")

if choix == "1" :
    note = float(input("saisir une note sur 20 : ").replace(",", "."))
    while note < 0 or note > 20 :
            print("Note invalide : la note doit être entre 0 et 20.")
    note = float(input("saisir une note sur 20 : ").replace(",", "."))
    sommes_des_notes += note
    nombre_de_notes += 1
    if note < note_minimale:
            note_minimale = note
    if note > note_maximale:
            note_maximale = note

    print(f"Note {note:.2f} enregistrée")
    
elif choix == "2" :
    quantite = int(input("Combien de notes voulez-vous rajouter?"))
    for numero in range(1, quantite +1)
        note = float(input(f"Note {numero} sur {quantite}" : ).replace(",", "."))
        #une note incorecte est entrée
    while note < 0 or note > 20 :
                print("Note invalide : la note doit être entre 0 et 20.")
    note = float(input("saisir une note sur 20 : ").replace(",", "."))
    sommes_des_notes += note
    nombre_de_notes += 1
        
elif choix == "3":
    if nombre_de_notes == 0:
        print("Aucune note enregistrée")
    else:
        moyenne = sommes_des_notes / nombre_de_notes
        print(f"Bulletin de {nom_etudiant} :")
        print(f"Nombre de notes : {nombre_de_notes}")
        print(f"Moyenne : {moyenne:.2f}/20")
elif choix == "0": 
    print("Au revoir")
else: 
    print("Choix invalide : tapez 1, 3 ou 0. ")



