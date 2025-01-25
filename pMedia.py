from docplex.mp.model import Model
def pMedia(arestas, vertices, grafo, p, model_name):
    # Criar modelo
    mdl = Model(name=model_name)

    # Variável binária y[i]: 1 se um centro de atendimento (facilidade) for aberto em i, 0 caso contrário
    y = {i: mdl.binary_var(name=f"y_{i}") for i in vertices}

    # Variável binária x[i, j]: 1 se o cliente i for atendido pela facilidade em j, 0 caso contrário
    x = {(i, j): mdl.binary_var(name=f"x_{i}_{j}") for i in vertices for j in vertices}

    # Função objetivo: minimizar a soma das distâncias entre os clientes e as facilidades que os atendem
    mdl.minimize(mdl.sum(x[i, j] * dist for (i, j, dist) in arestas for j in vertices if (i, j) in x))

    # Restrição (7): Cada cliente deve ser atendido por exatamente uma facilidade
    for i in vertices:
        mdl.add_constraint(mdl.sum(x[i, j] for j in vertices) == 1, f"assign_{i}")

    # Restrição (8): Um cliente só pode ser atendido por uma facilidade se essa facilidade foi aberta
    for i in vertices:
        for j in vertices:
            mdl.add_constraint(x[i, j] <= y[j], f"open_if_assigned_{i}_{j}")

    # Restrição (9): Exatamente p facilidades devem ser abertas
    mdl.add_constraint(mdl.sum(y[i] for i in vertices) == p, "p_medians")

    # Resolver o modelo
    solucao = mdl.solve()

    # Exibir resultados
    if solucao:
        facilidades_abertas = [i for i in vertices if y[i].solution_value > 0.5]
        facilidades_abertas = sorted(facilidades_abertas, key=lambda x: int(x[1:]))
        atribuicoes = [(i, j) for i in vertices for j in vertices if x[i, j].solution_value > 0.5]

        print("Facilidades abertas:")
        print(facilidades_abertas)

        print("\nAtribuições de clientes às facilidades:")
        for i, j in atribuicoes:
            print(f"Cliente {i} é atendido pela facilidade em {j}")

        print(f"\nDistância total minimizada: {solucao.objective_value}")
        grafo.visualizar_grafo(grafo.grafo_hcp, vertices_destaque=facilidades_abertas)  
    else:
        print("Nenhuma solução encontrada.")

    return