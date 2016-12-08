#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os
import time
from sklearn import metrics
import numpy as np
import cPickle as pickle

reload(sys)
sys.setdefaultencoding('utf8')

# Multinomial Naive Bayes Classifier
def naive_bayes_classifier(train_x, train_y):
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB(alpha=0.01)
    model.fit(train_x, train_y)
    return model


# KNN Classifier
def knn_classifier(train_x, train_y):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier( n_neighbors=3)
    model.fit(train_x, train_y)
    return model


# Logistic Regression Classifier
def logistic_regression_classifier(train_x, train_y):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty='l2')
    model.fit(train_x, train_y)
    return model


# Random Forest Classifier
def random_forest_classifier(train_x, train_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=8)
    model.fit(train_x, train_y)
    return model


# Decision Tree Classifier
def decision_tree_classifier(train_x, train_y):
    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    model.fit(train_x, train_y)
    return model


# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=200)
    model.fit(train_x, train_y)
    return model


# SVM Classifier
def svm_classifier(train_x, train_y):
    from sklearn.svm import SVC
    model = SVC(kernel='rbf', probability=True)
    model.fit(train_x, train_y)
    return model

# SVM Classifier using cross validation
def svm_cross_validation(train_x, train_y):
    from sklearn.grid_search import GridSearchCV
    from sklearn.svm import SVC
    model = SVC(kernel='rbf', probability=True)
    param_grid = {'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.001, 0.0001]}
    grid_search = GridSearchCV(model, param_grid, n_jobs = 1, verbose=1)
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    for para, val in best_parameters.items():
        print para, val
    model = SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)
    model.fit(train_x, train_y)
    return model

from pandas import DataFrame
def read_data(data_file):
    import gzip
    f = gzip.open(data_file, "rb")
    train, val, test = pickle.load(f)
    f.close()




    train_x = train[0]
    train_y = train[1]
    test_x = test[0]
    test_y = test[1]
    print train_x.shape
    print train_y.shape
    print test_x.shape
    print test_y.shape
    # print     DataFrame(dict(train_x)).head()

    print 'train_x'
    getddetail(train_x)
    print 'train_y'
    getddetail(train_y)
    print 'test_x'
    getddetail(test_x)
    print 'test_y'
    getddetail(test_y)
    return train_x, train_y, test_x, test_y
def getddetail(data):
    y=0
    for i in data:
        if y<20:
            print i
        else:
            break

        y+=1
import predeal
if __name__ == '__main__':
    thresh = 0.5
    model_save_file = None
    model_save = {}

    test_classifiers = [
        # 'NB',
        'KNN',
        'LR', 'RF', 'DT', 'SVM', 'GBDT'
    ]
    classifiers = {
        # 'NB':naive_bayes_classifier,
                  'KNN':knn_classifier,
                   'LR':logistic_regression_classifier,
                   'RF':random_forest_classifier,
                   'DT':decision_tree_classifier,
                  'SVM':svm_classifier,
                'SVMCV':svm_cross_validation,
                 'GBDT':gradient_boosting_classifier
    }

    print 'reading training and testing data...'
    train_x,train_y=predeal.load_data()
    test_x, test_y=predeal.load_testdata()
    # train_x, train_y, test_x, test_y = read_data(data_file)

    #
    #
    #
    num_train, num_feat = train_x.shape
    num_test, num_feat = test_x.shape
    is_binary_class = (len(np.unique(train_y)) == 2)
    print '******************** Data Info *********************'
    print '#training data: %d, #testing_data: %d, dimension: %d' % (num_train, num_test, num_feat)

    for classifier in test_classifiers:
        print '******************* %s ********************' % classifier
        start_time = time.time()
        model = classifiers[classifier](train_x, train_y)
        print 'training took %fs!' % (time.time() - start_time)



        predict = model.predict(test_x)


        if model_save_file != None:
            model_save[classifier] = model
        if is_binary_class:
            precision = metrics.precision_score(test_y, predict)
            recall = metrics.recall_score(test_y, predict)

            print 'precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall)











        # pkl_file=None
        # pkl_file = open(model_save_file, 'rb')
        # object = pickle.load(pkl_file)
        # if pkl_file is not None:
        #     pkl_file.close()
        # predict = object['KNN'].predict(test_x)




        accuracy = metrics.accuracy_score(test_y, predict)
        print 'accuracy: %.2f%%' % (100 * accuracy)

    if model_save_file != None:
        pickle.dump(model_save, open(model_save_file, 'wb'))
