from random import randrange
from math import ceil
import os
#somme de joeur
somme = 200
robot = randrange(50)
mod = robot%2
if mod == 0 : coleurRobot = "rouge"
else: coleurRobot = "noire"
quiter = False


while somme !=0 or quiter == False:
    choi = input("Choisire un nombre entre 0 est 49 \n")
    choix = int(choi)
    #tester l'element choix
    if choix >=0 and choix <50:
        if choix %2 ==0:
            coleur = "rouge"
        else: coleur =  "noire"
    # print("**********************************************************************************************")
    sommes = input("Entrer une somme $ \n")
    remise = int(sommes)
    if remise <10 or remise >201: print("entrer une somme entre 10$ est 200$ svp")
    print("Vous avez choisez le numero: ",choix,"coleur est :",coleur)
    print("***********************************************************************************************************")
    print("lance la roulette")
    print("...")
    print("la roulette arretee")
    print("le numero gagnant est ",robot,"coleur gagnent ",coleur)
    if robot ==somme :
        somme = remise*3+somme
        print("vous etes le gagnant felicitation !!, Votre somme est: ",somme,"$")
    elif coleur == coleurRobot:
        somme = somme-ceil(remise*0.5)
        print("Vous avez perdes 50%,votre somme est: ",somme,"$")
    else:
     somme = somme-remise
    print("votre somme est: ",somme,"$")
    print("#######################################################################################")
    if somme == 0: break
    print("pour quiter clicker sur \'Q\'")
    q = input()
    if q=="Q": quiter = True
    print("merci de jouer !")
    os.system("pause")



