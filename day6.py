from functools import reduce
from fetch import AdventCalendar


class GroupParser:

    def __init__(self):
        self.groups = reduce(lambda a,b: a + [[]] if b == '' else a[:-1] + [a[-1] + [b]], [[[]]] + AdventCalendar(6).get_daily_input_data())
        
    def count_unique_answers(self):
        return [len(set(''.join(group))) for group in self.groups]

    def count_universal_answers(self):
        return [len(reduce(lambda a,b: set(a).intersection(b), group)) for group in self.groups]



result1 = sum(GroupParser().count_unique_answers())
result2 = sum(GroupParser().count_universal_answers())

print(result1)
print(result2)
