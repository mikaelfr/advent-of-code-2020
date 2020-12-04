from fetch import AdventCalendar
import re

result = len([1 for e in list(map(lambda x: (int(re.match(r'(\d+)-\d+.*', x).group(1)), int(re.match(r'\d+-(\d+).*', x).group(1)), re.match(r'.*: (.*)', x).group(1).count(re.match(r'.*(\w):.*', x).group(1))), AdventCalendar(2).get_daily_input_data())) if e[2] <= e[1] and e[2] >= e[0]])

result2 = len([1 for e in list(map(lambda x: (int(re.match(r'(\d+)-\d+.*', x).group(1)), int(re.match(r'\d+-(\d+).*', x).group(1)), re.match(r'.*(\w):.*', x).group(1), re.match(r'.*: (.*)', x).group(1)), AdventCalendar(2).get_daily_input_data())) if (len(e[3]) >= e[0] and len(e[3]) < e[1] and e[3][e[0]-1] == e[2]) or ((len(e[3]) >= e[0] and len(e[3]) >= e[1]) and ((e[3][e[0]-1] == e[2] and e[3][e[1]-1] != e[2]) or (e[3][e[0]-1] != e[2] and e[3][e[1]-1] == e[2])))])

print(result)
print(result2)
