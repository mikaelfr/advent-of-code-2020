from fetch import AdventCalendar
import itertools

result = [x * y for x, y in itertools.combinations(list(map(int, AdventCalendar(1).get_daily_input_data())), 2) if x + y == 2020][0]

result3 = [x * y * z for x, y, z in itertools.combinations(list(map(int, AdventCalendar(1).get_daily_input_data())), 3) if x + y + z == 2020][0]

print(result)
print(result3)