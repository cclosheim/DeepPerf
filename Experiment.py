import numpy as np
import csv
from subprocess import Popen
from multiprocessing import Process, Manager,Lock
from time import sleep

def writeincsv(samplesize):
    dic = {1:(9.305251,2.419904),
    50:(2.269211,0.296360),
    75:(1.767358,0.108820),
    25:(3.266146,0.392857),
    62:(1.901243,0.150663),
    37:(2.780306,0.386427),
    87:(1.702163,0.101040),
    13:(4.203759,0.409933),
    43:(2.399444,0.151255),
    56:(2.262858,0.312726),
    7:(5.165574,0.368176),
    31:(2.649811,0.307924),
    19:(3.858860,0.457863),
    59:(2.164003,0.302704),
    40:(2.884935,0.393700),
    4:(7.258039,1.232105),
    28:(3.012510,0.320685),
    10:(4.690547,0.509553),
    16:(4.373510,0.540376),
    22:(3.869842,0.482764),
    2:(17.690332,2.253255),
    60:(2.087065,0.157625),
    41:(2.716995,0.303047),
    8:(4.956013,0.525131),
    29:(3.083593,0.371413),
    5:(5.646426,0.446568),
    26:(2.960168,0.378775),
    17:(3.763689,0.386953),
    23:(3.173734,0.331133),
    11:(5.088111,0.796996),
    42:(2.369400,0.153166),
    3:(8.472560,2.791842),
    30:(2.925948,0.352706),
    6:(5.588555,0.427156),
    9:(5.000465,0.371805),
    12:(4.685060,0.458757),
    100:(1.561620,0.078224)}
    """
       dic = {
          1:(11.112649, 4.824512),
       2:(16.248396, 1.993362),
       3:( 7.368396, 1.727204),
       4:(
       5.526472,
       0.508404),
       5:(
       5.812242,
       1.020117),
       6:(
       5.510856,
       0.952726),
       7:(
       4.646004,
       0.433114),
       8:(
       4.873316,
       0.829502),
       9:(
       4.393846,
       0.785269),
       10:(
       4.652575,
       0.616423),
       11:(
       4.415572,
       0.90022),
       12:(
       5.008804,
       0.974127),
       13:(
       4.043848,
       0.551638),
       14:(
       4.425019,
       0.805223),
       15:(
       3.682166,
       0.611863),
       16:(
       5.18467,
       1.619675),
       17:(
       3.995877,
       0.710808),
       18:(
       3.698249,
       0.855667),
       19:(
       3.672607,
       0.656182),
       20:(
       3.285206,
       0.535273),
       21:(
       3.490105,
       0.617339),
       22:(
       2.803479,
       0.424612),
       23:(
       3.017956,
       0.48867),
       24:(
       3.08737,
       0.459384),
       25:(
       3.566161,
       0.791659),
       26:(
       3.869231,
       0.84245),
       27:(
       2.69501,
       0.359742),
       28:(
       2.552708,
       0.250664),
       29:(
       2.86446,
       0.777013),
       30:(
       2.898491,
       0.344376),
       31:(
       2.695982,
       0.332611),
       32:(
       3.276395,
       0.444359),
       33:(
       2.723928,
       0.230808),
       34:(
       3.479388,
       0.941379),
       35:(
       2.360651,
       0.204518),
       36:(
       2.428164,
       0.508168),
       37:(
       2.48223,
       0.378698),
       38:(
       2.458839,
       0.192726),
       39:(
       2.910536,
       0.407944),
       40:(
       2.15225,
       0.229894),
       41:(
       2.299205,
       0.344025),
       42:(
       2.301447,
       0.413316),
       43:(
       2.328744,
       0.21334),
       44:(
       2.334312,
       0.454421),
       45:(
       2.847888,
       0.884413),
       46:(
       2.518594,
       0.532379),
       47:(
       2.579756,
       0.807393),
       48:(
       2.08856,
       0.269025),
       49:(
       2.109893,
       0.197322),
       50:(
       2.628673,
       0.810406),
       51:(
       2.163572,
       0.213335),
       52:(
       1.983516,
       0.337526),
       53:(
       1.896543,
       0.142833),
       54:(
       2.279843,
       0.365368),
       55:(
       1.830996,
       0.305085),
       56:(
       2.001687,
       0.271641),
       57:(
       2.177758,
       0.229696),
       58:(
       2.052371,
       0.261685),
       59:(
       1.898964,
       0.21783),
       60:(
       1.844129,
       0.177489),
       61:(
       1.699243,
       0.186724),
       62:(
       1.957558,
       0.251419),
       63:(
       2.027784,
       0.149302),
       64:(
       2.037565,
       0.232607),
       65:(
       1.77137,
       0.228321),
       66:(
       1.882896,
       0.217264),
       67:(
       1.88661,
       0.222933),
       68:(
       1.860198,
       0.140961),
       69:(
       1.746215,
       0.291991),
       70:(
       1.824096,
       0.178721),
       71:(
       1.749102,
       0.2172),
       72:(
       2.020879,
       0.186586),
       73:(
       1.728406,
       0.169473),
       74:(
       2.049037,
       0.266787),
       75:(
       1.872446,
       0.267355),
       76:(
       1.678252,
       0.18437),
       77:(
       1.784105,
       0.108659),
       78:(
       1.647729,
       0.116485),
       79:(
       1.713547,
       0.133432),
       80:(
       1.68506,
       0.196261),
       81:(
       1.708395,
       0.13371),
       82:(
       1.956476,
       0.219762),
       83:(
       2.018349,
       0.278006),
       84:(
       1.648589,
       0.204258),
       85:(
       1.721856,
       0.135284),
       86:(
       1.576376,
       0.12012),
       87:(
       1.701751,
       0.15277),
       88:(
       1.709645,
       0.262748),
       89:(
       1.696083,
       0.267208),
       90:(
       1.651849,
       0.151701),
       91:(
       1.693758,
       0.270902),
       92:(
       1.581701,
       0.183033),
       93:(
       1.654386,
       0.123248),
       94:(
       1.659714,
       0.183866),
       95:(
       1.902115,
       0.329742),
       96:(
       1.567998,
       0.124955),
       97:(
       1.691459,
       0.19166),
       98:(
       1.546733,
       0.078641),
       99:(
       1.708837,
       0.239233),
       100:(1.664917,0.171163)
      }
      """

    eintrag = dic[samplesize]
    result_sys = []
    result = [(float(samplesize),eintrag[0],eintrag[1])]

    result_arr = np.asarray(result)
    filename = 'result_' + "LLVM" + '.csv'
    np.savetxt(filename, result_arr, fmt="%f", delimiter=",",
               header="Sample size, Mean, Margin")
    print('Save the statistics to file ' + filename + ' ...')

    filename = 'result_' + "LLVM" + '_AutoML_veryrandom.npy'
    np.save(filename, result_sys)


#version mit Nebenläufigkeit dringent noch optimieren löuft sau langsam

def function(samplesize, dic, lock):
    name = "BDBC"

    process = Popen("python AutoDeepPerf.py "+name+" -ss %i -ne 30" %samplesize)
    #process = Popen("python AutoDeepPref_new_sampling_methode.py " + name + " -ss %i -ne 30" % samplesize)
    process.wait()
    lock.acquire()
    #writeincsv(samplesize)
    with open("result_"+name+".csv") as csvdatei:
        csv_reader_object = list(csv.reader(csvdatei))

        dic[int(float(csv_reader_object[1][0]))] = (float(csv_reader_object[1][1]), float(csv_reader_object[1][2]))

    with open("result_"+name+"_complete.csv","a") as csvdateiwrite:
        writer = csv.writer(csvdateiwrite, delimiter=',')
        writer.writerows([csv_reader_object[1]])
    lock.release()
"""
def condition(d):
    keylist = list(d.keys())
    keylist=sorted(keylist)
    check = False
    threads = []
    with Manager() as manager:
        dic = manager.dict(d)
        l = Lock()
        for i in range(len(keylist)-1):
            obererwert = (dic[keylist[i]])[0]
            unterwert = (dic[keylist[i+1]])[0]
            if abs(obererwert-unterwert)>0.2 :
                newtocheck = int((keylist[i] + keylist[i+1])/2)
                if(not(newtocheck in keylist)):
                    check = True
                    t = Process(target=function, args=(newtocheck, dic, l))
                    threads.append(t)
        for x in threads:
            x.start()
            #sleep(2)
        for x in threads:
            x.join()
        return (check,dic)
"""

if __name__ == '__main__':
    with Manager() as manager:

        dic = manager.dict()
        l = Lock()

        p = Process(target=function, args=(1, dic,l))
        t = Process(target=function, args=(100, dic,l))

        p.start()
        t.start()
        p.join()
        t.join()
        check = True
        while(check):
            keylist = list(dic.keys())
            keylist = sorted(keylist)
            check = False
            threads = []
            for i in range(len(keylist) - 1):
                obererwert = (dic[keylist[i]])[0]
                unterwert = (dic[keylist[i + 1]])[0]
                if abs(obererwert - unterwert) > 1:
                    newtocheck = int((keylist[i] + keylist[i + 1]) / 2)
                    if (not (newtocheck in keylist)):
                        check = True
                        t = Process(target=function, args=(newtocheck, dic, l))
                        threads.append(t)
            for x in threads:
                x.start()
                # sleep(2)
            for x in threads:
                x.join()


        print(dic)
