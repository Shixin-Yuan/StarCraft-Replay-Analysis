import os
import shutil

dir_data = ("./data")
dir_build_order_data = ('./buildOrder/')

def parser():
    for filename in os.listdir(dir_data):
        if not filename.endswith('.rgd'):
            continue
        buildOrderStringFile = open('buildingOrderStrings.txt', 'a')
        with open('dataSet/' + filename) as f:
            firstPlayerCreatedNumber = 0
            firstPlayerBeingDestroyedNumber = 0
            secondPlayerCreatedNumber = 0
            secondPlayerBeingDestroyedNumber = 0
            content = f.readlines()
            for line in content:
                tupleArray = line.split(',')
                if tupleArray is not None and len(tupleArray) > 4:
                    if tupleArray[2] == 'Created':
                        if tupleArray[1] == '0':
                            firstPlayerCreatedNumber += 1
                        else:
                            secondPlayerCreatedNumber += 1
                    if tupleArray[2] == 'Destroyed':
                        if tupleArray[1] == '0':
                            secondPlayerBeingDestroyedNumber += 1
                        else:
                            firstPlayerBeingDestroyedNumber += 1
            firstPlayerRemainUnit = firstPlayerCreatedNumber - firstPlayerBeingDestroyedNumber
            secondPlayerRemainUnit = secondPlayerCreatedNumber - secondPlayerBeingDestroyedNumber
            winner = '0'
            if firstPlayerRemainUnit < secondPlayerRemainUnit:
                winner = '1'
            buildOrderFile = open(dir_build_order_data + filename + '.txt', 'w+')
            buildOrder = ''
            for line in content:
                if line.__contains__(',' + winner + ',Created'):
                    lineArray = line.split(',')
                    if len(lineArray) < 5 or line.__contains__('SCV') or int(lineArray[0]) > 10000:
                        continue
                    buildOrder = buildOrder + lineArray[4] + ' & '
                    buildOrderFile.writelines(lineArray[4] + '\n')
            buildOrderStringFile.write(buildOrder + '\n')


parser()
