# gen_sudoku
This is a python program that solves generalized sudoku. The traditional nine by nine cell sudoku board can be a difficult problem for people to solve, but as it turns out sudoku in general is computational pretty difficult. In fact sudoku is [NP-Complete](https://en.wikipedia.org/wiki/Mathematics_of_Sudoku#Mathematical_context).
The traditional sudoku board is a problem of size n = 3, in general an n-sudoku has n<sup>2</sup> rows, columns, and regions and a total of n<sup>4</sup> cells.

  This solver will represent a sudoku board as graph, this is done in graph.py. To do this we interpret each cell in the board as a vertex and two cells are adjacent if they are in the same row, column, or region of the sudoku board. Under this interpretation a to find a solution to the sudoku we must find an n<sup>2</sup>-coloring for the graph.
