from img import *

ROUND = 2


# Face average
def face_avg(X):
    return np.sum(X, axis=0) / X.shape[0]

# Train_face -  average_face
def normalized_face(X, avg):
    return (X - avg)

# Covariance matrix
def covariance_mat(X):
    return X @ X.T

# Fungsi Mean
def mean(S):
    M = len(S)
    Mean = (np.sum(S, axis=0))
    Mean = np.floor_divide(Mean, M) # round
    return Mean

def meanFlatten(S):
    Mean = np.sum(S, axis=0)
    Mean = np.floor_divide(Mean, S.shape[0])
    return Mean  

# Prosedur Selisih
def difference(S, mean):
    a = np.subtract(S, mean)
    return np.abs(a)

def differenceFlatten(S, M):
    return abs(S - M)

# Fungsi Matriks Kovarian
def kovarian(S, dif):
    C = np.concatenate(dif, axis=1)
    L = np.matmul(C, np.transpose(C))
    return L

def covarianceFlatten(S):
    # return (S @ S.T)
    return np.matmul(S, S.T)

# Not Numpy 
def meanNotNumpy(S):
    M = len(S)
    nrows = len(S[0])
    ncols = len((S[0])[0])
    Mean = [[0 for _ in range(ncols)] for _ in range(nrows)]
    for m in range(0, M):
        for i in range(nrows):
            for j in range(ncols):
                Mean[i][j] += (S[m])[i][j]
    for i in range(nrows):
        for j in range(ncols):
            # Mean[i][j]=round((Mean[i][j]/M),ROUND)
            Mean[i][j] = mt.floor((Mean[i][j] / M))
    return Mean

def differenceNotNumpy(S, mean):
    M = len(S)
    nrows = len(S[0])
    ncols = len((S[0])[0])
    for m in range(0, M):
        for i in range(nrows):
            for j in range(ncols):
                (S[m])[i][j] = round(abs((S[m])[i][j] - mean[i][j]), ROUND)

def kovarianNotNumpy(S):
    M = len(S)
    nrows = len(S[0])
    ncols = len((S[0])[0])
    nc = ncols * M
    differenceNotNumpy(S, meanNotNumpy(S))
    # np.concatenate(S[0 for i in range M],axix = 0)
    C = [[0 for _ in range(nc)] for _ in range(nrows)]
    for m in range(0, M):
        for i in range(nrows):
            for j in range(ncols):
                C[i][j + ncols * m] = S[m][i][j]
    # print(C)
    L = np.matmul(C, np.transpose(C))
    return L