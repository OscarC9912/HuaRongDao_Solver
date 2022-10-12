from board import BoardState
from util import copy


# All of the poissible actions 
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
LORD = 1


class Move:
    """
    Generate how each state could move
    """

    def __init__(self, state: BoardState) -> None:
        self.currState = state


    def _movable(self, agent: int, dir: str) -> bool:
        """
        Checks if the agent could move at this dir for exactly one step

        @param dir: describe the direct for the agent to move

        Case1: when the agent is lord
        Case2: when the agent is general_h: guanyu
        Case3: when the agent is soldier
        Case4: when the agent is general_vS
        """

        generals_v = list(self.currState.board[1].keys())
        general_h = list(self.currState.board[2].keys())
        blank_pos = self.currState.board[4][0]
        lord_pos = self.currState.board[0][1]
        soldiers = self.currState.board[3]  # type dict

        # the lord case
        if agent == LORD:
            
            if dir == 'LEFT':
                delta_h = LEFT[0]
                temp10, temp11 = lord_pos[0][0] + delta_h,lord_pos[0][1]
                temp20, temp21 = lord_pos[2][0] + delta_h, lord_pos[2][1]
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp10 >= 0 and temp20 >= 0)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if dir == 'RIGHT':
                delta_h = RIGHT[0]
                temp10, temp11 = lord_pos[1][0] + delta_h,lord_pos[1][1]
                temp20, temp21 = lord_pos[3][0] + delta_h, lord_pos[3][1]
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp10 <= 3 and temp20 <= 3)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if dir == 'UP':
                delta_v = UP[1]
                temp10, temp11 = lord_pos[0][0],lord_pos[0][1] + delta_v
                temp20, temp21 = lord_pos[1][0], lord_pos[1][1] + delta_v
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 >= 0 and temp21 >= 0)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if dir == 'DOWN':
                delta_v = DOWN[1]
                temp10, temp11 = lord_pos[2][0],lord_pos[2][1] + delta_v
                temp20, temp21 = lord_pos[3][0], lord_pos[3][1] + delta_v
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 <= 4 and temp21 <= 4)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if in_board and vacant:
                return True
            return False
        
        # the horizontal general case: Guan YU
        if agent in general_h:

            general_h_pos = self.currState.board[2][agent]

            if dir == 'LEFT':
                delta_h = LEFT[0]
                temp10, temp11 = general_h_pos[0][0] + delta_h,general_h_pos[0][1]
                temp20, temp21 = general_h_pos[1][0] + delta_h, general_h_pos[1][1]
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 >= 0 and temp21 >= 0)

                # Figure out the left_most point
                if new_pos1[0] < new_pos2[0]:
                    vacant = (new_pos1 in blank_pos)
                else:
                    vacant = (new_pos2 in blank_pos)

            if dir == 'RIGHT':
                delta_h = RIGHT[0]
                temp10, temp11 = general_h_pos[0][0] + delta_h, general_h_pos[0][1]
                temp20, temp21 = general_h_pos[1][0] + delta_h, general_h_pos[1][1]
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp10 <= 3 and temp20 <= 3)

                # Figure out the right_most point
                if new_pos1[0] > new_pos2[0]:
                    vacant = (new_pos1 in blank_pos)
                else:
                    vacant = (new_pos2 in blank_pos)

            if dir == 'UP':
                delta_v = UP[1]
                temp10, temp11 = general_h_pos[0][0],general_h_pos[0][1] + delta_v
                temp20, temp21 = general_h_pos[1][0], general_h_pos[1][1] + delta_v
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 >= 0 and temp21 >= 0)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if dir == 'DOWN':
                delta_v = DOWN[1]
                temp10, temp11 = general_h_pos[0][0],general_h_pos[0][1] + delta_v
                temp20, temp21 = general_h_pos[1][0], general_h_pos[1][1] + delta_v
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 <= 4 and temp21 <= 4)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if in_board and vacant:
                return True
            return False
        
        # the soldier's case
        if agent in {70, 71, 72, 73}:
            
            if dir == 'LEFT':
                delta_h = LEFT[0]
                temp10, temp11 = soldiers[agent][0] + delta_h, soldiers[agent][1]
                new_pos = (temp10, temp11)

                in_board = (temp10 >= 0)
                vacant = (new_pos in blank_pos)

            if dir == 'RIGHT':
                delta_h = RIGHT[0]
                temp10, temp11 = soldiers[agent][0] + delta_h, soldiers[agent][1]
                new_pos = (temp10, temp11)

                in_board = (temp10 <= 3)
                vacant = (new_pos in blank_pos)

            if dir == 'UP':
                delta_v = UP[1]
                temp10, temp11 = soldiers[agent][0], soldiers[agent][1] + delta_v
                new_pos = (temp10, temp11)

                in_board = (temp11 >= 0)
                vacant = (new_pos in blank_pos)

            if dir == 'DOWN':
                delta_v = DOWN[1]
                temp10, temp11 = soldiers[agent][0], soldiers[agent][1] + delta_v
                new_pos = (temp10, temp11)

                in_board = (temp11 <= 4)
                vacant = (new_pos in blank_pos)

            if in_board and vacant:
                return True
            return False

        # the vertical generals case
        if agent in generals_v:

            pos = self.currState.board[1][agent]
            
            if dir == 'LEFT':
                delta_h = LEFT[0]
                temp10, temp11 = pos[0][0] + delta_h, pos[0][1]
                temp20, temp21 = pos[1][0] + delta_h, pos[1][1]
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp10 >= 0 and temp20 >= 0)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if dir == 'RIGHT':
                delta_h = RIGHT[0]
                temp10, temp11 = pos[0][0] + delta_h, pos[0][1]
                temp20, temp21 = pos[1][0] + delta_h, pos[1][1]
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp10 <= 3 and temp20 <= 3)
                vacant = (new_pos1 in blank_pos and new_pos2 in blank_pos)

            if dir == 'UP':
                delta_v = UP[1]
                temp10, temp11 = pos[0][0], pos[0][1] + delta_v
                temp20, temp21 = pos[1][0], pos[1][1] + delta_v
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 >= 0 and temp21 >= 0)

                if new_pos1[1] > new_pos2[1]:
                    vacant = new_pos2 in blank_pos
                else:
                    vacant = new_pos1 in blank_pos

            if dir == 'DOWN':
                delta_v = DOWN[1]
                temp10, temp11 = pos[0][0], pos[0][1] + delta_v
                temp20, temp21 = pos[1][0], pos[1][1] + delta_v
                new_pos1, new_pos2 = (temp10, temp11), (temp20, temp21)

                in_board = (temp11 <= 4 and temp21 <= 4)

                if new_pos1[1] < new_pos2[1]:
                    vacant = new_pos2 in blank_pos
                else:
                    vacant = new_pos1 in blank_pos

            if in_board and vacant:
                return True
            return False


    def move(self, agent: int, dir: str) -> BoardState:
        
        # Make a copy of the original state
        # So that Move object could be used for several times with the same state
        self.copy_state = copy(self.currState)
        could_move = self._movable(agent=agent, dir=dir)

        if could_move:
            general_h = list(self.copy_state.board[2].keys())
            generals_v = list(self.currState.board[1].keys())
            new_state = None

            if agent == LORD:
                new_state = self._lord_move(agent, dir)

            if agent in general_h:
                new_state = self._generalh_move(agent, dir)

            if agent in {70, 71, 72, 73}:
                new_state = self._soldier_move(agent, dir)

            if agent in generals_v:
                new_state = self._generalv_move(agent, dir)

            return new_state

        return None


    def _lord_move(self, lord: int, dir: str) -> BoardState:
        """
        Move the Lord by exactly one step and return the updated state.
        """
        original_pos = self.copy_state.board[0][lord]
        new_pos_lord = []
        new_pos_zero = []
        
        if dir == 'LEFT':

            self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0
            self.copy_state.list_config[original_pos[3][1]][original_pos[3][0]] = 0

            new_pos_zero.append(original_pos[1])
            new_pos_zero.append(original_pos[3])

            delta_h = LEFT[0]
            
            for i in range(len(original_pos)):
                new_x, new_y = original_pos[i][0] + delta_h, original_pos[i][1]
                new_pos_lord.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = lord
            
        if dir == 'RIGHT':

            self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            self.copy_state.list_config[original_pos[2][1]][original_pos[2][0]] = 0

            new_pos_zero.append(original_pos[0])
            new_pos_zero.append(original_pos[2])
            delta_h = RIGHT[0]

            for i in range(len(original_pos)):
                new_x, new_y = original_pos[i][0] + delta_h, original_pos[i][1]
                new_pos_lord.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = lord

        if dir == 'UP':
            self.copy_state.list_config[original_pos[2][1]][original_pos[2][0]] = 0
            self.copy_state.list_config[original_pos[3][1]][original_pos[3][0]] = 0

            new_pos_zero.append(original_pos[2])
            new_pos_zero.append(original_pos[3])
            delta_v = UP[1]
            for i in range(len(original_pos)):
                new_x, new_y = original_pos[i][0], original_pos[i][1] + delta_v
                new_pos_lord.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = lord

        if dir == 'DOWN':
            self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            new_pos_zero.append(original_pos[0])
            new_pos_zero.append(original_pos[1])
            delta_v = DOWN[1]

            for i in range(len(original_pos)):
                new_x, new_y = original_pos[i][0], original_pos[i][1] + delta_v
                new_pos_lord.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = lord

        self.copy_state.board[0][1] = new_pos_lord
        self.copy_state.board[4][0] = new_pos_zero
        return self.copy_state


    def _generalv_move(self, genv: int, dir) -> BoardState:

        original_pos = self.copy_state.board[1][genv]
        original_zero = self.copy_state.board[4][0]
        new_pos_genv = []
        new_pos_zero = []

        if dir == 'LEFT':

            self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            new_pos_zero = [original_pos[0], original_pos[1]]

            delta_h = LEFT[0]
            for i in range(2):
                new_x, new_y = original_pos[i][0] + delta_h, original_pos[i][1]
                new_pos_genv.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = genv

        if dir == 'RIGHT':

            # directly substitute with original position
            self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            new_pos_zero = [original_pos[0], original_pos[1]]

            delta_h = RIGHT[0]
            for i in range(2):
                new_x, new_y = original_pos[i][0] + delta_h, original_pos[i][1]
                new_pos_genv.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = genv

        if dir == 'UP':

            # deal with new_zero, append the rightmost to the new_zero
            if original_pos[0][1] - original_pos[1][1] > 0:
                new_pos_zero.append(original_pos[0])

                self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            else:
                new_pos_zero.append(original_pos[1])

                self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            # deal with new_pos
            delta_v = UP[1]
            for j in range(2):
                new_x, new_y = original_pos[j][0], original_pos[j][1] + delta_v
                new_pos_genv.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = genv

            ori_occ = None
            if new_pos_genv[0][1] < new_pos_genv[1][1]:
                ori_occ = new_pos_genv[0]
            else:
                ori_occ = new_pos_genv[1]
                
            for k in range(2):
                if original_zero[k] != ori_occ and original_zero[k] not in new_pos_genv:
                    new_pos_zero.append(original_zero[k])

        if dir == 'DOWN':
            # deal with new_zero, append the rightmost to the new_zero
            if original_pos[0][1] - original_pos[1][1] > 0:
                new_pos_zero.append(original_pos[1])

                self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0
            else:
                new_pos_zero.append(original_pos[0])

                self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0

            # deal with new_pos
            delta_v = DOWN[1]
            for j in range(2):
                new_x, new_y = original_pos[j][0], original_pos[j][1] + delta_v
                new_pos_genv.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = genv

            ori_occ = None
            if new_pos_genv[0][1] < new_pos_genv[1][1]:
                ori_occ = new_pos_genv[0]
            else:
                ori_occ = new_pos_genv[1]

            for k in range(2):
                if original_zero[k] != ori_occ and original_zero[k] not in new_pos_genv:
                    new_pos_zero.append(original_zero[k])
            
        self.copy_state.board[1][genv] = new_pos_genv
        self.copy_state.board[4][0] = new_pos_zero
        return self.copy_state


    def _generalh_move(self, genh: int, dir: str) -> BoardState:
        
        # right, left is done
        
        """
        Move the horizontal general for exactly one step at direction
        and return a new state
        """
        original_pos = self.copy_state.board[2][genh]
        original_zero = self.copy_state.board[4][0]
        new_pos_gh = []
        new_pos_zero = []

        if dir == 'LEFT':

            # deal with new_zero, append the rightmost to the new_zero
            if original_pos[0][0] - original_pos[1][0] > 0:
                new_pos_zero.append(original_pos[0])

                self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0

            else:
                new_pos_zero.append(original_pos[1])

                self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            # deal with new_pos
            delta_h = LEFT[0]
            for j in range(2):
                new_x, new_y = original_pos[j][0] + delta_h, original_pos[j][1]
                new_pos_gh.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = genh

            ori_occ = None
            if new_pos_gh[0][0] < new_pos_gh[1][0]:
                ori_occ = new_pos_gh[0]
            else:
                ori_occ = new_pos_gh[1]

            for k in range(2):
                if original_zero[k] != ori_occ:
                    new_pos_zero.append(original_zero[k])

        if dir == 'RIGHT':

           # deal with new_zero, append the rightmost to the new_zero
            if original_pos[0][0] - original_pos[1][0] > 0:
                new_pos_zero.append(original_pos[1])

                self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0
            else:
                new_pos_zero.append(original_pos[0])

                self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0

            # deal with new_pos
            delta_h = RIGHT[0]
            for j in range(2):
                new_x, new_y = original_pos[j][0] + delta_h, original_pos[j][1]
                new_pos_gh.append((new_x, new_y))

                self.copy_state.list_config[new_y][new_x] = genh

            ori_occ = None
            if new_pos_gh[0][0] < new_pos_gh[1][0]:
                ori_occ = new_pos_gh[1]
            else:
                ori_occ = new_pos_gh[0]
                
            for k in range(2):
                if original_zero[k] != ori_occ:
                    new_pos_zero.append(original_zero[k])

        if dir == 'UP':

            self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            # directly substitute with original position
            new_pos_zero = [original_pos[0], original_pos[1]]

            delta_v = UP[1]
            for i in range(2):
                new_x, new_y = original_pos[i][0], original_pos[i][1] + delta_v
                new_pos_gh.append((new_x, new_y))
                self.copy_state.list_config[new_y][new_x] = genh

        if dir == 'DOWN':

            self.copy_state.list_config[original_pos[0][1]][original_pos[0][0]] = 0
            self.copy_state.list_config[original_pos[1][1]][original_pos[1][0]] = 0

            new_pos_zero = [original_pos[0], original_pos[1]]

            delta_v = DOWN[1]
            for i in range(2):
                new_x, new_y = original_pos[i][0], original_pos[i][1] + delta_v
                new_pos_gh.append((new_x, new_y))
                self.copy_state.list_config[new_y][new_x] = genh

        self.copy_state.board[2][genh] = new_pos_gh
        self.copy_state.board[4][0] = new_pos_zero
        return self.copy_state


    def _soldier_move(self, soldier: int, dir: str) -> BoardState:

        ori_pos = self.copy_state.board[3][soldier]
        ori_zero = self.copy_state.board[4][0]
        temp = None

        if dir == 'LEFT':
            count = 0
            for i in range(2):
                same_y = (ori_zero[i][1] == ori_pos[1])
                det_one = (ori_zero[i][0] - ori_pos[0] == -1)
                if same_y and det_one and count == 0:
                    temp = ori_zero[i]
                    ori_zero[i] = ori_pos
                    ori_pos = temp
                    count += 1

        if dir == 'RIGHT':
            count = 0
            for i in range(2):
                same_y = (ori_zero[i][1] == ori_pos[1])
                det_one = (ori_zero[i][0] - ori_pos[0] == 1)
                if same_y and det_one and count == 0:
                    temp = ori_zero[i]
                    ori_zero[i] = ori_pos
                    ori_pos = temp
                    count += 1

        if dir == 'UP':
            count = 0
            for i in range(2):
                same_x = (ori_zero[i][0] == ori_pos[0])
                det_one = (ori_zero[i][1] - ori_pos[1] == -1)
                if same_x and det_one and count == 0:
                    temp = ori_zero[i]
                    ori_zero[i] = ori_pos
                    ori_pos = temp
                    count += 1

        if dir == 'DOWN':
            count = 0
            for i in range(2):
                same_x = (ori_zero[i][0] == ori_pos[0])
                det_one = (ori_zero[i][1] - ori_pos[1] == 1)
                if same_x and det_one and count == 0:
                    temp = ori_zero[i]
                    ori_zero[i] = ori_pos
                    ori_pos = temp
                    count += 1


        self.copy_state.board[3][soldier] = ori_pos
        self.copy_state.board[4][0] = ori_zero

        newx, newy = ori_pos[0], ori_pos[1]
        self.copy_state.list_config[newy][newx] = soldier
        for i in range(2):
            newx0, newy0 = ori_zero[i][0], ori_zero[i][1]
            self.copy_state.list_config[newy0][newx0] = 0

        return self.copy_state
    
        