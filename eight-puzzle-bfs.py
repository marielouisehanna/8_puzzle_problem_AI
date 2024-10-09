import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# 8-Puzzle Class
class EightPuzzle:
    def __init__(self, initial_state):
        self.state = np.array(initial_state)
        self.blank_pos = np.argwhere(self.state == 0)[0]

    def move(self, direction):
        """Move the blank tile in a given direction if possible."""
        row, col = self.blank_pos
        if direction == 'up' and row > 0:
            self._swap((row, col), (row - 1, col))
        elif direction == 'down' and row < 2:
            self._swap((row, col), (row + 1, col))
        elif direction == 'left' and col > 0:
            self._swap((row, col), (row, col - 1))
        elif direction == 'right' and col < 2:
            self._swap((row, col), (row, col + 1))

    def _swap(self, pos1, pos2):
        """Swap two positions in the puzzle."""
        self.state[tuple(pos1)], self.state[tuple(pos2)] = self.state[tuple(pos2)], self.state[tuple(pos1)]
        self.blank_pos = pos2  # Update the blank position

    def is_solved(self):
        """Check if the puzzle is solved."""
        return np.array_equal(self.state, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))

    def copy(self):
        """Return a copy of the current puzzle."""
        return EightPuzzle(self.state.copy())

    def legal_moves(self):
        """Returns a list of legal moves from the current state."""
        row, col = self.blank_pos
        moves = []
        if row > 0:
            moves.append('up')
        if row < 2:
            moves.append('down')
        if col > 0:
            moves.append('left')
        if col < 2:
            moves.append('right')
        return moves

    def result(self, move):
        """Returns the resulting state from applying a move."""
        new_puzzle = self.copy()
        new_puzzle.move(move)
        return new_puzzle

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

    def __hash__(self):
        return hash(self.state.tobytes())

    def __str__(self):
        """String representation of the puzzle state."""
        return '\n'.join([' '.join(map(str, row)) for row in self.state]) + '\n'


# BFS Solver
def bfs_solve(puzzle):
    """Solve the 8-puzzle using BFS and return the sequence of moves."""
    frontier = deque([(puzzle.copy(), [])])  # Queue of (puzzle, moves)
    explored = set()
    explored_nodes = 0

    while frontier:
        current_puzzle, moves = frontier.popleft()

        if current_puzzle.is_solved():
            return moves, explored_nodes  # Return the list of moves to solve the puzzle and explored nodes

        if current_puzzle not in explored:
            explored.add(current_puzzle)
            explored_nodes += 1

            for move in current_puzzle.legal_moves():
                new_puzzle = current_puzzle.result(move)
                frontier.append((new_puzzle, moves + [move]))

    return [], explored_nodes  # No solution found


def print_solution_path(puzzle_initial_state, solution_moves):
    """Print the puzzle states along the solution path."""
    current_puzzle = EightPuzzle(puzzle_initial_state.copy())  # Start from the initial state
    print("Initial state:")
    print(current_puzzle)

    for move in solution_moves:
        current_puzzle.move(move)
        print(f"After move {move}:")
        print(current_puzzle)


# Puzzle Display and Button-based Manual Progression
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

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1)  # Adjust to fit the button
    plt.draw()

def on_click(event, puzzle, ax, solution_moves, step_counter):
    """Handle button click to go to the next move."""
    if step_counter[0] < len(solution_moves):
        move = solution_moves[step_counter[0]]
        puzzle.move(move)
        update_display(puzzle, ax)
        step_counter[0] += 1

def manual_animation_with_button(puzzle_initial_state, solution_moves):
    fig, ax = plt.subplots(figsize=(5, 5))

    # Create a button
    ax_next = plt.axes([0.8, 0.02, 0.15, 0.07])  # Position for button
    next_btn = Button(ax_next, 'Next')

    # Initialize the puzzle to the original initial state (resetting it)
    puzzle = EightPuzzle(puzzle_initial_state.copy())  # Reset puzzle to initial state

    # Initialize step counter for manual progression
    step_counter = [0]

    # Button callback
    next_btn.on_clicked(lambda event: on_click(event, puzzle, ax, solution_moves, step_counter))

    # Initial display of the puzzle
    update_display(puzzle, ax)
    plt.show()

# Main execution logic
if __name__ == "__main__":
    # A solvable initial state
    initial_state = [[8, 0, 6],
                     [5, 4, 7],
                     [2, 3, 1]]  # The puzzle state

    # Create the EightPuzzle instance
    puzzle = EightPuzzle(initial_state)

    # Solve the puzzle using BFS (with solvability check)
    solution_moves, explored_nodes = bfs_solve(puzzle)

    # Print the explored nodes and the final path (solution)
    if solution_moves:
        print(f"Number of explored nodes: {explored_nodes}")
        print(f"Final path (moves): {solution_moves}")
        
        # Print the solution path (puzzle states after each move)
        print_solution_path(initial_state, solution_moves)

        # Animate the solution with a button to go to the next state
        manual_animation_with_button(initial_state, solution_moves)
    else:
        print("No solution found or the puzzle is unsolvable.")
