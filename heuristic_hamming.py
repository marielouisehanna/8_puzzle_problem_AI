
class Hamming:
    def evaluate(self, puzzle, goal_puzzle):
        """Calculate the Hamming distance."""
        return sum(puzzle.state[i][j] != goal_puzzle.state[i][j] and puzzle.state[i][j] != 0
                   for i in range(3) for j in range(3))
