# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:01:54 2017

@author: dg144
"""

#Ising model


from pylab import *

def calculate_total_energy_fast():
    
    global M, size, J, i, j, E
    
    #calculate old local energies of neighbors
    
    l1o = calculate_local_energy(M,size,J,i,j)
    l2o = calculate_local_energy(M,size,J,(i-1)%size,j)
    l3o = calculate_local_energy(M,size,J,(i+1)%size,j)
    l4o = calculate_local_energy(M,size,J,i,(j-1)%size)
    l5o = calculate_local_energy(M,size,J,i,(j+1)%size)
    
    Eo = l1o + l2o + l3o + l4o + l5o 
    
    M[i,j] = M[i,j]*-1 #switch to new configuration
    
    #calculate new local energies of neighbors

    l1n = calculate_local_energy(M,size,J,i,j)
    l2n = calculate_local_energy(M,size,J,(i-1)%size,j)
    l3n = calculate_local_energy(M,size,J,(i+1)%size,j)
    l4n = calculate_local_energy(M,size,J,i,(j-1)%size)
    l5n = calculate_local_energy(M,size,J,i,(j+1)%size)
    
    En = l1n + l2n + l3n + l4n + l5n
    
    #Calculate total energy
    
    E = E - Eo + En
    
    

                
    
    

def calculate_local_energy(M, size, J, i, j):
    
    local_energy = -J/2*M[i,j]*(   M[(i-1)%size,j] + M[(i+1)%size,j] + M[i,(j-1)%size] + M[i,(j+1)%size]  ) #divide by 2 to account for double pair sets
    
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

for i in range(1,size):
    
    for j in range(1,size):
        
        local_energy = calculate_local_energy(M, size, J, i, j)
        
        E = E + local_energy
     
        
print 'Total starting energy is %f' %(E)


#step through all pixels and flip spins

for time in range(1,100):
    
    for i in range(1,size):
    
        for j in range(1,size):
            
            #flip spin
            
            ini_le = calculate_local_energy(M, size, J, i, j) #enerpy before flipping
            
            M[i,j] = M[i,j]*-1
            
            fi_le = calculate_local_energy(M, size, J, i, j) #energy after flipping
            
            #if energy does not get lowered flip it back to original state

            if fi_le > ini_le:
                
                M[i,j] = M[i,j]*-1

            #if the spin did change,  update total energy

            else:
                
                M[i,j] = M[i,j]*-1 #revert just to see local old energies
                
                calculate_total_energy_fast() #do a quick calculation of total energy
                
            
            


    print E
    

            
     
plt.figure(2)
   
imshow(M,interpolation = 'none')


