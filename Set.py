"""
Gatlin Cruz
Brett Dale
11/20/20
"""


class Set:

    def __init__(self, size, current_lru=0, lines=[]):
        """
        Constructor for a Set
        :param size: The size of the set
        :param current_lru: Current int value for least recently used
        :param lines: The list of Lines that's contained in the set
        """
        self.__size = size
        self.__current_lru = current_lru
        self.__lines = lines

    def add_line(self, line):
        """
        Adds a line to the list of sets
        :param line: The Line object that's being stored
        :return: None
        """
        self.__lines.append(line)

    def hit_or_miss(self, tag):
        """
        Tells if data being accessed was a hit or miss
        :param tag: The tag used to see if
        :return: True if it was a hit, False otherwise
        """
        was_hit = False
        for line in self.__lines:
            if(line.get_tag() == tag and line.get_valid() == 1):
                was_hit = True
        return was_hit








class Line:

    def __init__(self, line_size, address, valid=0, lru=0, tag=0, mem_refs=0):
        self.__size = line_size
        self.__line_size = line_size
        self.__address = address
        self.__valid = valid
        self.__lru = lru
        self.__tag = tag
        self.__mem_refs = mem_refs

    def set_valid(self):
        self.__valid = 1

    def get_valid(self):
        return self.__valid

    def set_lru(self, lru):
        self.__lru = lru

    def get_lru(self):
        return self.__lru

    def set_tag(self, tag):
        self.__tag = tag

    def get_tag(self):
        return self.__tag
