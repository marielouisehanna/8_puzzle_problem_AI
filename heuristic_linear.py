
class ManhattanLinearConflict:
    def evaluate(self, puzzle, goal_puzzle):
        """Calculate the Manhattan distance plus linear conflicts."""
        manhattan_distance = 0
        linear_conflict = 0
        pos_dict = {}
        for row in range(3):
            for col in range(3):
                pos_dict[goal_puzzle.state[row][col]] = (row, col)

        for i in range(3):
            for j in range(3):
                value = puzzle.state[i][j]
                if value != 0:
                    goal_position = pos_dict[value]
                    manhattan_distance += abs(goal_position[0] - i) + abs(goal_position[1] - j)

                    # Check for linear conflicts in rows
                    if goal_position[0] == i:
                        for k in range(j + 1, 3):
                            other_value = puzzle.state[i][k]
                            if other_value != 0:
                                other_goal_position = divmod(other_value - 1, 3)
                                if other_goal_position[0] == i and other_goal_position[1] < goal_position[1]:
                                    linear_conflict += 1

                    # Check for linear conflicts in columns
                    if goal_position[1] == j:
                        for k in range(i + 1, 3):
                            other_value = puzzle.state[k][j]
                            if other_value != 0:
                                other_goal_position = divmod(other_value - 1, 3)
                                if other_goal_position[1] == j and other_goal_position[0] < goal_position[0]:
                                    linear_conflict += 1

        return manhattan_distance + 2 * linear_conflict
