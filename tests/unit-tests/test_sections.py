"""Unittests for the sections.py module"""
import unittest
from unittest import mock
from ini_handler.sections import Sections


class TestSections(unittest.TestCase):

    def test_instantiate(self):
        sections = Sections()

    def test_set_and_get_section(self):
        sections = Sections()
        sections['newSection'] = 'setting'
        self.assertEqual(sections['newSection'], {'setting'})

    def test_set_and_get_section_with_many_keys(self):
        sections = Sections()
        sections['newSection'] = 'setting1'
        sections['newSection'] = 'setting2'
        self.assertEqual(sections['newSection'], {'setting1', 'setting2'})
        self.assertEqual(len(sections), 1)

    def test_set_and_get_multiple_sections(self):
        sections = Sections()
        sections['newSection'] = 'setting1'
        sections['anotherSection'] = 'setting2'
        self.assertEqual(sections['newSection'], {'setting1'})
        self.assertEqual(sections['anotherSection'], {'setting2'})
        self.assertEqual(len(sections), 2)

    def test_remove_section(self):
        sections = Sections()
        sections['newSection'] = 'setting1'
        sections['newSection'] = 'setting2'
        sections.remove_setting('newSection', 'setting1')
        self.assertEqual(sections['newSection'], {'setting2'})

if __name__ == '__main__':
    unittest.main()
