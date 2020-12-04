import requests
import browser_cookie3 as browsercookie


class AdventCalendar(object):
    """ Class to authenticate and get input data from AoC
    """
    def __init__(self, day):
        """ Initialization
        """
        self.cached_response = None
        self.url = "https://adventofcode.com/2020/day/" + str(day) + "/input"

    def get_daily_input_data(self):
        """ Get session_id from cookie for AoC site"""
        if self.cached_response:
            return self.cached_response
        
        cj = browsercookie.firefox()
        response = requests.get(self.url, cookies=cj)
        self.cached_response = response.text.split('\n')[:-1]
        return response.text.split('\n')[:-1]