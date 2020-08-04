from queue import PriorityQueue
import datetime
import timeit
import time
# f = open("input.txt", "r")
# g = open("output.txt", "w")

# f = open("input1.txt", "r")
# g = open("output1.txt", "w")

f = open("../input/input2.txt", "r")
g = open("../output/output2.txt", "w")

# f = open("input3.txt", "r")
# g = open("output3.txt", "w")
edges = []
exit_node = 0
n = 0
ok = []
trace = []
queue = []
times = 0
is_found = 0

# helper


def distance(src, dst):
    global n
    x1 = src % n
    y1 = int(src/n)
    x2 = dst % n
    y2 = int(dst/n)
    return abs(x1-x2) + abs(y1 - y2)


# function
# def execution_time():
#     start_time = datetime.datetime.now()

#     x = 0
#     for i in range(1000):
#         x += i

#     end_time = datetime.datetime.now()

#     time_diff = (end_time - start_time)
#     exeTime = time_diff.total_seconds() * 1000
#     return exeTime


def read_input():
    inp = f.read()
    inp = inp.split('\n')

    global n, exit_node, edges
    n = int(inp[0])
    cnt = 1

    for i in range(0, n*n):
        edges.append([])
        edges[i] = []
        line = inp[cnt]
        cnt = cnt + 1
        list_neary_by = line.split(' ')
        for j in range(0, len(list_neary_by)):
            v = int(list_neary_by[j])
            edges[i].append(v)

    exit_node = int(inp[cnt])
    cnt = cnt + 1


def init():
    global ok, trace
    ok = []
    trace = []

    for i in range(0, n*n+1):
        ok.append(1)

    for i in range(0, n*n+1):
        trace.append(-1)


def visit(u):
    global trace, ok, exit_node, is_found

    if (is_found == 1):
        return

    ok[u] = 0

    if (u == exit_node):
        is_found = 1
        return

    for index in range(0, len(edges[u])):
        v = edges[u][index]
        if (ok[v] == 1):
            trace[v] = u
            visit(v)


def IDS():
    init()
    start = time.time()
    global is_found
    is_found = 0
    visit(0)

    global times
    print("IDS")
    g.write("IDS\n")
    times = 0
    print_result(exit_node)
    print()
    g.write("\n\n")
    end = time.time()
    g.write("Time measured: " + str(end-start) + "\n\n")
    print("Time measured:", end - start)


def bfs():
    init()
    start = time.time()
    global trace, times, ok, is_found
    is_found = 0
    queue.append(0)
    trace[0] = 0

    while (len(queue) > 0):
        u = queue.pop(0)

        for index in range(0, len(edges[u])):
            if (is_found == 1):
                break

            v = edges[u][index]
            if (ok[v] == 1):
                queue.append(v)
                ok[v] = 0
                trace[v] = u
                if (v == exit_node):
                    is_found = 1
                    break

    print("BFS")
    g.write("BFS\n")
    times = 0
    print_result(exit_node)
    print()
    g.write("\n\n")
    end = time.time()
    g.write("Time measured: " + str(end-start) + "\n\n")
    print("Time measured:", end - start)


def print_result(u):
    global times, n, ok

    if (u == -1):
        return

    if (u == 0):
        print("times : ", times)
        g.write("times : " + str(times) + "\n")

        print('explored node: ')
        for index in range(0, n*n):
            if (ok[index] == 0):
                print(index, end=' ')
                g.write(str(index) + " ")

        print()
        g.writelines("\n")

        print(0, end='')
        g.write(str(0))
        return

    times = times + 1
    print_result(trace[u])
    print(" ->", u, end='')
    g.write(" -> " + str(u))


def uniform_cost_search():
    init()
    start = time.time()
    global exit_node, ok, edges, times

    print("uniform_cost_search")
    g.write("uniform_cost_search\n")

    d = []
    for i in range(0, n*n+1):
        d.append(1000000000)
    d[0] = 0

    queue = PriorityQueue()
    queue.put((d[0], 0))
    while queue.qsize():
        u = queue.get()
        u = u[1]
        if (u == exit_node):
            break

        if (ok[u] == 0):
            continue
        ok[u] = 0

        for index in range(0, len(edges[u])):
            v = edges[u][index]
            if (d[v] > d[u] + 1):
                d[v] = d[u] + 1
                queue.put((d[v], v))
                trace[v] = u

    times = 0
    print_result(exit_node)
    print()
    g.write("\n\n")
    end = time.time()
    g.write("Time measured: " + str(end-start) + "\n\n")
    print("Time measured:", end - start)


def visit_best(u):
    global trace, ok, exit_node, is_found

    if (is_found == 1):
        return

    ok[u] = 0

    if (u == exit_node):
        is_found = 1
        return

    queue = PriorityQueue()

    for index in range(0, len(edges[u])):
        v = edges[u][index]
        queue.put((distance(v, exit_node), v))

    while queue.qsize():
        v = queue.get()[1]
        if (ok[v] == 1):
            trace[v] = u
            visit_best(v)


def greedy_best_fs():
    init()
    start = time.time()
    print("greedy_best_fs")
    g.write("greedy_best_fs\n")

    global is_found, times
    is_found = 0
    visit_best(0)

    times = 0
    print_result(exit_node)
    print()
    g.write("\n\n")
    end = time.time()
    g.write("Time measured: " + str(end-start) + "\n\n")
    print("Time measured:", end - start)


def a_star():
    init()
    start = time.time()
    print("a_star")
    g.write("a_star\n")

    global exit_node, ok, edges, times
    d = []
    for i in range(0, n*n+1):
        d.append(1000000000)
    d[0] = 0

    queue = PriorityQueue()
    queue.put((d[0], 0))
    while queue.qsize():
        u = queue.get()
        u = u[1]
        if (u == exit_node):
            break

        if (ok[u] == 0):
            continue
        ok[u] = 0

        for index in range(0, len(edges[u])):
            v = edges[u][index]
            if (d[v] > d[u] + 1):
                d[v] = d[u] + 1
                queue.put((distance(v, exit_node), v))
                trace[v] = u

    times = 0
    print_result(exit_node)
    print()
    g.write("\n\n")
    end = time.time()
    g.write("Time measured: " + str(end-start) + "\n\n")
    print("Time measured:", end - start)


def main():
    read_input()
    bfs()
    print()

    IDS()
    print()

    uniform_cost_search()
    print()

    a_star()
    print()

    greedy_best_fs()
    print()


if __name__ == "__main__":
    main()
