#　-*- coding:utf-8 -*-

from dataset_utils import tennisdataset
from sklearn import naive_bayes

def experiment(method="GaussianNB"):
    trX, trY = tennisdataset("train")
    clf = getattr(naive_bayes, method)()
    clf.fit(trX, trY)
    tX, tY = tennisdataset("train")
    predY = (clf.predict(tX))
    mean_accuracy = clf.score(tX, tY)
    print("Method: {}".format(method))
    print("Gold: ", tY)
    print("Pred: ", predY)
    print("Mean Accuracy: ", mean_accuracy)
    print()
    print()
    
if __name__ == "__main__":
    for method in ["BernoulliNB", "GaussianNB", "MultinomialNB", "ComplementNB"]:
        experiment(method)