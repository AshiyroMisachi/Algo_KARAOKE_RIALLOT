import random
class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.listeChanson = ["0","1","2","3","4"]
        self.listeScore = [0,0,0,0,0]

    def getListeChanson(self):
        return self.listeChanson

    def getChanson(self, x):
        return self.listeChanson[x]
    
    def getScore(self, x):
        return str(self.listeScore[x])

    def getPseudo(self):
        return self.pseudo

    def ajoutScore(self, x, score):
        if (score > self.listeScore[x]):
            self.listeScore[x] = score
            print("Vous avez battu votre ancien score !")
        else:
            print("Vous n'avez pas battu votre ancien score...")

    def calculeTotal(self):
        total = self.listeScore[0] + self.listeScore[1]  + self.listeScore[2]  + self.listeScore[3]  + self.listeScore[4] 
        return total

    def calculeMoy(self, total):
        moy = total / len(self.listeScore)
        return moy


game = True
choixMusique = -1
nomPlayer = input("Quel est ton pseudo ?")
player = Player(nomPlayer)
print("Bienvenue " + player.getPseudo() + " dans ce karaoke de folie !")
while game:
    print("Quel musique veut tu joué ?")
    print("0 - " + str(player.getChanson(0)) + " - " + player.getScore(0))
    print("1 - " + str(player.getChanson(1)) + " - " + player.getScore(1))
    print("2 - " + str(player.getChanson(2)) + " - " + player.getScore(2))
    print("3 - " + str(player.getChanson(3)) + " - " + player.getScore(3))
    print("4 - " + str(player.getChanson(4)) + " - " + player.getScore(4))
    print("5 - Voir votre score total")
    print("6 - Voir votre score moyen")
    print("7 - Quittez le karaoke")

    choixMusique = int(input())
    if (choixMusique < 5):
        print("Vous avez choisi la musique" + player.getChanson(choixMusique))
        score = random.randint(50,100)
        print("Vous avez fait un score de " + str(score))
        player.ajoutScore(choixMusique, score)
        input()
    elif (choixMusique == 5):
        print("Voici votre score total :" + str(player.calculeTotal()))
        input()
    elif (choixMusique == 6):
        print("Voici votre score moyen :" + str(player.calculeMoy(player.calculeTotal())))
        input()
    elif (choixMusique == 7):
        print("Vous quittez le jeu")
        game = False
        input()
    else:
        print("Choix incorecte, veuillez choisir une musique disponible")
        choixMusique = int(input())
    
