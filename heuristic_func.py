from board import BoardState



def manhattan_dist(state: BoardState) -> int:
    """
    Calculate the Mahhatan Distance between the current state and the 
    """
    lord_bottom_l = state.board[0][1][2]
    goal_set_l = (1, 4)

    return abs(lord_bottom_l[0] - goal_set_l[0]) + abs(lord_bottom_l[1] - goal_set_l[1])


def advanced_heuristic_function(state: BoardState) -> int:
    """
    The advanced Heuristic function
    """
    # the case when the state is in goal
    lord_bottom_l = state.board[0][1][2]
    goal_set_l = (1, 4)

    if state.is_goal():
        advancedVal = ((lord_bottom_l[0] - goal_set_l[0])**2 + (lord_bottom_l[1] - goal_set_l[1])**2)**(0.5)
    else:
        advancedVal = ((lord_bottom_l[0] - goal_set_l[0])**2 + (lord_bottom_l[1] - goal_set_l[1])**2 + 9)**(0.5)

    return advancedVal