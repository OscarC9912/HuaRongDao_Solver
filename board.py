from typing import List, Dict
from heuristic_func import manhattan_dist
from move import Move
from util import copy


class BoardState:
    """
    The state of the board.
    """

    def __init__(self, 
                list_config: List,
                lord: Dict=None, generals_v: Dict=None, general_h: Dict=None, 
                soldiers: Dict=None, blank: Dict=None) -> None:
        """
        @param lord: dict of length 1, contains a list of coordinates
        @param generals_v: dict of length 4, contains coord of four 2 * 1 generals
        @param general_h: dict of length 1, contains coord of one 1 * 2 general
        @param soldiers: dict of length 4, contains coord of four 1*1 soldiers
        @param blank: dict of length 2, contains coord of two balck position
        @param goal: weather the state is in the goal state
        @param width: the width of the board game (in unit space)
        @param height: the height of the board game (in unit space)

        @param state: an ordered list of length 5 stores in the order
                lord, generals_v, generals_h, soldies, blank

        @param parent: the prev State lead to this state
        @param cost: the cost from prev state to current state
        """

        self.rcost = 0  # the accumulative cost of the path till here
        self.pred_hcost = 0

        self.board = []
        self.list_config = list_config
        self.prev = None
        self.str_rep = None
        complete = (lord != None and generals_v != None and \
                    general_h != None and soldiers != None and blank != None)

        if complete:
            self.board.append(lord)
            self.board.append(generals_v)
            self.board.append(general_h)
            self.board.append(soldiers)
            self.board.append(blank)
        else:
            raise Exception("The Configuration of board is not Complete")


    def __lt__(self, other):
        v1 = self.rcost + self.pred_hcost
        v2 = other.rcost + other.pred_hcost
        return v1 < v2


    def is_goal(self) -> bool:
        """
        Checks if the current state is the output state

        It is in goal as long as the bottom two of the lord is in goal set
        """
        if self.board is None:
            raise Exception("Error: Board is Empty")

        goal_set = {(1, 4), (2, 4)}
        lord_pos = self.board[0][1]
        lord_bottom1, lord_bottom2 = lord_pos[2], lord_pos[3]

        if lord_bottom1 in goal_set and lord_bottom2 in goal_set:
            return True
        return False
    
    def display(self, on: bool=True) -> None:
        """
        Print the state in a human friendly version.
        """
        state = self.list_config

        for row in state:
            print(row)

    def display2(self, on: bool=True) -> None:
        """
        Print the state in a human friendly version.
        """
        state = self.board

        for i in range(5):
            curr_row = []

            for j in range(4):
                curr_pos = (j, i)

                for k in range(5):
                    curr_dict = state[k]

                    for key in curr_dict:

                        if curr_dict[key] == curr_pos or curr_pos in curr_dict[key]:

                            curr_row.append(key)

            if on:
                print(curr_row)
    
    def find_neighbor(self) -> Dict:
        """
        Returns a Dictionary of possible move
        {agent: dir}
        """
        output = {}
        namelist = self.list_config
        zero1, zero2 = self.board[4][0][0], self.board[4][0][1]
        zero1_x, zero1_y = zero1[0], zero1[1]
        zero2_x, zero2_y = zero2[0], zero2[1]

        if zero1_x + 1 <= 3:
            # right point move left
            target = namelist[zero1_y][zero1_x + 1]
            if target not in output:
                output[target] = ['LEFT']
            if 'LEFT' not in output[target]:
                output[target].append('LEFT')

        if zero1_x - 1 >= 0:
            # right point move left
            target = namelist[zero1_y][zero1_x - 1]
            if target not in output:
                output[target] = ['RIGHT']
            if 'RIGHT' not in output[target]:
                output[target].append('RIGHT')

        if zero2_x + 1 <= 3:
            # right point move left
            target = namelist[zero2_y][zero2_x + 1]
            if target not in output:
                output[target] = ['LEFT']
            if 'LEFT' not in output[target]:
                output[target].append('LEFT')

        if zero2_x - 1 >= 0:
            # right point move left
            target = namelist[zero2_y][zero2_x - 1]
            if target not in output:
                output[target] = ['RIGHT']
            if 'RIGHT' not in output[target]:
                output[target].append('RIGHT')

        if zero1_y + 1 <= 4:
            target = namelist[zero1_y + 1][zero1_x]
            if target not in output:
                output[target] = ['UP']
            if 'UP' not in output[target]:
                output[target].append('UP')

        if zero1_y - 1 >= 0:
            # right point move left
            target = namelist[zero1_y - 1][zero1_x]
            if target not in output:
                output[target] = ['DOWN']
            if 'DOWN' not in output[target]:
                output[target].append('DOWN')

        if zero2_y + 1 <= 4:
            target = namelist[zero2_y + 1][zero2_x]
            if target not in output:
                output[target] = ['UP']
            if 'UP' not in output[target]:
                output[target].append('UP')

        if zero2_y - 1 >= 0:
            # right point move left
            target = namelist[zero2_y - 1][zero2_x]
            if target not in output:
                output[target] = ['DOWN']
            if 'DOWN' not in output[target]:
                output[target].append('DOWN')

        if 0 in output:
            del output[0]
        return output


    def successor2(self) -> List[object]:
        """
        Return a list of all possible successors of the current state by moving 
        exactly one step for all the agent.
        """
        state_copy = copy(self)
        potential_move = self.find_neighbor()
        possible_next = {}

        for agent in potential_move:
            move_obj = Move(state_copy)
            for dir in potential_move[agent]:
                temp = move_obj.move(agent, dir)

                if temp is not None:
                     # Calculate the hcost here
                     temp.pred_hcost = manhattan_dist(temp)
                     temp.rcost += 1
                     possible_next[temp] = temp.pred_hcost + temp.rcost

        return possible_next

    def successor(self) -> List[object]:
        """
        Return a list of all possible successors of the current state by moving 
        exactly one step for all the agent.
        """
        state_copy = copy(self)
        potential_move = self.find_neighbor()
        possible_next = []

        for agent in potential_move:
            move_obj = Move(state_copy)
            for dir in potential_move[agent]:
                temp = move_obj.move(agent, dir)

                if temp is not None:
                    # Calculate the hcost here
                    temp.pred_hcost = manhattan_dist(temp)
                    temp.rcost += 1
                    possible_next.append(temp)

        return possible_next
