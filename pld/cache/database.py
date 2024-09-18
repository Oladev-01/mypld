#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}
        self.track = None

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        sorted_data = {key: self.cache_data[key] for key in sorted(self.cache_data.keys())}
        return sorted_data

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            lifo = list(self.cache_data.keys())[-2]
            del self.cache_data[lifo]
            return lifo
    def get(self, key):
        """ Get an item by key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]