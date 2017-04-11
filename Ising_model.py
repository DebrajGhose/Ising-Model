# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:01:54 2017

@author: dg144
"""

#Ising model


from pylab import *

seed()
 

def calculate_local_energy(M, size, J, i, j):
    
    local_energy = -J*M[i,j]*(   M[(i-1)%size,j] + M[(i+1)%size,j] + M[i,(j-1)%size] + M[i,(j+1)%size]  ) 
    
    return local_energy



#simulation parameters

global M, size, J, i, j, E


size = 40
J = 1


M = random((size,size)) #M is the matrix containing all the electron spin values

#set up electron spin values

M[M>0.5] = 1
M[M<0.5]=-1


plt.figure(1)

imshow(M,interpolation = 'none')

#calculate total energy of the system

E = 0 #energy

for i in range(0,size):
    
    for j in range(0,size):
        
        local_energy = calculate_local_energy(M, size, J, i, j)
        
        E = E + local_energy
        
E = E/2 #divide by 2 to account for all repeated pairs
        
print 'Total starting energy is %f' %(E)

#step through all pixels and flip spins

for time in range(1,1000000):
    
    #assign random index values to i and j
    
    i = int(round(rand()*(size-1))); j = int(round(rand()*(size-1)))
    
    #flip spin
    
    olde = calculate_local_energy(M, size, J, i, j) #enerpy before flipping
    
    M[i,j] = M[i,j]*-1
    
    newe = calculate_local_energy(M, size, J, i, j) #energy after flipping
    
    #if energy does not get lowered, flip it back to original state

    if newe > olde:
        
        M[i,j] = M[i,j]*-1

    #if the spin did change,  update total energy

    else:
        
        E = E - olde + newe #do a quick calculation of total energy by subtracting old energy and adding new
                
            
            


    print E
    

            
     
plt.figure(2)
   
imshow(M,interpolation = 'none')


