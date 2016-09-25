import sys
import os
import re
import pickle
import json



Dict1 = {}
tempDict = {}
distinctWords = set()
hCount =0
sCount =0




def getList1():
    List1 = {'spam':0, 'ham':0}
    return List1


def getCount(argList):

    if(sFlag == 1):
        argList['spam'] = argList['spam'] + 1


    return argList

def getCount2(argList):
    if (hFlag == 1):
        argList['ham'] = argList['ham'] + 1

    return argList


def addSmoothing():

    for i in Dict1:
        finalList = []
        tempList = Dict1[i]
        finalList.append((tempList['spam'] + 1) / float(sCount + len(distinctWords)))
        finalList.append((tempList['ham'] + 1) / float(hCount + len(distinctWords)))

        probabilityList[i] = finalList
    return probabilityList

for root, dir, files in os.walk(sys.argv[1]):

            for name in files:
                sFlag =0
                hFlag= 0
                words = []
                if name not in ['.DS_Store', '_MACOSX']:
                    with open(os.path.join(root,name), 'r',encoding="latin1") as f:
                        file1 = f.read()
                        #file1 = file1.lower()
                     

                        file1 = file1.split()
                        #print(file1)

                        for k in range(0,len(file1)):
                            words.append(file1[k])

                                #print(words)


                        if (re.search(r'(.)*spam(.)*', root)):
                            sFlag = 1
                            sCount = sCount + len(words)

                        elif (re.search(r'(.)*ham(.)*', root)):
                            hFlag = 1
                            hCount = hCount + len(words)

                        for i in range(0, len(words)):
                            distinctWords.add(words[i])
                            if words[i] in Dict1:
                                tempDict = Dict1[words[i]]
                                tempDict = getCount(tempDict)
                                tempDict = getCount2(tempDict)
                                Dict1[words[i]] = tempDict
                            else:
                                tempDict = getList1()
                                tempDict = getCount(tempDict)
                                tempDict = getCount2(tempDict)
                                Dict1[words[i]] = tempDict


#print(Dict1)

addSmoothing()


#print(probabilityList)

#addSmoothing()

with open('nbmodel.txt', 'w+') as a:
    json.dump(probabilityList, a)

def main():
    if __name__ == "__main__":
        main()