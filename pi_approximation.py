
import sys

def main(argv):
    num_points = get_input_as_int("How many points should be generated? ")
    
    


def get_input_as_int(message: str, error_message: str = "Not an integer, try again") -> int:
    while True:
        try:
            ret_value = int(input(message))
        except ValueError:
            print(error_message)
            continue
        break


if __name__ == '__main__':
    main(sys.argv[1:])