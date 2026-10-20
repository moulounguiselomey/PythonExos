total = 0
semaine = 0
prix_du_velo = 200
while total < prix_du_velo :
    semaine = semaine + 1
    total = total + 2 * semaine
    if semaine % 3 == 0 :
        total = total + 5

print(f"Il faut {semaine} semaines pour acheter le vélo (total : {total}€)")
      


