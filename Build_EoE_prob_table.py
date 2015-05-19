#!/usr/bin/env python

import numpy as np
import fractions as f

num_dice=6

def i_prob(i,j):
	return i+2,j-1

M=np.zeros((2*(num_dice+1)+1,num_dice),dtype=object) * f.Fraction(0,1)
F=np.zeros((2*(num_dice+1)+1,num_dice),dtype=object) * f.Fraction(0,1)
C=np.zeros((2*(num_dice+1)+1,num_dice),dtype=object) * f.Fraction(0,1)
S=np.zeros((2*(num_dice+1)+1,num_dice),dtype=object) * f.Fraction(0,1)


M[i_prob(0,1)]=f.Fraction(4,8)
M[i_prob(1,1)]=f.Fraction(3,8)
M[i_prob(2,1)]=f.Fraction(1,8)

F[i_prob(0,1)]=f.Fraction(5,8)
F[i_prob(1,1)]=f.Fraction(2,8)
F[i_prob(2,1)]=f.Fraction(1,8)

for n_d in np.arange(2,num_dice+1):
	for k in np.arange(0,2*n_d+1):
		for j in np.arange(0,3):
			M[i_prob(k,n_d)] += M[i_prob(k-j,n_d-1)]*M[i_prob(j,1)]
			F[i_prob(k,n_d)] += F[i_prob(k-j,n_d-1)]*F[i_prob(j,1)]

for n_d in np.arange(1,num_dice+1):
	for k in np.arange(0,2*num_dice+1):
		C[i_prob(k,n_d)] = np.sum(F[:k+3,n_d-1])

#head="DICEs "
#for k in np.arange(0,2*n_d+1):
	#head += "Probab(%2d)   " %(k)
#print head 
#for n in np.arange(1,num_dice+1):
	#s = "%5d " %(n) 
	#for k in np.arange(0,2*n_d+1):
		#s = s+"%14s " %(M[i_prob(k,n)])
	#print s

for na in np.arange(1,7):
	for nd in np.arange(1,7):
		s=f.Fraction(0,1)
		for k in np.arange(1,2*n_d+1):
			p = M[i_prob(k,na)] * C[i_prob(k-1,nd)]
			s += p
			#print "%3d %3d %3d %8.3f" %(k, na, nd, 100.0*float(p))
		print "Probability of at least 1 success with Ability = %d and Difficulty = %d : %5.2f" %(na,nd,100*float(s))


