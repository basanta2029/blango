class Boggle:
    def __init__(self, grid, dictionary):
        self.setGrid(grid)
        self.setDictionary(dictionary)
        self.solution = set()  # Initialize solution set in constructor

    def setGrid(self, grid):
        self.grid = [[cell.upper() for cell in row] for row in grid]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        print(f"Grid set: {self.grid}")  # Debug print

    def setDictionary(self, dictionary):
        self.dictionary = set(word.upper() for word in dictionary)
        self.prefix_set = self.build_prefix_set(self.dictionary)
        print(f"Dictionary set: {self.dictionary}")  # Debug print
        print(f"Prefix set: {self.prefix_set}")  # Debug print

    def build_prefix_set(self, dictionary):
        prefix_set = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])
        return prefix_set

    def getSolution(self):
        self.solution.clear()  # Clear any existing solutions
        self.findAllWords()
        print(f"Final solution: {self.solution}")  # Debug print
        return sorted(list(self.solution))

    def isValidWord(self, word):
        valid = word in self.dictionary and len(word) >= 3
        print(f"Checking word: {word}, Valid: {valid}")  # Debug print
        return valid

    def isValidPrefix(self, prefix):
        valid = prefix in self.prefix_set
        print(f"Checking prefix: {prefix}, Valid: {valid}")  # Debug print
        return valid

    def findAllWords(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.dfs(row, col, "")

    def dfs(self, row, col, path):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.visited[row][col]:
            return

        letter = self.grid[row][col]
        new_path = path + letter
        print(f"Exploring: {new_path}")  # Debug print

        if not self.isValidPrefix(new_path):
            return

        self.visited[row][col] = True

        if self.isValidWord(new_path):
            self.solution.add(new_path)
            print(f"Added to solution: {new_path}")  # Debug print

        for drow, dcol in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            self.dfs(row + drow, col + dcol, new_path)

        self.visited[row][col] = False