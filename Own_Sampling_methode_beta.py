import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from random import shuffle, gauss

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

    trainingsdaten =[]

    while(len(trainingsdaten)< samplesize):
        shuffle(liste_all)
        randomNormalint = int(gauss(mean,div))
        if randomNormalint < 0 or randomNormalint > size:
            continue
        for i in range(len(liste_all)):
            liste_der_optionen = list(liste_all[i][0:n])
            if(liste_der_optionen.count(1)==randomNormalint):
                trainingsdaten.append(liste_all[i])
                del liste_all[i]
                break



    trainingsarray = np.array(trainingsdaten)
    testarray = np.array(liste_all)
    return(trainingsarray, testarray)



print('Read whole dataset from csv file ...')
dir_data = 'Data/' + "x264" + '_AllNumeric.csv'
print('Dataset: ' + dir_data)

(training, test) = generate_trainingset_and_testingset(dir_data, 80)

print(len(training))
print(len(test))