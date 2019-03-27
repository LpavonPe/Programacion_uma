
# coding: utf-8

# In[1]:


import math


# In[2]:


class circulo:
    def __init__(self,radio):
        self.radio=radio
        
    def area(self):
        area=(math.pi)*(self.radio**2)
        return area
        


# In[3]:


class grados:
    def __init__(self,centigrados):
        self.centigrados=centigrados
    
    def fahrenheit(self):
        far=self.centigrados*(9/5)+32
        return far
    
    def kelvin(self):
        kelv= self.centigrados + 273.15
        return kelv


# In[4]:


class caja:
    def __init__(self, largo, alto, ancho):
        self.largo=largo
        self.alto=alto
        self.ancho=ancho
    
    def volumen(self):
        vol=self.largo*self.ancho*self.alto
        return vol
    
    def perimetro(self):
        per=(self.largo*4)+(self.ancho*4)+(self.largo*4)
        return per
    def area_sup(self):
        area=((self.largo*self.ancho)*2)+((self.largo*self.alto)*2)+((self.ancho*self.alto)*2)
        return area


# In[5]:


class calculadora:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    
    @a.setter
    def a(self,value):
        if type(value)!=int:
            raise ValueError("Los atributos deben ser enteros")
        self._a=value
    
    @b.setter
    def b(self,value):
        if type(value)!=int or b==0:
            raise ValueError("Los atributos deben ser enteros y distintos de 0")
        self._b=value
    
    def suma(self):
        return self.a+self.b
    def resta(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b


# In[25]:


class IPM_Tech:
    def __init__(self,nombre, num_empleado,edad,edo_civil,salario):
        self.nombre=nombre
        self.num_empleado=num_empleado
        self.edad=edad
        self.edo_civil=edo_civil
        self.salario=salario
        
    @property
    def nombre(self):
        return self._nombre
    @property
    def num_empleado(self):
        return self._num_empleado
    @property
    def edad(self):
        return self._edad
    @property 
    def edo_civil(self):
        return self._edo_civil
    @property
    def salario(self):
        return self._salario
    
    @nombre.setter
    def nombre(self,value):
        if type(value)!= str:
            raise ValueError("El nombre debe ser string")
        self._nombre=value
        
    @num_empleado.setter
    def num_empleado(self,value):
        if type(value)!= str:
            raise ValueError("El numero de empleado debe ser string")
        self._num_empleado=value 
    @edad.setter
    def edad(self,value):
        if type(value)!=int:
            raise ValueError("La edad debe ser un número entero")
        if value<18 or value>45:
            raise ValueError("El empleado debe tener entre 18 y 45 años")
        self._edad=value
    @edo_civil.setter
    def edo_civil(self,value):
        if type(value)!= str:
            raise ValueError("El estado civil debe ser string")
        self._edo_civil=value
    @salario.setter
    def salario(self,value):
        if type(value)!= int:
            raise ValueError("El salario debe ser un número entero")
        self._salario=value
    def clasificacion(self):
        if self.edad <= 21:
            return ("Principiante")
        elif self.edad <= 35:
            return("Intermedio")
        else:
            return ("Senior")


# In[32]:


class administrativos(IPM_Tech):
    def __init__(self,nombre,edad,salario,num_empleado,puesto,antiguedad):
        IMP_Tech.__init__(self,nombre,edad,salario,num_empleado)
        self.puesto=puesto
        self.antiguedad=antiguedad

class vendedor(IPM_Tech):
    def __init__(self,nombre,edad,salario,num_empleado,ventas_mensuales,objetivo_ventas):
        IMP_Tech.__init__(self,nombre,edad,num_empleado)
        self.ventas_mensuales=ventas_mensuales
        self.objetivo_ventas=objetivo_ventas

class becario(IPM_Tech):
    def __init__(self,nombre,edad,salario,num_empleado,escuela,semestre):
        IMP_Tech.__init_(self,nombre,edad,salario,num_empleado)
        self.escuela=escuela
        self.semestre=semestre
class obrero(IPM_Tech):
    def __init__(self,nombre,edad,salario,num_empleado,turno,renovacion):
        IMP_Tech.__init__(self,nombre,edad,salario,num_empleado)
        self.turno=turno
        self.renovacion=renovacion
    


# In[69]:


class producto:
    def __init__(self,fecha_caducidad,num_lote):
        self.fecha_caducidad=fecha_caducidad
        self.num_lote=num_lote
class producto_fresco(producto):
    def __init__(self,fecha_caducidad,num_lote,fecha_envasado,pais_origen):
        producto.__init__(self,fecha_caducidad,num_lote)
        self.fecha_envasado=fecha_envasado
        self.pais_origen=pais_origen

class producto_refrigerado(producto_fresco):
    def __init__(self,fecha_caducidad,num_lote,fecha_envasado,pais_origen,codigo_organismo,temperatura):
        producto_fresco.__init__(self,fecha_caducidad,num_lote,fecha_envasado,pais_origen)
        self.codigo_organismo=codigo_organismo
        self.temperatura=temperatura
class producto_congelado(producto_fresco):
    def __init__(self,fecha_caducidad,num_lote,fecha_envasado,pais_origen,temperatura):
        producto_fresco.__init__(self,fecha_caducidad,num_lote,fecha_envasado,pais_origen)
        self.temperatura=temperatura


# In[57]:


def archivo(x):
    if type(x)!= str:
        raise ValueError("La función solo acepta strings")
    if "archivo" in dir
    with open("archivo.txt",mode="w") as f:
        f.write(x)


# In[56]:


cuento= open ("Cuento.txt",mode="r+")
x=cuento.read()
cuento.close()
x.lower()
a=0
e=0
i=0
o=0
u=0
for j in x:
    if j =="a" or j== "á":
        a+=1
    elif j=="e" or j=="é":
        e+=1
    elif j =="i" or j=="í":
        i+=1
    elif j =="o" or j== "ó":
        o+=1
    elif j =="u" or j=="ú":
        u+=1
print(" a= ",a,"\n","e= ",e,"\n","i= ",i, "\n", "o= ",o,"\n","u= ",u)

