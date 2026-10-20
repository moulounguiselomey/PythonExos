# #for i in range(5): 
#     print("Tour numéro : ", i, end=" ")
# print()

total = 0
capfifty = False
caphundred = False

for semaine in range(1, 11):
    depot = semaine * 2
    total = total + depot
    
    if semaine % 3 == 0:
        total += 5
        print(f"Semaine {semaine} : dépôt de {depot} €, total = {total} € (+5 € bonus mamie !)")
        print()
    else:
        print(f"Semaine {semaine} : dépôt de {depot} €, total = {total} €")
        print()
    
    if total >= 50 and capfifty == False :
        print("bravo, cap des 50 euros franchi !")
        print()
        capfifty = True
     
    elif capfifty == True and caphundred == False and total >= 100 :
        print("objectif atteint !")
        print()
        caphundred = True 
    elif total < 100 :
        print("continue tes efforts")
        print()