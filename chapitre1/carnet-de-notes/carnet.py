nom_etudiant = "Timothée"
note_1 = 11.5
note_2 = 8
note_3 = 13

print("Etudiant : ",nom_etudiant)
print("NOTES : ", note_1, note_2, note_3)

#calculs :
nombre_de_notes = 3
somme_des_notes = note_1 + note_2 + note_3
moyenne = somme_des_notes / nombre_de_notes
print("Moyenne : ", moyenne)

#Comparaison : le résultat sera un booléen (True ou False)
est_admis = moyenne >= 10

#affichage des résultats :
print("Etudiant : ", nom_etudiant)
print("Somme des notes : ", somme_des_notes)
print("Moyenne : ", moyenne)
print("Admis : ", est_admis)

#vérification du typage
print("Type de l'étudiant : ", type(nom_etudiant))
print("Type de la somme des notes : ", type(somme_des_notes))
print("Type de la moyenne : ", type(moyenne))
print("Type de l'admission : ", type(est_admis))
