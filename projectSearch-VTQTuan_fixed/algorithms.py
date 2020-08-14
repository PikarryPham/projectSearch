from utils import *
def a_star_graph_search(start, goal, maze_graph, N, M):
    path = []
    explored_nodes = list()
    
    if start == goal:
        return path, explored_nodes, len(explored_nodes)

    path.append(start)
    path_cost = 0
    heuristic = get_manhattan_heuristic(start, goal, N, M)
    frontier = PriorityQueue()
    f = heuristic + path_cost
    frontier.append((f, path))

    while frontier.size() > 0:
        f_till_now, path_till_now = frontier.pop()
        current_node = path_till_now[-1]
        path_cost_till_now = f_till_now - get_manhattan_heuristic(current_node, goal, N, M)

        if current_node not in explored_nodes:
            if current_node == goal:
                explored_nodes.append(current_node)
                return path_till_now, explored_nodes, len(explored_nodes)

            explored_nodes.append(current_node)

            neighbours = maze_graph[current_node]
            neighbours_list_int = [int(n) for n in neighbours]
            neighbours_list_int.sort(reverse=False)
            neighbours_list_str = [str(n) for n in neighbours_list_int]

            for neighbour in neighbours_list_str:
                path_to_neighbour = path_till_now.copy()
                path_to_neighbour.append(neighbour)
                neighbour_cost = 1 + path_cost_till_now
                neighbour_heuristic = get_manhattan_heuristic(neighbour, goal, N, M)
                f_neighbour = neighbour_cost + neighbour_heuristic

                is_there, indexx, f_neighbour_old, _ = get_node_information(frontier, neighbour)
                if not is_there:
                    frontier.append((f_neighbour, path_to_neighbour))
                elif is_there:
                    if f_neighbour_old >= f_neighbour:
                        frontier.remove(indexx)
                        frontier.append((f_neighbour, path_to_neighbour))
    return None, None, None
