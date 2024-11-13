#pragma once
#include <vector>
#include <iterator>
#include <stdexcept>

template<typename T>
class Graph 
{
public:
    typedef T value_type;
    typedef std::vector<T> VertexList;
    typedef std::vector<VertexList> AdjacencyMatrix;
    typedef typename VertexList::iterator vertex_iterator;
    typedef typename AdjacencyMatrix::iterator adjacency_iterator;

private:
    AdjacencyMatrix adjacency_matrix;

public:
    Graph(int n) : adjacency_matrix(n, VertexList(n, T())) {}

    vertex_iterator vertex_begin(int i) 
    {
        check_vertex(i);
        return adjacency_matrix[i].begin();
    }

    vertex_iterator vertex_end(int i) 
    {
        check_vertex(i);
        return adjacency_matrix[i].end();
    }

    void add_edge(int i, int j, const T& value) 
    {
        check_vertex(i);
        check_vertex(j);
        adjacency_matrix[i][j] = value;
    }

    void remove_edge(int i, int j) 
    {
        check_vertex(i);
        check_vertex(j);
        adjacency_matrix[i][j] = T();
    }

    void add_vertex() 
    {
        for (auto& row : adjacency_matrix) 
        {
            row.push_back(T());
        }
        adjacency_matrix.push_back(VertexList(adjacency_matrix.size() + 1, T()));
    }

    void remove_vertex(int i) 
    {
        check_vertex(i);
        adjacency_matrix.erase(adjacency_matrix.begin() + i);
        for (auto& row : adjacency_matrix) 
        {
            row.erase(row.begin() + i);
        }
    }

    T& operator()(int i, int j) 
    {
        check_vertex(i);
        check_vertex(j);
        if (!edge_exists(i, j)) 
        {
            throw std::invalid_argument("Edge does not exist");
        }
        return adjacency_matrix[i][j];
    }

    int num_vertices() const 
    {
        return adjacency_matrix.size();
    }

    int num_edges() const 
    {
        int count = 0;
        for (const auto& row : adjacency_matrix) 
        {
            for (const auto& value : row) 
            {
                if (value != T()) 
                {
                    ++count;
                }
            }
        }
        return count;
    }

    int degree(int i) const 
    {
        check_vertex(i);
        int count = 0;
        for (const auto& value : adjacency_matrix[i]) 
        {
            if (value != T()) 
            {
                ++count;
            }
        }
        return count;
    }

    bool is_empty() const
    {
        return adjacency_matrix.empty();
    }

    void clear()
    {
        adjacency_matrix.clear();
    }

private:
    void check_vertex(int i) const 
    {
        if (i < 0 || i >= adjacency_matrix.size()) 
        {
            throw std::out_of_range("Vertex index out of range");
        }
    }

    bool edge_exists(int i, int j) const 
    {
        return adjacency_matrix[i][j] != T();
    }
};
