from docplex.mp.model import Model
def PCVM(arestas, vertices, grafo, model_name):
    # Criar modelo
    mdl = Model(name=model_name)

    # Criar variáveis binárias para os vértices
    x = {v: mdl.binary_var(name=f"x_{v}") for v in vertices}

    # Definir a função objetivo: minimizar o somatório dos pesos das arestas cobertas
    mdl.minimize(mdl.sum((x[u] + x[v]) * peso for u, v, peso in arestas))

    # Adicionar restrições: cada aresta deve ser coberta por pelo menos um de seus vértices
    for u, v, _ in arestas:
        mdl.add_constraint(x[u] + x[v] >= 1)

    # Resolver o modelo
    solucao = mdl.solve()

    # Verificar se há solução
    if solucao:
        vertices_cobertos = [v for v in vertices if x[v].solution_value > 0.5]
        print("Conjunto mínimo de cobertura de vértices:")
        vertices_cobertos = sorted(vertices_cobertos, key=lambda x: int(x[1:]))
        print(vertices_cobertos)
        print(f"Quantidade mínima de vértices necessários: {len(vertices_cobertos)}")
        print(f"Soma total dos pesos cobertos: {solucao.objective_value}")
        grafo.visualizar_grafo(grafo.grafo_hcp, vertices_destaque=vertices_cobertos)
    else:
        print("Nenhuma solução encontrada.")
    
    return len(vertices_cobertos)