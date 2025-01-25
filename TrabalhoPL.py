from Grafo import Grafo
import numpy as np
from pMedia import pMedia
from PCVM import PCVM

# Definição do conjunto de vértices e arestas com pesos (distâncias)
arestas = [
    ("v1", "v2", 140), ("v1", "v5", 41), ("v2", "v3", 116), ("v2", "v6", 55),
    ("v3", "v4", 152), ("v3", "v7", 57), ("v4", "v8", 61), ("v5", "v6", 153),
    ("v5", "v9", 67), ("v6", "v7", 117), ("v6", "v10", 57), ("v7", "v8", 148),
    ("v7", "v11", 56), ("v8", "v12", 53), ("v9", "v10", 145), ("v9", "v13", 48),
    ("v10", "v11", 120), ("v10", "v14", 48), ("v11", "v12", 148), ("v11", "v15", 48),
    ("v12", "v16", 59), ("v13", "v14", 137), ("v13", "v17", 56), ("v14", "v15", 115),
    ("v14", "v18", 52), ("v15", "v16", 155), ("v15", "v19", 54), ("v16", "v20", 52),
    ("v17", "v18", 145), ("v17", "v21", 52), ("v18", "v19", 118), ("v18", "v22", 49),
    ("v19", "v20", 154), ("v19", "v23", 53), ("v20", "v24", 61), ("v21", "v22", 139),
    ("v21", "v25", 52), ("v22", "v23", 124), ("v22", "v26", 52), ("v23", "v24", 152),
    ("v23", "v27", 56), ("v24", "v28", 59), ("v25", "v26", 144), ("v26", "v27", 126),
    ("v27", "v28", 147)
]

# Criar a instância do grafo
grafo = Grafo()

# Adicionando arestas com pesos (distâncias)
grafo.transformar_formatos(grafo.grafo_hcp, arestas)

# Gerando a matriz de adjacência
matriz_adjacencia = grafo.gerar_matriz_adjacencia(grafo.grafo_hcp) 
print("\nMatriz de Adjacência:")
print(np.array(matriz_adjacencia))

# Exibir grafo
grafo.exibir_grafo(grafo.grafo_hcp)
grafo.visualizar_grafo(grafo.grafo_hcp, vertices_destaque=None)

# Conjunto de vértices
vertices = set()
for u, v, _ in arestas:
    vertices.add(u)
    vertices.add(v)

vertices = sorted(vertices)  # Garantir ordem consistente dos vértices 

model_name = "Cobertura Minima de Vertices com Pesos"
# Número de facilidades a serem abertas
p = PCVM(arestas, vertices, grafo, model_name)

model_name = "P-Median"
pMedia(arestas, vertices, grafo, p, model_name)

# Criar a instância do grafo dinâmico
grafo = Grafo()

# Adicionando arestas com pesos (distâncias)
num_vertices = 80 
heigth_x = num_vertices//8
grafo.gerar_automaticamente_arestas(num_vertices=num_vertices, heigth_x=heigth_x, grafo = grafo.grafo_hcp)

# Gerando a matriz de adjacência
matriz_adjacencia = grafo.gerar_matriz_adjacencia(grafo.grafo_hcp) #!
print("\nMatriz de Adjacência:")
print(np.array(matriz_adjacencia))

# Exibir grafo
grafo.exibir_grafo(grafo.grafo_hcp)
grafo.visualizar_grafo(grafo.grafo_hcp)

arestas = grafo.re_transformar_formatos(grafo.grafo_hcp)

# Conjunto de vértices
vertices = set()
for u, v, _ in arestas:
    vertices.add(u)
    vertices.add(v)

vertices = sorted(vertices)  # Garantir ordem consistente dos vértices 

model_name = "Cobertura Minima de Vertices com Pesos"
# Número de facilidades a serem abertas
p = PCVM(arestas, vertices, grafo, model_name)

model_name = "P-Median"
pMedia(arestas, vertices, grafo, p, model_name)

p = p
