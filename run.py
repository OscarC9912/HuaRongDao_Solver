import sys
from src.util import converter, flat
from src.search_algo import dfs, a_star_search2


if __name__ == '__main__':

    arg_list = sys.argv
    puzzle_file = arg_list[1]
    dfs_out_file = arg_list[2]
    a_star_out_file = arg_list[3]
    
    initial_state = converter(puzzle_file)


    flat_init = flat(initial_state.list_config)

    general_h = list(initial_state.board[2].keys())
    generals_v = list(initial_state.board[1].keys())

    gh = '2'
    gv = '3'
    sd = '4'


    dfs_out = dfs(initial_state)
    dfs_curr = dfs_out
    dfs_trace = []


    while dfs_curr.prev is not None:
        dfs_trace.append(dfs_curr.str_rep)
        dfs_curr = dfs_curr.prev

    dfs_trace.append(flat_init)
    

    for i in range(len(dfs_trace)):
        temp = dfs_trace[i]
        new_item = ''
        for j in range(len(temp)):
            # 0 and 1 case
            if int(temp[j]) not in general_h and int(temp[j]) not in generals_v and int(temp[j]) != 7:
                new_item += temp[j]
            if int(temp[j]) == 7:
                new_item += sd
            if int(temp[j]) in generals_v:
                new_item += gv
            if int(temp[j]) in general_h:
                new_item += gh
        
        dfs_trace[i] = new_item



    with open(dfs_out_file, 'w') as f:
        f.write("Cost of the solution: {}".format(dfs_out.rcost))
        f.write('\n')
        for i in range(len(dfs_trace) - 1, 0, -1):
            line = dfs_trace[i]
            seg1 = line[0:4] + '\n'
            seg2 = line[4:8] + '\n'
            seg3 = line[8:12] + '\n'
            seg4 = line[12:16] + '\n'
            seg5 = line[16:20] + '\n' + '\n'
            f.write(seg1)
            f.write(seg2)
            f.write(seg3)
            f.write(seg4)
            f.write(seg5)



    a_star_out = a_star_search2(initial_state)
    a_curr = a_star_out
    a_trace = []

    while a_curr.prev is not None:
        a_trace.append(a_curr.str_rep)
        a_curr = a_curr.prev

    a_trace.append(flat_init)


    for i in range(len(a_trace)):
        temp = a_trace[i]
        new_item = ''
        for j in range(len(temp)):

            # 0 and 1 case
            if int(temp[j]) not in general_h and int(temp[j]) not in generals_v and int(temp[j]) != 7:
                new_item += temp[j]
            if int(temp[j]) == 7:
                new_item += sd
            if int(temp[j]) in generals_v:
                new_item += gv
            if int(temp[j]) in general_h:
                new_item += gh
        
        a_trace[i] = new_item

    with open(a_star_out_file, 'w') as f:
        f.write("Cost of the solution: {}".format(a_star_out.rcost))
        f.write('\n')
        for i in range(len(a_trace) - 1, 0, -1):
            line = a_trace[i]
            seg1 = line[0:4] + '\n'
            seg2 = line[4:8] + '\n'
            seg3 = line[8:12] + '\n'
            seg4 = line[12:16] + '\n'
            seg5 = line[16:20] + '\n' + '\n'
            f.write(seg1)
            f.write(seg2)
            f.write(seg3)
            f.write(seg4)
            f.write(seg5)