"""
Gatlin Cruz
Brett Dale
11/20/20
"""


class Set:

    def __init__(self, size, line_size, current_lru=0, lines=[]):
        """
        Constructor for a Set
        :param size: The size of the set
        :param current_lru: Current int value for least recently used
        :param lines: The list of Lines that's contained in the set
        """
        self.__size = size
        self.__line_size = line_size
        self.__current_lru = current_lru
        self.__lines = lines

    def add_lines(self):
        """
        Adds a line to the list of sets
        :return: None
        """
        for i in range(self.__size):
            line = Line(self.__line_size)
            self.__lines.append(line)
        #print(len(self.__lines))

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

    def get_size(self):
        return self.__size

    def print_lines(self):
        for i in range(self.__size):
            print(self.__lines[i].get_values())

    def get_line(self, tag):
        for i in range(self.__size):
            if(self.__lines[i].get_tag == tag):
                return self.__lines[i]

    def is_full(self):
        is_full = False
        i = 0
        for i in range(self.__size):
            if(self.__lines[i].get_valid() == 1):
                i += 1
        if(i == self.__size):
            is_full = True
        return is_full

    def get_lines(self):
        return self.__lines


class Line:

    def __init__(self, line_size, address=0, valid=0, lru=0, tag=0, mem_refs=0):
        self.__size = line_size
        self.__line_size = line_size
        self.__address = address
        self.__valid = valid
        self.__lru = lru
        self.__tag = tag
        self.__mem_refs = mem_refs
        self.__data=[]
        for i in range(self.__line_size):
            self.__data.append(0)

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

    def get_values(self):
        return self.__data
