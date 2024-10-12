class Manhattan_2:
    def evaluate(self, puzzle, goal_puzzle):
        total_distance = 0  
        for i in range(3):
            for j in range(3):
                current_value = puzzle.state[i][j]  # Accessing the state of the puzzle
                if current_value != 0:
                    goal_row, goal_col = self.find_position_in_goal(current_value, goal_puzzle.state)  # Accessing the state of goal_puzzle
                    
                    total_distance += abs(goal_row - i) + abs(goal_col - j)

        return total_distance

    def find_position_in_goal(self, value, goal_puzzle_state):
        for row_index in range(3):
            for col_index in range(3):
                if goal_puzzle_state[row_index][col_index] == value:  # Accessing the goal puzzle's state
                    return row_index, col_index
