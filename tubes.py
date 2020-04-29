#import library
import random 
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


#-------------Function Program--------------

def randomKata():
    kata=['sehat','terinfeksi']
    return kata[random.randint(0,1)]


#--------------Variabel Program-------------
xMin = -20
xMax = 20
yMin = -20 
yMax = 20
x_range = xMax - xMin
y_range = yMax - yMin

nIndividu = 200
rasioIndividuTerinfeksi = 5/100
probIndividuBergerak = 8/100
waktuPulih = 10
nHari=100
#-------------Prepare data-------------
posX=[];posY=[];stat_sehat=[];stat_imun=[];waktu_infeksi=[];total_nIfeksi=[]
dataAwal=pd.DataFrame()
for i in range (nIndividu):
    posX.append(0)
    posY.append(0)
    stat_sehat.append('sehat')
    stat_imun.append('belum memiliki imun')
    waktu_infeksi.append(0)
#--------------Main Program-------------
for j in range (nHari):
    nInfeksi=0
    for k in range (nIndividu):
        x=posX[k]; y=posY[k]
        #melakukan random bilangan float 0 dan 1
        rand = random.uniform(0,1)
        #right
        if rand <= 0.25 :
            x = x + 1
            y = y
        #down
        elif rand <= 0.50 :
            x = x 
            y = y - 1
        #left
        elif rand <= 0.75 :
            x = x - 1
            y = y
        #up
        else :
            x = x
            y = y + 1

        #periodic boundary condition
        #correction of x axis
        if (x > xMax) :
            x = x - x_range
            if (nInfeksi < nIndividu*rasioIndividuTerinfeksi):
                randomStat_sehat=randomKata()
                stat_sehat[k]=randomStat_sehat
            else :
                stat_sehat[k]='sehat'
        if (x < xMin) :
            x = x + x_range
            if (nInfeksi < nIndividu*rasioIndividuTerinfeksi):
                randomStat_sehat=randomKata()
                stat_sehat[k]=randomStat_sehat
            else :
                stat_sehat[k]='sehat'
        #correction of y axis
        if (y > yMax) :
            y = y - y_range
            if (nInfeksi < nIndividu*rasioIndividuTerinfeksi):
                randomStat_sehat=randomKata()
                stat_sehat[k]=randomStat_sehat
            else :
                stat_sehat[k]='sehat'
        if (y < yMin)  :
            y = y + y_range
            if (nInfeksi < nIndividu*rasioIndividuTerinfeksi):
                randomStat_sehat=randomKata()
                stat_sehat[k]=randomStat_sehat
            else :
                stat_sehat[k]='sehat'

        #correction of waktu_infeksi
        if (stat_sehat[k]=='terinfeksi'):
            waktu_infeksi[k]+=1
            nInfeksi+=1

        #correction of stat_sehat and stat_imun
        if (waktu_infeksi[k] > waktuPulih):
            stat_sehat[k]='Pulih'
            stat_imun[k]='memiliki imun'
            nIfeksi-=1

        #correction of jarak
        for l in range (nIndividu):
            if (posX[k]==posX[l] and posY[k]==posY[l]):
                #penularan virus
                if(stat_sehat[l]=='terinfeksi' and stat_imun[k]=='belum memiliki imun'):
                    stat_sehat[k]='terinfeksi'
                    nInfeksi+=1
                            
        posX[k]=x
        posY[k]=y
            
    print(stat_sehat)
    total_nIfeksi.append(nInfeksi)
print(total_nIfeksi)

#plotting random walker:
#plt.title("Random Walk ($n = " + str(nHari) + "$ steps)")
#plt.plot(posX, posY)
#plt.show()


        
