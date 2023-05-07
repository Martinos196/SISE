import argparse
import random
import time

BOARD_3x3 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
BOARD_4x4 = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
SOLVED_BOARD = BOARD_4x4
START_BOARD = []
EMPTY_FIELD = {}
ORDER = []
DEPTH = 20

class Node:
    def __init__(self, current_board, parent, last_move, way):
        self.board = current_board
        self.children = {}
        self.errors = {}
        if parent != 'Root':
            self.parent = parent
        self.last = last_move
        self.way = way.copy()
        self.way.append(last_move)
        self.to_visit = ORDER.copy()

    def create_child(self, board_after_move, move):
        child = Node(board_after_move, self, move, self.way)
        self.children[move] = child

    def make_move(self, move):
        y = EMPTY_FIELD['row']
        x = EMPTY_FIELD['column']
        if move == 'L':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x - 1], tmp_array[y][x] = tmp_array[y][x], tmp_array[y][x - 1]
            EMPTY_FIELD['column'] -= 1
            self.create_child(tmp_array, move)
        elif move == 'R':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x], tmp_array[y][x + 1] = tmp_array[y][x + 1], tmp_array[y][x]
            EMPTY_FIELD['column'] += 1
            self.create_child(tmp_array, move)
        elif move == 'U':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y - 1][x], tmp_array[y][x] = tmp_array[y][x], tmp_array[y - 1][x]
            EMPTY_FIELD['row'] -= 1
            self.create_child(tmp_array, move)
        elif move == 'D':
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x], tmp_array[y + 1][x] = tmp_array[y + 1][x], tmp_array[y][x]
            EMPTY_FIELD['row'] += 1
            self.create_child(tmp_array, move)

def change_position_of_empty_field(last_move):
    if last_move == 'U':
        EMPTY_FIELD['row'] += 1
    if last_move == 'D':
        EMPTY_FIELD['row'] -= 1
    if last_move == 'L':
        EMPTY_FIELD['column'] += 1
    if last_move == 'R':
        EMPTY_FIELD['column'] -= 1

def remove_impossible_moves(current_node, is_root=False):
    is_removed_l = False
    is_removed_r = False
    is_removed_u = False
    is_removed_d = False
    if EMPTY_FIELD['column'] == len(SOLVED_BOARD[0]) - 1 and EMPTY_FIELD['row'] == len(SOLVED_BOARD) - 1:
        current_node.to_visit.remove('R')
        current_node.to_visit.remove('D')
        is_removed_r = True
        is_removed_d = True
    elif EMPTY_FIELD['column'] == len(SOLVED_BOARD[0]) - 1 and EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('R')
        current_node.to_visit.remove('U')
        is_removed_r = True
        is_removed_u = True
    elif EMPTY_FIELD['column'] == 0 and EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('L')
        current_node.to_visit.remove('U')
        is_removed_l = True
        is_removed_u = True
    elif EMPTY_FIELD['column'] == 0 and EMPTY_FIELD['row'] == len(SOLVED_BOARD) - 1:
        current_node.to_visit.remove('L')
        current_node.to_visit.remove('D')
        is_removed_l = True
        is_removed_d = True
    elif EMPTY_FIELD['column'] == 0:
        current_node.to_visit.remove('L')
        is_removed_l = True
    elif EMPTY_FIELD['column'] == len(SOLVED_BOARD[0]) - 1:
        current_node.to_visit.remove('R')
        is_removed_r = True
    elif EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('U')
        is_removed_u = True
    elif EMPTY_FIELD['row'] == len(SOLVED_BOARD) - 1:
        current_node.to_visit.remove('D')
        is_removed_d = True
    if not is_root:
        if current_node.last == 'R' and not is_removed_l:
            current_node.to_visit.remove('L')
        elif current_node.last == 'L' and not is_removed_r:
            current_node.to_visit.remove('R')
        elif current_node.last == 'U' and not is_removed_d:
            current_node.to_visit.remove('D')
        elif current_node.last == 'D' and not is_removed_u:
            current_node.to_visit.remove('U')

def is_solved(test_board, solved_board):
    if test_board == solved_board:
        return True
    return False

def find_and_set_empty_field(test_board):
    for row in range(len(test_board)):
        for col in range(len(test_board[row])):
            if test_board[row][col] == '0':
                EMPTY_FIELD['row'] = row
                EMPTY_FIELD['column'] = col

def DFS(start_time):
    amount_of_processed_nodes = 1
    amount_of_visited_nodes = 1
    current_node = Node(START_BOARD, 'Root', None, [])
    root_flag = True
    is_a_return = False
    max_depth_reached = False
    depth_level = 0
    remove_impossible_moves(current_node, root_flag)
    while True:
        if is_solved(current_node.board, SOLVED_BOARD):
            if max_depth_reached:
                depth_level = DEPTH
            else:
                depth_level = len(current_node.way) - 1
            return current_node.way, amount_of_processed_nodes, amount_of_visited_nodes, depth_level
        elif len(current_node.way) == DEPTH:
            current_node = current_node.parent
            find_and_set_empty_field(current_node.board)
            is_a_return = True
            max_depth_reached = True
        elif len(current_node.to_visit) != 0:
            if not root_flag and not is_a_return:
                remove_impossible_moves(current_node)
            if len(current_node.to_visit) != 0:
                move = current_node.to_visit[0]
                current_node.make_move(move)
                current_node.to_visit.remove(move)
                current_node = current_node.children[move]
                find_and_set_empty_field(current_node.board)
                root_flag = False
                is_a_return = False
                amount_of_visited_nodes += 1
                amount_of_processed_nodes += 1
            else:
                if current_node.last is None or time.time() - start_time > DEPTH:
                    return -1, amount_of_processed_nodes, amount_of_visited_nodes, depth_level
                else:
                    current_node = current_node.parent
                    find_and_set_empty_field(current_node.board)
                    is_a_return = True
        else:
            if current_node.last is None or time.time() - start_time > DEPTH:
                return -1, amount_of_processed_nodes, amount_of_visited_nodes, depth_level
            else:
                current_node = current_node.parent
                find_and_set_empty_field(current_node.board)
                is_a_return = True

def BFS(start_time):
    amount_of_processed_nodes = 1
    amount_of_visited_nodes = 1
    current_node = Node(START_BOARD, 'Root', None, [])
    remove_impossible_moves(current_node, True)
    queue = []
    counter = 0
    while True:
        counter += 1
        if time.time() - start_time > DEPTH:
            return -1, amount_of_processed_nodes, amount_of_visited_nodes, len(current_node.way) - 1
        if is_solved(current_node.board, SOLVED_BOARD):
            return current_node.way, amount_of_processed_nodes, amount_of_visited_nodes, len(current_node.way) - 1
        else:
            if not current_node.last is None:
                remove_impossible_moves(current_node, False)
            for move in current_node.to_visit:
                amount_of_processed_nodes += 1
                current_node.make_move(move)
                current_node = current_node.children[move]
                queue.append(current_node)
                last_move = current_node.way[-1]
                change_position_of_empty_field(last_move)
                current_node = current_node.parent
            try:
                if current_node.last is not None:
                    queue.remove(current_node)
            except ValueError:
                pass
            current_node = queue[0]
            amount_of_visited_nodes += 1
            find_and_set_empty_field(current_node.board)

def ASTR(heuristic, start_time):
    amount_of_visited_nodes = 1
    amount_of_processed_nodes = 1

    def get_index_of_value(board, value):
        for index_row, row in enumerate(board):
            for index_col, elem in enumerate(row):
                if elem == value:
                    return index_row, index_col

    if heuristic == 'manh':
        def calculate_error(current_board, solved_board):
            manh_error = 0
            for index_row, row in enumerate(current_board):
                for index_col, elem in enumerate(row):
                    target_row, target_col = get_index_of_value(solved_board, elem)
                    manh_error += abs(index_row - target_row) + abs(index_col - target_col)
            return manh_error
    else:
        def calculate_error(current_board, solved_board):
            hamm_error = 0
            for index_row, row in enumerate(current_board):
                for index_col, elem in enumerate(row):
                    target_row, target_col = get_index_of_value(solved_board, elem)
                    if abs(index_row - target_row) + abs(index_col - target_col) != 0:
                        hamm_error += 1
            return hamm_error
    current_node = Node(START_BOARD, 'Root', None, [])
    remove_impossible_moves(current_node, True)
    while True:
        try:
            if time.time() - start_time > DEPTH:
                return -1, amount_of_processed_nodes, amount_of_visited_nodes, len(current_node.way) - 1
            if is_solved(current_node.board, SOLVED_BOARD):
                return current_node.way, amount_of_processed_nodes, amount_of_visited_nodes, len(current_node.way) - 1
            else:
                for move in current_node.to_visit:
                    amount_of_processed_nodes += 1
                    current_node.make_move(move)
                    current_node = current_node.children[move]
                    error = calculate_error(current_node.board, SOLVED_BOARD)
                    current_node = current_node.parent
                    find_and_set_empty_field(current_node.board)
                    current_node.errors[move] = error
                min_value = min(current_node.errors.values())
                tmp = []
                for key in current_node.errors:
                    if current_node.errors[key] == min_value:
                        tmp.append(key)
                nr = random.randint(0, len(tmp) - 1)
                next_move = tmp[nr]
                current_node.make_move(next_move)
                current_node = current_node.children[next_move]
                amount_of_visited_nodes += 1
                try:
                    remove_impossible_moves(current_node, False)
                except ValueError:
                    pass
        except MemoryError:
            return -1, amount_of_processed_nodes, amount_of_visited_nodes, len(current_node.way) - 1

def prepare_solution(data, output_file, stats_file, start_time):
    end_time = time.time() - start_time
    way, processed_nodes, visited_nodes, depth_level = data
    if way != -1:
        way.remove(way[0])
        solution_length = len(way)
        solution = way
    else:
        solution_length = -1
        solution = []
    file = open(output_file, 'w+')
    file.write(str(solution_length))
    if way != -1:
        file.write('\n')
        file.write(''.join(solution))
    file.close()
    file = open(stats_file, 'w+')
    file.write(str(solution_length))
    file.write('\n')
    file.write(str(visited_nodes))
    file.write('\n')
    file.write(str(processed_nodes))
    file.write('\n')
    file.write(str(depth_level))
    file.write('\n')
    file.write(str(round(end_time * 1000, 3)))
    file.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Algorithm, order, input file, output file, stats file.")
    parser.add_argument('algorithm')
    parser.add_argument('order')
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    parser.add_argument('stats_file')
    args = parser.parse_args()

    for elem in args.order:
        ORDER.append(elem)

    with open(args.input_file) as board:
        first_line_flag = True
        for line in board:
            if first_line_flag:
                first_line_flag = False
                continue
            else:
                START_BOARD.append(line.split())

    find_and_set_empty_field(START_BOARD)
    start_time = time.time()
    if args.algorithm == 'dfs':
        prepare_solution(DFS(start_time), args.output_file, args.stats_file, start_time)
    elif args.algorithm == 'bfs':
        prepare_solution(BFS(start_time), args.output_file, args.stats_file, start_time)
    else:
        if ORDER == 'manh':
            ORDER = ['L', 'R', 'D', 'U']
            prepare_solution(ASTR('manh', start_time), args.output_file, args.stats_file, start_time)
        else:
            ORDER = ['L', 'R', 'D', 'U']
            prepare_solution(ASTR('hamm', start_time), args.output_file, args.stats_file, start_time)