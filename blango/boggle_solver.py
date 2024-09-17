"""
NAME: Basanta Baral
ID: @03085905
"""

class Boggle:
    def __init__(self, grid, dictionary):
        """
        Constructor for the Boggle class.
        Initializes the grid, dictionary, and solution list.
        
        :param grid: 2D list of strings representing the Boggle board.
        :param dictionary: List of words to search for in the grid.
        """
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

    def setGrid(self, grid):
        """
        Sets the Boggle grid.
        
        :param grid: 2D list of strings representing the Boggle board.
        """
        self.grid = grid

    def setDictionary(self, dictionary):
        """
        Sets the dictionary of words.
        
        :param dictionary: List of words to search for in the grid.
        """
        self.dictionary = dictionary

    def getSolution(self):
        """
        Finds all valid words from the dictionary that can be formed in the grid.
        
        :return: List of valid words found in the grid.
        """
        self.solution = []
        # Convert grid to uppercase for case-insensitive comparison
        grid_upper = [[cell.upper() for cell in row] for row in self.grid]
        for word in self.dictionary:
            word_upper = word.upper()
            if len(word_upper) < 3:
                continue  # Skip words shorter than 3 letters
            if self.is_valid_word(word_upper, grid_upper):
                self.solution.append(word)
        return self.solution

    def is_valid_word(self, word, grid_upper):
        """
        Checks if a word can be formed in the grid following Boggle rules.
        
        :param word: The word to search for.
        :param grid_upper: The Boggle grid in uppercase.
        :return: True if the word is valid and can be formed, False otherwise.
        """
        rows = len(grid_upper)
        cols = len(grid_upper[0]) if rows > 0 else 0

        for x in range(rows):
            for y in range(cols):
                cell = grid_upper[x][y]
                if word.startswith(cell):
                    visited = [[False for _ in range(cols)] for _ in range(rows)]
                    if self.dfs(word, grid_upper, x, y, 0, visited):
                        return True
        return False

    def dfs(self, word, grid_upper, x, y, index, visited):
        """
        Depth-First Search to find the word in the grid.
        
        :param word: The word to search for.
        :param grid_upper: The Boggle grid in uppercase.
        :param x: Current row index.
        :param y: Current column index.
        :param index: Current index in the word.
        :param visited: 2D list tracking visited cells.
        :return: True if the word can be formed from this path, False otherwise.
        """
        rows = len(grid_upper)
        cols = len(grid_upper[0]) if rows > 0 else 0

        cell = grid_upper[x][y]
        cell_length = len(cell)

        # Check if the current cell matches the substring of the word
        if word[index:index + cell_length] != cell:
            return False

        # Move the index forward by the length of the current cell
        index += cell_length

        # If we've matched the entire word
        if index == len(word):
            return True

        # Mark the current cell as visited
        visited[x][y] = True

        # Explore all adjacent cells (including diagonals)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the current cell
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                    if self.dfs(word, grid_upper, new_x, new_y, index, visited):
                        return True

        # Unmark the current cell as visited for other paths
        visited[x][y] = False
        return False

def main():
    """
    Main function to create a Boggle instance and find solutions.
    """
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]
    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    
    solution = mygame.getSolution()
    print(solution)

if __name__ == "__main__":
    main()
