import csv
import pandas as pd
import math
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics

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
with open("../data/core/NewBatting.csv") as csvDataFile2:
    csvReader2 = csv.reader(csvDataFile2)
    for row in csvReader2:
        avg = 0.0
        obp = 0.0
        slg = 0.0

        if float(row[6]) != 0.0:
            avg = float(row[8]) / float(row[6])
            slg = (float(row[8]) + (2 * float(row[9])) + (3 * float(row[10])) + (4 * float(row[11]))) / float(row[6])

        if (float(row[6]) + float(row[15]) + float(row[17]) + float(row[18]) + float(row[20])) != 0.0:
            obp = (float(row[8]) + float(row[15]) + float(row[17]) + float(row[18])) / (float(row[6]) + float(row[15]) + float(row[17]) + float(row[18]) + float(row[20]))
        
        batters.append([row[0], row[1], row[3], str(avg), str(obp), str(slg), row[11], row[13]])

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

trainArr = []
testArr = []
for player in salaries:
    print(loopCounter)
    
    for batter in batters: 
        if player[3] == batter[0] and player[0] == batter[1] and batter[2] == player[1]:
            if len(player) <= 6:
                player.append(batter[3])
                player.append(batter[4])
                player.append(batter[5])
                player.append(batter[6])
                player.append(batter[7])

                time = 2017 - int(player[0])
                temp = math.pow(1.03, time)
                adjustedSalary = int(player[4]) * temp
                player.append(adjustedSalary)

                if adjustedSalary < 1000000:
                    player.append(1) # minimum

                elif adjustedSalary < 5000000 and adjustedSalary >= 1000000:
                    player.append(2) # very low 

                elif adjustedSalary < 10000000 and adjustedSalary >= 5000000:
                    player.append(3) # low
                
                elif adjustedSalary < 15000000 and adjustedSalary >= 10000000:
                    player.append(4) # average

                elif adjustedSalary < 20000000 and adjustedSalary >= 15000000:
                    player.append(5) # high

                elif adjustedSalary < 25000000 and adjustedSalary >= 20000000:
                    player.append(6) # very high

                elif adjustedSalary < 300000000 and adjustedSalary >= 25000000:
                    player.append(7) # mvp

                else:
                    player.append(-1) # no data

    for person in people:
        if player[3] == person[0]:
            age = int(player[0]) - int(person[1])
            player.append(age)

    trainingList.append(player)   

    loopCounter += 1
    print(loopCounter)

#     for pitcher in pitchers:
#         if player[3] == pitcher[0] and player[0] == pitcher[1]:
#             del pitcher[0:1]
#             player.append(pitcher)

trainingDF = pd.DataFrame(trainingList, columns=['Year', 'Team', 'League', 'Player ID', 'Salary', 'Average', 'On Base Percentage', 'Slugging Percentage', 'Home Runs', 'Stolen Bases', 'Adjusted Salary', 'Category', 'Age'])
# print(trainingDF)

# testDF = pd.DataFrame(testList, columns=['Year', 'Team', 'League', 'Player ID', 'Salary', 'Average', 'On Base Percentage', 'Slugging Percentage', 'Adjusted Salary', 'Category', 'Age'])
# print(testDF)

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

#trainingDF = pd.get_dummies(trainingDF, columns=['Year', 'Team', 'League', 'Player ID'])

# Fill in NaN values
trainingDF.fillna(0, inplace=True)

# trainingDF = clean_dataset(trainingDF)

# print(trainingDF.head())


# https://www.datacamp.com/community/tutorials/decision-tree-classification-python
# https://scikit-learn.org/stable/modules/tree.html#classification
features = ['Average']
x = trainingDF[features]
y = trainingDF.Category

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
tree.plot_tree(clf)
y_pred = clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# clf = tree.DecisionTreeClassifier(max_depth=10)
# clf = clf.fit(trainArr, y)



