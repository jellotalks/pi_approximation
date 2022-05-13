
import sys

def main(argv):
    is_verbose = True if '-v' in argv else False

    num_points = get_input_as_int("How many points should be generated? ")
    
    
    


def get_input_as_int(message: str, error_message: str = "Not an integer, try again") -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)
            continue


if __name__ == '__main__':
    main(sys.argv)