import re
from fetch import AdventCalendar

class Parser:

    def __init__(self):
        self.passports = ['']

        for row in AdventCalendar(4).get_daily_input_data():
            if row == '':
                self.passports.append('')
            else:
                self.passports[-1] += row + ' '

    def __iter__(self):
        for passport in self.passports:
            yield {attr.split(':')[0]: attr.split(':')[1] for attr in passport.split()}

    @staticmethod
    def is_valid(passport):
        if any (key not in passport for key in required_fields):
            return False

        if not re.match(r'[0-9]{4}$', passport['byr']) or not 1920 <= int(passport['byr']) <= 2002:
            return False

        if not re.match(r'[0-9]{4}$', passport['iyr']) or not 2010 <= int(passport['iyr']) <= 2020:
            return False

        if not re.match(r'[0-9]{4}$', passport['eyr']) or not 2020 <= int(passport['eyr']) <= 2030:
            return False

        if re.match(r'[0-9]+cm$|[0-9]+in$', passport['hgt']):
            ending = passport['hgt'][-2:]
            if ending == 'cm' and not 150 <= int(passport['hgt'][:-2]) <= 193:
                return False
            elif ending == 'in' and not 59 <= int(passport['hgt'][:-2]) <= 76:
                return False
        else:
            return False

        if not re.match(r'#[0-9a-f]{6}$', passport['hcl']):
            return False
        
        if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        if not re.match(r'[0-9]{9}$', passport['pid']):
            return False 

        return True       



required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
result1 = len([1 for passport in Parser() if all (key in passport for key in required_fields)])
result2 = len([1 for passport in Parser() if Parser.is_valid(passport)])

print(result1)
print(result2)
