# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:24:14 2021

@author: marti
"""
import pandas as pd
from datetime import datetime
import streamlit as st
import disc_help as dh
import numpy as np
from matplotlib.pyplot import bar 

data = pd.read_csv('https://docs.google.com/spreadsheets/d/1e8-6hwMTMTRcjGNROmV426hQwebfuF14ugcK5J_9sos/export?format=csv')
#numerodatistart = data.shape[0]
#second = datetime.now().strftime("%S")

st.dataframe(data)
#REALTIME
#while True:
#    print(numerodatistart)
#    second_before = datetime.now().strftime("%S")
#    if second != second_before:
#        second = second_before
#        data = pd.read_csv('https://docs.google.com/spreadsheets/d/1e8-6hwMTMTRcjGNROmV426hQwebfuF14ugcK5J_9sos/export?format=csv')
#        numerodatistart = data.shape[0]
#        if numerodatistart==4:
#            break

st.title("D.I.S.C.")
st.write("Car* grazie per utilizzare questo tool per capire meglio la tua personalità. Di seguito alcuni step fondamentali per la creazione del tuo punteggio DISC")

st.title("Compila il questionario")
st.write("Compila il questionario al seguente [link] https://forms.gle/rfSKMvMyKNx8uojd7, immetti un nome utente unico (la tua mail)")
usermail = st.text_input("per favore inserisci la stessa mail inserita nel form che hai compilato")
data
indice = np.where(data["EMAIL"].str.contains(usermail))[0]
indice
data_singola = data.iloc[indice,:]
valori = dh.disc_help(data_singola)
valori = np.array(valori)

indici_d = np.array([2,10,18,6,14,22]).astype(int)
D = np.sum(valori[indici_d])/2

indici_i = np.array([1,9,17,5,13,21]).astype(int)
I = np.sum(valori[indici_i])/2

indici_s = np.array([3,11,19,7,14,22]).astype(int)
S = np.sum(valori[indici_s])/2

indici_c = np.array([0,8,16,4,12,20]).astype(int)
C = np.sum(valori[indici_c])/2

df  =pd.DataFrame([[D,I,S,C]],columns=["D","I","S","C"]).transpose()
df = df.rename(columns = {0: 'PERCENTUALE'})

import plotly.express as px
infocolori = dh.informazioni_colori()
df = pd.concat([df,pd.Series(infocolori,index=df.index)],axis=1)
df = df.rename(columns = {0: 'DESCRIZIONE'})

#st.dataframe(df)
fig = px.bar(df,y="PERCENTUALE",color=df.index,color_discrete_sequence=["red", "yellow", "green","blue"],hover_name="PERCENTUALE")

st.plotly_chart(fig)


if sum(df.PERCENTUALE == np.max(df.PERCENTUALE))==1:
    st.write("Descrizione carattere " + ["rosso", "giallo", "verde","blue"][np.argmax(df.PERCENTUALE)])
    st.write(infocolori[np.argmax(df.PERCENTUALE)])
else:
    indici_a = np.where(df.PERCENTUALE == np.max(df.PERCENTUALE))
    for i in indici_a[0]:
        st.write("Descrizione carattere " + ["rosso", "giallo", "verde","blue"][i])
        st.write(infocolori[i])
