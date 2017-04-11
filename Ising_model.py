# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:01:54 2017

@author: dg144
"""

#Ising model


from pylab import *

def calculate_total_energy():
    
    global M, size, J, i, j, E
    
    
    
    

def calculate_local_energy(M, size, J, i, j):
    
    local_energy = -J/2*M[i,j]*(   M[(i-1)%size,j] + M[(i+1)%size,j] + M[i,(j-1)%size] + M[i,(j+1)%size]  ) #divide by 2 to account for double pair sets
    
    return local_energy



#simulation parameters

global M, size, J, i, j, E


size = 5
J = 1


M = random((5,5)) #M is the matrix containing all the electron spin values

#set up electron spin values

M[M>0.5] = 1
M[M<0.5]=-1

plt.figure(1)

imshow(M,interpolation = 'none')

#calculate total energy of the system

E = 0 #energy

for i in range(1,size):
    
    for j in range(1,size):
        
        local_energy = calculate_local_energy(M, size, J, i, j)
        
        E = E + local_energy
     
        
print 'Total starting energy is %f' %(E)


#step through all pixels and flip spins

for time in range(1,1000):
    
    for i in range(1,size):
    
        for j in range(1,size):
            
            #flip spin
            
            ini_le = calculate_local_energy(M, size, J, i, j) #enerpy before flipping
            
            M[i,j] = M[i,j]*-1
            
            fi_le = calculate_local_energy(M, size, J, i, j) #energy after flipping
            
            #if energy does not get lowered flip it back to original state

            if fi_le > ini_le:
                
                M[i,j] = M[i,j]*-1
            


    #calculate total energy
    
    

            
     
plt.figure(2)
   
imshow(M,interpolation = 'none')


