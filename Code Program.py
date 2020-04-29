#!/usr/bin/env python
# coding: utf-8

# In[14]:


#import library
import random 
import numpy as np
import pandas as pd
from os.path import exists
import matplotlib
import matplotlib.pyplot as plt

#--------------Variabel Program-------------
xMin = -20
xMax = 20
yMin = -20 
yMax = 20
x_range = xMax - xMin
y_range = yMax - yMin
nInfeksi = 0
nIndividu = 200
pulih = 0
day = 0
rasioIndividuTerinfeksi = 5/100
probIndividuBergerak = 8/100
waktuPulih = 10
conTerinfeksi = True
#-------------Prepare data-------------

posX=[]
posY=[]
stat_sehat=[] 
stat_imun=[]
waktu_infeksi=[]
total_nIfeksi=[]
dataAwal=pd.DataFrame()
for i in range (nIndividu):
    rndx = random.randint(-20, 20)
    rndy = random.randint(-20, 20)
    posX.append(rndx)
    posY.append(rndy)
    if i < 10 :
        stat_sehat.append('terinfeksi')
    else :
        stat_sehat.append('sehat')
    stat_imun.append('belum memiliki imun')
    waktu_infeksi.append(0)
#--------------Main Program-------------

while conTerinfeksi==True:
    posXsehat=[]
    posYsehat=[]
    posXpulih=[]
    posYpulih=[]
    posXsakit=[]
    posYsakit=[]
    for k in range (nIndividu):
        x=posX[k]
        y=posY[k]
        #melakukan random bilangan float 0 dan 1
        rand = random.uniform(0,1)
        #right
        if rand <= 0.20 :
            x = x + 1
            y = y
        #down
        elif rand <= 0.40 :
            x = x 
            y = y - 1
        #left
        elif rand <= 0.60 :
            x = x - 1
            y = y
        #up
        elif rand <= 0.80 :
            x = x
            y = y + 1
        #diam
        else :
            x = x
            y = y

        #periodic boundary condition
        #correction of x axis
        if (x > xMax) :
            x = x - 1
            rnd = random.uniform(0,1)
            if (rnd < rasioIndividuTerinfeksi):
                stat_sehat[k]='terinfeksi'
            else :
                stat_sehat[k]='sehat'
        if (x < xMin) :
            x = x + 1
            rnd = random.uniform(0,1)
            if (rnd < rasioIndividuTerinfeksi):
                stat_sehat[k]='terinfeksi'
            else :
                stat_sehat[k]='sehat'
                
        #correction of y axis
        if (y > yMax) :
            y = y - 1
            rnd = random.uniform(0,1)
            if (rnd < rasioIndividuTerinfeksi):
                stat_sehat[k]='terinfeksi'
            else :
                stat_sehat[k]='sehat'
        if (y < yMin)  :
            y = y + 1
            rnd = random.uniform(0,1)
            if (rnd < rasioIndividuTerinfeksi):
                stat_sehat[k]='terinfeksi'
            else :
                stat_sehat[k]='sehat'

        #correction of jarak
        for l in range (nIndividu):
            if (posX[k]==posX[l] and posY[k]==posY[l]):
                #penularan virus
                if(stat_sehat[k]=='terinfeksi'):
                    if(stat_sehat[l]=='sehat' and stat_imun[k]=='belum memiliki imun'):
                        stat_sehat[k]='terinfeksi'
                elif(stat_sehat[l]=='terinfeksi'):
                    stat_sehat[k]='terinfeksi'
                    
        #correction of waktu_infeksi
        if (stat_sehat[k]=='terinfeksi'):
            if (waktu_infeksi[k] == waktuPulih) : 
                stat_sehat[k]='Pulih'
                stat_imun[k]='memiliki imun'
                nInfeksi-=1
                pulih+=1
            elif (waktu_infeksi[k]==0) : 
                waktu_infeksi[k]+=1
                nInfeksi+=1
            else :
                waktu_infeksi[k]+=1
                
        if (stat_sehat[k]=='terinfeksi'):
            posXsakit.append(x)
            posYsakit.append(y)
        elif (stat_sehat[k]=='sehat'):
            posXsehat.append(x)
            posYsehat.append(y)
        elif (stat_sehat[k]=='Pulih'):
            posXpulih.append(x)
            posYpulih.append(y)
        posX[k]=x
        posY[k]=y
    if (nInfeksi==0):
        conTerinfeksi = False     
    day += 1
    total_nIfeksi.append(nInfeksi)
    if day == 1:
        plt.title('(Day-'+str(day)+') Infected = '+str(nInfeksi))
    elif day>1:
        plt.title('(Day-'+str(day)+') Infected = '+str(nInfeksi)+' Recovered = '+str(pulih))

    plt.scatter(posXsakit, posYsakit, c="red")
    plt.scatter(posXpulih, posYpulih, c="grey")
    plt.scatter(posXsehat, posYsehat, c="blue")
    if exists('plot.png') and (day!=1):
      plt.savefig('plot{}.png'.format(int(day)))
    else:
      plt.savefig('plot.png')

    plt.show()
    
print('VIRUS OVER on'+' Day-'+str(day))
print('RECOVERED  '+str(pulih))


# In[ ]:





# In[ ]:




