import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from random import shuffle

def generate_trainingset_and_testingset(data, samplesize):
    whole_data = genfromtxt(data, delimiter=',', skip_header=1)
    (N, n) = whole_data.shape
    n = n-1
    if (samplesize >= N):
        raise AssertionError("Sample size can't be larger than whole data")
    liste_all = list(whole_data)

    size = n

    mean = int(size/2)
    div = int((size-mean)/3)

    prüfungObNurWertImPrüfraumEnthalten = True

    while(prüfungObNurWertImPrüfraumEnthalten):
        randomNums = np.random.normal(loc=mean, scale=div, size=samplesize)
        randomInts = list(np.round(randomNums))
        normalverteile_Liste_von_Zahlen = []
        for i in randomInts:
            normalverteile_Liste_von_Zahlen .append(int(i))
        prüfungObNurWertImPrüfraumEnthalten = any(elem < 0 or elem > size for elem in normalverteile_Liste_von_Zahlen)

    trainingsdaten =[]

    for zahlen in normalverteile_Liste_von_Zahlen :
        shuffle(liste_all)
        for i in range(len(liste_all)):
            liste_der_optionen = list(liste_all[i][0:n])
            if(liste_der_optionen.count(1)==zahlen):
                trainingsdaten.append(liste_all[i])
                del liste_all[i]
                break
            if i ==len(liste_all)-1:
                normalverteile_Liste_von_Zahlen.append((i+1)%size)



    trainingsarray = np.array(trainingsdaten)
    testarray = np.array(liste_all)
    return(trainingsarray, testarray)



print('Read whole dataset from csv file ...')
dir_data = 'Data/' + "x264" + '_AllNumeric.csv'
print('Dataset: ' + dir_data)

(training, test) = generate_trainingset_and_testingset(dir_data, 55)

print(len(training))
print(len(test))