class Formatter():
    def get_coordinates(self):
        data = self.read_file()
        coordinates = []
        for row in data:
            c = self.remove_text(row)
            row_coordinates = self.format_coordinates(c)
            coordinates.append(row_coordinates)
        return coordinates
    
    def read_file(self):
        filestream = open('data.txt', 'r') 
        return filestream.readlines()

    def remove_text(self, row):
        c = row.replace('\n', '')
        return c.split(' -> ')
    
    def format_coordinates(self, row):
        row_coordinates = []
        for i in range(len(row)):
            c_arr = row[i].split(',')
            for i in range(len(c_arr)):
                c_arr[i] = int(c_arr[i])
            row_coordinates.append(c_arr)
        
        return row_coordinates