import requests
import browser_cookie3 as browsercookie


class AdventCalendar(object):
    """ Class to authenticate and get input data from AoC
    """
    cache = {}

    def __init__(self, day):
        """ Initialization
        """
        self.day = str(day)
        self.url = "https://adventofcode.com/2020/day/" + str(day) + "/input"

    def get_daily_input_data(self):
        """ Get session_id from cookie for AoC site"""
        if self.day in AdventCalendar.cache:
            return AdventCalendar.cache[self.day].copy()
        
        cj = browsercookie.firefox()
        response = requests.get(self.url, cookies=cj)
        AdventCalendar.cache[self.day] = response.text.split('\n')[:-1]
        return response.text.split('\n')[:-1]