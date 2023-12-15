import numpy as np
import cv2
import matplotlib.pyplot as plt

# Gerar um conjunto de dados sinteético com 500 pontos clusters
np.random.seed(42)

# Gerar 125 pontos em cada um dos 4 clusters

cluster1 = np.random.randn(125, 2) + np.array([2, 2])
cluster2 = np.random.randn(125, 2) + np.array([-2, 2])
cluster3 = np.random.randn(125, 2) + np.array([-2, -2])
cluster4 = np.random.randn(125, 2) + np.array([2, -2])

# Concatenar os clusters em um único conjunto de dados
X = np.concatenate((cluster1, cluster2, cluster3, cluster4), axis=0)

# COnverter os pontos para o tipo float(32
X = np.float32(X)]


