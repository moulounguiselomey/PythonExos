import string


compteur = 0
voyelles = "aeiouyéèêë"
choix = ""

def compteur_de_voyelles(voyelles):
    for lettre in voyelles:
        if lettre in voyelles:
            compteur = compteur + 1
            print(f"Il y a {compteur} voyelles dans cette phrase. ")
    while True :
        try:
            while choix != "2":
                print("1.Analyser une phrase\n2.Quitter")
                choix = input("Votre choix? ")
                if choix == "1" :
                    compteur = 0
                    print("Entrez votre phrase")
                    phrase = input(string("Votre phrase? ")).lower().strip()                   
                    compteur_de_voyelles(phrase)
                elif choix == "2":
                    print("Au revoir!")
                    break
                else:
                    print("Choix invalide, veuillez réessayer. ")
        except ValueError: 
            print("Erreur, veuillez saisir une chaîne de caractères")