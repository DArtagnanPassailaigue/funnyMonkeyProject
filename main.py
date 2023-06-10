import random
import os
print(os.getcwd()) # gets the Current Working Directory
folder = os.getcwd()

def braketChecker():
    n = 1
    teamX = int(input("How many teams? "))
    while (teamX != n):
        if (2**n == teamX):
            return teamX
        elif (2**n < teamX):
            n = n+1
            continue
        elif (2**n > teamX):
            print ("you cannot make a tournament with this number")
            teamX = int(input("TRY again!: "))
            n = 1
            continue
        else:
            print("KiLl mE")
def fileMaker(teamNum,nInTeams,nameType):
    list = [] 
    for i in range(teamNum):
        # Team File Creation 
        TeamName = input(f"{nameType} #{i} name:")
        affil = input("affiliation: ")
        fileName = folder + f"team {i, TeamName}.txt"
        file = open(fileName,"w")
        print(file)     
        file.writelines(f"{nameType} name:{TeamName}\n")
        file.writelines(f"affiliation name:{affil}\n")
        file.close  
        for p in range(nInTeams):
            pName = input(f"player {p} name:")
            file = open(fileName,"a")
            file.writelines(f"  Player{p}: {pName}\n")
            file.close 
        list.append(TeamName)
    return list
def matchType():
    gameType = input("Solo, Pairs, or Teams: ").lower()
    if gameType == "solo":        
        teamNum = braketChecker()
        print(teamNum)
        nInTeams = 1
        nameType = "Perfered"
        teamFile = fileMaker(teamNum,nInTeams,nameType)
    elif (gameType == "pairs") or (gameType == "pair"):
        teamNum = braketChecker()
        print(teamNum)
        nInTeams = 2
        nameType = "Pair"
        teamFile = fileMaker(teamNum,nInTeams,nameType)
    elif (gameType == "teams") or (gameType == "team"):
        teamNum = braketChecker()
        nInTeams = int(input("How many people per team? "))
        nameType = "Team"
        teamFile = fileMaker(teamNum,nInTeams,nameType)
    else:
        print("that is not a viable tournament format option!!! TRY again!!")
        matchType()  
    random.shuffle(teamFile)
    print(teamFile)

matchType()