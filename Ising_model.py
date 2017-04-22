# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:01:54 2017

@author: dg144
"""

#Ising model


from pylab import *

seed()
    
  
def calculate_local_energy( size, J, i, j):
    
    global M
    
    local_energy = -J*M[i,j]*(   M[(i-1)%size,j] + M[(i+1)%size,j] + M[i,(j-1)%size] + M[i,(j+1)%size]  ) 
    
    return local_energy


    
    
#simulation parameters

global M

size = 10 #pick a size of grid

numberofsims = 30

avgMag = [0.0]*numberofsims #average magnetization for given T
avgE = [0.0]*numberofsims #average energy for given T

for runnumber in range(0,numberofsims):
    
    T = runnumber/(numberofsims-1.0)*5.0 + 1#pick a temperature between 0 and 4
    
    snapshottime = size**2 #take snapshots that are uncorrelated
    
    average_count = 0 #reset the average weighting
    
    J = 1.5
    
    M = random((size,size)) #M is the matrix containing all the electron spin values
    
    #set up electron spin values based on some threshhold
    
    M[M>=0.1] = 1
    M[M<0.1]=-1
    
    
    #calculate total energy of the system
    
    E = 0 #energy
    
    for i in range(0,size):
        
        for j in range(0,size):
            
            local_energy = calculate_local_energy( size, J, i, j)
            
            E = E + local_energy
            
    E = E/2 #divide by 2 to account for all repeated pairs
    
    Mag = sum(M) 
    
    print T       
    
    #step through all pixels and flip spins
    
    for time in range(1,100000):
        
        #Pick out points at random and see what the local energy is. Flip the spin at the location and recalculate that energy.
        #If the flipped one has a lower energy, keep it. If it has a higher energy, flip it back with a certain probability
        
        #pick some point on the matrix at random
        
        i = int(round(rand()*(size-1))); j = int(round(rand()*(size-1)))
        
        #see what old energy is
        
        olde = calculate_local_energy( size, J, i, j) #calculate energy
        
        #flip spin and calculate energy
        
        M[i,j] = - M[i,j]
    
        newe = calculate_local_energy( size, J, i, j) #calculate energy
        
        energy_change = newe-olde
    
        #flip spin back
        
        M[i,j] = -M[i,j]
        
        
        #see if you want to keep the flipped version
        
        
        if energy_change <= 0: 
        
            #reaching a lower state will always flip spin
            
            M[i,j] = -M[i,j]

            E = E + energy_change
            
            Mag = Mag + 2*M[i,j] #Mag + M[i,j] - (-M[i,j])
        
        
        elif exp(-energy_change/T) > rand():
            
            #see if temperature fluctuations can flip spin
            
            M[i,j] = -M[i,j]

            E = E + energy_change
            
            Mag = Mag + 2*M[i,j]
          
    
        

        if time%100==0 and time > 5000:
            
            #notice that these calculations happen after some burn-in has taken place
            
            avgE[runnumber] = (avgE[runnumber]*average_count + E)/(average_count+1)
            
            avgMag[runnumber] = (avgMag[runnumber]*average_count + Mag)/(average_count+1)
            
            average_count = average_count + 1 #weighted average
    
    avgMag[runnumber] = abs(avgMag[runnumber])
    #plt.figure(2)
    #plot(avgMag)   
    #imshow(M,interpolation = 'none')


