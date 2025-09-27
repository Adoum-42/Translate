#i = 0
#while i < 10:
from random import randint
motEsp = ["La narradora","La protagonista","El titulo","La autora","La lluvia","La niebla","El miedo","Bello","Un viajero"]
motFr  = ["La naratrice","La protagoniste","Le titre","L'auteur","La pluie","Le brouillard","La peur","Beau","Un voyageur"]
score = 0
for i in range (10):
    x=randint(0,8)
 
    print(motEsp[x])
    motUtil = input("Quelle est sa traduction ? ")
    if motUtil==motFr[x] :
        score += 1
        print ("essai N°",i+1)
print("Score : ",score)

  

