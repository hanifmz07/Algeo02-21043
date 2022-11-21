from eigen import *

# from GUI import *
# Get threshold for identification (minimum value of training image distances)
def get_threshold(train):
    max = np.linalg.norm(train[0] - train[1])
    for i in range(train.shape[0]- 1):
        for j in range(i + 1, train.shape[0]):
            dist = np.linalg.norm(train[i] - train[j])
            if (max < dist):
                max = dist
    return max * 0.8

def identification(testFace, M, normal, eigenFace, trainImg):
    # Test weights calculation
    difTF = testFace - M
    eigenFaceTest = eigenFace @ difTF

    # Train weights calculation
    Y = eigenFace @ normal.T

    # eigenFaceTest = minMaxScaler(eigenFaceTest)
    # for i in range(Y.shape[0]):
    #     Y.T[i] = minMaxScaler(Y.T[i])

    # Storing each euclidean distance to an array
    n = len(eigenFace)
    ArrResult = np.arange(0, n, dtype=float) 
    
    # Euclidean distance between test weights and train weights
    for i in range (n):
        ArrResult[i] = np.linalg.norm(Y.T[i] - eigenFaceTest)
    
    # Return the index of the minimum distance
    idxMin = np.argmin(ArrResult)
    threshold = get_threshold(trainImg)
    # print(ArrResult[idxMin])
    
    if (ArrResult[idxMin] > threshold):
        # Barusan ini diganti idxMin lg soalnya blm nemu angka yg tepat, ntar klo setelah coba dapet angka yg bagus ganti lg aja jadi -1
        return idxMin
    else:
        return idxMin

# Store eigenfaces in a numpy binary file
def storeEigenFace(eigen_face):
    return np.save('eigenface', eigen_face)


# TestingDD
# Ntar klo misal yg dibawah gamau dipake, di comment aja
# test_img = preprocess('test_img')
# images = preprocess('sample_img')
# average_face = face_avg(images)
# normal = normalized_face(images, average_face)
# covariance = covariance_mat(normal)
# eig_val, eig_vec = eig_val_and_vec(covariance)
# eig_vec_img = normal.T @ eig_vec
# for i in range(test_img.shape[0]):
    # idx = identification(test_img[i], average_face, normal, eig_vec_img.T)
    # cv.imwrite(f'testing/pred_{i}_pred.jpg', images[idx].reshape(256,256))
    # cv.imwrite(f'testing/pred_{i}.jpg', test_img[i].reshape(256,256))

# TestingDD
# Ntar klo misal yg dibawah gamau dipake, di comment aja
# test_img = preprocess('C:/Users/Nerbi/Documents/A Project/Tubes/Tubes2-Algeo/Algeo02-21043/test_img')
# test_img = preprocessFile('C:/Users/Nerbi/Documents/A Project/Tubes/Tubes2-Algeo/Algeo02-21043/test_img/alycia dabnem carey155_50.jpg')
# print("preprocess test image DONE")
# images = preprocess('C:/Users/Nerbi/Documents/A Project/Tubes/Tubes2-Algeo/Algeo02-21043/sample_img')
# print("preprocess dataset DONE")
# average_face = face_avg(images)
# normal = normalized_face(images, average_face)
# covariance = covariance_mat(normal)
# eig_val, eig_vec = eig_val_and_vec(covariance)
# eig_vec_img = normal.T @ eig_vec
# # for i in range(1):
# print(test_img.shape)
# # print(test_img[0].shape)
# idx = identification(test_img, average_face, normal, eig_vec_img.T)
# print("hasil")
# print(idx)
# print() # cara print nama file nya gmn ?
    # cv.imwrite (f'testing/pred_{i}_pred.jpg', images[idx].reshape(256,256))
    # cv.imwrite (f'testing/pred_{i}.jpg', test_img[i].reshape(256,256))
        
    
    
    

# driver

# A1 = [[1, 2, 3], [3, 4, 5]]
# A2 = [[5, 6, 7], [5, 2, 4]]
# A3 = [[1, 2, 5], [4, 1, 3]]
# Am = [[1, 2, 5], [4, 1, 3]]
# A = [A1, A2, A3]
# S = np.empty((0, 3*3), int)
# t1 = np.array([[2, 0, 1], [1, 2, 0], [0, 2, 4]])
# t2 = np.array([[1, 1, 1], [0, 1, 0], [1, 2, 2]])
# tr = [t1, t2]
# S = np.append(S, [t1.flatten()], axis=0)
# S = np.append(S, [t2.flatten()], axis=0)
# s1 = [[2, 0, 1], [1, 2, 0], [0, 2, 4]]
# s2 = [[1, 1, 1], [0, 1, 0], [1, 2, 2]]
# # S = tr.flatten()
# # try:
# #     # folderDS = AskFolder.folderName
# #     dir = AskFile.fileName
# #     print(dir)
# #     print()
# #     # print(folderDS)
# #     # print()
# # except :
# #     print("belum input\n")

# # dir = 'C:\\Users\\Nerbi\\Documents\\A Project\Tubes\\Tubes2-Algeo\\archive\\datasetMini'
# dir = 'C:\\Users\\Nerbi\\Documents\\A Project\\Tubes\\Tubes2-Algeo\\archive\datasetMini\\pins_Alex Lawther'
# dirTest = 'C:\\Users\\Nerbi\\Documents\\A Project\\Tubes\\Tubes2-Algeo\\archive\datasetMini\\Alex Lawther64_128.jpg'
# # S = preprocess(dir)

# Mean = mean(tr)
# dif = difference(tr, Mean)

# # Mean2 = mean(S)
# # dif2 = difference(S, Mean2)
# # cov2 = kovarian(S, dif2)

# Meanf = meanFlatten(S)
# diff = differenceFlatten(S, Meanf)
# covf = covarianceFlatten(diff)

# # Vec = eig_val_and_vec(cov)
# print(S)
# print()
# print(Meanf)
# print()
# print(diff)
# print()
# print(covf)
# print()
# # tr2=tr
# # tr3=tr

# # start_time = time.time()
# # Mean = mean(tr2)
# # dif = difference(tr2, Mean)
# # L2 = kovarian(tr2, dif)
# # print(L2)
# # timNumpy= (time.time() - start_time)
# # print("--- %s seconds ---" % timNumpy)

# # start_time = time.time()
# # L = kovarianNotNumpy(tr)
# # print(L)
# # tim = (time.time() - start_time)
# # print("--- %s seconds ---" % tim)
# # print(L==L2)
# # if(timNumpy<tim) :
# #     print("numpy " + str(tim-timNumpy))
# # else :
# #     print("numpy kalah "+ str(timNumpy-tim))

# vr = [[1,2,3]]
# v = [[1],
#      [2],
#      [3]]
# Vec = [[1,-1,0],
#        [-1,-1,0],
#        [0,0,0]]
# testF1 = [[2,1,1],
#           [1,2,1],
#           [0,2,4]]
# print(dif)
# print()
# ef = eigenFace(dif, Vec)
# print(ef)
# print()
# a =[5,4,3,6,7,8]
# # print(np.argmin(a))
# res = identification(testF1, Mean, Vec, ef)
# print("gambar yang paling mendekati adalah gambar ke-" + str(res+1))



# array = np.arange(0, 737280, 1, np.uint8)
# array = np.reshape(array, (1024, 720))
# # folderDownload = open("../Save_Images")
# S = preprocess(dir)
# # print((S[0]).shape)
# # print(np.reshape(S[0], (256, 256)))
# MF = meanFlatten(S)
# DIFF = differenceFlatten(S, MF)
# k = covarianceFlatten(DIFF)
# eV = eig_val_and_vec(k)[1]

# print(DIFF.shape)
# print(k.shape)
# print(eV.shape)
# eface = eigenFace(DIFF,eV) 


# # Ak = np.reshape(eV,  (0, 65536))
# Ak = np.resize(eV,  (0, 65536))
# print(Ak.shape)
# AA = preprocess(dirTest)
# print(AA.shape)
# idx = identification(AA, MF, Ak, eface)

# # path = 'Tubes2-Algeo\Save_Images'
# # path = 'Tubes2-Algeo\Trash'
# # for i in range (len(S)):
# #     A = np.reshape(S[i], (256, 256))
# #     cv.imwrite(os.path.join(path, 'img_'+str(i)+'.jpg'), A)
# # print(ef)


# # img = cv.imread('1.jpg', 1)
# # path = 'D:/OpenCV/Scripts/Images'
# # cv.imwrite(os.path.join(path , 'waka.jpg'), img)
# # cv.waitKey(0)