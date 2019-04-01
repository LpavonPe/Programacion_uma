
# coding: utf-8

# In[29]:


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# In[30]:


def cargar_base(x,hojas=1):
    if hojas!= 1:
        if hojas == 2:
            order_df=pd.read_excel(x,sheet_name="Orders")
            returns_df=pd.read_excel(x, sheet_name="Returns")
            return order_df
        if hojas == 3:
            order_df=pd.read_excel(x,sheet_name="Orders")
            returns_df=pd.read_excel(x, sheet_name="Returns")    
            people_df=pd.read_excel(x,sheet_name="People")
            return order_df, returns_df, people_df
        elif hojas>3:
            raise ValueError("El documento solo tiene tres hojas")
    else:
        order_df=pd.read_excel(x,sheet_name="Orders")
        return order_df


# In[31]:


datos=cargar_base("Sample - Superstore.xls")


# In[32]:


def state():
    if "datos" in dir():
        order_df=datos
    else:
        order_df=cargar_base("Sample - Superstore.xls")
    state_list=[]
    for i in range(len(order_df['State'])):
        state_list.append(order_df['State'][i])
    return state_list


# In[33]:


def num_pedidos(x):
    if "datos" in dir():
        order_df=datos
    else:
        order_df=cargar_base("Sample - Superstore.xls")
    state_list=[]
    clientes_lista=[]
    num=0
    for i in range(len(order_df["Customer Name"])):
        if order_df["Customer Name"][i] == x:
            num+=1
    return num
    


# In[63]:


def clientes_ciudad(x):
    if "datos" in dir():
        order_df=datos
    else:
        order_df=cargar_base("Sample - Superstore.xls")
    clientes_prev=[]
    for i in range(len(order_df['City'])):
        if order_df['City'][i] == x:
            clientes_prev.append(order_df['Customer Name'][i])
        set_clientes=set(clientes_prev)
        clientes=list(set_clientes)
    return clientes


# In[35]:


def category(x):
    if "datos" in dir():
        order_df=datos
    else:
        order_df=cargar_base("Sample - Superstore.xls")
    Customer_Name_prev=[]
    Customer_ID_prev=[]
    State_prev=[]
    City_prev=[]
    for i in range(len(order_df['Category'])):
        if order_df['Category'][i] == x:
            Customer_Name_prev.append(order_df['Customer Name'][i])
            Customer_ID_prev.append(order_df['Customer ID'][i])
            State_prev.append(order_df['State'][i])
            City_prev.append(order_df['City'][i])
    con_Customer_Name=set(Customer_Name_prev)
    con_Customer_ID=set(Customer_ID_prev)
    con_State=set(State_prev)
    con_City=set(City_prev)
    Customer_Name=list(Customer_Name_prev)
    Customer_ID=list(Customer_ID_prev)
    State=list(State_prev)
    City=list(City_prev)
    datos_exl={"Customer ID":Customer_ID,"Customer Name":Customer_Name,"State":State,"City":City}
    datos_df=pd.DataFrame(data=datos_exl)
    with pd.ExcelWriter("Resultado.xls") as ex:
        datos_df.to_excel(ex,sheet_name="Hoja1")
    

