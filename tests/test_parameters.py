import unittest
from unittest import TestCase

from chessmanager.controllers import Parameters
from chessmanager.controllers import ArgParser


class TestParameters(TestCase):
    def test_parameters_output_directory(self):
        p = Parameters()
        self.assertEqual(p.output_directory, 'outputs')

    def test_parameters_data_directory(self):
        p = Parameters()
        self.assertEqual(p.data_directory, 'data')


class TestArgParser(TestCase):
    def test_read_parameters(self):
        args = ArgParser()
        the_parameters = args.read_parameters()
        self.assertEqual(
            (the_parameters.output_directory, the_parameters.data_directory),
            ('outputs', 'data')
        )
