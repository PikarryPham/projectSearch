import operator

def get_maze(fname):  # Get data from file
    N = X = 0
    M = []
    with open(fname, 'r') as f:
        fin = f.readlines()
    fin = [l.strip() for l in fin]
    N = int(fin[0])  # Size of matrix (NxN)
    X = int(fin[-1])  # Goal node
    M = [i.split(' ') for i in fin[1:-1]]  # Matrix of adjacent nodes
    M = [sorted([int(i) for i in M_i]) for M_i in M]
    print('Maze given: ' + str(M))
    if len(M) != N*N:
        print('<!> Not enough nodes given!')
        exit(1)
    return (M, X, N)


def print_result(path, explored, frontier, algo):
    print()
    if path[0] != -1:
        print('Path found (' + algo + '): \n    ' + str(path))
    else:
        print('No path found (' + algo + ').')
    print('    - Explored: ' + str(explored))
    print('    - Frontier: ' + str(frontier))
    if explored == []:
        print('    - Time taken: 0m')
        return
    if isinstance(explored[0], int):
        print('    - Time taken: ' + str(len(explored)) + 'm')
    else:
        leng = sum([len(e) for e in explored])
        print('    - Time taken: ' + str(leng) + 'm')


def BFS(problem):
    maze = problem[0]
    goal = problem[1]
    frontier = []
    explored = []
    trace = [-1] * len(maze)
    trace[0] = 0
    #
    if goal != 0:  # The goal is not at the start
        frontier.append(0)
        while frontier:
            node = int(frontier.pop(0))
            explored.append(node)
            for adj in maze[node]:
                if (adj not in explored) and (adj not in frontier):
                    trace[adj] = node
                    if goal == adj:
                        trace[goal] = node
                        break
                    frontier.append(adj)
            else:
                continue
            break
    #
    path = []
    trace_i = goal
    while True:
        path.append(trace_i)
        if trace_i == 0:
            break
        elif trace_i == -1:
            path = [-1]
            break
        trace_i = trace[trace_i]
    path = list(reversed(path))
    #
    print_result(path, explored, frontier, 'Breath First Search')
    return (path, explored, frontier)


def UCS(problem):
    cost = 1  # Cost to traverse to adj nodes
    maze = [[(0, adj_i) for adj_i in maze_i] for maze_i in problem[0]]
    goal = problem[1]
    frontier = []
    explored = []
    trace = [-1] * len(maze)
    trace[0] = 0
    #
    if goal != 0:  # The goal is not at the start
        frontier.append((0, 0))
        while frontier:
            node = frontier.pop(0)
            explored.append(node[1])
            # Sort the list -> Pop smallest cost first, then smallest val
            adjqueue = maze[node[1]]
            adjqueue.sort(key=operator.itemgetter(0, 1))
            for adj in adjqueue:
                if (adj[1] not in explored) and (adj not in frontier):
                    # Traverse cost of parent node + cost to traverse to adj
                    adj = (node[0] + cost, adj[1])
                    trace[adj[1]] = node[1]
                    if goal == adj[1]:
                        trace[goal] = node[1]
                        break
                    # Update cost
                    updated = False
                    for f_i in frontier:
                        if f_i[1] == adj[1]:
                            if f_i[0] > adj[0]:
                                frontier[frontier.index(f_i)] = adj
                                updated = True
                    if not updated:
                        frontier.append(adj)
            else:
                continue
            break
    #
    path = []
    trace_i = goal
    while True:
        path.append(trace_i)
        if trace_i == 0:
            break
        elif trace_i == -1:
            path = [-1]
            break
        trace_i = trace[trace_i]
    path = list(reversed(path))
    #
    print_result(path, explored, frontier, 'Uniform Cost Search')
    return (path, explored, frontier)


def IDS(problem):
    frontier = []
    ex_set = []
    path = []

    def dfs(lv):
        maze = problem[0]
        goal = problem[1]
        frontier = []
        explored = []
        trace = [-1] * len(maze)
        trace[0] = 0
        if goal != 0:  # The goal is not at the start
            frontier.append((0, 0))
            while frontier:
                node = frontier.pop()
                explored.append(node[1])
                for adj in list(reversed(maze[node[1]])):
                    if (adj not in explored):
                        if ((node[0] + 1, adj) not in frontier):
                            trace[adj] = node[1]
                            if goal == adj:
                                trace[goal] = node[1]
                                break
                            # Append adj nodes and it's level
                            frontier.append((node[0] + 1, adj))
                else:
                    # Remove invalid leveled nodes
                    frontier = [f for f in frontier if f[0] <= lv]
                    continue
                break
        #
        path = []
        trace_i = goal
        while True:
            path.append(trace_i)
            if trace_i == 0:
                break
            elif trace_i == -1:
                path = [-1]
                break
            trace_i = trace[trace_i]
        path = list(reversed(path))
        return (path, explored, frontier)
    lv = 0
    while True:
        d = dfs(lv)
        if len(ex_set) > 0 and ex_set[-1] == d[1]:  # Reached last level
            break
        ex_set.append(d[1])
        if d[0] != [-1]:
            path, frontier = d[0], d[2]
            break
        lv += 1
    if path == []:
        path = [-1]
    #
    print_result(path, ex_set, frontier, 'Iterative Deepening Search')
    return (path, ex_set, frontier)


def GFS(problem):
    maze = problem[0]
    goal = problem[1]
    frontier = []
    explored = []
    cost = []
    for maze_i in maze:
        cost_i = []
        for i in maze_i:
            dist_x = abs(i % problem[2] - goal % problem[2])
            dist_y = abs(i // problem[2] - goal // problem[2])
            cost_i.append(dist_x + dist_y)
        cost.append(cost_i)
    maze = [[(c_i, m_i) for (c_i, m_i) in zip(cost_i, maze_i)]
            for (cost_i, maze_i) in zip(cost, maze)]
    trace = [-1] * len(maze)
    trace[0] = 0
    #
    if goal != 0:  # The goal is not at the start
        frontier.append((0, 0))
        while frontier:
            node = frontier.pop(0)
            explored.append(node[1])
            # Sort the list -> Pop smallest cost first, then smallest val
            adjqueue = maze[node[1]]
            adjqueue.sort(key=operator.itemgetter(0, 1))
            for adj in adjqueue:
                if (adj[1] not in explored) and (adj not in frontier):
                    trace[adj[1]] = node[1]
                    if goal == adj[1]:
                        trace[goal] = node[1]
                        break
                    frontier.append(adj)
            else:
                continue
            break
    #
    path = []
    trace_i = goal
    while True:
        path.append(trace_i)
        if trace_i == 0:
            break
        elif trace_i == -1:
            path = [-1]
            break
        trace_i = trace[trace_i]
    path = list(reversed(path))
    #
    print_result(path, explored, frontier, 'Greedy-best First Search')
    return (path, explored, frontier)


def AS(problem):
    maze = problem[0]
    goal = problem[1]
    frontier = []
    explored = []
    h = []
    cost = 1
    for maze_i in maze:  # Manhattan distance
        h_i = []
        for i in maze_i:
            dist_x = abs(i % problem[2] - goal % problem[2])
            dist_y = abs(i // problem[2] - goal // problem[2])
            h_i.append(dist_x + dist_y)
        h.append(h_i)
    maze = [[(0, m_i) for m_i in maze_i] for maze_i in maze]
    trace = [-1] * len(maze)
    trace[0] = 0
    #
    if goal != 0:  # The goal is not at the start
        frontier.append((0, 0))
        last_h = [0] * len(maze[0])
        while frontier:
            node = frontier.pop(0)
            explored.append(node[1])
            # Sort the list -> Pop smallest cost first, then smallest val
            adjqueue = maze[node[1]]
            adjqueue.sort(key=operator.itemgetter(0, 1))
            for adj in adjqueue:
                if (adj[1] not in explored) and (adj not in frontier):
                    # f = f(node) - h(node) + cost + h(adj)
                    adj_i = adjqueue.index(adj)
                    adj_h = h[node[1]][adj_i]
                    node_h = last_h.pop(0)
                    adj = (node[0] - node_h + cost + adj_h, adj[1])
                    trace[adj[1]] = node[1]
                    if goal == adj[1]:
                        trace[goal] = node[1]
                        break
                    # Update cost
                    updated = False
                    for f_i in frontier:
                        if f_i[1] == adj[1]:
                            if f_i[0] > adj[0]:
                                frontier[frontier.index(f_i)] = adj
                                updated = True
                    if not updated:
                        frontier.append(adj)
                    last_h.append(adj_h if not updated else node_h)
            else:
                continue
            break
    #
    path = []
    trace_i = goal
    while True:
        path.append(trace_i)
        if trace_i == 0:
            break
        elif trace_i == -1:
            path = [-1]
            break
        trace_i = trace[trace_i]
    path = list(reversed(path))
    #
    print_result(path, explored, frontier, 'A* Search')
    return (path, explored, frontier)


def save_result(al, maze_data):
    with open('../output/output.txt', 'w') as fout:
        print('Maze given: ' + str(maze_data[0]), file=fout)
        print('    - Size: [%dx%d]' % (maze_data[2], maze_data[2]), file=fout)
        for a in al:
            path, explored, frontier, algo = a[0][0], a[0][1], a[0][2], a[1]
            if path[0] != -1:
                print('Path found (' + algo + '): \n    '+str(path), file=fout)
            else:
                print('No path found (' + algo + ').', file=fout)
            print('    - Explored: ' + str(explored), file=fout)
            print('    - Frontier: ' + str(frontier), file=fout)
            if explored == []:
                print('    - Time taken: 0m', file=fout)
                return
            if isinstance(explored[0], int):
                print('    - Time taken: '+str(len(explored)) + 'm', file=fout)
            else:
                leng = sum([len(e) for e in explored])
                print('    - Time taken: ' + str(leng) + 'm', file=fout)


maze_data = get_maze('../input/maze0.txt')
bfs = [BFS(maze_data), 'Breadth First Search']
ucs = [UCS(maze_data), 'Uniform Cost Search']
ids = [IDS(maze_data), 'Iterative Deepening Search']
gfs = [GFS(maze_data), 'Greedy-best First Search']
astar = [AS(maze_data), 'A* Search']
save_result([bfs, ucs, ids, gfs, astar], maze_data)
