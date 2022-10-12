from typing import List
from board import BoardState


def converter(file_name: str) -> BoardState:
    """
    Convert a txt file of configuration into the state of the Board。
    """
    complete_board = []  # a list that stores full board

    if file_name is None:
        raise Exception("File is not Found")

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    # transform the txt file to a 5 * 4 matrix first
    # listinized txt file
    lconfig = [[], [], [], [], []]  
    for i in range(len(lines)):
        lconfig[i].append(lines[i][0])
        lconfig[i].append(lines[i][1])
        lconfig[i].append(lines[i][2])
        lconfig[i].append(lines[i][3])
        lconfig[i] = list(map(int, lconfig[i]))

    
    hg = _hori_general(lconfig)  # find who is the horizontal general
    hg_set = set(hg)  # Map the hg to a set
    vg = {0, 1, 2, 3, 4, 5, 6, 7} - {0, 1, 7}  # find who is the vertical general
    vg = vg - hg_set

    lord = {1: []}
    generals_v, general_h = {}, {}
    soldiers = {7: []}
    blank = {0: []}
    soldier_names = [70, 71, 72, 73]

    scont = 0

    for i in range(5):
        for j in range(4):

            temp_coord, curr = (j, i), lconfig[i][j]

            if curr == 1:  # lord
                lord[1].append(temp_coord)
            elif curr == 0:  # blank
                blank[0].append(temp_coord)
            elif curr == 7:  # soldier
                soldiers[7].append(temp_coord)
                lconfig[i][j] = soldier_names[scont]
                scont += 1
            elif curr in hg:  # horizontal general
                if curr not in general_h:
                    general_h[curr] = [temp_coord]
                else:
                    general_h[curr].append(temp_coord)
            elif curr in vg:  # vertical generals
                if curr not in generals_v:
                    generals_v[curr] = [temp_coord]
                else:
                    generals_v[curr].append(temp_coord)


    soldier_pos = soldiers[7]

    soldiers = {}
    for i in range(4):
        soldiers[soldier_names[i]] = soldier_pos[i]

    boardState = BoardState(list_config=lconfig, 
                            lord=lord, generals_v=generals_v, 
                            general_h=general_h, soldiers=soldiers, blank=blank)

    return boardState   

def _hori_general(config: List) -> List[int]:
    """
    Returns who is the horizontal general (Guan Yu)
    """

    output = []

    for i in range(5):
        for j in range(4):
            curr = config[i][j]
            # make sure not in soldier and not the end
            if curr not in {0, 1, 7} and j < 3:
                if curr == config[i][j + 1]:
                    output.append(curr)
    return output

def copy(state: BoardState):
        """
        Make a copy of the current state to prevent aliasing
        """
        new_rcost = state.rcost
        new_pred_hcost = state.pred_hcost
        new_lconfig = []

        for i in range(len(state.list_config)):
            new_lconfig.append(state.list_config[i][:])

        new_lord, lord_pos = {}, []
        old_lord = state.board[0][1]  # List(tuple)
        lord_pos = old_lord[:]
        new_lord[1] = lord_pos

        new_gv = {}
        old_gv = state.board[1]  # Dict
        for x in old_gv:
            new_gv[x] = old_gv[x][:]

        new_hv = {}
        old_hv = state.board[2]  # Dict
        for x in old_hv:
            new_hv[x] = old_hv[x][:]

        new_sd = {}
        old_sd = state.board[3]  # Dict
        for x in old_sd:
            new_sd[x] = old_sd[x][:]

        new_blk, blk_pos = {}, []
        old_blk = state.board[4][0]  # List(tuple)
        blk_pos = old_blk[:]
        new_blk[0] = blk_pos

        copied = BoardState(list_config=new_lconfig, 
                            lord=new_lord, generals_v=new_gv, general_h=new_hv, 
                            soldiers=new_sd, blank=new_blk)

        copied.rcost = new_rcost
        copied.pred_hcost = new_pred_hcost

        return copied


def flat(input: List) -> List:
    out = ''
    add_on = '7'
    t = {70, 71, 72, 73}
    for row in input:
        for num in row:
            if num in t:
                out += add_on
            else:
                out += str(num)
    return out