#!/usr/bin/env python3
"""Test Access Nested Map"""
import sys
from utils import *
import unittest
from unittest import mock
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test Case"""
    """test the function for following inputs"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """method returns what it is supposed to"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
    
    """test a KeyError is raised for the inputs below"""
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ method testing that a KeyError is raised correctly"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], path[-1])

class TestGetJson(unittest.TestCase):
    """TestCase"""
    """Test the function for following inputs"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """method to test that utils.get_json returns the expected result"""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test Case"""
    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
            is returned but a_method is only called once using
            assert_called_once.
        """
        

        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
