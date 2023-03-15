import random
class Karaoke:
    def __init__(self, listeChanson):
        self.listeChanson = listeChanson
        self.listeJoueur = []

    def getChanson(self, x):
        return self.listeChanson[x]

    def getListeChanson(self):
        return self.listeChanson

    def getListeJoueur(self):
        return self.listeJoueur

    def getJoueur(self, x):
        return self.listeJoueur[x]

    def seeBestScoreM(self):
        print("Choisissez une musique")
        for i in range (len(self.getListeChanson())):
            print(str(i) + " - " + self.getChanson(i))
        choixMusique = -1
        choixMusique = int(input())
        if (choixMusique < len(self.getListeChanson())):
            best = 0
            for i in range (len(self.listeJoueur)):
                if (best < int(self.listeJoueur[i].getScore(choixMusique))):
                    best = self.listeJoueur[i].getScore(choixMusique)
            print("Le meilleur score de cette musique est " + str(best))
        else:
            self.seeBestScoreM()

    def seeBestScore(self):
        best = 0
        for y in range (len(self.listeChanson)):
            for i in range (len(self.listeJoueur)):
                if (best < int(self.listeJoueur[i].getScore(y))):
                    best = self.listeJoueur[i].getScore(y)
        print("Le meilleur score toute musique confondu est " + str(best))

    def seeBestTotal(self):
        best = 0
        for i in range (len(self.listeJoueur)):
                if (best < self.listeJoueur[i].calculeTotal()):
                    best = self.listeJoueur[i].calculeTotal()
        print("Le meilleur total est de " + str(best))
        return best
    
    def seeBestMoy(self):
        best = 0
        for i in range (len(self.listeJoueur)):
                if (best < self.listeJoueur[i].calculeMoy()):
                    best = self.listeJoueur[i].calculeMoy()
        print("La meilleure moyenne est de " + str(best))
        return best

    def ajoutJoueur(self):
        pseudo = input("Quelle est le pseudo du joueur ?")
        joueur = Player(pseudo)
        joueur.initScore(self.listeChanson)
        self.listeJoueur.append(joueur)
        return
    
    def deleteJoueur(self):
        if (len(self.listeJoueur) > 1):
            print("Quel joueur voulez vous effacé ?")
            print(self.listeJoueur)
            choix = input()
            self.listeJoueur.pop(choix)
        else:
            print("Vous ne pouvez pas supprimé de joueur")

class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.listeScore = []

    def initScore(self, listeChanson):
        for i in range (len(listeChanson)):
            self.listeScore.append(0)

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
        total = 0
        for i in range (len(self.listeScore)):
            total = total + self.listeScore[i]
        return total

    def calculeMoy(self):
        moy = self.calculeTotal() / len(self.listeScore)
        return moy
        
game = True
karaoke_1 = Karaoke (["ToiToiToi", "Jones-Burger", "Envole moi", "J'ai faim", "Pas assez rapide"])
karaoke_1.ajoutJoueur()

while game:
    print("Qui joue ?")
    print(karaoke_1.getListeJoueur())
    choixJoueur = int(input())
    joueurChoisi = karaoke_1.getJoueur(choixJoueur)

    print("Quel musique voulez vous joué ?")
    for i in range (len(karaoke_1.getListeChanson())):
        print(str(i) + " - " + karaoke_1.getChanson(i))
    print(str(len(karaoke_1.getListeChanson())+1) + " - Voir le meilleur score d'une musique")
    print(str(len(karaoke_1.getListeChanson())+2) + " - Voir le meilleur total entre les joueurs")
    print(str(len(karaoke_1.getListeChanson())+3) + " - Voir la meilleure moyenne entre les joueurs")
    print(str(len(karaoke_1.getListeChanson())+4) + " - Voir le meilleur score toute musique confondu")
    print(str(len(karaoke_1.getListeChanson())+5) + " - Ajouter un joueur")
    print(str(len(karaoke_1.getListeChanson())+6) + " - Supprimer un joueur")
    choixMusique = -1
    choixMusique = int(input())
    if (choixMusique < len(karaoke_1.getListeChanson())):
        print("Vous avez choisi la musique" + karaoke_1.getChanson(choixMusique))
        score = random.randint(50,100)
        print("Vous avez fait un score de " + str(score))
        joueurChoisi.ajoutScore(choixMusique, score)
        input()
    elif (choixMusique == len(karaoke_1.getListeChanson())+1):
        karaoke_1.seeBestScoreM()
    elif (choixMusique == len(karaoke_1.getListeChanson())+2):
        karaoke_1.seeBestTotal()
    elif (choixMusique == len(karaoke_1.getListeChanson())+3):
        karaoke_1.seeBestMoy()
    elif (choixMusique == len(karaoke_1.getListeChanson())+4):
        karaoke_1.seeBestScore()
    elif (choixMusique == len(karaoke_1.getListeChanson())+5):
        karaoke_1.ajoutJoueur()
    elif (choixMusique == len(karaoke_1.getListeChanson())+6):
        karaoke_1.deleteJoueur()
    else:
        print("Choix incorecte, veuillez choisir une musique disponible")
        choixMusique = int(input())