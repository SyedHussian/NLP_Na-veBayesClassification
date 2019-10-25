import math

import PreProcess as pre


def classProb(testFile, classMap, mergeMap):
    words = (pre.rmbPunc(pre.splitOneLine(pre.readOneLine(testFile))))
    prob = math.log(12500 / 25000, 2)
    mm = len(mergeMap)
    sm = sum(classMap.values())
    for word in words:
        p = (classMap.get(word, 0) + 1) / (mm + sm)
        prob = prob + math.log(p, 2)
    return prob


def ProbForAC(testFile, classMap, mergeMap, Count_1, Count_2):
    words = (pre.rmbPunc(pre.splitOneLine(pre.readOneLine(testFile))))
    prob = math.log(Count_1 / (Count_1 + Count_2), 2)
    mm = len(mergeMap)
    sm = sum(classMap.values())
    for word in words:
        p = (classMap.get(word, 0) + 1) / (mm + sm)
        prob = prob + math.log(p, 2)
    return prob


def doAC(cls_Test, dicForCls_Action, dicForCls_Comedy, dicMerge_AC, comedyPath, actionPath):
    comedy = (ProbForAC(cls_Test, dicForCls_Comedy, dicMerge_AC, len(comedyPath), len(actionPath)))
    action = (ProbForAC(cls_Test, dicForCls_Action, dicMerge_AC, len(actionPath), len(comedyPath)))
    final = action - comedy
    mergeMap = pre.mergeTwoDict(dicForCls_Action, dicForCls_Comedy)
    mm = len(mergeMap)
    com = sum(dicForCls_Comedy.values())
    act = sum(dicForCls_Action.values())

    print("Comedy: \n", dicForCls_Comedy)
    print("Action: \n", dicForCls_Action)

    testFile = pre.rmbPunc(pre.splitOneLine(pre.readOneLine(cls_Test)))

    for word in testFile:
        if word in dicForCls_Comedy:
            print("Comedy: " + word + " " , (dicForCls_Comedy[word]+1)/(mm+com))

        if word in dicForCls_Action:
            print("Action: " + word + " " , (dicForCls_Action[word]+1)/(mm+act))



    print("Probability of Comedy: ", comedy)
    print("Probability of Action: ", action)

    if comedy > action:
        print("Class Predicted: Comedy")
    else:
        print("Class Predicted: Action")

# def doAllAC(cls_Test, dicForCls_Action, dicForComedy)


def doAll(testPosDir, testNegDir, trainPosMap, trainNegMap, mergeTrainMap):
    allTestPosFiles = pre.complete_path(testPosDir)
    allTestNegFiles = pre.complete_path(testNegDir)


    allNegInPos = doAllPos(allTestPosFiles, trainPosMap, trainNegMap, mergeTrainMap)
    allPosInNeg = doAllNeg(allTestNegFiles, trainNegMap, trainPosMap, mergeTrainMap)
    print("Successful Positive run: ", (1 - allNegInPos / 12500) * 100)
    print("Successful Negative run: ", (1 - allPosInNeg / 12500) * 100)
    print("Total Accuracy For Positive and Negative: ", (1 - ((allNegInPos + allPosInNeg) / 25000)) * 100)


def doAllPos(allTestPosFiles, trainPosMap, trainNegMap, mergeTrinMap):
    f = open("all_Positive.txt", "w+")
    negInPos = 0
    for file in allTestPosFiles:
        file_name = file[49:len(file)]
        pos = classProb(file, trainPosMap, mergeTrinMap)
        neg = classProb(file, trainNegMap, mergeTrinMap)
        if neg > pos:
            negInPos += 1
            f.write(file_name + " (was + now -)" + "\n")
        else:
            f.write(file_name + " (was + now +)" + "\n")
    print("Predicted Negative files in Positive folder: ", negInPos)

    f.close()
    return negInPos


def doAllNeg(allTestPosFiles, trainPosMap, trainNegMap, mergeTrinMap):
    f = open("all_Negative.txt", "w+")
    posInNeg = 0
    for file in allTestPosFiles:
        file_name = file[49:len(file)]
        pos = classProb(file, trainPosMap, mergeTrinMap)
        neg = classProb(file, trainNegMap, mergeTrinMap)

        if neg > pos:
            posInNeg += 1
            f.write(file_name + " (was - now +)" + "\n")
        else:
            f.write(file_name + " (was - now -)" + "\n")
    print("Predicted Positive files in Negative folder: ", posInNeg)

    f.close()
    return posInNeg

# print(pre.dicForTrain_Pos)
# print(pre.dicForTrain_Neg)


doAC(pre.cls_Test, pre.dicForCls_Action, pre.dicForCls_Comedy, pre.dicMerge_AC, pre.actionPath, pre.comedyPath)
doAll(pre.test_pos, pre.test_neg, pre.dicForTrain_Pos, pre.dicForTrain_Neg, pre.dicMergeTrain)

