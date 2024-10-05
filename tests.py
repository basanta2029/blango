import unittest
from boggle_solver import Boggle  # Import the Boggle class

def lowercase_string_array(string_array):
    return [s.lower() for s in string_array]

class TestBoggleSolver(unittest.TestCase):

    def test_normal_case(self):
        grid = [['t', 'w', 'y', 'r'],
                ['e', 'n', 'p', 'h'],
                ['g', 'z', 'qu', 'r'],
                ['o', 'n', 't', 'a']]
        dictionary = ['art', 'ego', 'gent', 'get', 'net', 'new', 'newt', 'prat',
                      'pry', 'qua', 'quart', 'quartz', 'rat', 'tar', 'tarp',
                      'ten', 'went', 'wet', 'arty', 'egg', 'not', 'quar']
        expected = ['art', 'ego', 'gent', 'get', 'net', 'new', 'newt', 'prat', 
                    'pry', 'qua', 'quar', 'quart', 'quartz', 'rat', 'tar', 
                    'tarp', 'ten', 'went', 'wet']

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_empty_grid(self):
        grid = [[]]
        dictionary = ['art', 'ego', 'gent']
        expected = []

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_empty_dictionary(self):
        grid = [['a', 'b', 'c', 'd']]
        dictionary = []
        expected = []

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_edge_case_short_words(self):
        grid = [['a', 'b', 'c', 'd'],
                ['e', 'f', 'g', 'h']]
        dictionary = ['a', 'b', 'c', 'd']
        expected = []

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_single_letter_words(self):
        grid = [['a', 'b', 'c'],
                ['d', 'e', 'f']]
        dictionary = ['ad', 'be', 'cf', 'abc']
        expected = ['abc']

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_case_sensitive_words(self):
        grid = [['A', 'B', 'C', 'D'],
                ['E', 'F', 'G', 'H']]
        dictionary = ['ab', 'ACD', 'abC', 'ED']
        expected = ['acd', 'abc']

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_grid_with_no_possible_words(self):
        grid = [['x', 'y', 'z'],
                ['x', 'y', 'z']]
        dictionary = ['abc', 'def', 'ghi']
        expected = []

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_large_grid(self):
        grid = [['A', 'B', 'C', 'D', 'E'],
                ['F', 'G', 'H', 'I', 'J'],
                ['K', 'L', 'M', 'N', 'O'],
                ['P', 'Q', 'R', 'S', 'T'],
                ['U', 'V', 'W', 'X', 'Y']]
        dictionary = ['ABC', 'GHI', 'MNO', 'STU', 'XYZ']
        expected = ['abc', 'ghi', 'mno', 'stu', 'xyz']

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

    def test_grid_with_qu(self):
        grid = [['q', 'u', 'a', 'r'],
                ['t', 'e', 's', 't'],
                ['b', 'o', 'x', 'y'],
                ['a', 'r', 'e', 'd']]
        dictionary = ['quar', 'test', 'box', 'are', 'ear', 'red']
        expected = ['are', 'box', 'quar', 'red', 'test']

        boggle = Boggle(grid, dictionary)
        solutions = boggle.getSolution()

        self.assertEqual(sorted(lowercase_string_array(solutions)), sorted(lowercase_string_array(expected)))

if __name__ == '__main__':
    unittest.main()