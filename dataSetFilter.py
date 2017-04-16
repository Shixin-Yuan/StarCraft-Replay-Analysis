import os
import shutil

dir_src = ("./TvT/")
dir_dst = ("./dataSet/")
dir_data = ("./data")

def filterRGDFile():
    for filename in os.listdir(dir_src):
        if filename.endswith('.rgd'):
            shutil.copy( dir_src + filename, dir_dst)
        print(filename)


def choose2PlayerGames():
    for filename in os.listdir(dir_dst):
        if filename.endswith('.rgd'):
            numberOfPlayers = -1
            with open('dataSet/' + filename) as f:
                content = f.readlines()
                for line in content:
                    if line.startswith('The following '):
                        numberOfPlayers = -1
                    if line.startswith('Begin'):
                        print(numberOfPlayers)
                        if numberOfPlayers == 2:
                            shutil.copy( dir_dst + filename, dir_data)
                            break
                    numberOfPlayers += 1

# filterRGDFile()
choose2PlayerGames()