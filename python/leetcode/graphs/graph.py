from collections import deque
import pprint


pp = pprint.PrettyPrinter(indent=4)

class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.adjacency_list: dict[int, set[int]] = {}

    def add_edge(self, src: int, dest: int | None = None) -> None:
        if src not in self.adjacency_list:
            self.adjacency_list[src] = set()

        if dest is not None:
            if dest not in self.adjacency_list:
                self.adjacency_list[dest] = set()
            self.adjacency_list[src].add(dest)
            if not self.directed:
                self.adjacency_list[dest].add(src)

    def get_vertices(self) -> list[int]:
        return list(self.adjacency_list)

    def get_neighbors(self, vertex: int) -> set[int] | None:
        return self.adjacency_list.get(vertex)

    def visit(self, vertex: int) -> None:
        print(f"Visited vertex {vertex}")

    def dfs(self) -> tuple[set[int], dict[int, int | None]]:
        to_visit: list[int] = []
        parents: dict[int, int | None] = {}
        components: set[int] = set()
        vertices = self.get_vertices()

        for vertex in vertices:
            if vertex not in parents:
                components.add(vertex)
                parents[vertex] = None
                to_visit.append(vertex)

                while to_visit:
                    v = to_visit.pop()
                    self.visit(v)
                    neighbors = self.get_neighbors(v)
                    for nbr in neighbors:
                        if nbr not in parents:
                            parents[nbr] = v
                            to_visit.append(nbr)

        return components, parents

    def bfs(self) -> tuple[set[int], dict[int, int | None]]:
        to_visit: deque[int] = deque()
        parents: dict[int, int | None] = {}
        components: set[int] = set()
        vertices = self.get_vertices()

        for vertex in vertices:
            if vertex not in parents:
                components.add(vertex)
                parents[vertex] = None
                to_visit.appendleft(vertex)

                while to_visit:
                    v = to_visit.pop()
                    self.visit(v)
                    neighbors = self.get_neighbors(v)
                    for nbr in neighbors:
                        if nbr not in parents:
                            parents[nbr] = v
                            to_visit.appendleft(nbr)

        return components, parents

    def display(self):
        pp.pprint(self.adjacency_list)


def test_graph_1():
    print("******Running test 1********")
    dg = Graph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 3)
    dg.add_edge(1, 4)
    dg.add_edge(2, 4)
    dg.add_edge(2, 5)
    dg.add_edge(3, 1)
    dg.add_edge(4, 3)
    dg.add_edge(5, 5)

    dg.display()

    print("***********DFS***********")
    dfs_components, dfs_parents = dg.dfs()
    print(f"dfs_components: {dfs_components}")
    print(f"dfs parents: {dfs_parents}")

    print("***********BFS***********")
    bfs_components, bfs_parents  = dg.bfs()
    print(f"bfs_components: {bfs_components}")
    print(f"bfs parents: {bfs_parents}")

def test_graph_2():
    print("******Running test 2********")
    dg = Graph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 2)
    dg.add_edge(1, 3)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)

    dg.display()

    print("***********DFS***********")
    dfs_components, dfs_parents = dg.dfs()
    print(f"dfs_components: {dfs_components}")
    print(f"dfs parents: {dfs_parents}")

    print("***********BFS***********")
    bfs_components, bfs_parents  = dg.bfs()
    print(f"bfs_components: {bfs_components}")
    print(f"bfs parents: {bfs_parents}")

def test_undirected_graph_1():
    print("******Running test 3********")
    udg = Graph(False)
    udg.add_edge(0, 1)
    udg.add_edge(1, 2)
    udg.add_edge(1, 3)
    udg.add_edge(2, 3)
    udg.add_edge(3, 4)
    udg.add_edge(5)
    udg.add_edge(7, 6)
    udg.add_edge(6, 8)

    udg.display()

    print("***********DFS***********")
    dfs_components, dfs_parents = udg.dfs()
    print(f"dfs_components: {dfs_components}")
    print(f"dfs parents: {dfs_parents}")

    print("***********BFS***********")
    bfs_components, bfs_parents  = udg.bfs()
    print(f"bfs_components: {bfs_components}")
    print(f"bfs parents: {bfs_parents}")


def main():
    test_graph_1()
    test_graph_2()
    test_undirected_graph_1()


if __name__ == "__main__":
    main()
