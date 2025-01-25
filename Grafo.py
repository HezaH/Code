import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Grafo:
    def __init__(self):
        # Inicializa o dicionário para armazenar o grafo
        self.grafo_hcp = {}
        self.grafo_tsp = {}

    def add_vertice(self, vertice, grafo):
        # Adiciona um vértice ao grafo
        if vertice not in grafo:
            grafo[vertice] = {}

    def add_aresta(self, vertice1, vertice2, peso, grafo):
        # Adiciona uma aresta entre os vértices com um peso (distância)
        if vertice1 in grafo and vertice2 in grafo:
            if vertice2 != vertice1:
                grafo[vertice1][vertice2] = peso
                grafo[vertice2][vertice1] = peso

    def exibir_grafo(self, grafo):
        # Exibe o grafo com os pesos das arestas
        for vertice in grafo:
            print(f"{vertice}: {grafo[vertice]}")
    
    def neighbor(self, vertice, grafo): 
        """Retorna todos os vizinhos do vértice dado.""" 
        if vertice in grafo: 
            return list(grafo[vertice].keys()) 
        else: 
            return []

    def remove_aresta(self, vertice1, vertice2, grafo):
        # Remove uma aresta entre dois vértices
        if vertice1 in grafo and vertice2 in grafo:
            if vertice2 in grafo[vertice1]:
                del grafo[vertice1][vertice2]
                del grafo[vertice2][vertice1]
                print(f"Aresta entre {vertice1} e {vertice2} removida")
            else:
                print(f"Aresta entre {vertice1} e {vertice2} não encontrada")
        else:
            print(f"Vértices não encontrados")
    
    def gerar_matriz_adjacencia(self, grafo): 
        # Obter a lista de vértices 
        vertices = list(grafo.keys()) 
        n = len(vertices) 
        # Criar um dicionário para mapear os vértices para índices 
        indice = {vertices[i]: i for i in range(n)} 
        
        # Inicializar a matriz de adjacências com infinito (ausência de aresta) 
        matriz_adjacencia = np.full((n, n), float('inf')) 
        
        # Preencher a matriz de adjacências com os pesos das arestas 
        for v1 in grafo: 
            for v2 in grafo[v1]: 
                i, j = indice[v1], indice[v2] 
                matriz_adjacencia[i][j] = grafo[v1][v2] 
                
        # Substituir os elementos diagonais (vértice para ele mesmo) por zero 
        np.fill_diagonal(matriz_adjacencia, 0) 
        
        return matriz_adjacencia
        
    def atualizar_peso_aresta(self, vertice1, vertice2, novo_peso, grafo):
        """ Atualiza o peso de uma aresta e ajusta os caminhos afetados dinamicamente """
        if vertice1 in grafo and vertice2 in grafo:
            if vertice2 in grafo[vertice1]:
                grafo[vertice1][vertice2] = novo_peso
                grafo[vertice2][vertice1] = novo_peso
                print(f"Peso da aresta ({vertice1}, {vertice2}) atualizado para {novo_peso}")
            else:
                print(f"Aresta ({vertice1}, {vertice2}) não existe")
        else:
            print(f"Vértices {vertice1} ou {vertice2} não encontrados")
    
    def dividir_lista(self, lista, m):
        """Divide uma lista em sublistas de tamanho m."""
        return [lista[i:i + m] for i in range(0, len(lista), m)]

    def gerar_automaticamente_arestas(self, num_vertices, heigth_x, grafo):
        """Gera vértices e arestas mantendo um padrão de conexão e assegura que vértices soltos tenham conexões adicionais."""
        # Programação Dinâmica: Cache dos vértices criados
        vertices = [f"v{i}" for i in range(1, num_vertices + 1)]
        
        # Adiciona vértices ao grafo
        for vertice in vertices:
            self.add_vertice(vertice, grafo)

        # Divide os vértices em camadas de tamanho `heigth_x`
        camadas = self.dividir_lista(vertices, heigth_x)

        # Conectar vértices dentro de cada camada
        for camada in camadas:
            for i in range(len(camada) - 1):
                peso = random.randint(117, 155)
                self.add_aresta(camada[i], camada[i + 1], peso, grafo)

        # Conectar camadas adjacentes
        for i in range(len(camadas) - 1):
            min_length = min(len(camadas[i]), len(camadas[i + 1]))  # Evita IndexError
            for j in range(min_length):
                peso = random.randint(41, 67)
                self.add_aresta(camadas[i][j], camadas[i + 1][j], peso, grafo)

        # Adicionar conexões adicionais para vértices soltos
        for vertice in vertices:
            if len(grafo[vertice]) == 1:  # Verifica se o vértice está solto (apenas uma conexão)
                conexao = list(grafo[vertice].keys())[0]
                neighbor = sorted(self.neighbor(conexao, grafo))
                neighbor.remove(vertice)
                
                peso = random.randint(41, 67)
                self.add_aresta(vertice, neighbor[-1] , peso, grafo)

    def verificar_conectividade(self, grafo):
        """Verifica se o grafo é conexo."""
        visitados = set()
        def dfs(v):
            if v not in visitados:
                visitados.add(v)
                for vizinho in grafo[v]:
                    dfs(vizinho)
        # Inicie a busca a partir do primeiro vértice
        dfs(next(iter(grafo)))
        return len(visitados) == len(grafo)

    def conectar_componente(self, grafo):
        """Conecta componentes desconexos do grafo."""
        vertices = list(grafo.keys())
        visitados = set()

        def dfs(v):
            if v not in visitados:
                visitados.add(v)
                for vizinho in grafo[v]:
                    dfs(vizinho)

        # Inicie a busca a partir do primeiro vértice
        for vertice in vertices:
            if vertice not in visitados:
                # Conectar o vértice não visitado ao grafo
                for u in visitados:
                    peso = random.randint(41, 67)
                    self.add_aresta(u, vertice, peso, grafo)
                    break
            dfs(vertice)

    def atualizar_grafo(self, vertices, heigth_x, grafo):
        # Divide os vértices em camadas de tamanho `heigth_x`
        camadas = self.dividir_lista(vertices, heigth_x)
        
        # Conectar vértices dentro de cada camada
        if heigth_x > 1:
            for i in range(len(camadas[1]) - 1):
                peso = random.randint(117, 155)
                self.atualizar_peso_aresta(camadas[1][i], camadas[1][i + 1], peso, grafo)
    
    def transformar_formatos(self, grafo,  arestas):
        for origem, destino, peso in arestas:
            if origem not in grafo:
                grafo[origem] = {}
            if destino not in grafo:
                grafo[destino] = {}
            grafo[origem][destino] = peso
            grafo[destino][origem] = peso  # Supondo que o grafo seja não dirigido
    
    def re_transformar_formatos(self, grafo):
        arestas = []
        # Preencher a lista de arestas com os dados do dicionário
        for origem, destinos in grafo.items():
            for destino, peso in destinos.items():
                # Adicionar a aresta à lista se não estiver presente (evitar duplicatas)
                if (destino, origem, peso) not in arestas:
                    arestas.append((origem, destino, peso))
        return arestas
    
    def visualizar_grafo(self, grafo, fig_name, vertices_destaque=None):
        if vertices_destaque is None:
            vertices_destaque = []
        
        G = nx.Graph()

        # Adicionando vértices e arestas com peso
        for vertice, vizinhos in grafo.items():
            for vizinho, peso in vizinhos.items():
                G.add_edge(vertice, vizinho, weight=peso)

        num_nos = len(G.nodes)#Numero total de nos
        # Definir o layout dinamicamente
        if num_nos <= 10:
            pos = nx.shell_layout(G)
        elif num_nos <= 50:
            pos = nx.kamada_kawai_layout(G)
        else:
            pos = nx.spring_layout(G, seed=42, k=3 / num_nos) #Refino diamico

        plt.figure(figsize=(max(12, num_nos // 5), max(8, num_nos // 6))) #Ajusta o tamanho da figura em funcao dos nos
        plt.axis('off')  # Remover a moldura
        #Ajusta o tamanho da figuta baseado no numero de nos
        node_size = max(800, 5000 // num_nos)
        font_size = max(6, 16 - num_nos // 10)

        # Definir cores para os nós
        node_colors = ['red' if node in vertices_destaque else 'lightblue' for node in G.nodes]
        
        # Desenhando os nós
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_size)
        
        # Destacar as arestas com peso 500
        edges = G.edges(data=True)
        edge_colors = ['red' if edge[2]['weight'] == 500 else 'gray' for edge in edges]
        edge_styles = ['dotted' if edge[2]['weight'] == 500 else 'solid' for edge in edges]
        #Desenho de nos e arestas
        for style in set(edge_styles):
            edges_style = [edge[:2] for edge, es in zip(edges, edge_styles) if es == style]
            edge_c = [color for color, es in zip(edge_colors, edge_styles) if es == style]
            nx.draw_networkx_edges(G, pos, edgelist=edges_style, edge_color=edge_c, style=style, width=2)

        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_labels(G, pos, font_size=font_size, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=max(6, font_size - 2))

        plt.title("Visualização Dinâmica do Grafo", fontsize=16)
        plt.savefig(fig_name+".jpg", format="jpeg", dpi=300, bbox_inches='tight')


