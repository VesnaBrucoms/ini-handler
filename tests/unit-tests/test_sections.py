"""Unittests for the sections.py module"""
import unittest
from unittest import mock
from ini_handler.sections import Sections


class TestSections(unittest.TestCase):

    def test_instantiate(self):
        sections = Sections()
