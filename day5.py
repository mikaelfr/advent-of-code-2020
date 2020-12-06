from operator import itemgetter
from fetch import AdventCalendar

class PassParser:

    def __init__(self):
        boarding_passes = [PassParser.replace_to_bin(row) for row in AdventCalendar(5).get_daily_input_data()]

        self.passes = sorted([
            {
                'row': int(row[:7], 2),
                'col': int(row[7:], 2), 
                'sid': int(row[:7], 2) * 8 + int(row[7:], 2)
            }
            for row in boarding_passes
        ], key=itemgetter('sid'))

    def get_adjacent_pairs(self):
        for i in range(len(self.passes) - 1):
            yield (self.passes[i-1], self.passes[i])

    @staticmethod
    def replace_to_bin(row):
        return PassParser.bulk_replace(row, {'B': '1', 'F': '0', 'R': '1', 'L': '0'})

    @staticmethod
    def bulk_replace(in_str, mapping):
        for key in mapping:
            in_str = in_str.replace(key, mapping[key])
        return in_str
        

result1 = [bpass['sid'] for bpass in PassParser().passes][-1]
result2 = [pair[1]['sid']-1 for pair in PassParser().get_adjacent_pairs() if pair[0]['sid'] + 2 == pair[1]['sid']][0]

print(result1)
print(result2)
