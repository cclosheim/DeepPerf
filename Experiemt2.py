import csv
from subprocess import Popen
from time import sleep
import threading
import subprocess
from multiprocessing import Process



def experiment(samplesize):
    name = "LLVM"
    dic = []
    process = Popen("python AutoDeepPref_new_sampling_methode.py "+name+" -ss %i -ne 30" % samplesize)
    process.wait()
    with open("result_"+name+".csv") as csvdatei:
        csv_reader_object = list(csv.reader(csvdatei))
        dic.append(csv_reader_object[1])

    with open("result_"+name+"_complete.csv", "a") as csvdateiwrite:
        writer = csv.writer(csvdateiwrite, delimiter=',')
        writer.writerows(dic)

if __name__ == '__main__':
    Sample = [11, 22, 33, 44, 55]
    threads = []
    for i in Sample:
        t = Process(target=experiment, args=(i,))
        threads.append(t)

    for x in threads:
        x.start()
        sleep(10)

    for x in threads:
        x.join()