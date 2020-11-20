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
        print(cache_setup_values)
        print(cache_data)
    else:
        print("Invalid Data")


if __name__ == '__main__':
    main()
