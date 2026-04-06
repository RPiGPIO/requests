def pagerank(graph, d=0.85, iterations=3):
    pages = list(graph.keys())

    # Initial rank
    ranks = {page: 1 for page in pages}

    for i in range(iterations):
        new_ranks = {}

        for page in pages:
            rank_sum = 0

            for other_page in pages:
                if page in graph[other_page]:
                    out_degree = len(graph[other_page])
                    rank_sum += ranks[other_page] / out_degree

            new_ranks[page] = (1 - d) + d * rank_sum

        ranks = new_ranks
        print(f"Iteration {i+1}: {ranks}")

    return ranks


graph = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"]
}

pagerank(graph)
