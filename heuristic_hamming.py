
class Hamming:
    def evaluate(self, puzzle, goal_puzzle):
        x =0
        """Calculate the Hamming distance."""
        for i in range(0,3):
            for j in range(0,3):
                if puzzle.state[i][j] != goal_puzzle.state[i][j] and puzzle.state[i][j] != 0:
                    x += 1
        return x
        #return sum(puzzle.state[i][j] != goal_puzzle.state[i][j] and puzzle.state[i][j] != 0
        #           for i in range(3) for j in range(3))
