def validate_board(board):
    def is_valid_set(nums):
        nums = [n for n in nums if n != 0]
        return len(nums) == len(set(nums))

    # Check rows and columns
    for i in range(9):
        if not is_valid_set(board[i]) or not is_valid_set([board[j][i] for j in range(9)]):
            return False

    # Check sub-grids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not is_valid_set([
                board[row + i][col + j] for i in range(3) for j in range(3)
            ]):
                return False

    return True
