"""
Gatlin Cruz
Brett Dale
11/20/20
"""


class Set(object):

    def __init__(self, size, line_size, current_lru=0, lines=[], stats=[]):
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
        self.__stats = stats

    def add_lines(self):
        """
        Adds a line to the list of sets
        :return: None
        """
        for i in range(self.__size):
            #print(self.__size)
            #print(i)


            line = Line(self.__line_size)


            #print(line)
            self.__lines.append(line)
            print(self.__lines)

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
        """
        Returns the size of the set
        :return: the size of the set
        """
        return self.__size

    def print_lines(self):
        for i in range(self.__size):
            print(self.__lines[i].get_values())

    def get_line(self, tag):
        """
        Gets the line in the set based off the tag, if it exists
        :param tag: The tag that's being checked
        :return: the line with the same tag, None if it doesn't exist
        """
        for i in range(self.__size):
            if(self.__lines[i].get_tag == tag):
                return self.__lines[i]

    def is_full(self):
        """
        Returns if this set is full
        :return: True if set if full, False otherwise
        """
        is_full = False
        i = 0
        for i in range(self.__size):
            if(self.__lines[i].get_valid() == 1):
                i += 1
        if(i == self.__size):
            is_full = True
        return is_full

    def get_lines(self):
        """
        Returns the list of lines
        :return: the list of lines
        """
        return self.__lines

    def create_stats(self, index):
        """
        Creates the final stats of the cache
        :param index: The index of the current set
        :return: None
        """
        #self.__lines[1].set_valid()
        message = "set " + str(index) + "\n"
        for i in range(self.__size):
            if(self.__lines[i].get_valid() == 0):
                message += "\tline " + str(i) + " = invalid"
                if i < (self.__size - 1):
                    message += "\n"
            else:
                message += "\tline " + str(i) + " = byte address " + str(self.__lines[i].get_address()) + ", tag " + str(self.__lines[i].get_tag()) + ", lru " + str(self.__lines[i].get_lru())
                if i < (self.__size - 1):
                    message += "\n"
        self.__stats.append(message)

    def get_stats(self):
        return self.__stats


class Line(object):

    def __init__(self, line_size, address=0, valid=0, lru=0, tag=0, mem_refs=0, is_read=None):
        self.__size = line_size
        self.__line_size = line_size
        self.__address = address
        self.__valid = valid
        self.__lru = lru
        self.__tag = tag
        self.__mem_refs = mem_refs
        self.__is_read = is_read
        self.__data=[]
        for i in range(self.__line_size):
            self.__data.append(0)

    def set_valid(self):
        """
        Sets the valid field to 1
        :return: None
        """
        self.__valid = 1

    def get_valid(self):
        """
        Returns the valid field
        :return: the valid field
        """
        return self.__valid

    def set_address(self, address):
        """
        Sets the address
        :param address: The address being stored
        :return: None
        """
        self.__address = address

    def get_address(self):
        """
        Returns the address
        :return: The address
        """
        return self.__address

    def set_lru(self, lru):
        """
        Sets the lru field
        :param lru: The value being stored to the lru
        :return: None
        """
        self.__lru = lru

    def get_lru(self):
        """
        Returns the current lru
        :return: the current lru
        """
        return self.__lru

    def set_tag(self, tag):
        """
        Sets the tag field
        :param tag: The value for the tag field
        :return: None
        """
        self.__tag = tag

    def get_tag(self):
        """
        Returns the tag
        :return: The tag
        """
        return self.__tag

    def get_values(self):
        """
        Returns the values
        :return: The values
        """
        return self.__data

    def set_is_read(self, is_read):
        """
        Sets the is_read field
        :param is_read: The boolean being stored in is_read
        :return: None
        """
        self.__is_read = is_read

    def create_stat(self):
        """
        Creates a list of strings that will be printed out
        :return: the list of strings
        """
        stat = []
        if(self.__is_read):
            stat.append("read")
        else:
            stat.append("write")
        stat.append(self.__address)
        stat.append(self.__tag)
        stat.append("index")
        stat.append("offset")
        stat.append("HIT/MISS")
        stat.append(self.__mem_refs)
        return stat
