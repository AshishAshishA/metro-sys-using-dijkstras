from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.adjList={}
    
    def addNode(self,node1:str,node2:str,wt:int):
        if node1 not in self.adjList:
            self.adjList[node1]=[]
        if node2 not in self.adjList:
            self.adjList[node2]=[]
        
        self.adjList[node1].append((node2,wt))
        self.adjList[node2].append((node1,wt))

    def dijkstras(self,src:str):
        distMap={node:float('inf') for node in self.adjList}
        parent={node:node for node in self.adjList}
        distMap[src]=0

        pq=PriorityQueue()

        pq.put((0,src))

        while not pq.empty():
            c_dist,c_node=pq.get()
            
            for nbr,wt in self.adjList[c_node]:
                if c_dist+wt < distMap[nbr]:
                    distMap[nbr]=c_dist+wt
                    parent[nbr]=c_node
                    pq.put((distMap[nbr],nbr))

        return distMap,parent



    def printList(self):
        for node,nbrs in self.adjList.items():
            print(f"{node}: ",end="")
            for nbr,wt in nbrs:
                print(f"{nbr}-{wt} ",end="")
            print()

class Metro:
    def __init__(self):
        self.g=Graph()
        self.g.addNode('a','b',2)
        self.g.addNode('a','c',8)
        self.g.addNode('a','c',1)
        self.g.addNode('b','d',4)
        self.g.addNode('d','f',5)
        self.g.addNode('c','e',8)
        self.g.addNode('e','f',6)

    def get_Metro_List(self):
        self.g.printList()

    def get_shortest_Dist(self,src,dest):
        distMap,parent = self.g.dijkstras(src)

        node = dest
        #commented
            # print("------------Shortest Route-------------\n")
            # print(f"DEST--{dest}<-- ", end='')
            # while parent[node] != node:
            #     cost = distMap[node] - distMap[parent[node]]
            #     print(f"{cost}unit--{parent[node]}--", end='')
            #     node = parent[node]
            # print(f"<-- START")

            # print()

            # print(f"{src}-->{distMap[dest]}unit(total)-->{dest}")
            # print("\n----------------------------------------")

        station_list=[]
        while parent[node] != node:
            cost = distMap[node] - distMap[parent[node]]
            station_list.append((node,cost))
            node = parent[node]
        station_list.reverse()

        return distMap[dest],station_list


if __name__=="__main__":
    bhopal_metro=Metro()
    bhopal_metro.get_shortest_Dist('a','f')

    
