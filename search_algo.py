from board import BoardState
from util import flat
from frontier import Frontier2




def a_star_search2(init_state: BoardState) -> BoardState:

    """
    Performs the a_star_search for the init_state
    and returns a solved BoardState.
    """

    frontier = Frontier2(init_state)
    explored = set()

    while len(frontier.contain) != 0:
        
        curr = frontier.select_min()[0]

        if curr.is_goal():
            curr.display()
            return curr

        succ = curr.successor2()

        for ele in succ:

            temp = flat(ele.list_config)
            
            if temp not in explored:
                ele.prev = curr
                ele.str_rep = temp
                explored.add(temp)
                frontier.push(ele)

    print("No Solution")




def dfs(init_state: BoardState) -> BoardState:
    """
    DFS Algo
    """
    frontier = [init_state]
    explored = set()

    while len(frontier) != 0:

        curr = frontier[-1]
        frontier.remove(curr)

        flat_curr = flat(curr.list_config)

        if flat_curr not in explored:

            explored.add(flat_curr)

            if curr.is_goal():
                curr.display()
                return curr
            
            succ = curr.successor()

            for ele in succ:
                temp = flat(ele.list_config)
                if temp not in explored:
                    frontier.append(ele)
                    ele.prev = curr
                    ele.str_rep = temp

            # frontier += succ

    print('no solution')