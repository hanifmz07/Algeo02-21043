from eigen import *

# Get threshold for identification (minimum value of training image distances)
def get_threshold(train):
    max = np.linalg.norm(train[0] - train[1])
    for i in range(train.shape[0]- 1):
        for j in range(i + 1, train.shape[0]):
            dist = np.linalg.norm(train[i] - train[j])
            if (max < dist):
                max = dist
    return max * 0.8

def identification(testFace, M, normal, eigenFace):
    # Test weights calculation
    difTF = testFace - M
    eigenFaceTest = eigenFace @ difTF

    # Train weights calculation
    Y = eigenFace @ normal.T

    # Storing each euclidean distance to an array
    n = len(eigenFace)
    ArrResult = np.arange(0, n, dtype=float) 
    
    # Euclidean distance between test weights and train weights
    for i in range (n):
        ArrResult[i] = np.linalg.norm(Y.T[i] - eigenFaceTest)
    
    # Return the index of the minimum distance
    return np.argmin(ArrResult)

# Store eigenfaces in a numpy binary file
def storeEigenFace(eigen_face):
    return np.save('eigenface', eigen_face)
