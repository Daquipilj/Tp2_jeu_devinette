import random

def jeu_devinette():

    borne_minimal = int(input("Choisissez une borne minimal"))
    borne_maximal = int(input("Choisissez une borne maximal"))

    nombre_random = random.randint(borne_minimal, borne_maximal)
    essai = int(input("Entrez votre essai:"))
    nb_essai = 0


    while essai != nombre_random:
            nb_essai += 1

            if essai < nombre_random:
                essai = int(input("le nombre est plus grand "))


            elif essai > nombre_random:
                 essai = int(input("le nombre est plus petit"))

    while essai == nombre_random:
        print ("bravo  vous avez devinez mon chiffre en " + str(nb_essai) + " essai")
        rejouer = str(input("voulez vous rejouer? oui/non"))
        if rejouer == "non":
            exit()
        if rejouer =="oui":
            jeu_devinette()

jeu_devinette()
