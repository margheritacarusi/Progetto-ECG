
# coding: utf-8

# In[10]:

import numpy as np
get_ipython().system(u'pip install biosppy ')
from biosppy.signals import ecg
import csv
import scipy

with open('samples.csv') as csvfile:                    #apro file csv contenente i campioni del segnale presi da physionet 
    readCSV = csv.reader(csvfile, delimiter=',')

    ecg_samples = list()                 #creo liste (ecg_ordinatae tempo_ascissa)
    tempo = list()

    for row in readCSV:                       # con un ciclo for richiamo tutti i valori contenuti nel file exel (samples)
        tempo.append(float(row[0]))
        ecg_samples.append(float(row[1]))
 
    #calcolo frequenza campionamento che mi serve nella funzione out (già implementate)
    Tc = tempo[2]-tempo[1]
    fc = 1/Tc

    out = ecg.ecg(signal=ecg_samples, sampling_rate= fc, show=True)   # identifico picchi R 


# In[ ]:




# In[ ]:



