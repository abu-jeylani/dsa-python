
class QueensProblem: 

    def __init__(self,n) -> None:
        self.n = n
        self.chess_table = [[None for i in range(n)] for j in range(n)]

    def solve_n_queens(self):

        #we start with the first queen with index 0

        if self.solve(0):
            self.print_queens
        else:
            pass
    def solve(self, col_index):
        if col_index == self.n:
            return True

    def print_queens(self):
        print(self.chess_table)


if __name__ == '__main__':

    queens = QueensProblem(4)
    queens.print_queens()
