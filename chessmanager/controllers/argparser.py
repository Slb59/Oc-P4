import chessmanager
import argparse
from .parameters import Parameters


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser('chess')

        self.parser.add_argument('--version', '-v',
                                 action='store_true',
                                 help='show current version')

        self.parser.add_argument('--output-dir',
                                 type=str,
                                 help='set the output files directory')

        self.parser.add_argument('--data-dir',
                                 type=str,
                                 help='set the data files directory')

        self.args = self.parser.parse_args()

        # LOGGER.debug(self.args)

        if self.args.version:
            print('chess ' + chessmanager.controllers.__version__)

    def read_parameters(self):

        p = Parameters()

        if self.args.output_dir is not None:
            p.output_directory = self.args.output_dir

        if self.args.data_dir is not None:
            p.data_directory = self.args.data_dir

        return p
