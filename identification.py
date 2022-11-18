from eigen import *
# from GUI import *

def eigenFace(D, V):
    eigFace = D  
    eigFace = np.matmul(V, D)
    return eigFace 

def identification(testFace, M, V, Eigenface):
    difTF = difference(testFace, M)
    eigenFaceTest = np.matmul(V, difTF)
    MatResult = difference(Eigenface, eigenFaceTest)
    n = len(Eigenface)
    ArrResult = np.arange(0, n, dtype=float) 
    for i in range (n):
        ArrResult[i] = np.linalg.norm(MatResult[i])
    # print(ArrResult)
    return np.argmin(ArrResult)


# driver

# A1 = [[1, 2, 3], [3, 4, 5]]
# A2 = [[5, 6, 7], [5, 2, 4]]
# A3 = [[1, 2, 5], [4, 1, 3]]
# Am = [[1, 2, 5], [4, 1, 3]]
# A = [A1, A2, A3]
S = np.empty((0, 3*3), int)
t1 = np.array([[2, 0, 1], [1, 2, 0], [0, 2, 4]])
t2 = np.array([[1, 1, 1], [0, 1, 0], [1, 2, 2]])
S = np.append(S, [t1.flatten()], axis=0)
S = np.append(S, [t2.flatten()], axis=0)
s1 = [[2, 0, 1], [1, 2, 0], [0, 2, 4]]
s2 = [[1, 1, 1], [0, 1, 0], [1, 2, 2]]
# S = tr.flatten()
# try:
#     # folderDS = AskFolder.folderName
#     dir = AskFile.fileName
#     print(dir)
#     print()
#     # print(folderDS)
#     # print()
# except :
#     print("belum input\n")

# dir = 'C:\\Users\\Nerbi\\Documents\\A Project\Tubes\\Tubes2-Algeo\\archive\\datasetMini'
dir = 'C:\\Users\\Nerbi\\Documents\\A Project\\Tubes\\Tubes2-Algeo\\archive\datasetMini\\pins_Alex Lawther'
dirTest = 'C:\\Users\\Nerbi\\Documents\\A Project\\Tubes\\Tubes2-Algeo\\archive\datasetMini\\Alex Lawther64_128.jpg'
# S = preprocess(dir)

# Mean = mean(S)
# dif = difference(S, Mean)
# cov = kovarian(S, dif)

Mean = meanFlatten(S)
dif = differenceFlatten(S, Mean)
cov = covarianceFlatten(dif)

# Vec = eig_val_and_vec(cov)
print(S)
print()
print(Mean)
print()
print(dif)
print()
print(cov)
# tr2=tr
# tr3=tr

# start_time = time.time()
# Mean = mean(tr2)
# dif = difference(tr2, Mean)
# L2 = kovarian(tr2, dif)
# print(L2)
# timNumpy= (time.time() - start_time)
# print("--- %s seconds ---" % timNumpy)

# start_time = time.time()
# L = kovarianNotNumpy(tr)
# print(L)
# tim = (time.time() - start_time)
# print("--- %s seconds ---" % tim)
# print(L==L2)
# if(timNumpy<tim) :
#     print("numpy " + str(tim-timNumpy))
# else :
#     print("numpy kalah "+ str(timNumpy-tim))

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