from fetch import AdventCalendar

class EndlessList:
    def __init__(self, l):
        self.l = l

    def __getitem__(self, x):
        return self.l[x % len(self.l)]

class Atlas:

    def __init__(self, data, slope_x, slope_y, x = None):
        self.x = x
        self.slope_x = slope_x
        self.slope_y = slope_y
        self.map = [EndlessList(row) for row in data]

    def __getitem__(self, val):
        if self.x is not None:
            return self.map[val][self.x]
        return Atlas(data, self.slope_x, self.slope_y, val)

    def __iter__(self):
        for y in range(int(len(self.map) / self.slope_y)):
            yield self[y * self.slope_x][y * self.slope_y]


data = AdventCalendar(3).get_daily_input_data()
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for slope in slopes:
    result *= len([1 for slot in Atlas(data, slope[0], slope[1]) if slot == '#'])

print(result)
