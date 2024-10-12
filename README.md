
# 8-Puzzle Solver using A* Algorithm 🧩🔍

This project implements the 8-puzzle solver using the **A*** search algorithm with different heuristic functions: **Hamming Distance**, **Manhattan Distance**, and **Manhattan Distance with Linear Conflict**.

### 📂 Files and Their Purpose

- **`eight_puzzle.py`**: 🧮  
  Defines the puzzle board, legal moves, and puzzle-solving functionality.

- **`astar.py`**: 🧠🚀  
  Implements the A* search algorithm to find the optimal solution with a priority queue.

- **`heuristic_hamming.py`**: 🎯  
  Implements Hamming Distance heuristic, counting misplaced tiles.

- **`heuristic_manhattan.py`**: 🛣️  
  Implements Manhattan Distance heuristic, summing the distance each tile needs to move.

- **`heuristic_manhattan_.py`**: 🛣️  
  Implements Manhattan Distance heuristic, summing the distance each tile needs to move.
  But this is the improved version of the previous one , it can take many form of goals (unlike the previous one)

- **`heuristic_linear.py`**: 🔀💥  
  Adds Linear Conflict to Manhattan, penalizing misplaced tiles in the same row or column.

- **`main.py`**: 🏁  
  The main script to test the A* algorithm with different heuristics, showing solution and timing.

## 🛠️ Requirements

You’ll need **Python 3.x** and **`numpy`** (install it with `pip install numpy`).

### 🚀 How to Run

1. Clone/download the project.
2. Navigate to the directory:
```bash
cd 8-puzzle-solver
```
3. Run the main script:
```bash
python main.py
```

### 📝 Example output:
```

Running A* Solver with Hamming Heuristic:
A* (Hamming) Solution found after exploring 53419 nodes in 10.0843 seconds
Moves: ['down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'left', 'down', 'right', 'up', 'left', 'up', 'right', 'down', 'right', 'down']

Running A* Solver with Manhattan + Linear Conflict Heuristic:
A* (Manhattan + Linear Conflict) Solution found after exploring 2346 nodes in 0.5514 seconds
Moves: ['down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'left', 'down', 'right', 'up', 'left', 'up', 'right', 'down', 'right', 'down']

Running A* Solver with Manhattan Heuristic:
A* (Manhattan) Solution found after exploring 4321 nodes in 0.8191 seconds
Moves: ['down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'left', 'down', 'right', 'up', 'left', 'up', 'right', 'down', 'right', 'down']
Running BFS Solver:
BFS Solution found after exploring 174373 nodes
Moves: ['down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'left', 'down', 'right', 'up', 'left', 'up', 'right', 'down', 'right', 'down']
```

