import random
teamFile = ["Team1", "Team2", "Team3", "Team4", "Team5", "Team6"]
random.shuffle(teamFile)
print(teamFile)
if len(teamFile) % 2:
    teamFile.append('Day off')
n = int(len(teamFile))
matchs = []
fixtures = []
return_matchs = []
for fixture in range(1, n):
    for i in range(n/2):
        matchs.append((teamFile[i], teamFile[n - 1 - i]))
        return_matchs.append((teamFile[n - 1 - i], teamFile[i]))
    teamFile.insert(1, teamFile.pop())
    fixtures.insert(len(fixtures)/2, matchs)
    fixtures.append(return_matchs)
    matchs = []
    return_matchs = []

for fixture in fixtures:
    print (fixture)