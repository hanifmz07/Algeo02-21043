from functions import *

# Eigenvalue and eigenvector using QR decomposition
def eig_val_and_vec(M):
    first = True
    # i = 0
    while (True):
        Q, R = qr_householder(M)
        # Q, R = np.linalg.qr(M)
        eigval_prev = M.diagonal().copy()
        M = R @ Q
        if first:
            eigvec = Q.copy()
            first = False
            continue
        else:
            eigvec = eigvec @ Q
            # If the error reached a very small value, the process will be stopped
            if np.allclose(eigval_prev, M.diagonal(), rtol=1e-6, atol=1e-8):
                break
        # i += 1
        # print(f"{(i+1)/50}%")
    # print(i)
    return M.diagonal(), eigvec  

# Norm vector
def norm_vector(v):
    return np.sqrt(np.sum(v**2))

# QR decomposition with householder matrix
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

# Scale matrix to 0-255 for displaying
def minMaxScalerImg(X):
    X = (X - np.min(X)) / (np.max(X) - np.min(X)) * 255
    return X


# Normalize eigenvectors
def normalizeEigVec(eig_vect):
    for i in range(int(eig_vect.T.shape[0])):
        eig_vect.T[i] = eig_vect.T[i] / norm_vector(eig_vect.T[i])
    return eig_vect

# Get eigenface from eigenvectors
# Ratio: ratio between len(eigenface) and len(eigenvectors), value from 0-1
def eigenFace(X, ratio):
    eigen_face = np.empty((0, X.T.shape[1]), 'float64')
    for i in range(int(X.T.shape[0] * ratio)):
        eigen_face = np.append(eigen_face, [X.T[i]], axis=0)
    return eigen_face

# Scaling eigen face for display
def scaledEigenFace(X):
    E_scaled = np.empty((0, X.shape[1]), 'float64')
    for i in range(int(X.shape[0])):
        E_scaled = np.append(E_scaled, [minMaxScalerImg(X.T[i])], axis=0)

# Face identification
def identification(testFace, M, normal, Eigenface):
    # Test weights calculation
    difTF = testFace - M
    eigenFaceTest = Eigenface @ difTF

    # Train weights calculation
    Y = Eigenface @ normal.T
    
    # Storing each euclidean distance to an array
    n = len(Eigenface)
    ArrResult = np.arange(0, n, dtype=float) 
    for i in range (n):
        # Euclidean distance between test weights and train weights
        ArrResult[i] = np.linalg.norm(Y.T[i] - eigenFaceTest)
    
    # Return the index of the minimum distance
    return np.argmin(ArrResult)

# Store eigenfaces in a numpy binary file
def storeEigenFace(eigen_face):
    return np.save('eigenface', eigen_face)

