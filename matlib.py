#
"""
matlib library 
29/10/2017
"""

import numpy as np
from scipy import linalg 


def colmax(x):
	'''
	# PURPOSE : Compute the minimum of a matrix by columns
	#--------------------------------------------------
	# Input  x  as matrix (nr x nc)
	# Output matrix (1 x nc)
	# Version 1.0, B.Bellone, 29/10/2017
	'''
	return np.max(x, axis=0)
	#apply(as.matrix(x),2,max, na.rm=TRUE)}

def rowmax(x):
	''' 
	PURPOSE : Compute the maximum  by rows
 	#--------------------------------------------------
 	# Input  x  as matrix (nr x nc)
 	# Output matrix (nr x 1)
 	# Version 1.0, B.Bellone, 29/10/2017)
	'''
	return np.max(x, axis=0)
    #<- function(x){apply(as.matrix(x),1,max, na.rm=TRUE)}



if __name__ == '__main__':
    
    A=np.arange(1,10).reshape((3,3))
    B=np.arange(10,20).reshape((3,3))
    C=np.arange(1,11)

    print(A)
    print(B)
    print(C)
    
    print(rowmax(A)) 
    print(rowmin(A))
