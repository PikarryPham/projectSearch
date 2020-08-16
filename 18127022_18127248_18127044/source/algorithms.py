from utils import *
def breadth_first_graph_search(maze_graph, start, goal):
    path = []
    explored_nodes = list()

    if start == goal:
        return path, explored_nodes, len(explored_nodes)

    path.append(start)
    frontier = [path]
    while len(frontier) > 0:
        path_till_now = frontier.pop(0)
        current_node = path_till_now[-1]

        if current_node not in explored_nodes:
            
            explored_nodes.append(current_node)
            neighbours = maze_graph[current_node]
            neighbours_list_int = [int(n) for n in neighbours]
            neighbours_list_int.sort(reverse=False)
            neighbours_list_str = [str(n) for n in neighbours_list_int]

            for neighbour in neighbours_list_str:

                path_to_neighbour = path_till_now.copy()
                path_to_neighbour.append(neighbour)
                if neighbour == goal:
                    explored_nodes.append(goal)
                    return path_to_neighbour, explored_nodes, len(explored_nodes)
                frontier.append(path_to_neighbour)
    return None, None, None

def uniform_cost_search(maze_graph, start, goal):
    path = []
    explored_nodes = list()

    if start == goal:
        return path, explored_nodes, len(explored_nodes)

    path.append(start)
    path_cost = 0

    frontier = PriorityQueue()
    frontier.append((path_cost, path))
    while frontier.size() > 0:

        path_cost_till_now, path_till_now = frontier.pop()
        current_node = path_till_now[-1]
        explored_nodes.append(current_node)

        if current_node == goal:
            return path_till_now, explored_nodes, len(explored_nodes)

        neighbours = maze_graph[current_node]

        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int.sort(reverse=False)
        neighbours_list_str = [str(n) for n in neighbours_list_int]

        for neighbour in neighbours_list_str:
            path_to_neighbour = path_till_now.copy()
            path_to_neighbour.append(neighbour)
            neighbour_cost = 1 + path_cost_till_now
            new_element = (neighbour_cost, path_to_neighbour)

            is_there, indexx, neighbour_old_cost, _ = get_node_information(frontier, neighbour)

            if (neighbour not in explored_nodes) and not is_there:
                frontier.append(new_element)

            elif is_there:
                if neighbour_old_cost > neighbour_cost:
                    frontier.remove(indexx)
                    frontier.append(new_element)
    return None, None, None
    
def depth_first_tree_search(maze_graph, start, goal):
    path = []
    expand_nodes = list()
    if start == goal:
        return path, expand_nodes

    path.append(start)
    frontier = [path]
    while len(frontier) > 0:
        path_till_now = frontier.pop()
        current_node = path_till_now[-1]
        expand_nodes.append(current_node)

        neighbours = maze_graph[current_node]
        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int.sort(reverse=True)
        neighbours_list_str = [str(n) for n in neighbours_list_int]

        for neighbour in neighbours_list_str:
            if neighbour not in path_till_now:
                path_to_neighbour = path_till_now.copy()
                path_to_neighbour.append(neighbour)
                frontier.append(path_to_neighbour)
                
                if neighbour == goal:
                    return path_to_neighbour, expand_nodes
                else:
                    frontier.append(path_to_neighbour)

    return None, None

def depth_first_limit_tree_search(maze_graph, start, goal, limit):
    path = []
    expand_nodes = list()
    if start == goal:
        return path, expand_nodes, len(expand_nodes)

    path.append(start)
    frontier = [path]
    while len(frontier) > 0:
        path_till_now = frontier.pop()
        current_node = path_till_now[-1]
        expand_nodes.append(current_node)

        if current_node == goal:
            return path_till_now, expand_nodes, len(expand_nodes)

        if len(path_till_now) <= limit: 
            neighbours = maze_graph[current_node]
            neighbours_list_int = [int(n) for n in neighbours]
            neighbours_list_int.sort(reverse=True)
            neighbours_list_str = [str(n) for n in neighbours_list_int]

            for neighbour in neighbours_list_str:
                if neighbour not in path_till_now:
                    path_to_neighbour = path_till_now.copy()
                    path_to_neighbour.append(neighbour)
                    frontier.append(path_to_neighbour)

    return None,expand_nodes, len(expand_nodes)

def iterative_depeening_search(maze_graph, start, goal):
    expand_list = list()
    time = 0
    for i in range(0, max_possible_value):
        path, expand_nodes, timeout = depth_first_limit_tree_search(maze_graph, start, goal, i)
        time += timeout
        expand_list.append(expand_nodes)
        if path != None:
            return path, expand_list, time

def greedy_best_first_graph_search(start, goal, maze_graph, N, M):
    path = []
    explored_nodes = list()

    if start == goal:
        return path, explored_nodes, len(explored_nodes)

    path.append(start)

    heuristic = get_manhattan_heuristic(start, goal, N, M)
    frontier = PriorityQueue()
    frontier.append((heuristic, path))

    while frontier.size() > 0:
        heuristic_till_now, path_till_now = frontier.pop()
        current_node = path_till_now[-1]

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
                neighbour_heuristic = get_manhattan_heuristic(neighbour, goal, N, M)
                frontier.append((neighbour_heuristic, path_to_neighbour))
    return None, None, None 

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

