#!/usr/bin/python3

"""
Test Module for HBNBCommand class
"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
# sys.path.append('../')
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment."""
        del self.console
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """Test the help command."""
        with patch('builtins.input', return_value='quit'):
            expected_output = (
                    "Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  count  create  destroy  help  quit  show\
                      update"
            )
            HBNBCommand().onecmd("help")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """Test the quit command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("quit")
            self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        """Test the create command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_base_model_command(self, mock_stdout):
        """Test the show command for the BaseModel class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_city_command(self, mock_stdout):
        """Test the show command for the City class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show City")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_amenity_command(self, mock_stdout):
        """Test the show command for the Amenity class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Amenity")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_place_command(self, mock_stdout):
        """Test the show command for the Place class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Place")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_review_command(self, mock_stdout):
        """Test the show command for the Review class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show Review")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_state_command(self, mock_stdout):
        """Test the show command for the State class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show State")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user_command(self, mock_stdout):
        """Test the show command for the User class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("show User")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        """Test the update command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("update")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        """Test the destroy command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("destroy")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_base_model_command(self, mock_stdout):
        """Test the create command for the BaseModel class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]\
            {4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user_command(self, mock_stdout):
        """Test the create command for the User class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create User")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-\
            [0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place_command(self, mock_stdout):
        """Test the create command for the Place class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Place")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-\
            [0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_city_command(self, mock_stdout):
        """Test the create command for the City class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create City")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-\
            [0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_state_command(self, mock_stdout):
        """Test the create command for the State class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create State")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-\
            [0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_review_command(self, mock_stdout):
        """Test the create command for the Review class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Review")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}\
            -[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_amenity_command(self, mock_stdout):
        """Test the create command for the Amenity class."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create Amenity")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}\
            -[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        """Test the show command."""
        with patch('builtins.input', return_value='quit'):
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}\
            -[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')


if __name__ == '__main__':
    unittest.main()
