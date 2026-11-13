import random
#============ Tours joueurs ==========
def tourj1(joueur1):
    print("A", joueur1, "de jouer")
    """
    message d'info pour les tours (J1)
    paramètre : variable(str)
    return : none
    """

def tourj2(joueur2):
    print("A", joueur2, "de jouer")
    """
    message d'info pour les tours (J2)
    paramètre : variable (str)
    return : none
    """
#============ Tours joueurs ==========
#====================JEU easy===============================
def jeu_easy(case, malus_easy, bonus_easy):
    """
    focntion pour lancer le jeu en mode facile
    paramètre : 3 variable : (int, int, int)
    return : none
    """
    joueur1_case = 0
    joueur2_case = 0
    passe1 = False
    passe2 = False
    continuer = True
    while continuer == True:
        #------ joueur 1 lancer de dé ---------
        if passe1 == True:
            print("")
            print(joueur1, "passe son tour !")
            passe1 = False
        else:
            print("")
            tourj1(joueur1)
            print("")
            lance1 = True
            while lance1 == True:
                print(joueur1,"Quel dé veux-tu, dé de 6(1) ou dé de 4(2) ou dé de 8(3) ou dé de 12(4) ?")
                print("")
                de_choix1 = int(input())
                if de_choix1 == 1:
                    de6 = random.randint(1,6)
                    joueur1_case += de6
                    lance1 = False
                elif de_choix1 == 2:
                    de4 = random.randint(1,4)
                    joueur1_case += de4
                    lance1 = False
                elif de_choix1 == 3:
                    de8 = random.randint(1, 8)
                    joueur1_case += de8
                    lance1 = False
                elif de_choix1 == 4:
                    de12 = random.randint(1, 12)
                    joueur1_case += de12
                    lance1 = False
                else:
                    print("Vous devez choisir un chiffre entre 1 et 4")
                    lance1 = True

            print("")
            if joueur1_case <= case:
                print(joueur1, " est à la case ", joueur1_case)
            elif joueur1_case > case:
                joueur1_case = case
                print(joueur1, "est à la case", joueur1_case)
#===================== Cases bonus, Malus ou passe ton tours J1 ====================
#=================================== Malus J1 ======================================
            if joueur1_case == 26 or joueur1_case == 31 or joueur1_case == 39:
                joueur1_case = joueur1_case - malus_easy
                print(joueur1, "est arrivé sur une case malus")
                print(joueur1 ,"est descendu de", malus_easy, "cases")
                print("")
                print(joueur1 ,"est donc à la case", joueur1_case)
#=================================== Bonus J1 ======================================
            elif joueur1_case == 3 or joueur1_case == 18 or joueur1_case == 24:
                joueur1_case = joueur1_case + bonus_easy
                print(joueur1 ,"est arrivé sur une case bonus")
                print(joueur1 ,"est monté de", bonus_easy, "cases")
                print("")
                print(joueur1 ,"est donc à la case", joueur1_case)
#================================= passe tour J1 ====================================
            if joueur1_case == 15 or joueur1_case == 20:
                passe1 = True
                print(joueur1 ," est sur une cass 'passe son tour'")
                print(joueur1 ," ne jouera pas son prochain tour")

        #------ joueur 2 lancer de dé -------
        if joueur1_case < case :
            de6 = random.randint(1,6)
            de4 = random.randint(1,4)
            de8 = random.randint(1,8)
            de12 = random.randint(1,12)

            if passe2 == True:
                print("")
                print(joueur2, "passe son tour !")
                passe2 = False
            else:
                print("")
                tourj2(joueur2)
                print("")
                lance2 = True
                while lance2 == True:
                    print(joueur2,"quel dé veux tu, dé de 6(1) ou dé de 4(2) ou dé de 8(3) ou dé de 12(4) ?")
                    print("")
                    de_choix2 = int(input(""))
                    if de_choix2 == 1:
                        joueur2_case += de6
                        lance2 = False
                    elif de_choix2 == 2:
                        joueur2_case += de4
                        lance2 = False
                    elif de_choix2 == 3:
                        joueur2_case += de8
                        lance2 = False
                    elif de_choix2 == 4:
                        joueur2_case += de12
                        lance2 = False
                    else:
                        print("Vous pouvez uniquement choisir un chiffre entre 1 et 4")
                        lance2 = True
                print("")
                if joueur2_case <= case:
                    print(joueur2, " est à la case ", joueur2_case)
                elif joueur2_case > case:
                    joueur2_case = case
                    print(joueur2, "est à la case", joueur2_case)

                if joueur1_case>=case or joueur2_case >=case:
                    continuer = False
#===================== Cases bonus, Malus ou passe ton tours J2 ====================
#=================================== Malus J2 ======================================
                if joueur2_case == 26 or joueur2_case == 31 or joueur2_case == 39:
                    joueur2_case = joueur2_case - malus_easy
                    print(joueur2 ,"est arrivé sur une case malus")
                    print("")
                    print(joueur2 ,"est descendu de", malus_easy, "cases")
                    print("")
                    print(joueur2 ,"est donc à la case", joueur2_case)
#=================================== Bonus J2 ======================================
                elif joueur2_case == 3 or joueur2_case == 18 or joueur2_case == 24:
                    joueur2_case = joueur2_case + bonus_easy
                    print(joueur2 ,"est arrivé sur une case bonus")
                    print("")
                    print(joueur2 ,"est monté de", bonus_easy, "cases")
                    print("")
                    print(joueur2 ,"est donc à la case", joueur2_case)
#================================= passe tour J2 ====================================
                if joueur2_case == 15 or joueur2_case == 20:
                    passe2 = True
                    print(joueur2 ," est sur une casse 'passe son tour'")
                    print(joueur2 ," ne jouera pas son prochain tour")

#---------Victoire-------------------
        if joueur1_case >= case :
            print(joueur1, "à gagné.")
            continuer = False
        elif joueur2_case >= case:
            print(joueur2, "à gagné.")
            continuer = False

#====================JEU easy===============================

#====================JEU hard===============================
def jeu_hard(case, malus_hard, bonus_hard):
    """
    fonction pour lancer le jeu en mode difficile
    paramètre : 3 variable(int, int, int)
    return : none
    """
    joueur1_case = 0
    joueur2_case = 0
    passe1 = False
    passe2 = False
    continuer = True
    while continuer == True:
        de6 = random.randint(1,6)
        de4 = random.randint(1,4)
        de12 = random.randint(1, 12)
        de8 = random.randint(1, 8)
        #------ joueur 1 lancer de dé ---------
        if passe1 == True:
            print("")
            print(joueur1, "passe son tour !")
            passe1 = False
        else:
            print("")
            tourj1(joueur1)
            print("")
            lance1 = True
            while lance1 == True:
                print(joueur1,"Quel dé veux-tu, dé de 6(1) ou dé de 4(2) ou dé de 8(3) ou dé de 12(4) ?")
                print("")
                de_choix1 = int(input())
                if de_choix1 == 1:
                    joueur1_case += de6
                    lance1 = False
                elif de_choix1 == 2:
                    joueur1_case += de4
                    lance1 = False
                elif de_choix1 == 3:
                    joueur1_case += de8
                    lance1 = False
                elif de_choix1 == 4:
                    joueur1_case += de12
                    lance1 = False
                else:
                    print("Vous pouvez uniquement choisir un chiffre entre 1 et 4")
                    lance1 = True
            print("")
            if joueur1_case <= case:
                print(joueur1, " est à la case ", joueur1_case)
            elif joueur1_case > case:
                joueur1_case = case
                print(joueur1, "est à la case", joueur1_case)
#===================== Cases bonus, Malus ou passe ton tours J1 ====================
#=================================== Malus J1 ======================================
            if joueur1_case == 26 or joueur1_case == 31 or joueur1_case == 39 or joueur1_case == 45 or joueur1_case == 53:
                joueur1_case = joueur1_case - malus_hard
                print(joueur1, "est arrivé sur une case malus")
                print(joueur1 ,"est descendu de", malus_hard, "cases")
                print("")
                print(joueur1 ,"est donc à la case", joueur1_case)
#=================================== Bonus J1 ======================================
            elif joueur1_case == 3 or joueur1_case == 18 or joueur1_case == 24 or joueur1_case == 38 or joueur1_case == 52:
                joueur1_case = joueur1_case + bonus_hard
                print(joueur1 ,"est arrivé sur une case bonus")
                print(joueur1 ,"est monté de", bonus_hard, "cases")
                print("")
                print(joueur1 ,"est donc à la case", joueur1_case)
#================================= passe tour J1 ====================================
            if joueur1_case == 15 or joueur1_case == 20 or joueur1_case == 25 or joueur1_case == 40 or joueur1_case == 57:
                passe1 = True
                print(joueur1 ," est sur une casse 'passe son tour'")
                print(joueur1 ," ne jouera pas son prochain tour")

        #------ joueur 2 lancer de dé -------
        if joueur1_case < case :
            de6 = random.randint(1,6)
            de4 = random.randint(1,4)
            de8 = random.randint(1,8)
            de12 = random.randint(1,12)

            if passe2 == True:
                print("")
                print(joueur2, "passe son tour !")
                passe2 = False
            else:
                print("")
                tourj2(joueur2)
                print("")
                lance2 = True
                while lance2 == True:
                    print(joueur2,"quel dé veux tu, dé de 6(1) ou dé de 4(2) ou dé de 8(3) ou dé de 12(4) ?")
                    print("")
                    de_choix2 = int(input(""))
                    if de_choix2 == 1:
                        joueur2_case += de6
                        lance2 = False
                    elif de_choix2 == 2:
                        joueur2_case += de4
                        lance2 = False
                    elif de_choix2 == 3:
                        joueur2_case += de8
                        lance2 = False
                    elif de_choix2 == 4:
                        joueur2_case += de12
                        lance2 = False
                    else:
                        print("Vous pouvez uniquement choisir des chiffres entre 1 et 4")
                        lance2 = True
                print("")
                if joueur2_case <= case:
                    print(joueur2, " est à la case ", joueur2_case)
                elif joueur2_case > case:
                    joueur2_case = case
                    print(joueur2, "est à la case", joueur2_case)

                if joueur1_case>=case or joueur2_case >=case:
                    continuer = False
#===================== Cases bonus, Malus ou passe ton tours J2 ====================
#=================================== Malus J2 ======================================
                if joueur2_case == 26 or joueur2_case == 31 or joueur2_case == 39 or joueur2_case == 45 or joueur2_case == 53:
                    joueur2_case = joueur2_case - malus_hard
                    print(joueur2 ,"est arrivé sur une case malus")
                    print("")
                    print(joueur2 ,"est descendu de", malus_hard, "cases")
                    print("")
                    print(joueur2 ,"est donc à la case", joueur2_case)
#=================================== Bonus J2 ======================================
                elif joueur2_case == 3 or joueur2_case == 18 or joueur2_case == 24 or joueur2_case == 38 or joueur2_case == 52:
                    joueur2_case = joueur2_case + bonus_hard
                    print(joueur2 ,"est arrivé sur une case bonus")
                    print("")
                    print(joueur2 ,"est monté de", bonus_hard, "cases")
                    print("")
                    print(joueur2 ,"est donc à la case", joueur2_case)
#================================= passe tour J2 ====================================
                if joueur2_case == 15 or joueur2_case == 20 or joueur2_case == 25 or joueur2_case == 40 or joueur2_case == 57:
                    passe2 = True
                    print(joueur2 ," est sur une casse 'passe son tour'")
                    print(joueur2 ," ne jouera pas son prochain tour")

#---------Victoire-------------------
        if joueur1_case >= case :
            print(joueur1, "à gagné.")
            continuer = False
        elif joueur2_case >= case:
            print(joueur2, "à gagné.")
            continuer = False

#====================JEU hard===============================

#==================== MENU =============================
joueur1= input("choisis ton pseudo joueur 1 ")
joueur2= input("choisis ton pseudo joueur 2 ")

menu =  True
while menu == True :
    print("┎─────────────────┒")
    print("┃1 - Jouer        ┃")
    print("┠─────────────────┫")
    print("┃2 - Règle du jeu ┃")
    print("┠─────────────────┫")
    print("┃3 - Quitter      ┃")
    print("┖─────────────────┚")
    début = int(input())
    if début == 1:
        print("┎──────────────────┒")
        print("┃4 - mode facile   ┃")
        print("┠──────────────────┫")
        print("┃5 - mode difficile┃")
        print("┖──────────────────┚")
        mode = int(input())
        if mode == 4:
            case = 40
            malus_easy = 5
            bonus_easy = 5
            rejouer = True
            jeu_easy(case, malus_easy, bonus_easy)
        elif mode == 5:
            case = 60
            malus_hard = 8
            bonus_hard = 4
            rejouer = True
            jeu_hard(case, malus_hard, bonus_hard)
        else:
            print("erreur de saisis (relancer)")
        menu = False
    elif début == 2:
        print("Le but du jeu de l'oie est d'être le premier à atteindre exactement la case final avec son pion (40 case max en facile et 60 en difficle)")
    elif début == 3:
        menu = False
        rejouer = False
    else:
        print("Erreur seulement (1 - 2 - 3)")
        menu = True
#==================== MENU =============================



rejouer = False

while rejouer == True:
    print("")
    print("┎──────────────┒")
    print("┃1 - Rejouer   ┃")
    print("┠──────────────┫")
    print("┃2 - quitter   ┃")
    print("┖──────────────┚")
    print("")
    replay = int(input())
    print("")
    if replay == 1:
        print("┎──────────────────┒")
        print("┃4 - mode facile   ┃")
        print("┠──────────────────┫")
        print("┃5 - mode difficile┃")
        print("┖──────────────────┚")
        replay_difficult = int(input(""))
        if replay_difficult == 4:
            case = 40
            malus_easy = 5
            bonus_easy = 5
            jeu_easy(case, malus_easy, bonus_easy)
        elif replay_difficult == 5:
            case = 60
            malus_hard = 8
            bonus_hard = 4
            jeu_hard(case, malus_hard, bonus_hard)
        else:
            print("Vous pouvez seulement choisir 4 ou 5")
    elif replay == 2:
        rejouer = False
    else:
        print("Erreur, veuillez selectionner 1 ou 2. ")