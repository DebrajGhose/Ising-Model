# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:01:54 2017

@author: dg144
"""

#Ising model

from __future__ import division

from pylab import *

seed()
    
  
def calculate_local_energy( size, J, i, j):
    
    global M
    
    local_energy = -J*M[i,j]*(   M[(i-1)%size,j] + M[(i+1)%size,j] + M[i,(j-1)%size] + M[i,(j+1)%size]  )
    
    return local_energy

    
    
#simulation parameters

global M

#for size in [50]: #this is for part A of the question
    

for size in [50]:

    
    #initialize your matrix
    
    M = random((size,size)) #M is the matrix containing all the electron spin values
    
    #set up electron spin values based on some threshhold
    
    M[M>=0.3] = 1
    M[M<0.3]=-1
        
    
    #parameters
    J = 1.5
    microstates = size*size #total number of cells in the grid
    #Temperatures = [ 1.5, 2.0, 3.0, 3.1, 3.3, 3.35, 3.45, 3.5, 3.55, 3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9, 3.95, 4 , 4.05, 4.1, 4.15, 4.25, 4.3, 4.5, 4.7, 5.0 , 5.5, 6.0 , 7.0 , 8.0, 9.0]
    #Temperatures = [1.5, 2, 3, 4, 5]
    Temperatures = [ 1.5, 2, 2.5, 2.7, 2.9, 3, 3.1, 3.2, 3.3, 3.35, 3.4, 3.45, 3.5, 3.55, 3.6, 3.7, 3.8, 4.0, 4.4, 5]
    

    snapshottime = size**2 #start collecting data after this burn in period
        
    numberofsims = len(Temperatures)
    
    #initialize arrays to store stuff
    
    avgMag = [0.0]*numberofsims #average magnetization for given T
    avgE = [0.0]*numberofsims #average energy for given T
    avgE2 = [0.0]*numberofsims #arrays to hold E2 and M2
    avgMag2 = [0.0]*numberofsims    



    arraySH = [0.0]*numberofsims #specific heat array
    arraySus = [0.0]*numberofsims #susceptibility
    
    
    
    
    for runnumber in range(0,numberofsims):
        
        average_count = 0 #reset the average weighting for each new temperature
        
        T = Temperatures[runnumber]
    
        print T
        
        #exponential hack
        
        higher = exp(-12.0/T); lower = exp(-6.0/T); #set exponential values in advance to speed up program
    
            
        """
        #calculate energy and magnetization FAST!

        MD = np.vstack(( M[(size-1),:] , M[0:(size-1),:]  )) #displace array by one location downward
        MR = np.hstack((  M[:,(size-1):(size)] ,  M[:,0:(size-1)]  )) #displace array by one location to the right
        Ematrix = -J*(multiply(M,MD) + multiply(M,MR))
        E = sum(Ematrix)
        Mag = sum(M) #calculate magnetization
        """
        
        



        
        for time in range(0,500):
            
            #step through matrix and do your flips
            
            for i in range(0, size):
                for j in range(0,size):
                    
                    #see what old energy is
                    
                    olde = calculate_local_energy( size, J, i, j) #calculate energy
                    
                    newe = -olde #energy of flipped spin
                    
                    energy_change = newe-olde
                
                    
                    if energy_change == 12:
                        
                        expo = higher
                        
                    elif energy_change == 6:
                        
                        expo = lower
                    
                    
                    #see if you want to keep the flip
                    
                    
                    
                    
                    if energy_change <= 0: 
                    
                        #reaching a lower state will always flip spin
                        
                        M[i,j] = -M[i,j]
            
                    
                    elif expo > rand():
                        
                        #see if temperature fluctuations can flip spin
                        
                        M[i,j] = -M[i,j]
            
            #let equilibration be done with
            if time>1:
        
                #calculate energy and magnetization FAST!
    
                MD = np.vstack(( M[(size-1),:] , M[0:(size-1),:]  )) #displace array by one location downward
                MR = np.hstack((  M[:,(size-1):(size)] ,  M[:,0:(size-1)]  )) #displace array by one location to the right
                Ematrix = -J*(multiply(M,MD) + multiply(M,MR)) #obtain a matrix that has cumulative values
                E = sum(Ematrix) #find energy by summing
                Mag = abs(sum(M))/microstates #calculate magnetization
                
    
            
    
                E2 = E*E
                Mag2 = Mag*Mag
                
                #notice that these calculations happen after some burn-in has taken place
                
                avgE[runnumber] = (avgE[runnumber]*average_count + E )/(average_count+1)
                
                avgMag[runnumber] = (avgMag[runnumber]*average_count + Mag)/(average_count+1) 
                
                avgE2[runnumber] = (avgE2[runnumber]*average_count + E2 )/(average_count+1)
                
                #avgMag2[runnumber] = (avgMag2[runnumber]*average_count + Mag2 )/(average_count+1)
                 
                
                average_count = average_count + 1 #weighted average
        
        
        
        arraySH[runnumber] = (avgE2[runnumber] - avgE[runnumber]**2 )/(microstates*T**2)
#        arraySus[runnumber] = (avgMag2[runnumber] - avgMag[runnumber]**2)/T**2

    
    
    plt.figure()
    name1 = 'E' + '_' + str(size)
    np.save(name1, avgE)
    plot(Temperatures,avgE,'.',color='#b08272')
    plt.xlabel('Temperature')
    plt.ylabel('Energy')
    savefig(name1 + '.pdf')
    plt.close()
    
    plt.figure()
    name2 = 'Magnetization' + '_' + str(size)
    np.save(name2, avgMag)
    plot(Temperatures,avgMag,'.',color='#00a3b2')
    plt.xlabel('Temperature')
    plt.ylabel('Magnetization')
    savefig(name2 + '.pdf')
    plt.close()
    
    plt.figure()
    name3 = 'CV' + '_' + str(size)
    np.save(name3, arraySH)
    plot(Temperatures,arraySH,'.',color='#71167a')
    plt.xlabel('Temperature')
    plt.ylabel('CV')
    savefig(name3 + '.pdf')
    plt.close()
    