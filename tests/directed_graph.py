from graph import Graph
import unittest


class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        # initialize graph will be called once per each test (test fixture)
        self.__graph = Graph()

        self.__graph.add_vertex("1")
        self.__graph.add_vertex("2")
        self.__graph.add_vertex("3")
        self.__graph.add_vertex("4")
        self.__graph.add_vertex("5")
        self.__graph.add_vertex("6")

        self.__graph.add_edge("1", "2", 1)
        self.__graph.add_edge("1", "3", 2)
        self.__graph.add_edge("2", "3", 3)
        self.__graph.add_edge("2", "6", 4)
        self.__graph.add_edge("4", "3", 5)
        self.__graph.add_edge("5", "2", 6)
        self.__graph.add_edge("5", "3", 7)
        self.__graph.add_edge("6", "4", 8)
        self.__graph.add_edge("6", "5", 9)

    def tearDown(self):
        pass  # deinitialize will be called once per each test (test fixture)

    def test_add_vertex(self):
        self.assertEqual(len(self.__graph.get_vertices()), 6)
        self.assertIsNone(self.__graph.get_vertex("7"))

        self.__graph.add_vertex("7")

        self.assertEqual(len(self.__graph.get_vertices()), 7)
        self.assertIsNotNone(self.__graph.get_vertex("7"))

    def test_add_the_same_vertex_multiple_times(self):
        self.assertEqual(len(self.__graph.get_vertices()), 6)
        self.assertIsNone(self.__graph.get_vertex("7"))

        self.__graph.add_vertex("7")
        self.__graph.add_vertex("7")
        self.__graph.add_vertex("7")

        self.assertEqual(len(self.__graph.get_vertices()), 7)
        self.assertIsNotNone(self.__graph.get_vertex("7"))

    def test_add_edge(self):
        self.assertEqual(len(self.__graph.get_edges()), 9)
        self.assertEqual(self.__graph.get_indegree("1"), 0)
        self.assertEqual(self.__graph.get_outdegree("5"), 2)

        self.__graph.add_edge("5", "1")

        self.assertEqual(len(self.__graph.get_edges()), 10)
        self.assertEqual(self.__graph.get_indegree("1"), 1)
        self.assertEqual(self.__graph.get_outdegree("5"), 3)

    def test_add_edge_with_the_same_direction_and_other_weight(self):
        self.assertEqual(len(self.__graph.get_edges()), 9)
        self.assertEqual(self.__graph.get_indegree("3"), 4)
        self.assertEqual(self.__graph.get_outdegree("1"), 2)

        self.__graph.add_edge("1", "3", 3)

        self.assertEqual(len(self.__graph.get_edges()), 10)
        self.assertEqual(self.__graph.get_indegree("3"), 5)
        self.assertEqual(self.__graph.get_outdegree("1"), 3)

    def test_add_the_same_edge_multiple_times(self):
        self.assertEqual(len(self.__graph.get_edges()), 9)
        self.assertEqual(self.__graph.get_indegree("1"), 0)
        self.assertEqual(self.__graph.get_outdegree("5"), 2)

        self.__graph.add_edge("5", "1", 6)
        self.__graph.add_edge("5", "1", 6)
        self.__graph.add_edge("5", "1", 6)

        self.assertEqual(len(self.__graph.get_edges()), 10)
        self.assertEqual(self.__graph.get_indegree("1"), 1)
        self.assertEqual(self.__graph.get_outdegree("5"), 3)

    def test_remove_vertex(self):
        self.assertIsNotNone(self.__graph.get_vertex("2"))
        self.assertEqual(len(self.__graph.get_vertices()), 6)

        self.__graph.remove_vertex("2")

        self.assertIsNone(self.__graph.get_vertex("2"))
        self.assertEqual(len(self.__graph.get_vertices()), 5)

    def test_remove_not_existing_vertex(self):
        with self.assertRaises(ValueError):
            self.__graph.remove_vertex("NonExistingVertex")

    def test_remove_edge(self):
        self.assertEqual(self.__graph.get_indegree("3"), 4)
        self.assertEqual(self.__graph.get_outdegree("5"), 2)
        self.assertEqual(len(self.__graph.get_edges()), 9)

        self.__graph.remove_edge("5", "3", 7)

        self.assertEqual(self.__graph.get_indegree("3"), 3)
        self.assertEqual(self.__graph.get_outdegree("5"), 1)
        self.assertEqual(len(self.__graph.get_edges()), 8)

    def test_remove_not_existing_edge(self):
        with self.assertRaises(ValueError):
            self.__graph.remove_edge(
                "NonExistingVertex1", "NonExistingVertex2", 4)

    def test_vertices_count(self):
        self.assertEqual(len(self.__graph.get_vertices()), 6)

    def test_edges_count(self):
        self.assertEqual(len(self.__graph.get_edges()), 9)

    def test_get_vertex(self):
        self.assertIsNotNone(self.__graph.get_vertex("1"))

    def test_get_not_existing_vertex(self):
        self.assertIsNone(self.__graph.get_vertex("NonExistingVertex"))

    def test_vertex_indegree(self):
        self.assertEqual(self.__graph.get_indegree("3"), 4)

    def test_vertex_outdegree(self):
        self.assertEqual(self.__graph.get_outdegree("6"), 2)

    def test_degree(self):
        self.assertEqual(self.__graph.get_degree("6"), 3)

    def test_graph_is_directed(self):
        self.assertTrue(self.__graph.is_directed())


if __name__ == "__main__":
    unittest.main()
