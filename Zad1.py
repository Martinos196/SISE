import argparse
import random
import time

# GLOBAL VARIABLES
SOLVED_BOARD_3x3 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
SOLVED_BOARD_4x4 = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
SOLVED_BOARD = SOLVED_BOARD_4x4
START_BOARD = []  # lista
EMPTY_FIELD = {}  # mapa dla lokalizacji pustego pola, globalna
ORDER = []
DEPTH = 20


class Node:
    def __init__(self, current_board, parent, last_move, way):
        self.board = current_board  # każda iteracja zamienia 2 elementy miejscami, a więc powstaje zupełnie nowa tablica
        self.children = {}  # mapa zawierająca maksymalnie 4 wartości, gdzie kierunek ruchu - klucz
        self.errors = {}  # mapa zawierająca oszacowania błędów, dla poszczególnych ruchów
        if parent != 'Root':
            self.parent = parent
        self.last = last_move  # poprzedni względem aktualnego stanu planszy ruch (L, R, D, U)
        self.way = way.copy()  # ścieżka do zwrócenia na koniec
        self.way.append(last_move)  # przy każdym kroku dodajemy do trasy
        self.to_visit = ORDER.copy()  # Kolejka do odwiedzenia, domyślnie wszystkie możliwe, później będą wykluczane

    # Tworzenie nowego węzła po uprzednim wyliczeniu stanu dla ruchu
    def create_child(self, board_after_move, move):
        child = Node(board_after_move, self, move, self.way)
        self.children[move] = child

    # wykonujemy ruch, obliczamy stan, tworzymy kolejny węzeł
    def make_move(self, move):
        y = EMPTY_FIELD['row']  # pierwszy z kluczy mapy EMPTY_FIELD - wartość, to y
        x = EMPTY_FIELD['column']  # drugi z kluczy mapy EMPTY_FIELD - wartość, to x
        if move == 'L':  # zakładamy, że taki ruch wgl jest możliwy
            tmp_array = []
            for row in self.board:
                tmp_array.append(row.copy())
            tmp_array[y][x - 1], tmp_array[y][x] = tmp_array[y][x], tmp_array[y][x - 1]  # swap pola pustego z polem po lewej itd.
            EMPTY_FIELD['column'] -= 1  # przesuwamy w lewo, więc zmniejszamy numer kolumny itd.
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


# Zweryfikowanie, które kierunki są niemożliwe dla danego stanu planszy
def remove_impossible_moves(current_node, is_root=False):
    is_removed_l = False
    is_removed_r = False
    is_removed_u = False
    is_removed_d = False
    if EMPTY_FIELD['column'] == len(SOLVED_BOARD[0]) - 1 and EMPTY_FIELD['row'] == len(SOLVED_BOARD) - 1:  # prawy dolny róg
        current_node.to_visit.remove('R')
        current_node.to_visit.remove('D')
        is_removed_r = True
        is_removed_d = True
    elif EMPTY_FIELD['column'] == len(SOLVED_BOARD[0]) - 1 and EMPTY_FIELD['row'] == 0:  # prawy górny róg
        current_node.to_visit.remove('R')
        current_node.to_visit.remove('U')
        is_removed_r = True
        is_removed_u = True
    elif EMPTY_FIELD['column'] == 0 and EMPTY_FIELD['row'] == 0:  # lewy górny róg
        current_node.to_visit.remove('L')
        current_node.to_visit.remove('U')
        is_removed_l = True
        is_removed_u = True
    elif EMPTY_FIELD['column'] == 0 and EMPTY_FIELD['row'] == len(SOLVED_BOARD) - 1:  # lewy dolny róg
        current_node.to_visit.remove('L')
        current_node.to_visit.remove('D')
        is_removed_l = True
        is_removed_d = True
    elif EMPTY_FIELD['column'] == 0:  # lewa ściana
        current_node.to_visit.remove('L')
        is_removed_l = True
    elif EMPTY_FIELD['column'] == len(SOLVED_BOARD[0]) - 1:  # prawa ściana
        current_node.to_visit.remove('R')
        is_removed_r = True
    elif EMPTY_FIELD['row'] == 0:
        current_node.to_visit.remove('U')  # górna ściana
        is_removed_u = True
    elif EMPTY_FIELD['row'] == len(SOLVED_BOARD) - 1:  # dolna ściana
        current_node.to_visit.remove('D')
        is_removed_d = True
    if not is_root:  # jeśli aktualny węzeł jest rootem, to i tak nie mamy gdzie wracać, więc nie trzeba usuwać
        if current_node.last == 'R' and not is_removed_l:
            current_node.to_visit.remove('L')
        elif current_node.last == 'L' and not is_removed_r:
            current_node.to_visit.remove('R')
        elif current_node.last == 'U' and not is_removed_d:
            current_node.to_visit.remove('D')
        elif current_node.last == 'D' and not is_removed_u:
            current_node.to_visit.remove('U')


# xD
def is_solved(test_board, solved_board):
    if test_board == solved_board:
        return True
    return False


# Znalezienie pustego pola w pierwszej iteracji
def find_and_set_empty_field(test_board):
    for row in range(len(test_board)):
        for col in range(len(test_board[row])):
            if test_board[row][col] == '0':
                EMPTY_FIELD['row'] = row
                EMPTY_FIELD['column'] = col


# obróbka otrzymanych danych
def prepare_solution(data, solution_file, statistic_file, start_time):
    end_time = time.time() - start_time
    way, processed_nodes, visited_nodes, depth_level = data
    if way != -1:  # znalazł rozwiązanie
        way.remove(way[0])  # usunięcie pierwszego elementu, zapewne None-a
        solution_length = len(way)
        solution = way
    else:  # nie znalazł
        solution_length = -1
        solution = []
    file = open(solution_file, 'w+')  # w+ - write + read
    file.write(str(solution_length))
    if way != -1:
        file.write('\n')
        file.write(''.join(solution))
    file.close()
    file = open(statistic_file, 'w+')
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


# Przeszukiwanie wgłąb
def dfs(start_time):
    amount_of_processed_nodes = 1  # liczba węzłów, dla których wyliczony był nowy stan planszy (było wywołane make_move)
    amount_of_visited_nodes = 1  # liczba węzłów, dla których stan planszy był porównywany z wzorcem
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
        elif len(current_node.to_visit) != 0:  # jeśli nadal można isć wgłąb
            if not root_flag and not is_a_return:
                remove_impossible_moves(current_node)  # domyślnie zabroniony ruch wstecz
            if len(current_node.to_visit) != 0:  # jeśli nadal mamy coś do odwiedzenia
                move = current_node.to_visit[0]  # pierwszy z lewej ruch z nie-usuniętych
                current_node.make_move(move)  # tworzymy nowy stan w oparciu o ruch
                current_node.to_visit.remove(move)  # usunięcie z kolejki tego ruchu, aby go nie powtórzyć
                current_node = current_node.children[move]  # przechodzimy na dziecko z tym ruchem
                find_and_set_empty_field(current_node.board)  # szukamy nowego pustego miejsca xD (da się to zoptymalizować)
                root_flag = False  # jeśli poszliśmy wgłąb na pewno nie jesteśmy rootem
                is_a_return = False  # jeśli poszliśmy wgłąb na pewno nie było wycofania
                amount_of_visited_nodes += 1
                amount_of_processed_nodes += 1
            else:  # nie mamy już nic do odwiedzenia w danym węźle
                if current_node.last is None or time.time() - start_time > DEPTH:
                    return -1, amount_of_processed_nodes, amount_of_visited_nodes, depth_level  # wróciliśmy do roota
                else:  # wróciliśmy do rodzica, ale nie jest on rootem
                    current_node = current_node.parent
                    find_and_set_empty_field(current_node.board)
                    is_a_return = True
        else:  # skończyły nam się ruchy
            if current_node.last is None or time.time() - start_time > DEPTH:
                return -1, amount_of_processed_nodes, amount_of_visited_nodes, depth_level
            else:
                current_node = current_node.parent
                find_and_set_empty_field(current_node.board)
                is_a_return = True


# Przeszukiwanie wszerz
def bfs(start_time):
    amount_of_processed_nodes = 1
    amount_of_visited_nodes = 1
    current_node = Node(START_BOARD, 'Root', None, [])
    remove_impossible_moves(current_node, True)
    queue = []  # kolejka, ponieważ najpierw odwiedzamy wszystkich na danym poziomie głębokości
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
                amount_of_processed_nodes += 1  # wszystkie dzieci są dodawane do kolejki, więc są jako processed
                current_node.make_move(move)
                current_node = current_node.children[move]
                queue.append(current_node)
                last_move = current_node.way[-1]  # ostatni element listy
                change_position_of_empty_field(last_move)
                current_node = current_node.parent
            try:
                if current_node.last is not None:  # jeżeli current_node nie jest rootem
                    queue.remove(current_node)
            except ValueError:
                pass  # pass = nop
            current_node = queue[0]
            amount_of_visited_nodes += 1
            find_and_set_empty_field(current_node.board)


# Metoda A*
def astr(heuristic, start_time):
    amount_of_visited_nodes = 1
    amount_of_processed_nodes = 1

    # Metoda w metodzie, bo czemu nie xD
    def get_index_of_value(board, value):
        for index_row, row in enumerate(board):  # enumerate - tworzy listę krotek na podstawie listy w formacie (index, wartość)
            for index_col, elem in enumerate(row):
                if elem == value:
                    return index_row, index_col  # zwracanie współrzędnych danej wartości

    if heuristic == 'manh':
        # heurystyka liczy odległość danego stanu od stanu wzorcowego
        def calculate_error(current_board, solved_board):
            manh_error = 0
            for index_row, row in enumerate(current_board):
                for index_col, elem in enumerate(row):
                    target_row, target_col = get_index_of_value(solved_board, elem)
                    manh_error += abs(index_row - target_row) + abs(index_col - target_col)  # różnica x-ów + różnica y-ków
            return manh_error
    else:
        def calculate_error(current_board, solved_board):
            hamm_error = 0
            for index_row, row in enumerate(current_board):
                for index_col, elem in enumerate(row):
                    target_row, target_col = get_index_of_value(solved_board, elem)
                    if abs(index_row - target_row) + abs(index_col - target_col) != 0:
                        hamm_error += 1  # jeśli jest jakiekolwiek odstępstwo, zwiększamy wartość błędu o 1, mniejsza dokładność
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
                    error = calculate_error(current_node.board, SOLVED_BOARD)  # wyliczamy wartość błędu dla każdego z dzieci
                    current_node = current_node.parent
                    find_and_set_empty_field(current_node.board)
                    current_node.errors[move] = error
                min_value = min(current_node.errors.values())  # w heurystyce wybieramy ten z najmniejszym błędem
                tmp = []
                for key in current_node.errors:  # sprawdzamy czy jest tylko jeden min
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


if __name__ == '__main__':

    # Parsing
    parser = argparse.ArgumentParser(description="Algorithm, order, source file, solution file, statistics file.")
    parser.add_argument('algorithm')
    parser.add_argument('order')
    parser.add_argument('source_file')
    parser.add_argument('solution_file')
    parser.add_argument('statistic_file')
    args = parser.parse_args()

    for elem in args.order:
        ORDER.append(elem)

    # Loading start board from file
    with open(args.source_file) as board:  # open zwraca liczbę linii
        first_line_flag = True  # w pierwszej linii zawarty jest rozmiar, trzeba ją pominąć
        for line in board:
            if first_line_flag:
                first_line_flag = False
                continue  # element zbędny, ale dodający czytelności
            else:
                START_BOARD.append(line.split())

    # Setting coordinates of empty field
    find_and_set_empty_field(START_BOARD)
    start_time = time.time()  # włączenie timera
    if args.algorithm == 'dfs':
        prepare_solution(dfs(start_time), args.solution_file, args.statistic_file, start_time)
    elif args.algorithm == 'bfs':
        prepare_solution(bfs(start_time), args.solution_file, args.statistic_file, start_time)
    else:
        if ORDER == 'manh':
            ORDER = ['L', 'R', 'D', 'U']  # heurystyka również musi przyjąć jakąś kolejność
            prepare_solution(astr('manh', start_time), args.solution_file, args.statistic_file, start_time)
        else:
            ORDER = ['L', 'R', 'D', 'U']
            prepare_solution(astr('hamm', start_time), args.solution_file, args.statistic_file, start_time)
