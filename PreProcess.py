import os
import string
import math

def complete_path(path):
    allFiles = os.listdir(path)
    pathList = []
    for file in allFiles:
        p = os.getcwd()+"/"+path+"/"+file
        pathList.append(p)
    return pathList

def read(files):
    allList = []
    for file in files:
        f = open(file, encoding="utf8")
        line = f.readline().lower()
        f.close()
        allList.append(line)
    return allList

def readOneLine(file):
    f = open(file, encoding="utf8")
    line = f.readline().rstrip().lower()
    f.close()
    return line

def readDirectory(files):
    for file in files:
        print(file)

def split(unProcessed):
    wordList = []
    for line in unProcessed:
        for word in line.split():
            wordList.append(word)
    return wordList

def splitOneLine(unProcessed):
    wordList = []
    for word in unProcessed.split():
        wordList.append(word)
    return wordList

def rmbPunc(words):
    line = []
    for s in words:
        s = s.translate(str.maketrans('', '', string.punctuation))
        line.append(s.lower())
    return (line)

def crtDic(words):
    dictionary = dict()
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

def mergeTwoDict(dict1, dict2):
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = dict1[key] + dict2[key]
    return dict3


#===================    Path      =============================

test_neg = "test/neg"
test_pos = "test/pos"
train_neg = "train/neg"
train_pos = "train/pos"
cls_action = "smlCorpus/action"
cls_comedy = "smlCorpus/comedy"
cls_Test = "smlCorpus_Test/0_1.txt"

#===================    Global Dictionarys      =============================

dicForTest_Pos = dict()
dicForTest_Neg = dict()
dicForTrain_Pos = dict()
dicForTrain_Neg = dict()
dicForCls_Comedy = dict()
dicForCls_Action = dict()
dicMerge_AC = dict()
dicMergeTrain = dict()

#===================    Action Comedy      =============================


comedyPath = complete_path(cls_comedy)
comedyList = read(comedyPath)
comWordList = split(comedyList)
comPunc = rmbPunc(comWordList)
dicForCls_Comedy = crtDic(comPunc)


actionPath = complete_path(cls_action)
actionList = read(actionPath)
actWordList = split(actionList)
actPunc = rmbPunc(actWordList)
dicForCls_Action = crtDic(actPunc)


dicMerge_AC = mergeTwoDict(dicForCls_Comedy, dicForCls_Action)


#===================    train      =============================

trainPathPos = complete_path(train_pos)
trainListPos = read(trainPathPos)
trnWordListPos = split(trainListPos)
trainPuncPos = rmbPunc(trnWordListPos)
dicForTrain_Pos = crtDic(trainPuncPos)


trainPathNeg = complete_path(train_neg)
trainListNeg = read(trainPathNeg)
trnWordListNeg = split(trainListNeg)
trainPuncNeg = rmbPunc(trnWordListNeg)
dicForTrain_Neg = crtDic(trainPuncNeg)


dicMergeTrain = mergeTwoDict(dicForTrain_Pos, dicForTrain_Neg)


#===================    Test      =============================







