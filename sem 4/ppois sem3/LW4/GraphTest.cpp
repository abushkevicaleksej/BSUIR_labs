#include "pch.h"
#include "CppUnitTest.h"
#include "../Project1/Graph.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(Num_of_edges)
		{
			Graph<int> g(5);
			g.add_edge(0, 1, 1);
			g.add_edge(1, 2, 2);
			g.add_edge(2, 3, 3);
			g.add_edge(3, 4, 4);
			g.add_edge(4, 0, 5);
			Assert::AreEqual(g.num_edges(), 5);
		}
		TEST_METHOD(Num_of_vertexes)
		{
			Graph<int> g(5);
			g.add_edge(0, 1, 1);
			g.add_edge(1, 2, 2);
			g.add_edge(2, 3, 3);
			g.add_edge(3, 4, 4);
			g.add_edge(4, 0, 5);
			Assert::AreEqual(g.num_vertices(), 5);
		}
		TEST_METHOD(Num_of_edges_after_deleting)
		{
			Graph<int> g(5);
			g.add_edge(0, 1, 1);
			g.add_edge(0, 2, 2);
			g.add_edge(0, 3, 3);
			g.remove_edge(0, 3);
			Assert::AreEqual(g.num_edges(), 2);
		}
		TEST_METHOD(Check_vertex)
		{
			Graph<int> g(5);
			g.add_edge(0, 1, 1);
			g.add_edge(1, 2, 2);
			g.add_edge(0, 4, 4);
			g.add_edge(4, 1, 5);
			g.degree(4);
			Assert::AreEqual(g.degree(4), 1);
		}
	};
}
