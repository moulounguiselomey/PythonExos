while True:
    try: 
        annee_de_naissance = int(input("Quelle est votre année de naissance? "))
        if 1900 <= annee_de_naissance <= 2026:
            break
        else:
            print("Erreur : veuillez saisir une annnée entre 1900 et 2026. ")
        
    except ValueError: 
        print("Erreur, veuillez saisir un nombre entier pour l'année de naissance")
        
age = 2026 - annee_de_naissance
print(f"Vous avez {age} ans. ")