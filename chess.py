from chessmanager.controllers import ArgParser
from chessmanager.controllers import ChessManager

""" __ __ """
if __name__ == '__main__':
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = ChessManager(the_parameters)
    my_app.run()
