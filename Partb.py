# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:05:03 2017

@author: dg144
"""


from pylab import *

sizes = [5, 10, 20, 30, 40, 50, 75, 100, 200, 500]

CVmax = [0.0]*len(sizes)
logn = [0.0]*len(sizes)


count = 0

for size in sizes:
    
    
    A = np.load( 'CV' + '_' + str(size) + '.npy')
    
    CVmax[count] = max(A)
    
    logn[count] = log(size)
    
    count += 1
    
    
#plot(np.divide(1.0,sizes),CVmax)    
    
    
plot(sizes,CVmax,'.',color='#7515e1')
#plot(sizes,CVmax,'.',color='#1875e1')
#plt.yscale('log')
xlabel('n')
ylabel('Cmax/N')

savefig('partb.pdf')

plt.figure()

plot(logn,CVmax,'.',color='#1585e1')
#plot(sizes,CVmax,'.',color='#1875e1')
#plt.yscale('log')
xlabel('log(n) ')
ylabel('Cmax/N')

#plot fit

logn = array(logn)
CVmax = array(CVmax)

a = logn.dot(CVmax)/logn.dot(logn)


fitx = linspace(1,7,50)
fity = a*fitx

plot(fitx,fity,'--')

savefig('partblog.pdf')

print a