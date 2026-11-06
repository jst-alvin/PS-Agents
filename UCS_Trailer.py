import heapq
from itertools import count

# Directed road network: (destination, distance in kilometres)
graph = {
    "Nairobi": [
        ("Nakuru", 163),
        ("Narok", 145),
    ],
    "Nakuru": [
        ("Kericho", 107),
        ("Eldoret", 156),
    ],
    "Narok": [
        ("Bomet", 81),
    ],
    "Bomet": [
        ("Kericho", 76),
    ],
    "Kericho": [
        ("Kisumu", 84),
    ],
    "Eldoret": [
        ("Kisumu", 138),
    ],
    "Kisumu": [],
}


def uniform_cost_search(graph, start, goal):
    """Return the least-cost path and show the UCS traversal."""
    sequence = count()

    # Each queue item is: (total_cost, insertion_order, current_node, path)
    frontier = [(0, next(sequence), start, [start])]
    best_cost = {start: 0}
    explored = set()

    print(f"START: {start}")
    print(f"GOAL:  {goal}\n")
    print("UNIFORM COST SEARCH")
    print("-" * 65)

    while frontier:
        cost, _, current, path = heapq.heappop(frontier)

        # Ignore an outdated queue entry.
        if cost != best_cost.get(current):
            continue

        if current in explored:
            continue

        explored.add(current)
        print(f"Expand {current:<10} | Path cost: {cost:>3} km")

        # UCS stops when the goal is removed from the priority queue.
        if current == goal:
            print("\nGOAL REACHED")
            return path, cost

        for neighbour, edge_cost in graph.get(current, []):
            new_cost = cost + edge_cost

            if neighbour not in explored and new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                new_path = path + [neighbour]
                heapq.heappush(
                    frontier,
                    (new_cost, next(sequence), neighbour, new_path)
                )
                print(
                    f"  Add {neighbour:<10} | "
                    f"Edge: {edge_cost:>3} km | "
                    f"Total: {new_cost:>3} km"
                )

        print()

    return None, float("inf")


if __name__ == "__main__":
    optimal_path, total_cost = uniform_cost_search(
        graph,
        start="Nairobi",
        goal="Kisumu"
    )

    print("-" * 65)
    if optimal_path:
        print("OPTIMAL PATH:")
        print(" -> ".join(optimal_path))
        print(f"TOTAL PATH COST: {total_cost} km")
    else:
        print("No route was found.")
