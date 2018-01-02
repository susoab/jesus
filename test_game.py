"""
　　　　 ∧_∧::
　(⌒=- (Д｀ )::
⊂~ﾍ　 /⌒　 ⌒i/~つ
　＼＼/ ｜ 　| / /::
　　＼_/｜　 ヽ_/::
　　 　 /　　/::
　　　／　 　)::
　　／ ／/　/::
　 (　< /　/::
　　＼ (　ｲ_:
　　　`｜ | ):
　 　　｜ |/::
＿＿＿ /　)＿＿＿＿＿
　　　(_／

"""
import random
import itertools
import numpy

EMPTY = 0
BLACK = -1
WHITE = 1

map1 = [
    [120, -20, 20, 5, 5, 20, -20, 120],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [120, -20, 20, 5, 5, 20, -20, 120],
]


map2 = [
    [30, -12, 0, -1, -1, 0, -12, 30],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [30, -12, 0, -1, -1, 0, -12, 30],
]

class osero:
    def __init__(self, orig=None):
        self.board = []
        for i in range(8):
            self.board.append([EMPTY] * 8)

        self.board[3][3] = self.board[4][4] = BLACK
        self.board[4][3] = self.board[3][4] = WHITE
        if orig:
            assert isinstance(orig, osero)
            for i in range(8):
                for j in range(8):
                    self.board[i][j] = orig.board[i][j]

    def count(self, bwe):
        assert bwe in (BLACK, WHITE, EMPTY)
        n = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == bwe:
                    n += 1
        return n

    def _has_my_piece(self, bw, x, y, delta_x, delta_y):
        assert bw in (BLACK, WHITE)
        assert delta_x in (-1, 0, 1)
        assert delta_y in (-1, 0, 1)
        x += delta_x
        y += delta_y

        if x < 0 or x > 7 or y < 0 or y > 7 or self.board[x][y] == EMPTY:
            return False
        if self.board[x][y] == bw:
            return True
        return self._has_my_piece(bw, x, y, delta_x, delta_y)

    def reversible_directions(self, bw, x, y):
        assert bw in (BLACK, WHITE)

        directions = []
        if self.board[x][y] != EMPTY:
            return directions

        for d in itertools.product([-1,1,0],[-1,1,0]):
            if d == (0, 0):
                continue
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx > 7 or ny < 0 or ny > 7 or self.board[nx][ny] != bw * -1:
                continue
            if self._has_my_piece(bw, nx, ny, d[0], d[1]):
                directions.append(d)
        return directions

    def _reverse_piece(self, bw, x, y, delta_x, delta_y):
        assert bw in (BLACK, WHITE)

        x += delta_x
        y += delta_y
        assert self.board[x][y] in (BLACK, WHITE)

        if self.board[x][y] == bw:
            return

        self.board[x][y] = bw
        return self._reverse_piece(bw, x, y, delta_x, delta_y)

    def put(self, x, y, bw):
        assert bw in (BLACK, WHITE)
        directions = self.reversible_directions(bw, x, y)
        if len(directions) == 0:
            return False
        self.board[x][y] = bw
        for delta in directions:
            self._reverse_piece(bw, x, y, delta[0], delta[1])
        return True


    def _calc_score(self, bw, weight_matrix):
        assert bw in (BLACK, WHITE)
        my_score = 0
        against_score = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == bw:
                    my_score += weight_matrix[i][j]
                elif self.board[i][j] == bw * -1:
                    against_score += weight_matrix[i][j]
        return my_score - against_score

    def find_best_position(self, bw, weight_matrix):
        assert bw in (BLACK, WHITE)

        next_positions = {}
        for i in range(8):
            for j in range(8):
                reversi = osero(self)
                if reversi.put(i, j, bw):
                    next_positions.setdefault(
                        reversi._calc_score(bw, weight_matrix), []
                    ).append((i, j))
        if next_positions:
            next_position = random.choice(next_positions[max(next_positions)])
        else:
            next_position = None
        return next_position


#-------------------------------------------------------------------------------#

BLACK_MARK = 'M'
WHITE_MARK = 'S'


def print_board(reversi):
    print('\n   a b c d e f g h \n  +-+-+-+-+-+-+-+-+')
    for i, row in enumerate(reversi.board):
        print(' %d|' % (i+1), end='')
        for r in row:
            print('{}|'.format({EMPTY: ' ', BLACK: BLACK_MARK, WHITE: WHITE_MARK}[r]), end='')
        print('\n  +-+-+-+-+-+-+-+-+')
    print()


def input_level():
    while True:
        s = input('Level "1" or "2" ?')
        if s == '':
            return 1
        if s in ('1', '2'):
            return int(s)


def input_position(player):
    while True:
        s = input('{}? [a-h][1-8]'.format(BLACK_MARK if player == BLACK else WHITE_MARK))
        if s == '' or (len(s) == 2 and s[0] in list('abcdefgh') and s[1] in list('12345678')):
            break
    if s == '':
        return None

    y, x = ord(s[0]) - 97, ord(s[1]) - 49
    #print('input_position=', x, y)
    return x, y


def print_position(player, xy):
    if xy is None:
        print('{}: skip'.format(BLACK_MARK if player == BLACK else WHITE_MARK))
    else:
        print('{}: {}{}'.format(
            BLACK_MARK if player == BLACK else WHITE_MARK,
            chr(xy[1]+97),
            chr(xy[0]+49),
        ))

def start_game():
    reversi = osero()
    level = input_level()
    if level == 2:
        weight_matrix = map1
    else:
        weight_matrix = map2

    player = BLACK
    while not (
        reversi.count(EMPTY) == 0 or
        reversi.count(BLACK) == 0 or
        reversi.count(WHITE) == 0
    ):
        print_board(reversi)
        xy = input_position(player)
        while xy and not reversi.put(xy[0], xy[1], player):
            xy = input_position(player)

        print_board(reversi)
        xy = reversi.find_best_position(player * -1, weight_matrix)
        if xy:
            reversi.put(xy[0], xy[1], player * -1)
        print_position(player * -1, xy)

    print_board(reversi)
    if reversi.count(player) > reversi.count(player * -1):
        print('You win!')
    elif reversi.count(player) < reversi.count(player * -1):
        print('You lose!')


if __name__ == "__main__":
    start_game()
#-------------------------------------------------------------------------------
    """
    testtest
    """
    