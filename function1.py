import numpy as np
import math as mt
import time

start_time = time.time()

ROUND = 2
# Fungsi Mean
def mean(S):
    M = len(S)
    nrows = len(S[0])
    ncols = len((S[0])[0])
    Mean = [[0 for _ in range(ncols)] for _ in range(nrows)]
    # np.sum()
    for m in range(0, M):
        for i in range(nrows):
            for j in range(ncols):
                Mean[i][j] += (S[m])[i][j]
    for i in range(nrows):
        for j in range(ncols):
            # Mean[i][j]=round((Mean[i][j]/M),ROUND)
            Mean[i][j] = mt.floor((Mean[i][j] / M))
            #   ??? di floor kah ?
    return Mean


# Prosedur Selisih
def difference(S, mean):
    M = len(S)
    nrows = len(S[0])
    ncols = len((S[0])[0])
    for m in range(0, M):
        for i in range(nrows):
            for j in range(ncols):
                (S[m])[i][j] = round(abs((S[m])[i][j] - mean[i][j]), ROUND)


# Fungsi Matriks Kovarian
def kovarian(S):
    M = len(S)
    nrows = len(S[0])
    ncols = len((S[0])[0])
    nc = ncols * M
    difference(S, mean(S))
    # np.concatenate(S[0 for i in range M],axix = 0)
    C = [[0 for _ in range(nc)] for _ in range(nrows)]
    for m in range(0, M):
        for i in range(nrows):
            for j in range(ncols):
                C[i][j + ncols * m] = S[m][i][j]
    # print(C)
    L = np.matmul(C, np.transpose(C))
    return L


# driver
# A1 = [[1, 2, 3], [3, 4, 5]]
# A2 = [[5, 6, 7], [5, 2, 4]]
# A3 = [[1, 2, 5], [4, 1, 3]]
# A = [A1, A2, A3]
# t1 = [[2, 0, 1], [1, 2, 0], [0, 2, 4]]
# t2 = [[1, 1, 1], [0, 1, 0], [1, 2, 2]]
# tr = [t1, t2]
# # print (A)
# print(tr)

# # print("")
# # me = mean(A)
# # print (me)
# # print("")
# # difference(A,me)
# # print (A)
# # C = [[0 for _ in range (nc)] for _ in range (nr)]
# L = kovarian(tr)
# print(L)
# # f = [[1,2,3],[4,5,6]]
# # print(np.matmul(f,np.transpose(f)))
# # print (len(A1), len(A1[0]))


# print("--- %s seconds ---" % (time.time() - start_time))
