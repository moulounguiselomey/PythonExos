# total = 0
# semaine = 0
# prix_du_velo = 200
# while total < prix_du_velo :
#     semaine = semaine + 1
#     total = total + 2 * semaine
#     if semaine % 3 == 0 :
#         total = total + 5

# print(f"Il faut {semaine} semaines pour acheter le vélo (total : {total}€)")

#menu interractif

solde = 0
choix = ""
while choix != "3": 
    print(f"--- Tirelire de Mélodie (solde : {solde} euros) ---- ")
    print("1. Déposer\n2. Retirer\n3. Quitter")
    choix = input("Votre choix ? ")
    
    if choix == "1":
        montant = int(input("Montant à déposer : "))
        if(montant > 0): #vérifier que le montant soit positif
            solde = solde + montant
            print(f"Vous avez déposé {montant}")
        else:
            print("Le montant à déposer toit être postitif")
    elif choix == "2":
        montant = int(input("Montant à retirer : "))
        if montant <= 0 :
            print("Le montant à retirer doit êre positif")
        elif montant > solde:
            print("Retrait refusé ! Le montant à retirer dépasse ke solde disponible")
        else: 
            solde -= montant #soustraire le montant du solde
            print(f"Vous avez retiré {montant} euros ")
    elif choix == "3":
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer. ")