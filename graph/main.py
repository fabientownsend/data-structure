from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for _ in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        for i in range(self.vertices):
            print("|", i, end=" | => ")

            temp = self.array[i].get_head()
            while temp:
                print("[", temp.value, end=" ] -> ")
                temp = temp.next

            print("None")


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()
