import random

def jeu_devinette():

    print("J'ai choisi un nombre entre 0 et 1000. Deviner le nombre")

    nombre_random = random.randint(0, 1000)
    print(nombre_random)
    essai = int(input("Entrez votre essai:"))
    nb_essai = 0



    while essai != nombre_random:
        nb_essai += 1

        if essai < nombre_random:
            essai = int(input("le nombre est plus grand "))


        elif essai > nombre_random:
             essai = int(input("le nombre est plus petit"))

        if essai == nombre_random:
            print ("bravo  vous avez devinez mon chiffre en" + nb_essai + "essai")
            rejouer = int(input("voulez vous rejouer? oui/non"))
            if rejouer: "non"
                break




jeu_devinette()