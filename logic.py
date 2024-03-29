import random
import os
print(os.getcwd()) # gets the Current Working Directory
folder = os.getcwd()

def braketChecker():
    '''This function asks for the ammont of teams and make sure it works with the ideal team formula, 2^X'''
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
    '''This function makes team files which store team names, member names, and affiliation'''
    list = [] 
    for i in range(teamNum):
        # Team File Creation 
        TeamName = input(f"{nameType} #{i} name:")  #ever since i learned about f literal strings I've been using them a lot
        affil = input("affiliation: ")
        fileName = folder + f"team {i} {TeamName}.txt" #like ALOT
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
    ''' This function asks the user what kind of game they'd like to play and sets variable as such'''
    gameType = input("Solo, Pairs, or Teams: ").lower()
    if gameType == "solo":        
        teamNum = braketChecker() # asks for number of teams
        print(teamNum)
        nInTeams = 1    # number of people in a team
        nameType = "Perfered"   #  proper grammar
        teamFile = fileMaker(teamNum,nInTeams,nameType) # creates file
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
     
    if teamNum > 2:
        print(teamFile)
        seeding(teamFile, teamNum)
    elif teamNum == 2:
        print(teamFile)

def nest_list(teamFile,rows, columns):  
    ''' This function makes four list in side the list, making it easier to check for duplicates'''
    result=[]               
    start = 0
    end = columns
    for x in range(rows): 
        result.append(teamFile[start:end])
        start +=columns
        end += columns
    return result    
def seeding(teamFile,teamNum):
    ''' This fuction does the actual seeding [incomplete]'''
    nOfDivision = teamNum//4 #divides the amount of teams by 4
    print(nOfDivision)
    random.shuffle(teamFile) # shuffles teams 
    division=nest_list(teamFile,4,nOfDivision)
    print(division)

# actual call of the function
matchType()