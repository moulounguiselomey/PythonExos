nomduproduit = input("Quel est le nom du produit ? ")
prixunitaire = float(input("Quel est le prix du produit en euros?")).replace(",", ".")
quantite = int(input("Quelle est la quantité achetée ? "))
remise = int(input("Quel est le taux de la remise en % ? ")).replace(",", ".")
totalbrut = prixunitaire * quantite
montantremise = totalbrut * remise / 100
totalnet = totalbrut - montantremise
totalnet_formate = str(totalnet).replace(".", ",")
print("                    ")
print("===== Caisse =====")
print(f"Produit : {nomduproduit}")
print(f"Prix unitaire : {prixunitaire_formate} (en euros)")
print(f"Quantité : {quantite}")
print(f"Remise : {remise_formate} (en %)")
print("============================")
print("           TICKET           ")
print("============================")
print(f"Produit : {nomduproduit:<16}")