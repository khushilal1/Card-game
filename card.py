import random
print("WELCOME TO THE RANDOME CARD GENERATOR GAME")


type=["Spade","Diamond","club","Heart"]
rank=["2","3","4","5","6","7","8","10","Ace","Queen","King","jack"]

x=input("press y\yes to start game\n")
while(x=="y" or x=="yes"):
    a=random.choice(type)
    b=random.choice(rank)
    print(f"the randomly selected card:    {b} of {a}")

    x=input("Do you wann to play again? yes/no\n")
    if(x=="n" or x=="no"):
        print("Thanks for playing game")
        break
