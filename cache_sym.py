import sys
from set import Set
from line import Line
import math
"""
Gatlin Cruz
Brett Dale
11/20/20
"""


def main():
    show_final_stats = False
    if(len(sys.argv) < 3):
        if(len(sys.argv) == 2 and sys.argv[1].lower() == "f"):
            show_final_stats = True
        go(show_final_stats)

    else:
        print("Too many arguments")


def go(show_final_stats):
    # Data used to build the cache
    cache_setup_values = []
    stats = []

    # Data used within the cache
    cache_accesses = []

    # Contents of the file being passed in to stdin
    file_contents = sys.stdin.read().splitlines()

    # Boolean variable to see if the file being used is valid
    correct_data = True

    for i in range(3):
        cache_setup_values.append(file_contents[i].split(":"))
        if (len(cache_setup_values[i]) != 2):
            correct_data = False

    for i in range(3, len(file_contents)):
        cache_accesses.append(file_contents[i].split(":"))
        if (len(cache_accesses[i - 3]) != 3):
            correct_data = False
    if (int(cache_setup_values[2][1]) < 4 or int(cache_setup_values[2][1]) % 2 != 0 or int(
            cache_setup_values[0][1]) % 2 != 0):
        correct_data = False

    if (correct_data):
        cache_num_sets = cache_setup_values[0][1]
        cache_set_size = cache_setup_values[1][1]
        cache_line_size = cache_setup_values[2][1]
        cache = Cache(cache_num_sets, cache_set_size, cache_line_size)
        cache.setup_cache()
        cache.set_total_access(len(cache_accesses))

        for i in range(len(cache.get_sets())):
            for j in range(len(cache.get_sets()[i].get_lines())):
                stats.append(cache.get_sets()[i].get_lines()[j].create_stat())

        """
        Calculate the size for offset, and index
        """
        offset = math.log(int(cache_line_size), 2)
        index = math.log(int(cache_num_sets), 2)

        for i in range(len(cache_accesses)):
            values = cache.calculate(str(cache_accesses[i][0]), int(offset), int(index))
            offset_value = int(values[0])
            offset_v = cache.bin_to_dec(offset_value)
            index_value = int(values[1])
            index_v = cache.bin_to_dec(index_value)
            tag_value = int(values[2])
            tag_v = cache.bin_to_dec(tag_value)
            if (cache_accesses[i][1] == "R" or cache_accesses[i][1] == "r"):
                cache.check_cache(True, offset_v, index_v, tag_v, cache_accesses[i][0])
            else:
                cache.check_cache(False, offset_v, index_v, tag_v, cache_accesses[i][0])
        cache.print_config(cache_set_size, cache_num_sets, cache_line_size)

        cache.print_results()

        if(show_final_stats):
            print("\tFinal Data Cache State")
            print("\t-------------------------")
            for i in range(int(cache_num_sets)):  # Used when the user enters F
                cache.get_sets()[i].create_stats(i)
                for j in range(len(cache.get_sets()[i].get_stats())):
                    print(cache.get_sets()[i].get_stats()[j])


    else:
        print("Invalid Data")


class Cache:

    def __init__(self, num_sets, set_size, line_size, sets=None, total_hits=0, total_misses=0, total_access=0,
                 total_mem_refs=0, stats=None, hit_ratio=0, miss_ratio=0):
        if sets is None:
            sets = []
        if stats is None:
            stats = []
        self.__num_sets = int(num_sets)
        self.__set_size = int(set_size)
        self.__line_size = int(line_size)
        self.__sets = sets
        self.__total_hits = total_hits
        self.__total_misses = total_misses
        self.__total_access = total_access
        self.__total_mem_refs = total_mem_refs
        self.__stats = stats
        self.__hit_ratio = hit_ratio
        self.__miss_ratio = miss_ratio

    def setup_cache(self):
        """
        Sets up the cache to the desired size
        :return: None
        """
        for i in range(int(self.__num_sets)):
            temp = Set(self.__set_size, self.__line_size)
            self.__sets.append(temp)

        for set in self.__sets:
            set.add_lines()

    def set_total_access(self, accesses):
        self.__total_access = accesses

    def calculate(self, hex_value, offset_size, index_size):
        """
        Takes in the bit size for index and tag and returns index a list of the 3 values
        :param hex_value:
        :param index_size:
        :param tag_size:
        :return:
        """
        values = []
        hex_to_bin = "{0:08b}".format(int(hex_value, 16))

        if(len(hex_to_bin) % 4 != 0):
            num = (4 - len(hex_to_bin) % 4)
            str_num = ""
            for i in range(num):
                str_num += "0"

            hex_to_bin = str_num + hex_to_bin

        zero = list(str(0) * len(hex_to_bin))
        for i in range(int(offset_size)):
            zero[-1 - i] = hex_to_bin[-1 - i]
        offset = "".join(zero)
        offset = offset[len(hex_to_bin) - offset_size:]

        zero = list(str(0) * len(hex_to_bin))
        for i in range(index_size):
            zero[-1 - i] = hex_to_bin[-1 - i - offset_size]
        index = "".join(zero)

        index = index[len(hex_to_bin) - index_size:]

        tag = hex_to_bin[:len(hex_to_bin) - offset_size - index_size]
        values.append(offset)
        values.append(index)
        values.append(tag)
        return values


    def bin_to_dec(self, binary):
        """
        Converts binary to decimal
        :param binary: The binary to be converted
        :return: The decimal value of the binary
        """
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        return decimal


    def print_config(self, set_size, total_sets, line_length):
        """
        Prints the config heading
        :param set_size: The number of lines in a set
        :param total_sets: The number of sets
        :param line_length: The length of each line
        :return: None
        """
        print("\nCache Configuration\n")
        print("    " + str(set_size) + "-way set associative entries")
        print("    " + str(total_sets) + " sets total")
        print("     " + str(int(line_length) // 4) + " words per set\n")
        if(int(set_size) == 1):
            print("    DIRECT MAPPED CACHE\n")
        elif(int(total_sets) == 1):
            print("    FULLY ASSOCIATIVE CACHE\n")

    def print_results(self):
        total_mem_refs = 0
        print("Results for Each Reference\n")
        print("Access Address    Tag   Index Offset Result Memrefs")
        print("------ -------- ------- ----- ------ ------ -------")
        for stat in self.__stats:
            print(stat.to_string())
        for i in range(len(self.__stats)):
            total_mem_refs += self.__stats[i].get_mem_refs()
        self.__hit_ratio = self.__total_hits / (self.__total_misses + self.__total_hits)
        self.__miss_ratio = self.__total_misses / (self.__total_hits + self.__total_misses)

        print("\nSimulation Summary Statistics")
        print("---------------------------")
        print("Total hits                      : " + str(self.__total_hits))
        print("Total misses                    : " + str(self.__total_misses))
        print("Total accesses                  : " + str(self.__total_access))
        print("Total memory references         : " + str(self.__total_mem_refs))
        print("Hit ratio                       : " + str(self.__hit_ratio))
        print("Miss ratio                      : " + str(self.__miss_ratio) + "\n")

    def get_sets(self):
        """
        Returns the set list
        :return: The set list
        """
        return self.__sets


    def check_cache(self, isRead, offset, index, tag, address):
        mem_refs = 0
        was_hit = False
        line = self.__sets[index].get_line(tag)
        if(line != None and line.get_valid() == 1):
            print("first")
            if(isRead):
                was_hit = True
                self.__total_hits += 1
            else:
                was_hit = True
                self.__total_hits += 1
                if(not line.is_dirty()):
                    line.set_dirty(True)

            line.set_lru(self.__sets[index].get_lru() + 1)
            self.__sets[index].increment_lru()

        elif(self.__sets[index].is_full()):
            print("second")
            temp_line = self.__sets[index].get_lines()[0]
            for i in range(len(self.__sets[index].get_lines())):
                if(self.__sets[index].get_lines()[i].get_lru() < temp_line.get_lru()):
                    temp_line = self.__sets[index].get_lines()[i]
            line_index = self.__sets[index].find_line_index(temp_line)
            mem_refs += 1
            self.__total_mem_refs += 1

            new_line = Line(self.__sets[index].get_line_size(), str(hex(int(address, 16)-offset))[2:], 1, self.__sets[index].get_lru() + 1, tag, mem_refs, isRead)
            if(temp_line.is_dirty()):
                mem_refs += 1
                self.__total_mem_refs += 1

            if(not isRead):
                new_line.set_dirty(True)

            self.__sets[index].increment_lru()
            self.__sets[index].set_line(new_line, line_index)
            self.__total_misses += 1

        else:
            print("third")
            for i in range(self.__sets[index].get_size()):
                if(self.__sets[index].get_lines()[i].get_valid() == 0):
                    self.__sets[index].get_lines()[i].set_valid()
                    self.__sets[index].get_lines()[i].set_lru(self.__sets[index].get_lru() + 1)
                    self.__sets[index].increment_lru()
                    self.__sets[index].get_lines()[i].set_tag(tag)
                    self.__sets[index].get_lines()[i].set_address(str(hex(int(address, 16)-offset))[2:])
                    if(isRead):
                        mem_refs += 1
                        self.__total_mem_refs += 1
                    else:
                        self.__sets[index].get_lines()[i].set_dirty(True)
                        mem_refs += 1
                        self.__total_mem_refs += 1
                    break
            self.__total_misses += 1
        if(isRead):
            access = "read"
        else:
            access = "write"
        if(was_hit):
            hit_or_miss = "HIT"
        else:
            hit_or_miss = "MISS"
        temp = Cache_Result(access, address, tag, index, offset, hit_or_miss, mem_refs)
        self.__stats.append(temp)


class Cache_Result(object):

    def __init__(self, access, address, tag, index, offset, result, mem_refs=0):
        self.__access = access
        self.__address = address
        self.__tag = tag
        self.__index = index
        self.__offset = offset
        self.__result = result
        self.__mem_refs = mem_refs

    def increment_mem_refs(self):
        self.__mem_refs += 1

    def get_mem_refs(self):
        return self.__mem_refs

    def is_this_result(self, tag, index):
        is_this_result = False
        if(tag == self.__tag and index == self.__index):
            is_this_result = True
        return is_this_result

    def to_string(self):
        message = self.__access.rjust(6) + str(self.__address).rjust(9)  + str(self.__tag).rjust(8) \
                  + str(self.__index).rjust(6) + str(self.__offset).rjust(7) +  self.__result.rjust(7)\
                  + str(self.__mem_refs).rjust(8)
        return message


if __name__ == '__main__':
    main()
