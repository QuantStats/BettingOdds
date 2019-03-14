import numpy as np
import matplotlib.pyplot as plt
from numpy import exp as exp
from math import factorial
from scipy.optimize import broyden1

class odd:

##this is a minimal working example
##class variables can go here in the future

    #the poisson probability for under n+0.5 odd market at tau, tau is defined
    #as the remaining time for a match
    def pois_prob(lam, n, T, tau):
        def compute(lam, n, T, tau=None):
            if tau is None:
                prob_vec = [exp(-lam)*sum([lam**j/(factorial(j)) \
                                           for j in range(0, k+1)]) for k in range(0, n+1)]           

            else:
                R = lam/T
                prob_vec = np.zeros((1,len(tau)))
                for j in range(0,n+1):
                    temp = (exp(-R*tau)*((R*tau)**(j)))/factorial(j)
                    temp=temp.reshape((1,len(temp)))
                    prob_vec = np.concatenate((prob_vec,temp),axis=0)
                prob_vec = np.cumsum(prob_vec,axis=0)
                prob_vec = np.delete(prob_vec,0,axis=0)
                dec_odd = 1/prob_vec
    #return the decimal odd
            return dec_odd
            
        return compute(lam, n, T, tau), compute
    
    #plot and visualize
    def visual(tau, dec_odd):
        fig = plt.figure(figsize=(8,6))
        for j in range(dec_odd.shape[0]):
            plt.plot(tau, dec_odd[j],label='Under '+str(j)+'.5')

        plt.title('Decimal odd for the under-goal market')
        plt.xlabel('Time (t)')
        plt.ylabel('Decimal odd')
        plt.axis([0, 90, 0, 1.1*max(dec_odd[0])])
        plt.legend()
        fig.savefig('decimal_odd.png')
        plt.show()
        

            
#main
        
lam = 3
n = 3
T = 90
delta = 0.1
t = np.arange(0.1, T+delta, delta)
tau = T-t
    
y = odd.pois_prob(lam, n, T, tau)
odd.visual(T-tau, y[0])

