from formatter import Formatter

class Pipes():
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.covered = {}
        self.more_than_one = {}

    def get_coordinates_covered(self):
        for c in self.coordinates:
            start = c[0]
            end = c[1]
            if self.is_line_horizontal_or_vertical(start, end):
                self.add_horizontal_and_vertical_line_coordinates(start, end)
            else: 
                self.add_diagonal_line_cordinates(start, end)
        return len(self.more_than_one)
    
    def is_line_horizontal_or_vertical(self, start, end):
        return start[0] == end[0] or start[1] == end[1]

    def add_horizontal_and_vertical_line_coordinates(self, start, end):
        self.update_covered((start[0], start[1]))
        self.update_covered((end[0], end[1]))
        while start != end:
            if start[0] < end[0]:
                start[0] += 1
            elif start[0] > end[0]:
                start[0] -= 1
            elif start[1] < end[1]:
                start[1] += 1
            else:
                start[1] -= 1
            if start != end:
                self.update_covered((start[0], start[1]))

    def add_diagonal_line_cordinates(self, start, end):
        self.update_covered((start[0], start[1]))
        self.update_covered((end[0], end[1]))
        while start != end:
            if start[0] < end[0]:
                start[0] += 1
            else:
                start[0] -= 1
            if start[1] < end[1]:
                start[1] += 1
            else:
                start[1] -= 1
            if start != end:
                self.update_covered((start[0], start[1]))

    def update_covered(self, coordinates):
        if coordinates in self.covered:
            self.covered[coordinates] += 1
        else: 
            self.covered[coordinates] = 1
        if self.covered[coordinates] > 1:
            self.more_than_one[coordinates] = True


formatter = Formatter()
coordinates = formatter.get_coordinates()
pipes = Pipes(coordinates)
covered = pipes.get_coordinates_covered()
print(covered)