print("Bienvenue dans mon premier jeux!")

name = input("Quelle est votre nom?")
age = int(input("Quelle age avez vous?"))

health = 10
print("Vous commencez avec ",health," vie.")

if age > 100:
    print("Ce jeux est trop dangeureux pour votre âge...")
elif age < 18:
    print("Vous êtes jeune soyez accompagné pour cette aventure...")
else:
    print("Vous allez commencer un jeux dangereux!")
    want_to_play = input("Voulez vous jouer?").lower()
    if want_to_play == "oui":
        print("Alors jouons!")
        left_right = input("Premier choix... Gauche ou Droite (gauche/droite)")
        if left_right == "gauche":
            ans = input("Bien, vous suivez un chemin et tombez en face d'un lac... Vouslez vous traverser à la nage ou le contourner? (traverser/contourner)")
            if ans == "traverser":
                print("Vous traversez et vous perdez 5 vie")
                health -= 5
            elif ans == "contourner":
                print("Vous contournez et...")
            else:
                print("Vous avez perdu.")
        else:
            print("Vous tombez dans un trou et vous avez perdu...")
    else:
        print("Ok, à bientôt...")