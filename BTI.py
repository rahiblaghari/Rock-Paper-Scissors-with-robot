import random

#Counter
Wincount=0
Losscount=0
Drawcount=0
x=1
while (x>0):
    cpu=random.randrange(3)
    y=input("Rock, Paper, Scissors, or End Game? ")
    if cpu==0:
        cpuchoice="Rock"
    elif cpu==1:
        cpuchoice="Paper"
    elif cpu==2:
        cpuchoice="Scissors"
    print(cpuchoice)
    def conv(ltr):
        if ltr=="Rock":
            return 0
        elif ltr=="Paper":
            return 1
        elif ltr=="Scissors":
            return 2
        else:
            return 3
    if y==cpuchoice:
        print("Draw")
        Drawcount+=1
    elif y=="End Game":
        x=0
    elif conv(y)==3:
        print("Invalid Response")
    elif cpu==(1+conv(y)) or (cpu + 2)==conv(y):
        print("Loss")
        Losscount+=1
    elif conv(y)==(1+cpu) or (conv(y)+2)==cpu:
        print("Win")
        Wincount+=1
print("Wins: " + str(Wincount))
print("Losses: " + str(Losscount))
print("Draws: " + str(Drawcount))
