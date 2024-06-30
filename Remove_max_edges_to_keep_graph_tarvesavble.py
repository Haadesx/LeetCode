# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
# Solved
# Hard
# Topics
# Companies
# Hint
# Alice and Bob have an undirected graph of n nodes and three types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

# Example 1:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:



# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

# Constraints:

# 1 <= n <= 105
# 1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= typei <= 3
# 1 <= ui < vi <= n
# All tuples (typei, ui, vi) are distinct.









class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n  # initially n components
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.components -= 1
            return True
        return False

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Alice's and Bob's Union-Find structures
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        # Count of edges that can be removed
        removable_edges = 0
        
        # Step 1: Process type 3 edges
        for edge in edges:
            if edge[0] == 3:
                if not (uf_alice.union(edge[1], edge[2]) and uf_bob.union(edge[1], edge[2])):
                    removable_edges += 1
        
        # Step 2: Process type 1 edges for Alice
        for edge in edges:
            if edge[0] == 1:
                if not uf_alice.union(edge[1], edge[2]):
                    removable_edges += 1
        
        # Step 3: Process type 2 edges for Bob
        for edge in edges:
            if edge[0] == 2:
                if not uf_bob.union(edge[1], edge[2]):
                    removable_edges += 1
        
        # Check if both Alice and Bob can traverse all nodes
        if uf_alice.components > 2 or uf_bob.components > 2:
            return -1
        
        return removable_edges

# Example test cases
solution = Solution()
print(solution.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))  # Output: 2
print(solution.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))  # Output: 0
print(solution.maxNumEdgesToRemove(4, [[3,2,3],[1,1
