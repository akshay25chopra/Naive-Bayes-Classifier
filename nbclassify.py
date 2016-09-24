import os
import json
import sys
import math



with open("nbmodel.txt", 'r',encoding="latin1") as fmodel:
    modelData = json.load(fmodel)


spamProb = 0
hamProb = 0

foutput = open("nboutput.txt", 'w+')


for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:

        trainDict = []
        spamProb = 0
        hamProb = 0
        if name not in ['.DS_Store','_MACOSX']:
            with open(os.path.join(root,name), 'r',encoding="latin1") as f:
               # print(os.path.join(root,name))
                file1 = f.read()
                #file1 = file1.lower()
                file1 = file1.split()

                for k in range(0,len(file1)):
                   trainDict.append(file1[k])

                for l in range(0,len(trainDict)):
                    if(trainDict[l] in modelData):
                        spamProb += math.log(modelData[trainDict[l]][0])
                        hamProb += math.log(modelData[trainDict[l]][1])

                    #print(spamProb)

                if (spamProb>=hamProb):
                    foutput.write("spam ")
                else:
                    foutput.write("ham ")

                foutput.write(os.path.join(root,name)+"\n")
               # print(foutput)

