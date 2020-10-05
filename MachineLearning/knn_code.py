#K-NN a PALO como lo querias

#importar libreria NUMPY, esta es basica
import numpy as np
import operator
# import matplotlib.pyplot as plt

def distancia(x1, x2):
    x1, x2 = np.array(x1), np.array(x2)

    distancias = 0
    for i in range(len(x1)):
        distancias += (x1[i] - x2[i]) ** 2

    return np.sqrt(distancias)

def predecir(k, X, Y):

    predicciones = []

    for i in range(len(Y)):
        dist = []
        for j in range(len(X)):
            #print(X[j][:-1], Y[i])
            dist.append(distancia(X[j][:-1], Y[i]))

        dist = np.array(dist)
        print("Dist: ", dist)
        sorted_dist = dist.argsort()[:k]
        print("Sorted dist: ", sorted_dist)
        count = {}

        for t in sorted_dist:
            if X[t][-1] in count:
                count[X[t][-1]] += 1
            else:
                count[X[t][-1]] = 1
        #print("Count: ", count)
        final_sort = sorted(count.items(), key = operator.itemgetter(1), reverse=True)
        #print("Final sort: ", final_sort)
        predicciones.append(final_sort[0][0])
    return predicciones

#
# x = np.array([[1,1,1],
#               [1.5,1.5,1],
#               [2,2,1],
#               [5,5,2],
#               [5.5, 5.5,2]])
# #print(x)
# y = np.array([[1.2,1.2],
#               [1.3, 1.3],
#               [5.3, 5.3]])
#print(y)
# plt.figure()
# for i in range(len(x)):
#     plt.scatter(x[i][0], x[i][1], c = ('b' if x[i][-1]==1 else 'r'))
#
#
# plt.scatter(y[0][0], y[0][1], c='g')

# pred = predecir(2, x, y)
# print(pred)
