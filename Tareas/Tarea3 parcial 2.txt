import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def cargar_base(x):
with pd.ExcelWriter(x) as ex:
order_df.to_excel(ex,sheet_name="Orders")
returns_df.to_excel(ex, sheet_name="Returns")
people_df.to_excel(ex,sheet_name="People")
return order_df, returns_df, people_df

def state(x):
if x == order_df:

state_list=[]
    for i in range(len(x['State'])):
    	state_list.append(x['State'][i])
return state_list

def num_pedidos(x):
if "order_df" in dir:
clientes_lista=[]
num=0
for i in range(len(order_df["Customer Name"])):
 if order_df["Customer Name])) == x:
		num+=1
return num
else:
raise ValueError("No se ha cargado la base de datos, usar la función cargar_base(nombre de la base de datos) para cargarla")

def clientes_ciudad(x):
if "order_df" in dir:
clientes_prev=[]
    for i in range(len(order_df['State'])):
    	if order_df['State'][i] == x:
		clientes_prev.append(order_df['Customer Name'][i])
set_clientes=set(clientes_prev)
clientes=list(set_clientes)
return clientes
else
raise ValueError("No se ha cargado la base de datos , usar la función cargar_base(nombre de la base de datos) para cargarla")

def category(x):
if "order_df" in dir:
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

datos={"Customer ID":Customer_ID,"Customer Name":Customer_Name,"State":State,"City":City}
datos_df=pd.DataFrame(data=datos)
with pd.ExcelWriter("Resultado.xls") as ex:
       datos_df.to_excel(ex,sheet_name="Hoja1")
else
raise ValueError("No se ha cargado la base de datos, usar la función cargar_base(nombre de la base de datos) para cargarla")