from sklearn.tree import DecisionTreeClassifier

# Define training and target set for the classifier
train = [[1,2,3],[2,5,1],[2,1,7]]
target = [10,20,30]

# Initialize Classifier. 
# Random values are initialized with always the same random seed of value 0 
# (allows reproducible results)
dectree = DecisionTreeClassifier(random_state=0)
dectree.fit(train, target)

# Test classifier with other, unknown feature vector
test = [[1,2,34],[52,15,1],[32,11,7]]
predicted = dectree.predict(test)

print(predicted)