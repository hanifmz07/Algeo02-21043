import numpy as np
from tabulate import tabulate
from scipy.linalg import hessenberg

def eig_val_rumusjadi(M):
    for i in range(30):
        # H = hessenberg(M)
        # Q, R = np.linalg.qr(H - H[M.shape[0] - 1][M.shape[0] - 1] * np.eye(M.shape[0], M.shape[0]))
        # Q, R = qr_householder(H - H[M.shape[0] - 1][M.shape[0] - 1] * np.eye(M.shape[0], M.shape[0]))
        # M = R @ Q + H[M.shape[0] - 1][M.shape[0] - 1] * np.eye(M.shape[0], M.shape[0])
        # Q, R = qr_householder(M - M[M.shape[0] - 1][M.shape[0] - 1] * np.eye(M.shape[0], M.shape[0]))
        # M = R @ Q + M[M.shape[0] - 1][M.shape[0] - 1] * np.eye(M.shape[0], M.shape[0])
        Q, R = qr_householder(M)
        M = R @ Q
        # Q, R = qr(M)
        M = R @ Q
        if i == 0:
            eigvec = Q.copy()
        else:
            eigvec = eigvec @ Q
    
    return M.diagonal(), eigvec

def norm_vector(v):
    return np.sqrt(np.sum(v**2))

def qr_householder(M):
    init_size = M.shape[0]
    R = M.copy()
    for i in range(init_size - 1):
        
        A = R[i:, i].reshape(M.shape[0] - i, 1)
        # print("A:")
        # print(A)
        AE = np.zeros(M.shape[0] - i)
        AE[0] = norm_vector(A)
        # print(A)
        U = A + np.copysign(AE.reshape(AE.shape[0], 1), A[0])
        # print(U)
        V = U / np.sqrt(norm_vector(A))
        V = V / norm_vector(V)
        # print(V)
        # print(norm_vector(V))
        Q = np.eye(init_size)
        Q[i:, i:] = np.eye(A.shape[0]) - 2 * (V @ V.T)
        if i == 0:
            Q_final = (Q.T).copy()
            R = Q @ M
        else :
            Q_final = Q_final @ Q.T
            R = Q @ R
        
        # print("Q:")
        # print(Q)
        # print("R:")
        # print(R)
        # print("Q_final:")
        # print(Q_final)
    return Q, R
        

# def hessenberg_transform(M):
#     return 0
# def eig_val(M):
#     return 0

# def qr(A):
#     m, n = A.shape
#     Q = np.eye(m)
#     for i in range(n - (m == n)):
#         H = np.eye(m)
#         H[i:, i:] = make_householder(A[i:, i])
#         Q = np.dot(Q, H)
#         A = np.dot(H, A)
        
#     return Q, A

# def make_householder(a):
#     # print(a)
#     v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
#     # print(v)
#     v[0] = 1
#     H = np.eye(a.shape[0])
#     H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
#     # print(v[:, None], v[None, :])
#     # print(np.dot(v,v))
#     return H

M1 = np.array([12,-51,4,6,167,-68,-4,24,-41]).reshape(3,3)
M2 = np.arange(64).reshape(8,8)
M3 = np.arange(256*256).reshape(256,256)
# qr_householder(M1)
eigVal, eigVec = eig_val_rumusjadi(M3)
# npEigVal, npEigVec = np.linalg.eig(M1)
# testEigVal = qr_householder
# print(npEigVal)
# print(npEigVec)
print(eigVal)
print(eigVec)
