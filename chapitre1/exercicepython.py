# Demande à l'utilisateur de saisir son nom
nom = input("Comment vous appelez-vous ? ")
# Affiche un message de bienvenue avec le nom saisi
print("Bonjour, " + nom + "! Bienvenue en Python !")

#Demande à l'utilisateur de saisir son âge
age = input("Quel est votre âge ? ")
#Calculer dans combien d'années l'utilisateur aura 100 ans
age = int(age)
#Ecrire dans combien d'années l'utilisateur aura 100 ans
print("Dans", 100 - age, "ans , vous aurez 100 ans !")    
#Calculer et ecrire en quelle année l'utilisateur aura 100 ans
print("Cela sera en", 2026 + (100 - age), "!")

