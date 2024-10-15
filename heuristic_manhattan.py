class Manhattan:
    def evaluate(self, puzzle, goal_puzzle):
        """Calculate the Manhattan distance."""
        total_distance = 0
        for i in range(3):
            for j in range(3):
                value = puzzle.state[i][j]
                if value != 0:
                    goal_position = divmod(value - 1, 3)
                    total_distance += abs(goal_position[0] - i) + abs(goal_position[1] - j)
        return total_distance 
