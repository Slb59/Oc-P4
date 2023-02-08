from chessmanager.controllers import ArgParser
from chessmanager.controllers import DatabaseLoader


if __name__ == '__main__':
    args = ArgParser()
    the_parameters = args.read_parameters()

    database_loader = DatabaseLoader(the_parameters)
    my_app = database_loader.load_database()

    my_app.run()
