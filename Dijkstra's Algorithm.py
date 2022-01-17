import timeit
import heapq
import sys
def Distace_Calculatio(graph, Staring_Vertix):
    Distances = {vertex: float('infinity') for vertex in graph}
    Distances[Staring_Vertix] = 0
    Priority_Queue = [(0, Staring_Vertix)]
    while len(Priority_Queue) > 0:
        Current_Distance, Current_Vertes = heapq.heappop(Priority_Queue)
        if Current_Distance > Distances[Current_Vertes]:
            continue
        for neighbor, weight in graph[Current_Vertes].items():
            Dist = Current_Distance + weight
            if Dist < Distances[neighbor]:
                Distances[neighbor] = Dist
                heapq.heappush(Priority_Queue, (Dist, neighbor))
    return Distances

def value(val1, val2, graph):
    return graph[val1][val2]

def Get_Edges(node, nodes, graph):
    connection =[]
    for i in nodes:
        if graph[node].get(i, False) != False:
            connection.append(i)
    return connection
def dijkstra_algorithm(graph,start_node):
        graph = graph
        unvisited_nodes = ['U','V','W','X','Y','Z']
        Shortest_path = {}
        Previous_Nodes = {}
        Maximum_Value = sys.maxsize
        for node in unvisited_nodes:
            Shortest_path[node] = Maximum_Value
        Shortest_path[start_node] = 0    
        while unvisited_nodes:
            Current_Minimum_Node = None
            for node in unvisited_nodes: 
                if Current_Minimum_Node == None:
                    Current_Minimum_Node = node
                elif Shortest_path[node] < Shortest_path[Current_Minimum_Node]:
                    Current_Minimum_Node = node
            neighbors = Get_Edges(Current_Minimum_Node, unvisited_nodes, graph)
            for neighbor in neighbors:
                Tenative_Value = Shortest_path[Current_Minimum_Node] + value(Current_Minimum_Node, neighbor,graph)
                if Tenative_Value < Shortest_path[neighbor]:
                    Shortest_path[neighbor] = Tenative_Value
                    Previous_Nodes[neighbor] = Current_Minimum_Node
            unvisited_nodes.remove(Current_Minimum_Node)
        return Previous_Nodes, Shortest_path
    
graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 2},
    'Z': {'W': 5, 'Y': 2},}

print('Following are the shortest route from the node "X" Using Dijistra Having Complexity n2 ')
print(Distace_Calculatio(graph,'X'))
print('\n')
print('Following are the shortest route from the node "X" Using Dijistra Having Complexity nlogn ')
print(dijkstra_algorithm(graph,'X'))
print('\n')

Time = timeit.timeit(lambda: dijkstra_algorithm(graph,'X'), number=10)
print('Time Taken By Dijistra Having Complexity nlogn: ',"{:.6f}".format(round(Time, 10)))