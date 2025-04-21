from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import metrics
from wt_st_SA import *
from timeit import default_timer as timer


def conv_3x3_sobel_exact(ipimage,kernal1):

    height=len(ipimage)
    width=len(ipimage[0])
    # print("Exact Sobel - Image Size : ",height," ",width)

    ipimage=[[ipimage[j][i] for i in range(width)]for j in range(height)]

    exact_op_k1=[[0 for i in range(width)] for j in range(height)]

    exact_op=[[0 for i in range(width)] for j in range(height)]

    for i in range(1,height-1):
        for j in range(1,width-1):
            inmat=[ipimage[i+1][j-1:j+2], ipimage[i][j-1:j+2]  ,ipimage[i-1][j-1:j+2]]
            exact_op_k1[i][j]=matrix_mul_exact(inmat,kernal1)
            
    exact_op=np.array(exact_op_k1)

    exact_op1=exact_op.astype('float64')

    max_ap=max(max(x) for x in exact_op1)
    min_ap=min(min(x) for x in exact_op1)
    R2=exact_op1-min_ap
    exact_op=R2/max_ap

    return [exact_op]


def conv_3x3_sobel_approx(ipimage,kernal1,pos):
    
    dict = {}
  
    height=len(ipimage)
    width=len(ipimage[0])
    # print("Approx Sobel - Image Size : ",height," ",width)
 
    ipimage=[[ipimage[j][i] for i in range(width)]for j in range(height)]
  
    approx_op_k1=[[0 for i in range(width)] for j in range(height)]

    approx_op=[[0 for i in range(width)] for j in range(height)]

    for i in range(1,height-1):
        for j in range(1,width-1):
            inmat=[ipimage[i+1][j-1:j+2], ipimage[i][j-1:j+2]  ,ipimage[i-1][j-1:j+2]]
            inmat_tuple = tuple(tuple(row) for row in inmat)
            if inmat_tuple not in dict:
                dict[inmat_tuple] = matrix_mul_approx(inmat,kernal1,pos)
            
            approx_op_k1[i][j] = dict[inmat_tuple]
            
            # approx_op_k1[i][j]=(approxop_k1[0][0]+approxop_k1[1][1]+approxop_k1[2][2])/32

    approx_op=np.array(approx_op_k1)

    approx_op1=approx_op.astype('float64')

    max_ap=max(max(x) for x in approx_op1)
    min_ap=min(min(x) for x in approx_op1)
    R2=approx_op1-min_ap
    approx_op=R2/max_ap
                   
    return [approx_op]







