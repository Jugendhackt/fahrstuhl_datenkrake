from scipy import misc
import numpy as np
import glob, os
from math import ceil
import scipy.misc
import matplotlib.pyplot as plt

# Generate indentifier dicts for the two NNs
def genStateDict():
    dicLevel = {}
    dicArrow = {}
    inc = 0
    for i in ["0","1","2","3","4","L"]:
        dicLevel[i + "_" + 'L'] = inc
        inc += 1
    inc = 0
    for j in ["H","L","R"]:
        dicArrow['L' + '_' + j] = inc
        inc += 1

    return (dicLevel, dicArrow)

# Array with all files we use
def fileArray(path):
    root = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    paths = []
    for f in glob.glob("*.jpg"):
        paths.append(path + "/" + f)
    os.chdir(root)
    return (paths)

# Create list of tuples containing picture and indentifier
def loadPictures(files):
    pictures = []
    for f in files:
        face = misc.imread(f, "L")
        pictures.append((face, pictureInfo(f)))
    return pictures

# Create picture info from file name
def pictureInfo(name):
    name = name[name.rfind("/") + 1:]
    name = name[:name.rfind("_")]
    return name

# Sort by pics by indenifiers
def createSortedDict(pictures):
    dic = {} # Newly sorted pictures
    for p in pictures:
        pic = p[0]
        name = p[1]

        if name in dic.keys():
            dic[name].append(pic)
        else:
            dic[name] = [pic]

    return dic

# Create a test and a training list from sorted dict
def splitList(picDict, stateEncodeDict):
    x_train = np.ndarray((128,128))
    x_test = np.ndarray((128,128))

    y_train = np.ndarray((1))
    y_test = np.ndarray((1))

    x_train_list = []
    x_test_list = []

    y_train_list = []
    y_test_list = []


    for i in picDict.keys():
        length = len(picDict[i])
        pics = picDict[i]
        ratio = int(length / 2)

        x = 0
        for j in pics:
            if (x % 2) != 0:
                x_train_list.append(np.reshape(misc.imresize(j, (40,40)), (40,40,1)))
                y_train_list.append(stateEncodeDict[i])
            else:
                x_test_list.append(np.reshape(misc.imresize(j, (40,40)), (40,40,1)))
                y_test_list.append(stateEncodeDict[i])
            x += 1
        if x == 1:
                x_test_list.append(np.reshape(misc.imresize(pics[0], (40,40)), (40,40,1)))
                y_test_list.append(stateEncodeDict[i])
        x_test = np.stack(x_test_list)
        x_train = np.stack(x_train_list)
        y_test = np.stack(y_test_list)
        y_train = np.stack(y_train_list)
    return (x_train,x_test,y_train,y_test)

# Not yet tested with arrow net yet
def showLists(test_list):
    for i in range(test_list[0].shape[0]):
        plt.imshow(test_list[0][i,:,:])
        plt.show()

    print("TEST TEST")
    for i in range(test_list[1].shape[0]):
        plt.imshow(test_list[2][i,:,:])
        plt.show()

# Not tested with arrow net yet
def manualTest(test_list):
    dic = genStateDict()
    print("TRAIN TEST")
    for z in [0,1]:
        for i,item in enumerate(test_list[z]):
            plt.imshow(item)
            plt.show()
            p = input("Pfeil:")
            s = input("Stock:")

            if s == 'X' or p == 'X':
                break
            if dic[s + "_" + p] == test_list[z+2][i]:
                print ("PASSED")
            else:
                print ("FAILED")
        print("TEST TEST")

# Return the neccessary training lists. i = 0: lists for level recog; i = 1 lists for arrow rec
def getList():
    EncodeDict = genStateDict()
    fa = fileArray("Pictures/Pfeile")
    fl = fileArray("Pictures/Levels")
    la = loadPictures(fa)
    ll = loadPictures(fl)
    da = createSortedDict(la)
    dl = createSortedDict(ll)
    sl = splitList(dl, EncodeDict[0])
    sa = splitList(da, EncodeDict[1])
    return (sl,sa)
