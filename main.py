from eight_puzzle import EightPuzzle
from bfs import bfs_solve
from astar import AStarSolver
from heuristic_hamming import Hamming
from heuristic_manhattan import Manhattan
from heuristic_manhattan_2 import Manhattan_2

from heuristic_linear import ManhattanLinearConflict

import matplotlib.pyplot as plt
from matplotlib.widgets import Button


# Puzzle Display and Button-based Manual Progression Functions
def update_display(puzzle, ax):
    """Update the puzzle display."""
    ax.clear()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)

    # Reverse row index to show first row at the top
    for i in range(3):
        for j in range(3):
            value = puzzle.state[2 - i][j]  # Reverse row index
            label = '' if value == 0 else str(value)
            ax.text(j + 0.5, i + 0.5, label, ha='center', va='center', fontsize=45, fontweight='bold',
                    bbox=dict(facecolor='lightgray' if value == 0 else 'white', 
                              edgecolor='black', boxstyle='round,pad=0.6', linewidth=2))

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1)
    plt.draw()

def on_click(event, puzzle, ax, solution_moves, step_counter):
    """Handle button click to go to the next move."""
    if step_counter[0] < len(solution_moves):
        move = solution_moves[step_counter[0]]
        puzzle.move(move)
        update_display(puzzle, ax)
        step_counter[0] += 1

def manual_animation_with_button(puzzle_initial_state, solution_moves):
    """Set up the puzzle display with a button for manual progression."""
    fig, ax = plt.subplots(figsize=(5, 5))

    # Create a button
    ax_next = plt.axes([0.8, 0.02, 0.15, 0.07])
    next_btn = Button(ax_next, 'Next')

    # Initialize the puzzle to the original initial state
    puzzle = EightPuzzle(puzzle_initial_state.copy())  # Reset puzzle to initial state

    # Initialize step counter for manual progression
    step_counter = [0]

    # Button callback
    next_btn.on_clicked(lambda event: on_click(event, puzzle, ax, solution_moves, step_counter))

    # Initial display of the puzzle
    update_display(puzzle, ax)
    plt.show()


def run_bfs_solver():
    """Run BFS solver and display results."""
    initial_state = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]  # Example initial state
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state
    
    puzzle = EightPuzzle(initial_state)
    goal_puzzle = EightPuzzle(goal_state)

    # Solve using BFS
    solution_moves, explored_nodes = bfs_solve(puzzle, goal_puzzle)

    if solution_moves:
        print(f"BFS Solution found after exploring {explored_nodes} nodes")
        print(f"Moves: {solution_moves}")

        # Animate the solution with a button-based progression
        manual_animation_with_button(initial_state, solution_moves)
    else:
        print("No solution found with BFS")



def run_a_star_solver(heuristic, heuristic_name):
    initial_state = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]  # Example initial state
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Standard goal state for 8-puzzle
    puzzle = EightPuzzle(initial_state)
    goal_puzzle = EightPuzzle(goal_state)
    
    solver = AStarSolver(heuristic)

    solution_moves, explored_nodes, elapsed_time = solver.search(puzzle, goal_puzzle)

    if solution_moves:
        print(f"A* ({heuristic_name}) Solution found after exploring {explored_nodes} nodes in {elapsed_time:.4f} seconds")
        print(f"Moves: {solution_moves}")

        manual_animation_with_button(initial_state, solution_moves)
    else:
        print(f"No solution found with A* ({heuristic_name})")


if __name__ == "__main__":

    # Run A* Solver with Manhattan Heuristic (improved version)
    print("\nRunning A* Solver with Manhattan Heuristic (improved version):")
    run_a_star_solver(Manhattan_2(), "Manhattan")


    # Run A* Solver with Hamming Heuristic
    print("\nRunning A* Solver with Hamming Heuristic:")
    run_a_star_solver(Hamming(), "Hamming")

    # Run A* Solver with Manhattan + Linear Conflict Heuristic
    print("\nRunning A* Solver with Manhattan + Linear Conflict Heuristic:")
    run_a_star_solver(ManhattanLinearConflict(), "Manhattan + Linear Conflict")


    # Run A* Solver with Manhattan Heuristic
    print("\nRunning A* Solver with Manhattan Heuristic:")
    run_a_star_solver(Manhattan(), "Manhattan")




    # Run BFS Solver
    print("Running BFS Solver:")
    run_bfs_solver()
