/**
 * A simple BFS problem:
 * Given an undirected graph represented as an adjacency list, starting at a given vertex.
 * write a function to perform a breadth-first search and return the order in which the vertices are visited.
 * Here's an example input:
    [
        [1, 2],    // vertex 0 is connected to vertices 1 and 2
        [0, 2, 3], // vertex 1 is connected to vertices 0, 2, and 3
        [0, 1, 3], // vertex 2 is connected to vertices 0, 1, and 3
        [1, 2],    // vertex 3 is connected to vertices 1 and 2
    ]

 * Starting at vertex 0, the function should return [0, 1, 2, 3], which is the order in which the vertices are visited.
 */

    const ds =[
        [1, 2],    // vertex 0 is connected to vertices 1 and 2
        [0, 2, 3], // vertex 1 is connected to vertices 0, 2, and 3
        [0, 1, 3], // vertex 2 is connected to vertices 0, 1, and 3
        [1, 2],    // vertex 3 is connected to vertices 1 and 2
    ]

function bfs(arr = ds) {
    for(let j = 0; j < arr.length; j++) {

    }
}