import numpy as np

def eig_val_and_vec(M):
    for i in range(30):
        Q, R = qr_householder(M)
        M = R @ Q
        if i == 0:
            eigvec = Q.copy()
        else:
            eigvec = eigvec @ Q
    
    return M.diagonal(), eigvec

def norm_vector(v):
    return np.sqrt(np.sum(v**2))

def qr_householder(M):
    init_size, y = M.shape
    R = M.copy()
    Q = np.eye(init_size)
    for i in range(init_size - 1):
        x = R[i:, i]
        u = x / np.absolute(x).max()
        e = np.zeros(M.shape[0] - i)
        e[0] = norm_vector(u)
        u = (u + np.copysign(e, u[0]))
        H = np.eye(init_size)
        H[i:, i:] = np.eye(u.shape[0]) - (2 / (u.T @ u)) * np.dot(u[:, None], u[None, :])
        Q = Q @ H
        R = H @ R
    return Q, R
