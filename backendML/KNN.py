from sklearn.neighbors import KNeighborsClassifier


'''
K nearest neighbour Learner
'''

class KNN:
    def __init__(self, kwargs=None):
        if kwargs==None:
            self.learner = KNeighborsClassifier()
        else:
            self.learner = KNeighborsClassifier(**kwargs)

    def train(self,X,y):
        self.learner.fit(X,y)

    def query(self,X):
        rt = self.learner.predict(X)
        return rt

    def score(self,X,y):
        rt = self.learner.score(X,y)
        return rt