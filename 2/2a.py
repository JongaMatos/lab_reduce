# Implementação do algoritmo PageRank em Python
def pagerank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    num_pages = len(graph)
    initial_value = 1.0 / num_pages
    ranks = [initial_value] * num_pages

    for _ in range(max_iterations):
        new_ranks = [0] * num_pages
        for i in range(num_pages):
            for j in range(num_pages):
                if graph[j][i]:
                    new_ranks[i] += ranks[j] / sum(graph[j])
        
        # Aplicar fator de amortecimento
        new_ranks = [(1 - damping_factor) / num_pages + damping_factor * rank for rank in new_ranks]

        # Verificar a convergência
        if sum(abs(new_ranks[i] - ranks[i]) for i in range(num_pages)) < tolerance:
            return new_ranks

        ranks = new_ranks

    return ranks

# Exemplo de uso
graph = [
    [0, 1, 1],
    [1, 0, 0],
    [0, 1, 0]
]
result = pagerank(graph)
print("PageRank:", result)
