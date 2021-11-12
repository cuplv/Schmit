import numpy as np
from sklearn import preprocessing, neighbors, tree
from sklearn.model_selection import cross_validate as cross_validation
import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
from sklearn import decomposition
import argparse
import time
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.model_selection import GroupKFold
from sklearn.model_selection import GroupShuffleSplit
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.tree import _tree
from sklearn import preprocessing

def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))
    lst_name = []
    lst_val = []
    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            # print("{}if {} <= {}:".format(indent, name, threshold))
            lst_name.append(name)
            lst_val.append(threshold)
            recurse(tree_.children_left[node], depth + 1)
            # print("{}else:  # if {} > {}".format(indent, name, threshold))
            lst_name.append(name)
            lst_val.append(-1*threshold)
            recurse(tree_.children_right[node], depth + 1)
            if lst_name != [] and lst_val != []:
                lst_name.pop()
                lst_val.pop()
        else:
            val = ""
            len_name = len(lst_name)
            for i in range(len_name):
                if lst_val[i] > 0:
                    val += lst_name[i] + " <= " + str(abs(lst_val[i]))
                else:
                    val += lst_name[i] + " > " + str(abs(lst_val[i]))
                if i < len_name - 1:
                    val += " && "
            # print("{}return {}".format(indent, np.argmax(tree_.value[node][0])))
            print("CLASS {} THEN {}".format(np.argmax(tree_.value[node][0]), val))
            if lst_name != [] and lst_val != []:
                lst_name.pop()
                lst_val.pop()

    recurse(0, 1)

argparser = argparse.ArgumentParser()

argparser.add_argument("--filename", help="input_file", required=False)

argparser.add_argument("--kfolds", help="number of k", default = "20", required=False)

argparser.add_argument("--depth", help="depth of tree", default = "", required=False)

argparser.add_argument("--output", help="name of output", default = "tmp", required=False)

argparser.add_argument("--criterion", help="function to measure quality of split", default = "gini", required=False)

args = argparser.parse_args()

if(args.filename == None):
    filename = raw_input("Enter the name of your input data set (.csv) without file type: ")
    kfolds = raw_input("Please enter the number of random folds for cross-validation step (default is 20)? ")
    if(kfolds == ""):
        kfolds_numbers = 20
    else:
        try:
            kfolds_numbers = int(kfolds)
        except ValueError:
            print("K-fold should be an integer!")
    max_depth_tree = raw_input("Please enter the maximum depth of tree (do not specify any number if default value of algorithm is the best)? ")
    if(max_depth_tree == ""):
        max_depth_tree_num = None
    else:
        try:
            max_depth_tree_num = int(max_depth_tree)
        except ValueError:
            print("Max depth should be integer!")

    df = pd.read_csv("Classification_input/" + filename + ".csv",index_col = 'id')
else:
    filename = args.filename
    kfolds = args.kfolds
    if(kfolds == ""):
        kfolds_numbers = 20
    else:
        try:
            kfolds_numbers = int(kfolds)
        except ValueError:
            print("K-fold should be an integer!")
    max_depth_tree = args.depth
    if(max_depth_tree == ""):
        max_depth_tree_num = None
    else:
        try:
            max_depth_tree_num = int(max_depth_tree)
        except ValueError:
            print("Max depth should be integer!")
    criterion = args.criterion
    df = pd.read_csv(filename)

header = list(df.columns.values)
header.remove('label')
header.remove('weight')
header.remove('id')

id = np.array(df['id'])
df = df.drop(['id'],1)
y = np.array(df['label'])
X = np.array(df.drop(['label'],1))
XX = []
le = preprocessing.LabelEncoder()
flag_contains = False
for x in X.T:
    for e in x:
        if "y" in str(e):
            flag_contains = True
    if flag_contains:
        le_fit = le.fit(x)
        arr = le.transform(x)
        XX.append(arr)
    else:
        XX.append(x)
    flag_contains = False
XX = np.asarray(XX,dtype='int64')
X = XX.T

accuracy_max = 0.0
precision_max = 0.0
recall_max = 0.0
rTime_max = 0
startTime = int(round(time.time() * 1000))

for i in range(3):
    accuracy_avg = 0
    precision_avg = 0
    recall_avg = 0
    kf = GroupShuffleSplit(n_splits=kfolds_numbers,test_size=0.1)
    iteration = 0
    for train_index, test_index in kf.split(X, y,id):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        train_weights = X_train[:,0]
        X_train = np.delete(X_train,0,1)

        test_weights = X_test[:,0]
        X_test = np.delete(X_test,0,1)

        clf_temp = DecisionTreeClassifier(criterion=criterion,splitter='best',max_depth=max_depth_tree_num,min_samples_split = 10)
        clf_temp.fit(X_train,y_train,train_weights)

        accuracy = clf_temp.score(X_test,y_test,test_weights)
        y_predict = clf_temp.predict(X_test)
        precision = precision_score(y_test,y_predict,average='weighted',sample_weight = test_weights)
        recall = recall_score(y_test,y_predict,average='weighted',sample_weight = test_weights)
        endTime = int(round(time.time() * 1000))
        rTime = endTime - startTime
        accuracy_avg = accuracy_avg + accuracy
        precision_avg = precision_avg + precision
        recall_avg = recall_avg + recall
        if(accuracy > accuracy_max):
            accuracy_max = accuracy
            precision_max = precision
            recall_max = recall
            clf = clf_temp
            rTime_max = rTime
        iteration = iteration + 1

    if(args.filename==None):
        out = "Classification_results/" + filename +'_tree'+str(i)+'.dot'
    else:
        out = args.output +'_tree'+str(i)+'.dot'
    tree.export_graphviz(clf,out_file=out,feature_names=header)
    print_out ='accuracy - precision - recall' + filename +'_tree'+str(i) + ': '
    print_out = print_out + str(accuracy_avg/iteration) + " " +  str(precision_avg/iteration) + " " + str(recall_avg/iteration)
    print(print_out)
    print('Number of data is ' + str(len(X_train)))
    print('Number of test data is ' + str(len(test_index)))
    print('Time of computation for tree ' + str(i) + ': ' + str(rTime))
    accuracy_max = 0
    tree_to_code(clf, list(df.drop(['label'],1).drop(['weight'],1).columns.values))

if(args.filename==None):
    print("\n The program generates three trees with highest accuracy. Please run: dot -Tpng Classification_results/" + filename +"_tree0.dot" + " -o tree.png to see the final decision tree. Please note that treen is tree0, tree1, or tree2. \n")
else:
    print("\n The program generates three trees with highest accuracy. Please run: dot -Tpng " + args.output +"_tree0.dot" + " -o tree.png to see the final decision tree. Please note that treen is tree0, tree1, or tree2. \n")
