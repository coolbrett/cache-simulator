import sys
"""
Gatlin Cruz
Brett Dale
11/20/20
"""

def main():
    # Data used to build the cache
    cache_setup_values = []

    # Data used within the cache
    cache_data = []

    # Contents of the file being passed in to stdin
    file_contents = sys.stdin.read().splitlines()

    # Boolean variable to see if the file being used is valid
    correct_data = True


    for i in range(3):
        cache_setup_values.append(file_contents[i].split(":"))
        #cache_setup_values[i] = cache_setup_values[i].split(":")
        if(len(cache_setup_values[i]) != 2):
            correct_data = False

    for i in range(3,len(file_contents)):
        cache_data.append(file_contents[i].split(":"))
        if(len(cache_data[i - 3]) != 3):
            correct_data = False

    if(correct_data):
        cache_num_sets = cache_setup_values[0][1]
        cache_set_size = cache_setup_values[1][1]
        cache_line_size = cache_setup_values[2][1]
        values = calculate('aaaa', 3, 7)
        print(values)

        setup_cache(cache_num_sets, cache_set_size, cache_line_size)
    else:
        print("Invalid Data")


def setup_cache(num_sets, set_size, line_size):
    print("Hello")

def calculate(hex_value, index_size, tag_size):
    values = []
    hex_to_bin = "{0:08b}".format(int(hex_value, 16))
    print(hex_to_bin)
    zero = list(str(0) * len(hex_to_bin))
    for i in range(index_size):
        zero[-1 - i] = hex_to_bin[-1 - i]
    index = "".join(zero)
    #print(index)
    zero = list(str(0) * len(hex_to_bin))
    for i in range(tag_size):
        zero[-1 - i - index_size] = hex_to_bin[-1 - i - index_size - 1]
    tag = "".join(zero)
    tag = tag[len(hex_to_bin) - index_size - tag_size: len(hex_to_bin) - tag_size]
    #print(tag)

    offset = hex_to_bin[:len(hex_to_bin) - index_size - tag_size]
    #print(offset)
    values.append(index)
    values.append(tag)
    values.append(offset)
    return values




if __name__ == '__main__':
    main()
