edges = int(input())
case = 1

while edges != 0:
    # build graph 
    graph = {}
    ans = set()
    for _ in range(edges):
        node1, node2 = input().split()
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

    # for each node, determine all different paths to each node of length greater than two 
    for node in graph:

        neighbors = list(graph[node]) # deep copy 
        visitedNodes = set(node)
        
        while len(neighbors) > 0:
            nextNode = neighbors.pop(0)

            # if we haven't seen this node 
            if nextNode not in visitedNodes:
                visitedNodes.add(nextNode)
                if nextNode in graph: # add all nodes we can now reach from this node 
                    for x in graph[nextNode]:
                        neighbors.append(x)
                        if x in graph[node]: #this node was reachable from two paths and one path is of length one, therefor redundant 
                            ans.add((node, x))

    #clean up and print the answer
    listAns = list(ans)
    listAns.sort()

    print("Case %d: %d" % (case, len(listAns)), end=" ")

    for x,y in listAns:
        print("%s,%s" % (x, y), end=" ")
        
    print()

    case += 1
    edges = int(input())