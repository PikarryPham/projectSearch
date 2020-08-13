#author: VTQTuan
import re
#Node in the graph
#do not edit this class
class Node:
    """
    attribute:
        content:
            0: empty path
            1: wall
            2: food
            3: monster
        position: the (x, y) position
        num_order: numerical order of this position (using to find path like lab01)
    """
    def __init__(self, pos_init, content_init, num_order_init):
        """
        Constructor of class Node
        """
        #initialize position of this node
        self.position = pos_init
        #initialize content of this node
        self.content = content_init
        #initialize numerical order of this node
        self.num_order = num_order_init

    def __str__(self):
        """
        Using for print function in python.
        return:
            pos: position of this node in map graph -> tuple(x,y)
            content:
                0: empty path
                1: wall
                2: food
                3: monster
            number_order: numerical order of this position (using to find path like lab01)
            number_order was numbering from left to right, along axis=1 and down to axis=0
        """
        return "pos: {}".format(self.position) + "\ncontent: {}".format(self.content) + "\nnumber order: {}".format(self.num_order)

    def list_node_near(self):
        """
        From this position of this node, find the left node, right node, up node, down node
        return:
            list_node_position: list of node's position near the node call this function
        """
        list_node_position = []

        (x,y) = self.position
        near_x = x - 1
        near_y = y
        if (near_x >= 0 and near_y >= 0):
            list_node_position.append((near_x, near_y))
        
        near_x = x + 1
        near_y = y
        if (near_x >= 0 and near_y >= 0):
            list_node_position.append((near_x, near_y))

        near_x = x
        near_y = y - 1
        if (near_x >= 0 and near_y >= 0):
            list_node_position.append((near_x, near_y))
        
        near_x = x
        near_y = y + 1
        if (near_x >= 0 and near_y >= 0):
            list_node_position.append((near_x, near_y))
        
        return list_node_position

    def copy_of_node(self, position_or_content):
        """
        return a copy of information of current node.
        """
        if self.position == position_or_content or self.content == position_or_content:
            return Node(self.position, self.content, self.num_order)

    def numerical_of_node(self, position_or_content):
        """
        return the numerical order of the current node if it matchs the position or content
        """
        if self.position == position_or_content or self.content == position_or_content:
            return self.num_order
            
    def content_of_node(self, position):
        """
        return the content of current node if it matchs the position
        """
        if self.position == position:
            return self.content

#preprocessing line by line of the input file.
#do not edit this function.
def process_line_by_line(line):
    list_token = re.split(" |\n", line)
    del list_token[-1]
    return list_token

#read the input file. 
#do not edit this function.
def read_file(file_name):
    """
    Read the file input (.txt)
    return:
        int(N): N rows of this map -> concast to int
        int(M): M columns of this map -> concast to int
        start: (x, y) is the position of the start, type(x) == type(y) == class <'str'>
        map_matrix: matrix indicate the map of game, each element contain the content
        of every node at map, type(content) == str.
    """
    file = open(file_name, 'r')
    #read the map information.
    map_inf = process_line_by_line(file.readline())
    #N: number of rows, M: number of columns
    N, M = tuple(map_inf)
    #read all of file input. 
    all_lines = file.readlines()
    #start position. 
    start = tuple(process_line_by_line(all_lines[-1]))
    del all_lines[-1]
    #read the matrix of this map
    map_matrix = []
    for i in range(len(all_lines)):
        line = process_line_by_line(all_lines[i])
        map_matrix.append(line)
    return int(N), int(M), start, map_matrix

#pre processing the matrix of map to list of node on graph
#do not edit this function.
def process_map_matrix(map_matrix):
    num = 0
    #list of all node on the map
    list_node = []
    map_graph = dict()
    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[i])):
            node = Node((i, j), map_matrix[i][j], str(num))
            num += 1
            list_node.append(node)

    #
    for node in list_node:
        if node.content != '1' and node.content != '3':
            near_curr_node = node.list_node_near()
            adjacency_list = []
            for pos in near_curr_node:
                #print(pos)
                for item in list_node:
                    if item.numerical_of_node(pos) != None and item.content_of_node(pos) != '1' and         item.content_of_node(pos) != '3':
                        adjacency_list.append(item.numerical_of_node(pos))
            #print(adjacency_list)
            map_graph["{}".format(node.num_order)] = adjacency_list

        
    return list_node, map_graph

#Map
#can be edit for using.
class Map:
    """
    attribute:
        N: number of rows of this map
        M: number of columns of this map
        start_node: node in graph where pacman starting it's actions
        list_foods: list of nodes in graph contain position of foods
        map_graph: dictionary of node and it's adjacency node is empty path
        list_of_nodes: list all nodes in graph indicating for map of game.
        list_of_monsters: list all nodes in graph contain position of monsters
    """
    def __init__(self, file_name):
        self.N, self.M, start, map_matrix = read_file(file_name)
        self.list_of_nodes, self.map_graph = process_map_matrix(map_matrix)

        start = (int(start[0]), int(start[1]))
        for node in self.list_of_nodes:
            res = node.copy_of_node(start)
            if res != None:
                self.start = res
                break
        
        self.list_foods = []

        for node in self.list_of_nodes:
            res = node.copy_of_node('2')
            if res != None:
                self.list_foods.append(res)
        
        self.list_monsters = []
        for node in self.list_of_nodes:
            res = node.copy_of_node('3')
            if res != None:
                self.list_monsters.append(res)


