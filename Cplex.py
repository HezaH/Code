from docplex.mp.model import Model
# import os
# print(os.environ['PYTHONPATH'])
# os.environ['PYTHONPATH'] += "cplex\python\3.13\<platform>"

# Definição da matriz de distâncias (Apenas uma parte dela está visível, substitua pela sua matriz completa)
dist_matrix = [   
    [ 0, 140, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 140, 0, 116, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 116, 0, 152, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 152, 0, 0, 0, 0, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 41, 0, 0, 0, 0, 153, 0, 0, 67, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 55, 0, 0, 153, 0, 117, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 57, 0, 0, 117, 0, 148, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 61, 0, 0, 148, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 67, 0, 0, 0, 0, 145, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 57, 0, 0, 145, 0, 120, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 56, 0, 0, 120, 0, 148, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 53, 0, 0, 148, 0, 0, 0, 0, 59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, 0, 0, 137, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, 137, 0, 115, 0, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, 115, 0, 155, 0, 0, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 0, 0, 155, 0, 0, 0, 0, 61, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 145, 0, 0, 52, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 0, 0, 145, 0, 118, 0, 0, 49, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 118, 0, 154, 0, 0, 53, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 0, 0, 154, 0, 0, 0, 0, 61, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 139, 0, 0, 52, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 0, 0, 139, 0, 124, 0, 0, 52, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53, 0, 0, 124, 0, 152, 0, 0, 56, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 0, 0, 152, 0, 0, 0, 0, 59],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 0, 0, 0, 0, 144, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 0, 0, 144, 0, 126, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 0, 0, 126, 0, 147],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 0, 0, 147, 0],
 ]
# arestas = [
#     ("v1", "v2", 140), ("v1", "v5", 41), ("v2", "v3", 116), ("v2", "v6", 55),
#     ("v3", "v4", 152), ("v3", "v7", 57), ("v4", "v8", 61), ("v5", "v6", 153),
#     ("v5", "v9", 67), ("v6", "v7", 117), ("v6", "v10", 57), ("v7", "v8", 148),
#     ("v7", "v11", 56), ("v8", "v12", 53), ("v9", "v10", 145), ("v9", "v13", 48),
#     ("v10", "v11", 120), ("v10", "v14", 48), ("v11", "v12", 148), ("v11", "v15", 48),
#     ("v12", "v16", 59), ("v13", "v14", 137), ("v13", "v17", 56), ("v14", "v15", 115),
#     ("v14", "v18", 52), ("v15", "v16", 155), ("v15", "v19", 54), ("v16", "v20", 52),
#     ("v17", "v18", 145), ("v17", "v21", 52), ("v18", "v19", 118), ("v18", "v22", 49),
#     ("v19", "v20", 154), ("v19", "v23", 53), ("v20", "v24", 61), ("v21", "v22", 139),
#     ("v21", "v25", 52), ("v22", "v23", 124), ("v22", "v26", 52), ("v23", "v24", 152),
#     ("v23", "v27", 56), ("v24", "v28", 59), ("v25", "v26", 144), ("v26", "v27", 126),
#     ("v27", "v28", 147)
# ]
n = len(dist_matrix)  # Número de vértices
p = 14  # Número de instalações a serem abertas

# Criar modelo
mdl = Model("p-Median")

# Variáveis de decisão
x = {(i, j): mdl.binary_var(name=f"x_{i}_{j}") for i in range(n) for j in range(n)}
y = {j: mdl.binary_var(name=f"y_{j}") for j in range(n)}

# Função Objetivo: Minimizar a soma das distâncias dos clientes às instalações
mdl.minimize(mdl.sum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)))

# Restrição 1: Cada vértice deve ser atendido por pelo menos uma instalação
for i in range(n):
    mdl.add_constraint(mdl.sum(x[i, j] for j in range(n)) == 1, f"Atendimento_{i}")

# Restrição 2: Um vértice só pode ser atendido por outro que seja uma instalação
for i in range(n):
    for j in range(n):
        mdl.add_constraint(x[i, j] <= y[j], f"Restricao_Atendimento_{i}_{j}")
#verificação para garantir que a distância entre os vértices seja positiva antes de permitir que um vértice seja atendido por outro
for i in range(n):
    for j in range(n):
        if dist_matrix[i][j] > 0:  # Só permitir atendimento se houver uma conexão válida
            mdl.add_constraint(x[i, j] <= y[j], f"Restricao_Atendimento_{i}_{j}")


# Restrição 3: Exatamente p vértices devem ser instalações
mdl.add_constraint(mdl.sum(y[j] for j in range(n)) == p, "Num_Instalacoes")

# Resolver o modelo
solution = mdl.solve(log_output=True)

# Exibir resultados
if solution:
    print("Instalações abertas nos vértices:")
    for j in range(n):
        if y[j].solution_value > 0.5:
            print(f"Vértice {j} é uma instalação")

    print("\nAtribuição de vértices às instalações:")
    for i in range(n):
        for j in range(n):
            if x[i, j].solution_value > 0.5:
                print(f"Vértice {i} é atendido por {j}")
else:
    print("Nenhuma solução encontrada.")
