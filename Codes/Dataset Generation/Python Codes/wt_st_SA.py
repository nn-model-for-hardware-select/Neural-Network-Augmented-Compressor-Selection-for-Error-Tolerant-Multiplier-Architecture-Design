from PE import *
import numpy as np

def matrix_mul_exact(A,B):
   
    C = 0
    for i in range(len(A)):
        for j in range(len(B)):
                C += PE_exact(A[i][j], B[i][j])
    return C

def matrix_mul_approx(A,B,pos):
  
    C = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if(A[i][j] == 0 or B[i][j] == 0):
                res = 0
            else:
                res = PE_approx(A[i][j], B[i][j], pos)
            C += res
    # C = [[0 for _ in range(3)] for _ in range(3)]
    # for i in range(len(ipA)):
    #     for j in range(len(B[0])):
    #         for k in range(len(B)):
    #             C[i][j] += PE_approx(ipA[i][k], B[k][j], pos)
    return C
def matrix_mul_test(A,B,pos):
  
    C = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if(A[i][j] == 0 or B[i][j] == 0):
                res = 0
            else:
                res = PE_test(A[i][j], B[i][j], pos)
            C += res
    # C = [[0 for _ in range(3)] for _ in range(3)]
    # for i in range(len(ipA)):
    #     for j in range(len(B[0])):
    #         for k in range(len(B)):
    #             C[i][j] += PE_approx(ipA[i][k], B[k][j], pos)
    return C

