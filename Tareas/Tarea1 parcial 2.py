
# coding: utf-8

# In[3]:


def triangulo(a,b,c):
    if a==c and b==c:
        print("Equilátero")
    elif a==c and b!=c or b==c and a!=c or a==b and a!=c:
        print("Isoceles")
    else:
        print("Escaleno")


# In[16]:


def bono(x):
    if x>0:
        bono=0
        if x<1000:
            return .01
        elif x>=1000 and x<4000:
            return .03
        elif x>=4000 and x<8000:
            return .05
        elif x>=8000:
            return.07
    else:
        return("El monto debe ser positivo")


# In[31]:


def vocales(x):
    if type(x) ==str:
        x.lower()
        na=0
        ne=0
        ni=0
        no=0
        nu=0
        ls=list(x)
        for i in ls:
            if i=="a":
                na+=1
            elif i=="e":
                ne+=1
            elif i =="i":
                ni+=1
            elif i =="o":
                no+=1
            elif i =="u":
                nu+=1
    print("a:",na,"\n", "e:",ne,"\n","i:",ni,"\n","o:",no,"\n","u:",nu)


# In[46]:


def multiplo(n,m):
    if n%m ==0:return True


# In[52]:


def suma_cuadrados(x):
    suma=0
    for i in range(x+1):
        suma+=i**2
    return suma


# In[8]:


def repetidos(x):
    x.sort()
    rep=0
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            rep=1
    if rep==1:
        return True
    else:
        return False
    


# In[77]:


def factorial(x):
    fact=1
    if x==0:
        return 1
    elif x<0:
        return("El factorial para números negativos no esta definido")
    elif x>0:
        for i in range(1,x+1):
            fact=fact*i
        return fact


# In[80]:


def unidad(x):
    if x//10 ==0:
        return True
    else:
        return False


# In[84]:


def area_poligono(n_lados,m_lado,apotema):
    perimetro=n_lados*m_lado
    area=(perimetro*apotema)/2
    return area


# In[29]:


def valida(x):
    xlist=list(x)
    m_err="Contraseña Invalida"
    if len(xlist)<6 or len(xlist)>12:
        return(m_err)
    else:
        n_mayus=0
        for i in xlist:
            if i.isupper() == True:
                n_mayus+=1
        if n_mayus<2:
            return(m_err)
        else:
            n_num=0
            for i in xlist:
                if i.isnumeric() ==True:
                    n_num+=1
            if n_num<2:
                return(m_err)
            else:
                esp=["!", "#","$","%","&","@"]
                n_esp=0
                for i in xlist:
                    if i in esp:
                        n_esp+=1
                if n_esp<1:
                    return(m_err)
                else:
                    return("Contraseña Valida")

