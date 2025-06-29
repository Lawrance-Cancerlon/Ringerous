import unittest
import json
import csv
import tempfile
import os
from unittest.mock import patch, mock_open
from modules.media import import_rings, export_single_result, export_batch_results
from shared.models.Ring import Ring


class TestMedia(unittest.TestCase):
    def test_import_rings_single_file(self):
        ring = {
            'elements': ['a', 'b', 'c'],
            'add_table': [
                ['a', 'b', 'c'],
                ['b', 'c', 'a'],
                ['c', 'a', 'b']
            ],
            'mul_table': [
                ['a', 'a', 'a'],
                ['a', 'b', 'c'],
                ['a', 'c', 'b']
            ]
        }
        json_content = json.dumps(ring)
        with patch('builtins.open', mock_open(read_data=json_content)):
            with patch('json.load', return_value=ring):
                _, rings = import_rings(['ring.json'])
                self.assertEqual(len(rings), 1)
                self.assertIsInstance(rings[0], Ring)
                self.assertEqual(rings[0].elements, ['a', 'b', 'c'])

    def test_import_rings_multiple_files(self):
        ring_1 = {
            'elements': ['a', 'b', 'c'],
            'add_table': [
                ['a', 'b', 'c'],
                ['b', 'c', 'a'],
                ['c', 'a', 'b']
            ],
            'mul_table': [
                ['a', 'a', 'a'],
                ['a', 'b', 'c'],
                ['a', 'c', 'b']
            ]
        }
        ring_2 = {
            'elements': ['x', 'y'],
            'add_table': [
                ['x', 'y'],
                ['y', 'x']
            ],
            'mul_table': [
                ['x', 'x'],
                ['x', 'y']
            ]
        }
        json_content_1 = json.dumps(ring_1)
        json_content_2 = json.dumps(ring_2)
        with patch('builtins.open', mock_open(read_data=json_content_1)), patch('builtins.open', mock_open(read_data=json_content_2)):
            with patch('json.load', side_effect=[ring_1, ring_2]):
                _, rings = import_rings(['ring1.json', 'ring2.json'])
                self.assertEqual(len(rings), 2)
                self.assertIsInstance(rings[0], Ring)
                self.assertIsInstance(rings[1], Ring)
                self.assertEqual(rings[0].elements, ['a', 'b', 'c'])
                self.assertEqual(rings[1].elements, ['x', 'y'])

    def test_import_rings_empty_list(self):
        paths, rings = import_rings([])
        self.assertEqual(len(rings), 0)
        self.assertEqual(rings, [])

    def test_export_single_result(self):
        result = {
            'prop1': {'result': True, 'counterexample': ''},
            'prop2': {'result': False, 'counterexample': '(a, b)'},
            'prop3': {'result': True, 'counterexample': ''}
        }
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
            temp_path = tmp_file.name
        try:
            export_single_result(result, temp_path)
            with open(temp_path, 'r', newline='') as f:
                reader = csv.reader(f)
                rows = list(reader)
                expected_headers = ["Property", "Result", "Counterexample"]
                self.assertEqual(rows[0], expected_headers)
                self.assertEqual(len(rows), 4)
                self.assertEqual(rows[1], ['prop1', 'True', ''])
                self.assertEqual(rows[2], ['prop2', 'False', '(a, b)'])
                self.assertEqual(rows[3], ['prop3', 'True', ''])
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_export_batch_results(self):
        results = {
            'file1.json': {
                'prop1': {'result': True, 'counterexample': ''},
                'prop2': {'result': False, 'counterexample': '(a, b)'}
            },
            'file2.json': {
                'prop3': {'result': True, 'counterexample': ''}
            }
        }
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
            temp_path = tmp_file.name
        try:
            export_batch_results(results, temp_path)
            with open(temp_path, 'r', newline='') as f:
                reader = csv.reader(f)
                rows = list(reader)
                expected_headers = ["Filename", "Property", "Result", "Counterexample"]
                self.assertEqual(rows[0], expected_headers)
                self.assertEqual(len(rows), 4)
                self.assertEqual(rows[1], ['file1.json', 'prop1', 'True', ''])
                self.assertEqual(rows[2], ['file1.json', 'prop2', 'False', '(a, b)'])
                self.assertEqual(rows[3], ['file2.json', 'prop3', 'True', ''])
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

if __name__ == '__main__':
    unittest.main()
