from sklearn import svm
# source: https://pythonprogramminglanguage.com/python-machine-learning/

X = [[1, 1], [0, 0]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
# make predictions
print(clf.predict([[2., 2.]]))


