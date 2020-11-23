import sys
from Set import Set
"""
Gatlin Cruz
Brett Dale
11/20/20
"""

def main():
    # Data used to build the cache
    cache_setup_values = []
    stats = []

    # Data used within the cache
    cache_data = []

    # Contents of the file being passed in to stdin
    file_contents = sys.stdin.read().splitlines()

    # Boolean variable to see if the file being used is valid
    correct_data = True

    for i in range(3):
        cache_setup_values.append(file_contents[i].split(":"))
        if(len(cache_setup_values[i]) != 2):
            correct_data = False

    for i in range(3, len(file_contents)):
        cache_data.append(file_contents[i].split(":"))
        if(len(cache_data[i - 3]) != 3):
            correct_data = False

    if(correct_data):
        cache_num_sets = cache_setup_values[0][1]
        cache_set_size = cache_setup_values[1][1]
        cache_line_size = cache_setup_values[2][1]
        cache = Cache(cache_num_sets, cache_set_size, cache_line_size)
        cache.setup_cache()
        #print(len(cache.get_sets()))
        #print(len(cache.get_sets()[1].get_lines()))
        #for i in range(len(cache.get_sets())):
         #   cache.get_sets()[i].add_lines()
        k = 0
        for i in range(len(cache.get_sets())):
            #print(i)
            cache.get_sets()[i].print_lines()
            for j in range(len(cache.get_sets()[i].get_lines())):
                #print(k)
                #print(len(cache.get_sets()[i].get_lines()))
                k += 1
                stats.append(cache.get_sets()[i].get_lines()[j].create_stat())
        #for i in range(len(stats)):
            #print(stats[i])



        # for i in range(int(cache_num_sets)):                                     #Used when the user enters F
        #     cache.get_sets()[i].create_stats(i)
        #     print(cache.get_sets()[i].get_stats()[i])






        #values = cache.calculate('11', 4, 3)
        #print(values)
        #print(bin_to_dec(int(values[0])))
        #print(bin_to_dec(int(values[1])))
        #print(bin_to_dec(int(values[2])))
        #print_config(cache_set_size, cache_num_sets, int(cache_line_size) // 4)
    else:
        print("Invalid Data")


class Cache:

    def __init__(self, num_sets, set_size, line_size, sets=[], total_hits=0, total_misses=0, total_access=0, total_mem_refs=0, stats=[]):
        self.__num_sets = int(num_sets)
        self.__set_size = int(set_size)
        self.__line_size = int(line_size)
        self.__sets = sets
        self.__total_hits = total_hits
        self.__total_misses = total_misses
        self.__total_access = total_access
        self.__total_mem_refs = total_mem_refs
        self.__stats = stats

    def setup_cache(self):
        """
        Sets up the cache to the desired size
        :return: None
        """
        for i in range(int(self.__num_sets)):
            temp = Set(self.__set_size, self.__line_size)
            self.__sets.append(temp)

        #for i in range(int(self.__num_sets)):
         #   print(self.__sets[i])
          #  self.__sets[i].add_lines()
        for set in self.__sets:
            set.add_lines()

    def calculate(self, hex_value, offset_size, index_size):
        """
        Takes in the bit size for index and tag and returnsindex a list of the 3 values
        :param hex_value:
        :param index_size:
        :param tag_size:
        :return:
        """
        values = []
        hex_to_bin = "{0:08b}".format(int(hex_value, 16))
        print(hex_to_bin)
        zero = list(str(0) * len(hex_to_bin))
        for i in range(offset_size):
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
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        return decimal


    def print_config(self, set_size, total_sets, line_length):
        print("Cache Configuration\n")
        print("\t" + str(set_size) + "-way set associative entries")
        print("\t" + str(total_sets) + " sets total")
        print("\t " + str(line_length) + " words per set\n")
        if(total_sets == 1):
            print("\tDIRECT MAPPED CACHE\n")
        else:
            print("")

    def print_results(self):
        print("Results for Each Reference\n")
        print("Access Address    Tag   Index Offset Result Memrefs")
        print("------ -------- ------- ----- ------ ------ -------")


    def get_sets(self):
        return self.__sets


    def check_cache(self, isRead, offset, index, tag):
        line = self.__num_sets[index].get_line(tag)
        if(line != None and line.get_valid() == 1):
            if(isRead):
                print("Hit")
            else:
                print("Hit and memref += 1")
        elif(self.__sets[index].is_full()):
            print("Get the lru and replace lowest lru")
        else:
            for i in range(self.__sets[index].get_size()):
                if(self.__sets[index].get_lines()[i].get_valid == 0):
                    self.__sets[index].get_lines()[i].set_valid = 1
                    self.__sets[index].get_lines()[i].set_lru = 0
                    self.__sets[index].get_lines()[i].set_tag = tag
                    #TODO Come back to this


if __name__ == '__main__':
    main()
