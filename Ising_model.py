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

#for size in [50]: #this is for part A of the question

for size in [5, 10, 20, 30, 40, 50, 75, 100, 200, 500]:
    
    microstates = size*size #total number of cells in the grid
    Temperatures = [ 1.5, 2.0, 3.0, 3.1, 3.3, 3.35, 3.45, 3.5, 3.55, 3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9, 3.95, 4 , 4.05, 4.1, 4.15, 4.25, 4.3, 4.5, 4.7, 5.0 , 5.5, 6.0 , 7.0 , 8.0, 9.0]
    
    snapshottime = size**2 #start collecting data after this burn in period
        
    numberofsims = len(Temperatures)
    
    #initialize arrays to store stuff
    
    avgMag = [0.0]*numberofsims #average magnetization for given T
    avgE = [0.0]*numberofsims #average energy for given T
    arraySH = [0.0]*numberofsims #specific heat array
    arraySus = [0.0]*numberofsims #susceptibility
    
    
    
    
    for runnumber in range(0,numberofsims):
        
        average_count = 0 #reset the average weighting for each new temperature
        
        
        T = Temperatures[runnumber]
    
        print T
    
            
        #initialize your matrix
        
        J = 1.5
        
        M = random((size,size)) #M is the matrix containing all the electron spin values
        
        #set up electron spin values based on some threshhold
        
        M[M>=0.001] = 1
        M[M<0.001]=-1
        
        #calculate total energy of the system
        
        E = 0 #energy
        
        
        for i in range(0,size):
            
            for j in range(0,size):
                
                local_energy = calculate_local_energy( size, J, i, j)
                
                E = E + local_energy
                
        E = E/2 #divide by 2 to account for all repeated pairs
        
        Mag = sum(M) #calculate magnetization
        
        E2 = J**2 #mean squared energy of pairs. 2*N^2 pairs * J^2/(2*N^2 pairs)
        
        Mag2 = 1.0 #mean squared magnetization
        
        #step through all pixels and flip spins
        
        for time in range(1,snapshottime + 10000*size):
            
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
            
            
            #see if you want to keep the flip
            
            
            if energy_change <= 0: 
            
                #reaching a lower state will always flip spin
                
                M[i,j] = -M[i,j]
    
                E = E + energy_change #update energy
                
                Mag = Mag + 2*M[i,j] #Mag + M[i,j] - (-M[i,j]) -- update Magnetization 
                
            
            
            elif exp(-energy_change/T) > rand():
                
                #see if temperature fluctuations can flip spin
                
                M[i,j] = -M[i,j]
    
                E = E + energy_change #update energy
                
                Mag = Mag + 2*M[i,j]
              
        
            
    
            if time%(size)==0 and time > snapshottime:
                
                #notice that these calculations happen after some burn-in has taken place
                
                avgE[runnumber] = (avgE[runnumber]*average_count + E/(2*microstates) )/(average_count+1)
                
                avgMag[runnumber] = (avgMag[runnumber]*average_count + abs(Mag/microstates))/(average_count+1) 
                
                average_count = average_count + 1 #weighted average
        
        
        
        arraySH[runnumber] = (E2 - avgE[runnumber]**2 ) /T**2
        arraySus[runnumber] = (Mag2 - avgMag[runnumber]**2)/T**2
    
    
    
    plt.figure()
    name1 = 'E' + '_' + str(size)
    np.save(name1, avgE)
    plot(Temperatures,avgE,color='#b08272')
    plt.xlabel('Temperature')
    plt.ylabel('Energy')
    savefig(name1 + '.pdf')
    plt.close()
    
    plt.figure()
    name2 = 'Magnetization' + '_' + str(size)
    np.save(name2, avgMag)
    plot(Temperatures,avgMag,color='#00a3b2')
    plt.xlabel('Temperature')
    plt.ylabel('Magnetization')
    savefig(name2 + '.pdf')
    plt.close()
    
    plt.figure()
    name3 = 'CV' + '_' + str(size)
    np.save(name3, arraySH)
    plot(Temperatures,arraySH,color='#71167a')
    plt.xlabel('Temperature')
    plt.ylabel('CV')
    savefig(name3 + '.pdf')
    plt.close()
    
    plt.figure()
    name4 = 'Sus' + '_' + str(size)
    np.save(name4, arraySus)
    plot(Temperatures,arraySus,color='#da8768')
    plt.xlabel('Temperature')
    plt.xlabel('Chi')
    savefig(name4 + '.pdf')
    plt.close()