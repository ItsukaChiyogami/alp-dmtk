import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graf = nx.Graph()

    def add_node(self, node):
        """Menambah node ke dalam graf."""
        self.graf.add_node(node)

    def add_edge(self, node1, node2, weight=1):
        """Menambah edge dengan bobot di antara dua node."""
        self.graf.add_edge(node1, node2, weight=weight)

    def visualize_graph(self):
        """Menampilkan visualisasi graf."""
        pos = nx.spring_layout(self.graf)
        weights = nx.get_edge_attributes(self.graf, 'weight')
        nx.draw(self.graf, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10)
        nx.draw_networkx_edge_labels(self.graf, pos, edge_labels=weights)
        plt.show()

    def shortest_path(self, start, end):
        """Menghitung jalur terpendek dari satu node ke node lain."""
        try:
            return nx.shortest_path(self.graf, source=start, target=end, weight='weight')
        except nx.NetworkXNoPath:
            return f"Tidak ada jalur antara {start} dan {end}."

    def visual_shortest_path(self, start, end):
        """Menampilkan visualisasi jalur terpendek di graf."""
        path = self.shortest_path(start, end)
        if isinstance(path, str):
            print(path)
            return
        
        path_edges = list(zip(path, path[1:]))
        pos = nx.spring_layout(self.graf)
        weights = nx.get_edge_attributes(self.graf, 'weight')
        nx.draw(self.graf, pos, with_labels=True, node_color='lightgrey', node_size=700, font_size=10)
        nx.draw_networkx_edges(self.graf, pos, edgelist=path_edges, edge_color='red', width=2)
        nx.draw_networkx_edge_labels(self.graf, pos, edge_labels=weights)
        plt.show()

    # Metode tambahan
    def is_connected(self):
        """Memeriksa apakah graf terhubung sepenuhnya."""
        return nx.is_connected(self.graf)

    def degree_of_node(self, node):
        """Mengembalikan derajat dari sebuah node."""
        if node in self.graf:
            return self.graf.degree[node]
        else:
            return f"Node {node} tidak ditemukan dalam graf."

    def clustering_coefficient(self):
        """Mengembalikan koefisien clustering untuk setiap node."""
        return nx.clustering(self.graf)

    def all_pairs_shortest_path(self):
        """Menghitung jalur terpendek antara semua pasangan node."""
        return dict(nx.all_pairs_dijkstra_path(self.graf, weight='weight'))

    def minimum_spanning_tree(self):
        """Mengembalikan pohon rentang minimum graf."""
        mst = nx.minimum_spanning_tree(self.graf, weight='weight')
        return mst

# Contoh penggunaan
if __name__ == "__main__":
    graph = Graf()

    # Menambah node
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    # Menambah edge
    graph.add_edge(1, 2, weight=4.5)
    graph.add_edge(1, 3, weight=3.2)
    graph.add_edge(2, 4, weight=2.7)
    graph.add_edge(3, 4, weight=1.8)
    graph.add_edge(1, 4, weight=6.7)
    graph.add_edge(3, 5, weight=2.7)

    # Visualisasi graf
    graph.visualize_graph()

    # Jalur terpendek
    print("Jalur terpendek 1 -> 5:", graph.shortest_path(1, 5))

    # Visualisasi jalur terpendek
    graph.visual_shortest_path(1, 5)

    # Metode tambahan
    print("Graf terhubung:", graph.is_connected())
    print("Derajat node 3:", graph.degree_of_node(3))
    print("Koefisien clustering:", graph.clustering_coefficient())
    print("Semua jalur terpendek:", graph.all_pairs_shortest_path())
    print("Pohon rentang minimum:", graph.minimum_spanning_tree().edges(data=True))
