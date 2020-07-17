#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import IFrame
from jupyterthemes import jtplot


# In[10]:


jtplot.style(theme='monokai')


# In[2]:


plt.rc('font',size=14)
plt.rc('figure',figsize=(8,6))
plt.rc('text', usetex=True)


# lo que me pregunto es qué tan mal estaba el voumen. efectivamente los cambios de parametro de red son demasiado pequeños y estan pasando cosas raras.
# Notar que hay cambios de pendiente para a = 1.005

# In[3]:


datavol = pd.read_csv('datavol.dat', sep=' ')


# In[4]:


datavol


# In[17]:


fig, ax = plt.subplots(1,2, figsize=(15,8))
ax[0].plot(datavol['Vol'], datavol['Evsk1'],'-o', label='9x9x7', ms=10)
ax[0].plot(datavol['Vol'], datavol['Evsk2'],'-o', label='11x11x9',ms=8)
ax[0].plot(datavol['Vol'], datavol['Evsk3'],'-o', label='13x13x11', ms = 6)
ax[0].plot(datavol['Vol'], datavol['Evsk4'],'-o', label='15x15x9', ms=4)
ax[0].plot(datavol['Vol'], datavol['Evsk5'],'-o', label='17x17x9', ms=2)
ax[0].legend()
for i in datavol.index:
    ax[1].plot(datavol.loc[i][2:]-datavol.loc[i][-1],'-o',label=datavol.loc[i][0])
ax[1].legend()
ax[0].set_xlabel(r'cell vol ($\AA$)')
ax[0].set_ylabel('E (eV)')
ax[1].set_ylabel(r'$\Delta E (eV)$')
plt.savefig('datavol.pdf')


# In[44]:


datavol[datavol['dir']=='ZrO2-new-00'].as_matrix()[0,1:]


# el volumen de minima energía es:

# In[12]:


# vopt = datavol['Vol'][datavol['evsk4'].dimin()]
vopt=datavol['Vol'][datavol['Evsk4'].idxmin()]


# In[13]:


vopt


# # Estructura de bandas con calculo bueno

# In[14]:


IFrame('more_useful_data.txt',width=600, height=800)


# In[15]:


databands = pd.read_csv('more_useful_data.txt',sep='#') 


# In[16]:


databands


# ## masa del electron

# In[17]:


m_e = databands[(databands['mass']=='m_e')]
m_e_gx_up = m_e[(m_e['toname']=='(X)') & (m_e['spin']=='(up)')]
m_e_gx_dn = m_e[(m_e['toname']=='(X)') & (m_e['spin']=='(down)')]
m_e_gz_up = m_e[(m_e['toname']=='(Z)') & (m_e['spin']=='(up)')]
m_e_gz_dn = m_e[(m_e['toname']=='(Z)') & (m_e['spin']=='(down)')]


# ### electron en el camino $\Gamma \rightarrow Z$, spin down

# In[18]:


m_e_gz_dn


# ### spin up

# In[19]:


m_e_gz_up


# notar que en este camino la masa para espin down es 10 veces mayor que con spin down.

# ## electron camino $\Gamma \rightarrow X$

# ### spin up

# In[20]:


m_e_gx_up


# ### spin down

# In[21]:


m_e_gx_dn


# En este camino, ambas masas (up y down) son iguales.

# ### gráficos para electron

# In[28]:


fig, ax = plt.subplots(2,1, sharex=True)
ax[0].set_title('conduction band')
ax[0].plot(m_e_gx_up['Vol'], m_e_gx_up['value'],'-o', label=r'up, $ \Gamma \rightarrow X$')
ax[0].plot(m_e_gx_dn['Vol'], m_e_gx_dn['value'],'-o', label=r'down, $ \Gamma \rightarrow X$')
#ax[0].plot(m_e_gz['Vol'], m_e_gz['value'],'-o', label=r'$ \Gamma \rightarrow Z$')
ax[1].plot(m_e_gz_up['Vol'], m_e_gz_up['value'],'-o', label=r'up, $ \Gamma \rightarrow Z$')
ax[1].plot(m_e_gz_dn['Vol'], m_e_gz_dn['value']/10,'-o', label=r'down, $\times \frac{1}{10}, \Gamma \rightarrow Z$')
ax[1].set_xlabel(r'$a(\AA)$', fontsize=18)
ax[0].axvline(vopt,c='k')
ax[1].axvline(vopt,c='k')
ax[0].set_ylabel( r'$m^* (\hbar / m_e)$', fontsize=18)
ax[0].legend()
ax[1].legend()


# # masas del hueco

# la masa del hueco tiene un comportamiento mas raro. para empezar, esta desdoblada en dos bandas segun la direccion. 

# In[29]:


m_h = databands[(databands['mass']=='m_h')]
# m_h = databands[(databands['fname']=='(gamma)') & (databands['toname']=='(X)') & (databands['spin']=='(up)')]


# In[30]:


m_h_za = databands[(databands['mass']=='m_h') & (databands['toname']=='(A)')]
m_h_zr = databands[(databands['mass']=='m_h') & (databands['toname']=='(R)')]
m_h_tz = databands[(databands['mass']=='m_h') & (databands['toname']=='(Z)')]
m_h_fz = databands[(databands['mass']=='m_h') & (databands['fname']==' (Z)')]


# In[32]:


m_h


# ## Hueco en el camino $Z \rightarrow A$

# In[31]:


m_h_za


# ### En el camino $A \rightarrow R$

# In[327]:


m_h_zr


# In[ ]:





# In[328]:


m_h_tz


# In[331]:


m_h_fz


# todos los valores que puse ahi estan $v < v_{eq}$, que pasa arriva ?

# In[334]:


m_h_vbig = databands[(databands['Vol']>vopt) & (databands['mass']=='m_h')]


# In[335]:


m_h_vbig


# In[ ]:





# es curioso que para volumenes grandes, el máximo de la banda de valencia se corre de $Z$ a $[0.33, 0, 0 ]$ !

# In[33]:


IFrame('ZrO2-new-05/BANDSdir/ZrO2-new-05_band.pdf',width=800, height=300)


# In[344]:



IFrame('ZrO2-new-06/BANDSdir/ZrO2-new-06_band.pdf',width=400, height=300)


# In[346]:



IFrame('ZrO2-new-07/BANDSdir/ZrO2-new-07_band.pdf',width=400, height=300)


# In[347]:



IFrame('ZrO2-new-10/BANDSdir/ZrO2-new-10_band.pdf',width=400, height=300)

