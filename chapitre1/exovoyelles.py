
compteur = 0
voyelles = "aeiouy"
choix = ""
while True :
        try:
            while choix != "2":
                print("1.Analyser une phrase\n2.Quitter")
                choix = input("Votre choix? ")
                if choix == "1":
                    compteur = 0
                    print("Entrez votre phrase")
                    phrase = input("Votre phrase? ").lower().strip()
                    for lettre in phrase :
                        if lettre in voyelles :
                            compteur = compteur + 1
                    print(f"Il y a {compteur} voyelles dans cete phrase.")
                            
                elif choix == "2":
                    print("Au revoir!")
                    break
                else:
                    print("Choix invalide, veuillez réessayer. ")
        except ValueError: 
                print("Erreur, veuillez saisir une chaîne de caractères")