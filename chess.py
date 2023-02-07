from chessmanager.controllers import ArgParser
from chessmanager.controllers import ChessManager


if __name__ == '__main__':
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = ChessManager(the_parameters)
    my_app.run()
