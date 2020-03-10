import csv
import pandas as pd
import math

batters =  []
pitchers = []
people = []
salaries = []

trainingList = []
testList = []

with open("../data/core/Salaries.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        salaries.append([row[0], row[1], row[2], row[3], row[4]])
with open("../data/core/People.csv") as csvDataFile1:
    csvReader1 = csv.reader(csvDataFile1)
    for row1 in csvReader1:
        #id, birth year, month, day, first name, last name
        people.append([row1[0], row1[1], row1[2], row1[3], row1[13], row1[14]])
        # if tempPerson1[0] == tempPerson[0]:
        #     tempPerson.append([row1[1], row1[2], row1[3]])
with open("../data/core/NewBatting.csv") as csvDataFile2:
    csvReader2 = csv.reader(csvDataFile2)
    for row in csvReader2:
        # id, year, stint, team, g, ab, r, h, 2b, 3b, hr, rbi, sb, cs, bb, so, ibb,
        # hbp, sh, sf, gidp
        avg = 0.0
        obp = 0.0
        slg = 0.0

        if float(row[6]) != 0.0:
            avg = float(row[8]) / float(row[6])
            slg = (float(row[8]) + (2 * float(row[9])) + (3 * float(row[10])) + (4 * float(row[11]))) / float(row[6])

        if (float(row[6]) + float(row[15]) + float(row[17]) + float(row[18]) + float(row[20])):
            obp = (float(row[8]) + float(row[15]) + float(row[17]) + float(row[18])) / (float(row[6]) + float(row[15]) + float(row[17]) + float(row[18]) + float(row[20]))
        
        batters.append([row[0], row[1], row[3], str(avg), str(obp), str(slg)])
        # batters.append(row[1])
        # batters.append(str(avg))
        # batters.append(str(obp))
        # batters.append(str(slg))

        
        
        # batters.append([row[0], row[1], row[5], row[6], row[7], row[8], row[9], row[10], 
        # row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20],
        # row[21]])
        # if tempPerson2[0] == tempPerson[3] and tempPerson2[1] == tempPerson[0]:
        #     tempPerson.append([row2[5], row2[6], row2[7], row2[8], row2[9], row2[10], 
        #     row2[11], row2[12], row2[13], row2[14], row2[15], row2[16], row2[17], row2[18], row2[19], row2[20],
        #     row2[21]])

with open("../data/core/Pitching.csv") as csvDataFile3:
    csvReader3 = csv.reader(csvDataFile3)
    for row3 in csvReader3:
        # id, year, w, l, g, gs, cg, sho, sv, ip, h, er, hr,
        # bb, so, oppavg, era, ibb, wp, hbp, bk, bfp, gf, r
        # sh, sf, gidp
        pitchers.append([row3[0], row3[1], row3[5], row3[6], row3[7], row3[8], row3[9], row3[10], row3[11], row3[12], row3[13],
        row3[14], row3[15], row3[16], row3[17], row3[18], row3[19], row3[20], row3[21], row3[22], row3[23], row3[24], row3[25], 
        row3[26], row3[27], row3[28], row3[29]])
        # if tempPerson3[0] == tempPerson[3] and tempPerson3[1] == tempPerson[0]:
        #     tempPerson.append([row3[5], row3[6], row3[7], row3[8], row3[9], row3[10], row3[11], row3[12], row3[13],
        # row3[14], row3[15], row3[16], row3[17], row3[18], row3[19], row3[20], row3[21], row3[22], row3[23], row3[24], row3[25], 
        # row3[26], row3[27], row3[28], row3[29]])

loopCounter = 0
for player in salaries:
    print(loopCounter)
    for batter in batters:
        
        if player[3] == batter[0] and player[0] == batter[1] and batter[2] == player[1]:
            #del batter[0:1]
            if len(player) <= 5:
                player.append(batter[3])
                player.append(batter[4])
                player.append(batter[5])
            
                time = 2017 - int(player[0])
                temp = math.pow(1.03, time)
                adjustedSalary = int(player[4]) * temp
                player.append(adjustedSalary)

                if adjustedSalary < 1000000:
                    player.append("Very Low")

                elif adjustedSalary < 5000000 and adjustedSalary >= 1000000:
                    player.append("Low")

                elif adjustedSalary < 10000000 and adjustedSalary >= 5000000:
                    player.append("Average")
                
                elif adjustedSalary < 15000000 and adjustedSalary >= 10000000:
                    player.append("Above Average")

                elif adjustedSalary < 20000000 and adjustedSalary >= 15000000:
                    player.append("High")

                elif adjustedSalary < 25000000 and adjustedSalary >= 20000000:
                    player.append("Very High")

                elif adjustedSalary < 300000000 and adjustedSalary >= 25000000:
                    player.append("MVP")

                else:
                    player.append("oops no data")

    if loopCounter % 2 == 0:
        trainingList.append(player)
    else:
        testList.append(player)    

    loopCounter += 1

#     for pitcher in pitchers:
#         if player[3] == pitcher[0] and player[0] == pitcher[1]:
#             del pitcher[0:1]
#             player.append(pitcher)

trainingDF = pd.DataFrame(trainingList, columns=['Year', 'Team', 'League', 'Player ID', 'Salary', 'Average', 'On Base Percentage', 'Slugging Percentage', 'Adjusted Salary', 'Category'])
print(trainingDF)

testDF = pd.DataFrame(testList, columns=['Year', 'Team', 'League', 'Player ID', 'Salary', 'Average', 'On Base Percentage', 'Slugging Percentage', 'Adjusted Salary', 'Category'])
print(testDF)


