#Импорт модулей
import networkx as nx
import numpy as np
#Матрица смежности
d_ij = np.array([
      [0,2,4,10,0,0,0],
      [0,0,0,11,5,0,0],
      [0,0,0,3,0,1,0],
      [0,0,0,0,8,7,0],
      [0,0,0,0,0,0,6],
      [0,0,0,0,0,0,9],
      [0,0,0,0,0,0,0]])
#Алгоритм Дейкстра     
G = nx.from_numpy_matrix(d_ij, create_using=nx.DiGraph())
U = (nx.dijkstra_path(G, 0, 6))
for i in range(0,len(U)):
    U[i] = U[i]+1
#Вывод кратчайшего пути в массиве
print("Кратчайший путь =",U)


