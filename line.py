class Line(object):

    def __init__(self, line_size, address=0, valid=0, lru=0, tag=0, mem_refs=0, is_read=None, dirty_bit=False):
        self.__size = line_size
        self.__line_size = line_size
        self.__address = address
        self.__valid = valid
        self.__lru = lru
        self.__tag = tag
        self.__mem_refs = mem_refs
        self.__is_read = is_read
        self.__data=[]
        self.__dirty_bit = dirty_bit
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

    def set_dirty(self, is_dirty):
        self.__dirty_bit = is_dirty

    def is_dirty(self):
        return self.__dirty_bit

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
