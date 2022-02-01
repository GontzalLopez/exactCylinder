#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:02:19 2022

@author: gontzal
"""

import numpy as np
import matplotlib.pyplot as plt

Vin=2;
alpha=0;
Tau=np.pi;
Pi=np.pi;
R=0.5;

L=300
x=np.linspace(-1, 1, num=L);
y=np.linspace(-1, 1, num=L);

Y,X = np.meshgrid(y,x);

r=np.sqrt(X**2+Y**2);

u=Vin*np.cos(alpha)-(((X[:,:]**2-Y[:,:]**2)*np.cos(alpha)+2*X[:,:]*Y[:,:]*np.sin(alpha))/(r[:,:]**4))*Vin*(R**2)+(Y[:,:]*Tau)/(2*Pi*(r[:,:]**2));

v=Vin*np.sin(alpha)+(((X[:,:]**2-Y[:,:]**2)*np.sin(alpha)-2*X[:,:]*Y[:,:]*np.cos(alpha))/(r[:,:]**4))*Vin*(R**2)-(X[:,:]*Tau)/(2*Pi*(r[:,:]**2));

Cp=1-(u**2+v**2)/Vin;

for i in range(L):
    for j in range(L):
        if(np.sqrt(X[i,j]**2+Y[i,j]**2)<R):   
            u[i,j]=np.nan;
            v[i,j]=np.nan;
            Cp[i,j]=np.nan;
    
fig,ax=plt.subplots(1,1)

N=250;
cp = ax.contourf(X, Y, Cp,N, cmap="viridis")
cbar=fig.colorbar(cp) # Add a colorbar to a plot
cbar.set_label('Pressure Coeff. Cp')
#ax.contour(X,Y,Cp)
skip=(slice(None,None,8),slice(None,None,8))
quiv = ax.quiver(X[skip], Y[skip], u[skip], v[skip],color='black')

#ax.set_title('Filled Contours Plot')
#ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_aspect('equal')


plt.show()

