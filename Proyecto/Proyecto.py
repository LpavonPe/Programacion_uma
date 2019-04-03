
# coding: utf-8

# In[1]:


#importación de modulos necesarios
import pandas as pd
import math
import random as rnd
import sys
from PyQt5 import uic, QtWidgets


# In[ ]:


pantalla proyecto.ui


# In[2]:


#Carga la base de datos en un df distinto por hoja para poder manipularlo
tiempo_vista_df=pd.read_excel("Base_de_datos.xlsx",sheet_name="Watch time")
fuente_trafico_df=pd.read_excel("Base_de_datos.xlsx",sheet_name="Traffic source")
tipo_rep_df=pd.read_excel("Base_de_datos.xlsx",sheet_name="Playback location")
demografia_df=pd.read_excel("Base_de_datos.xlsx",sheet_name="Demographics")


# In[4]:


qtCreatorFile = "pantalla proyecto.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): # Inicializa la pantalla
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Ambas.clicked.connect(self.info_pais)  #se asigna el boton a la función, segun el nombre de la función
        self.Suscriptores.clicked.connect(self.sus_ganados)
        self.Vistas.clicked.connect(self.tiempo_vista_dia)
        


    #Función que regresa el tiempo total de vista del canal por día dado.
    def tiempo_vista_dia(x):
        tiempo=0
        for i in range(len(tiempo_vista_df['Watch time (minutes)'])):
            if tiempo_vista_df['Date'] == x:
                tiempo+= tiempo_vista_df['Watch time (minutes)'][i]
        return tiempo
    #Función auxiliar que segmenta los datos por día dado
    def datos_dia(dia,mes,dia_final=0,mes_final=0):
        final=0
        inicio=0
        contador=0
        if mes_final ==0:
            mes_final=mes
        if dia_final ==0:
            dia_final=dia
        for i in range(len(tiempo_vista_df['Date'])):
            if tiempo_vista_df['Date'][i].month >= mes and tiempo_vista_df['Date'][i].month <= mes_final:
                if tiempo_vista_df['Date'][i].day >= dia and tiempo_vista_df['Date'][i].day <= dia_final:
                    final =i
                    contador+=1
        inicio=final-contador
        df_dia=tiempo_vista_df[inicio:final]
        return df_dia

    # Función que regresa en una lista  los paises en donde se vio el canal.
    def paises():
        paises_prev=[]
        for i in range(len(tiempo_vista_df['Geography'])):
            paises_prev.append(tiempo_vista_df['Geography'][i])
        paises_conj=set(paises_prev)
        paises=list(paises_conj)
        return paises

    # Función que regresa el pais donde se vio el canal por más minutos por día, rango de días
    def pais_minutos_dia(dia,mes,dia_final=0,mes_final=0):
        if dia_final == 0:
            dia_final == dia
        if mes_final == 0:
            mes_final == mes
        minutos=[]
        df_dia=datos_dia(dia,mes, dia_final, mes_final)
        for i in range(len(df_dia['Watch time (minutes)'])):
            minutos.append(df_dia['Watch time (minutes)'][i])
        maximo=df_dia['Geography'][maximo.index(max(maximo))]
        return maximo

    # Función que regresa el número de minutos totales, número de vistas o promedio de duración por vista del pais dado
    # en un día, rango de días , mes o rango de meses dados

    def info_pais(pais,dia,mes,minu=1,nvistas=0,prom=0,dia_final=0,mes_final=0):
            df_datos=datos_dia(dia,mes,dia_final,mes_final)
            if dia_final == 0:
                dia_final == dia
            if mes_final == 0:
                mes_final == mes
            numero="nd"
            promedio="nd"
            minutos="nd"
            if nvistas ==1:
                numero=0
                for i in range(len(df_datos["Views"])):
                    if df_datos["Geography"][i]== pais:
                        numero= numero + df_datos["Views"]
            if prom == 1:
                promedio=0
                for i in range(len(df_datos['Average view duration (minutes)'])):
                    if df_datos["Geography"][i]== pais:
                        promedio+= ddf_atos['Average view duration (minutes)']
            if minu == 1:
                minutos=0
                for i in range(len(datos['Watch time (minutes)'])):
                    if df_datos["Geography"][i]== pais:
                        minutos= minutos + df_datos['Watch time (minutes)']
            resultados=[]
            if numero != "nd":
                resultados.append(numero)
            if promedio != "nd":
                resultados.append(promedio)
            if minutos != "nd":
                resultados.append(minutos)
            return resultados

    #Función que dado un mes, regrese el día que más suscriptores se ganaron
    def sus_ganados(mes):
        indices=[]
        suscriptores=[]
        for i in range(len(tiempo_vista_df['Subscribers gained'])):
            if tiempo_vista_df['Date'][i].month == mes:
                suscriptores.append(tiempo_vista_df['Subscribers gained'][i])
                indices.append(i)
        indice_maximo=suscriptores.index(max(suscriptores))
        indice=indices[indice]
        maximo=tiempo_vista_df['Date'][indice]
        return maximo

    #Función que dado un mes, regresa los suscriptores que se perdieron
    def sus_perdidos(mes):
        indices=[]
        suscriptores=[]
        for i in range(len(tiempo_vista_df['Subscribers lost'])):
            if tiempo_vista_df['Date'][i].month == mes:
                suscriptores.append(tiempo_vista_df['Subscribers lost'][i])
                indices.append(i)
        if max(suscriptores) !=0:
            indice_maximo=suscriptores.index(max(suscriptores))
            indice=indices[indice]
            maximo=tiempo_vista_df['Date'][indice]
            return maximo
        else:
            print("No se perdieron suscriptores en el mes dado")

    #Esta funcion busca los paises y el numero de suscriptores
    def pais_suscriptores_mes(mes):
        diccionario = {}
        suscriptores = []
        for i in range(len(list(tiempo_vista_df["Date"]))):
            if tiempo_vista_df["Date"][i].month == mes:
                if tiempo_vista_df["Subscribers gained"][i] != 0:
                    if tiempo_vista_df["Geography"][i] in diccionario:
                        diccionario[tiempo_vista_df["Geography"][i]] += tiempo_vista_df["Subscribers gained"][i]
                    else: 
                        diccionario[tiempo_vista_df["Geography"][i]] = tiempo_vista_df["Subscribers gained"][i]
        for item in diccionario:
            print(f"{item} : {diccionario[item]}")
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


# In[21]:


tiempo_vista_df['Views']


# In[4]:


tiempo_vista_df.head()

